from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import shutil
import csv
from io import StringIO
import sqlite3
import json
import re
from datetime import datetime
import os
import database
import asyncio

app = FastAPI(title="Sistem Pengadaan Terintegrasi PT KMU", version="1.0")

# =============================================================================
# SCHEDULER: ESKALASI OTOMATIS (Fase 4 & 5)
# =============================================================================
async def eskalasi_scheduler():
    while True:
        try:
            conn = database.get_db_connection()
            cursor = conn.cursor()
            
            # Simulasi Pengecekan Keterlambatan Maintenance (Fase 5) dan Bidding (Fase 4)
            # Pada implementasi nyata, ini akan mengecek tabel `kso_contracts` atau `tenders` berdasarkan tanggal.
            now = datetime.now()
            
            # Mock Data Eskalasi: Kita tambahkan notifikasi peringatan jika ada SLA yang terlewat
            cursor.execute("""
                INSERT INTO vendor_notifications (vendor_category, title, message, priority) 
                VALUES (?, ?, ?, ?)
            """, ("SYSTEM", "Auto-Eskalasi", f"Sistem mendeteksi keterlambatan SLA Vendor pada {now.strftime('%Y-%m-%d %H:%M')} (Simulasi)", "high"))
            
            conn.commit()
            conn.close()
            print(f"[SCHEDULER] Auto-Eskalasi berjalan pada {now.strftime('%Y-%m-%d %H:%M:%S')}")
            
        except Exception as e:
            print(f"[SCHEDULER] Error: {e}")
        
        # Berjalan setiap 1 jam (3600 detik). Untuk demo, bisa kita set ke 1 jam.
        await asyncio.sleep(3600)

@app.on_event("startup")
async def startup_event():
    database.init_db()
    asyncio.create_task(eskalasi_scheduler())

@app.get("/")
def root():
    return RedirectResponse(url="/frontend/portal_hub.html")

# Mount frontend folder
frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')
app.mount("/frontend", StaticFiles(directory=frontend_path, html=True), name="frontend")

# Create and mount uploads folder
UPLOADS_DIR = os.path.join(os.path.dirname(__file__), '..', 'uploads')
os.makedirs(UPLOADS_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOADS_DIR), name="uploads")

# Enable CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Run DB Initialization on startup
@app.on_event("startup")
def startup_db():
    database.init_db()

class VendorRegistration(BaseModel):
    company_name: str
    company_name_short: str = ""
    vendor_type: str
    vendor_category: str
    business_license_number: str
    tax_id_npwp: str
    phone_main: str
    email_company: str
    website: str = ""
    office_address_street: str
    office_address_city: str
    office_address_province: str
    office_address_postal_code: str
    bank_name: str
    bank_account_number: str
    bank_account_holder: str
    contact_person_name: str
    contact_person_title: str
    contact_person_phone: str
    contact_person_email: str
    metadata_json: dict = {}

class RequisitionCreate(BaseModel):
    req_type: str
    sbu_name: str
    title: str
    description: str
    budget_code: str
    total_amount: float
    created_by: str

class PurchaseOrderCreate(BaseModel):
    req_id: int
    vendor_id: str
    total_amount: float

class VendorEvalCreate(BaseModel):
    vendor_id: str
    po_number: str
    score_delivery: int
    score_quality: int
    score_response: int
    remarks: str

class QCEvalCreate(BaseModel):
    vendor_id: str
    po_number: str
    evaluator_name: str
    score_delivery: int
    score_quality: int
    score_response: int
    remarks: str

@app.post("/api/vendors/register")
async def register_vendor(vendor: VendorRegistration):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Generate vendor_id
        cursor.execute("SELECT COUNT(*) as count FROM vendors")
        count = cursor.fetchone()['count']
        vendor_id = f"VND-{str(count + 1).zfill(3)}"
        
        # Insert Vendor
        cursor.execute('''
            INSERT INTO vendors (
                vendor_id, company_name, company_name_short, vendor_type, vendor_category,
                phone, email, website, address_street, address_city, address_province, address_postal_code,
                npwp, sio, bank_name, bank_account_number, bank_account_holder,
                contact_person_name, contact_person_title, contact_person_phone, contact_person_email,
                metadata, registration_date
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            vendor_id, vendor.company_name, vendor.company_name_short, vendor.vendor_type, vendor.vendor_category,
            vendor.phone_main, vendor.email_company, vendor.website, vendor.office_address_street, vendor.office_address_city,
            vendor.office_address_province, vendor.office_address_postal_code, vendor.tax_id_npwp, vendor.business_license_number,
            vendor.bank_name, vendor.bank_account_number, vendor.bank_account_holder,
            vendor.contact_person_name, vendor.contact_person_title, vendor.contact_person_phone, vendor.contact_person_email,
            json.dumps(vendor.metadata_json), datetime.now()
        ))
        
        vendor_pk = cursor.lastrowid
        
        # Log Activity
        cursor.execute('''
            INSERT INTO activity_log (activity_type, entity_type, entity_id, entity_reference, action_date, description, vendor_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', ('vendor_registration_submitted', 'vendor', vendor_pk, vendor_id, datetime.now(), f'Vendor registration submitted: {vendor.company_name}', vendor_pk))
        
        conn.commit()
        return {"status": "success", "message": "Pendaftaran berhasil dikirim", "vendor_id": vendor_id}
        
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/vendors")
async def get_vendors(status: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    if status:
        cursor.execute("SELECT * FROM vendors WHERE vendor_status = ? ORDER BY id DESC", (status,))
    else:
        cursor.execute("SELECT * FROM vendors ORDER BY id DESC")
        
    vendors = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": vendors}

@app.post("/api/vendors/{vendor_id}/status")
async def update_vendor_status(vendor_id: str, request: Request):
    data = await request.json()
    new_status = data.get("status")
    
    if new_status not in ["approved", "rejected", "need_revision"]:
        raise HTTPException(status_code=400, detail="Status tidak valid")
        
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("UPDATE vendors SET vendor_status = ? WHERE vendor_id = ?", (new_status, vendor_id))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Vendor tidak ditemukan")
        
    # Log Activity
    cursor.execute("SELECT id FROM vendors WHERE vendor_id = ?", (vendor_id,))
    vendor_pk = cursor.fetchone()['id']
    
    cursor.execute('''
        INSERT INTO activity_log (activity_type, entity_type, entity_id, entity_reference, action_date, description, vendor_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (f'vendor_status_updated_{new_status}', 'vendor', vendor_pk, vendor_id, datetime.now(), f'Vendor status updated to: {new_status}', vendor_pk))
        
    conn.commit()
    conn.close()
    
    return {"status": "success", "message": f"Status vendor berhasil diubah menjadi {new_status}"}

# --- REQUISITIONS API ---

@app.post("/api/requisitions")
async def create_requisition(req: RequisitionCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) as count FROM requisitions")
        count = cursor.fetchone()['count']
        req_number = f"REQ-{datetime.now().strftime('%Y%m')}-{str(count + 1).zfill(3)}"
        
        cursor.execute('''
            INSERT INTO requisitions (
                req_number, req_type, sbu_name, title, description, budget_code, total_amount, created_by
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (req_number, req.req_type, req.sbu_name, req.title, req.description, req.budget_code, req.total_amount, req.created_by))
        
        conn.commit()
        return {"status": "success", "message": "Requisition berhasil dibuat", "req_number": req_number}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/requisitions")
async def get_requisitions(sbu: str = None, status: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM requisitions WHERE 1=1"
    params = []
    
    if sbu:
        query += " AND sbu_name = ?"
        params.append(sbu)
    if status:
        query += " AND status = ?"
        params.append(status)
        
    query += " ORDER BY id DESC"
    cursor.execute(query, params)
    
    reqs = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": reqs}

@app.post("/api/requisitions/{req_number}/approve")
async def approve_requisition(req_number: str, request: Request):
    data = await request.json()
    action = data.get("action") # approve or reject
    level = data.get("level") # kasie, manager, gm, dir_ops, dir_utama
    
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM requisitions WHERE req_number = ?", (req_number,))
        req = cursor.fetchone()
        if not req:
            raise HTTPException(status_code=404, detail="Requisition tidak ditemukan")
            
        if action == "reject":
            new_status = "rejected"
        else:
            amt = req['total_amount']
            is_jasa = req['req_type'].startswith('SPPJ')
            
            if level == "kasie": 
                new_status = "pending_manager"
            elif level == "manager": 
                if is_jasa:
                    new_status = "pending_gm" if amt > 25000000 else "approved_final"
                else:
                    new_status = "pending_gm" if amt > 10000000 else "approved_final"
            elif level == "gm": 
                if is_jasa:
                    new_status = "pending_dir_ops" if amt > 100000000 else "approved_final"
                else:
                    new_status = "pending_dir_ops" if amt > 25000000 else "approved_final"
            elif level == "dir_ops": 
                if is_jasa:
                    new_status = "pending_dir_utama" if amt > 1000000000 else "approved_final"
                else:
                    new_status = "pending_dir_utama" if amt > 50000000 else "approved_final"
            elif level == "dir_utama": 
                new_status = "approved_final"
            else: 
                new_status = "approved_final"
            
        cursor.execute("UPDATE requisitions SET status = ? WHERE req_number = ?", (new_status, req_number))
        
        # Log Activity
        cursor.execute("SELECT id FROM requisitions WHERE req_number = ?", (req_number,))
        req_id = cursor.fetchone()['id']
        cursor.execute('''
            INSERT INTO activity_log (activity_type, entity_type, entity_id, entity_reference, action_date, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (f'requisition_{new_status}', 'requisition', req_id, req_number, datetime.now(), f'{level} approved/rejected to {new_status}'))
        
        conn.commit()
        return {"status": "success", "message": f"Status diubah ke {new_status}"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# --- PURCHASE ORDERS API ---

@app.post("/api/purchase-orders")
async def create_purchase_order(po: PurchaseOrderCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) as count FROM purchase_orders")
        count = cursor.fetchone()['count']
        po_number = f"PO-{datetime.now().strftime('%Y%m')}-{str(count + 1).zfill(3)}"
        
        cursor.execute('''
            INSERT INTO purchase_orders (po_number, req_id, vendor_id, total_amount, status)
            VALUES (?, ?, ?, ?, 'issued')
        ''', (po_number, po.req_id, po.vendor_id, po.total_amount))
        
        # Update requisition status
        cursor.execute("UPDATE requisitions SET status = 'po_created' WHERE id = ?", (po.req_id,))
        
        conn.commit()
        return {"status": "success", "message": "Purchase Order berhasil diterbitkan", "po_number": po_number}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/purchase-orders")
async def get_purchase_orders(status: str = None, vendor_id: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT po.*, v.company_name as vendor_name FROM purchase_orders po LEFT JOIN vendors v ON po.vendor_id = v.vendor_id"
        params = []
        conditions = []
        if status:
            conditions.append("po.status = ?")
            params.append(status)
        if vendor_id:
            conditions.append("po.vendor_id = ?")
            params.append(vendor_id)
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " ORDER BY po.id DESC"
        cursor.execute(query, params)
        pos = [dict(row) for row in cursor.fetchall()]
        return {"status": "success", "data": pos}
    finally:
        conn.close()

# --- VENDOR PORTAL & KSO EVALUATION API ---

@app.get("/api/vendor-portal/{vendor_id}/pos")
async def get_vendor_pos(vendor_id: str):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT po.*, req.title, req.description 
        FROM purchase_orders po
        JOIN requisitions req ON po.req_id = req.id
        WHERE po.vendor_id = ?
        ORDER BY po.id DESC
    ''', (vendor_id,))
    
    pos = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": pos}

@app.post("/api/kso-evaluations/vendor")
async def create_vendor_evaluation(eval: VendorEvalCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        # Check if exists
        cursor.execute("SELECT id FROM kso_evaluations WHERE po_number = ?", (eval.po_number,))
        existing = cursor.fetchone()
        if existing:
            cursor.execute('''
                UPDATE kso_evaluations SET 
                vendor_score_delivery = ?, vendor_score_quality = ?, vendor_score_response = ?, vendor_remarks = ?, status = 'pending_qc'
                WHERE po_number = ?
            ''', (eval.score_delivery, eval.score_quality, eval.score_response, eval.remarks, eval.po_number))
        else:
            cursor.execute('''
                INSERT INTO kso_evaluations (
                    vendor_id, po_number, vendor_score_delivery, vendor_score_quality, vendor_score_response, vendor_remarks, status
                ) VALUES (?, ?, ?, ?, ?, ?, 'pending_qc')
            ''', (eval.vendor_id, eval.po_number, eval.score_delivery, eval.score_quality, eval.score_response, eval.remarks))
        
        conn.commit()
        return {"status": "success", "message": "Self-Reporting Vendor berhasil disimpan, menunggu validasi QC."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.post("/api/kso-evaluations/qc")
async def create_qc_evaluation(eval: QCEvalCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        qc_avg = (eval.score_delivery + eval.score_quality + eval.score_response) / 3.0
        
        # Check if vendor has self-reported
        cursor.execute("SELECT * FROM kso_evaluations WHERE po_number = ?", (eval.po_number,))
        existing = cursor.fetchone()
        
        deviation_flag = False
        final_score = qc_avg
        
        if existing and existing['vendor_score_delivery'] is not None:
            ven_avg = (existing['vendor_score_delivery'] + existing['vendor_score_quality'] + existing['vendor_score_response']) / 3.0
            if abs(ven_avg - qc_avg) > 15: # Deviation tolerance 15 points
                deviation_flag = True
            status = 'disputed' if deviation_flag else 'completed'
            
            cursor.execute('''
                UPDATE kso_evaluations SET 
                qc_evaluator_name = ?, qc_score_delivery = ?, qc_score_quality = ?, qc_score_response = ?, qc_remarks = ?,
                final_score = ?, deviation_flag = ?, status = ?
                WHERE po_number = ?
            ''', (eval.evaluator_name, eval.score_delivery, eval.score_quality, eval.score_response, eval.remarks, final_score, deviation_flag, status, eval.po_number))
            
        else:
            # PENALTY: Vendor did not self-report -> FINAL SCORE BECOMES 0.
            # Sistem didesain memaksa habit produktif vendor.
            deviation_flag = True
            final_score_penalty = 0.0
            status = 'completed_penalty' 
            cursor.execute('''
                INSERT INTO kso_evaluations (
                    vendor_id, po_number, qc_evaluator_name, qc_score_delivery, qc_score_quality, qc_score_response, qc_remarks,
                    final_score, deviation_flag, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 1, ?)
            ''', (eval.vendor_id, eval.po_number, eval.evaluator_name, eval.score_delivery, eval.score_quality, eval.score_response, eval.remarks, final_score_penalty, status))

        # Log Activity
        cursor.execute('''
            INSERT INTO activity_log (activity_type, entity_type, entity_id, entity_reference, action_date, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('kso_evaluation_qc_submitted', 'evaluation', eval.po_number, eval.po_number, datetime.now(), f'QC Evaluated PO {eval.po_number} with deviation={deviation_flag}'))
        
        conn.commit()
        return {"status": "success", "message": "Evaluasi QC berhasil disimpan", "final_score": final_score, "deviation": deviation_flag}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/kso-financials")
async def get_kso_financials():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    # Ambil metrik finansial
    cursor.execute('''
        SELECT m.*, v.company_name 
        FROM kso_metrics m
        JOIN vendors v ON m.vendor_id = v.vendor_id
    ''')
    metrics_raw = cursor.fetchall()
    
    # Ambil tarif
    cursor.execute('''
        SELECT t.test_name, t.price, t.vendor_id, v.company_name 
        FROM kso_tariffs t
        JOIN vendors v ON t.vendor_id = v.vendor_id
    ''')
    tariffs_raw = cursor.fetchall()
    
    conn.close()
    
    metrics = [dict(r) for r in metrics_raw]
    
    # Susun matriks perbandingan tarif
    # Bentuk akhir: [ {test_name: "Gamma GT", vendor1_price: 28000, vendor2_price: 26000, diff_amount: 2000, diff_percent: 7.7} ]
    tariffs_dict = {}
    for r in tariffs_raw:
        test_name = r['test_name']
        if test_name not in tariffs_dict:
            tariffs_dict[test_name] = {}
        tariffs_dict[test_name][r['vendor_id']] = r['price']
        
    return {"status": "success", "metrics": metrics, "tariffs": tariffs_dict}

@app.get("/api/kso-evaluations")
async def get_kso_evaluations(vendor_id: str = None, disputed_only: bool = False):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM kso_evaluations WHERE 1=1"
    params = []
    if vendor_id:
        query += " AND vendor_id = ?"
        params.append(vendor_id)
    if disputed_only:
        query += " AND deviation_flag = 1"
        
    query += " ORDER BY id DESC"
    cursor.execute(query, params)
    evals = [dict(row) for row in cursor.fetchall()]
    
    # Calculate average score per vendor if all
    averages = {}
    if not vendor_id:
        cursor.execute("SELECT vendor_id, AVG(final_score) as avg_score FROM kso_evaluations WHERE final_score IS NOT NULL GROUP BY vendor_id")
        averages = {row['vendor_id']: row['avg_score'] for row in cursor.fetchall()}
        
    conn.close()
    return {"status": "success", "data": evals, "averages": averages}


# =============================================================================
# VENDOR SCORECARD 7 DIMENSI API
# =============================================================================

@app.get("/api/vendor-scorecard")
async def get_all_vendor_scorecards():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.vendor_id, v.company_name, v.company_name_short,
            COUNT(e.id) as total_evaluations,
            AVG(CASE WHEN e.status != 'completed_penalty' THEN e.qc_score_delivery END)      as avg_delivery,
            AVG(CASE WHEN e.status != 'completed_penalty' THEN e.qc_score_quality END)       as avg_quality,
            AVG(CASE WHEN e.status != 'completed_penalty' THEN e.qc_score_response END)      as avg_response,
            AVG(CASE WHEN e.status != 'completed_penalty' THEN e.score_pricing END)          as avg_pricing,
            AVG(CASE WHEN e.status != 'completed_penalty' THEN e.score_compliance END)       as avg_compliance,
            AVG(CASE WHEN e.status != 'completed_penalty' THEN e.score_financial_health END) as avg_financial,
            AVG(CASE WHEN e.status != 'completed_penalty' THEN e.score_relationship END)     as avg_relationship,
            AVG(e.final_score) as avg_final,
            SUM(CASE WHEN e.deviation_flag=1 THEN 1 ELSE 0 END)           as total_disputes,
            SUM(CASE WHEN e.status='completed_penalty' THEN 1 ELSE 0 END) as total_penalties
        FROM kso_evaluations e JOIN vendors v ON e.vendor_id=v.vendor_id
        GROUP BY e.vendor_id ORDER BY avg_final DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    scorecards = []
    for r in rows:
        d = dict(r)
        ws = round(
            (d["avg_delivery"] or 0)*0.20 + (d["avg_quality"] or 0)*0.20 +
            (d["avg_response"] or 0)*0.15 + (d["avg_pricing"] or 0)*0.15 +
            (d["avg_compliance"] or 0)*0.15 + (d["avg_financial"] or 0)*0.10 +
            (d["avg_relationship"] or 0)*0.05, 2)
        d["weighted_score"] = ws
        d["star_rating"] = round(ws/20, 1)
        if ws >= 85:   d["badge"] = "Excellent";         d["badge_color"] = "emerald"
        elif ws >= 70: d["badge"] = "Good";              d["badge_color"] = "blue"
        elif ws >= 55: d["badge"] = "Needs Improvement"; d["badge_color"] = "yellow"
        else:          d["badge"] = "At Risk";            d["badge_color"] = "red"
        scorecards.append(d)
    return {"status": "success", "data": scorecards}


@app.get("/api/vendor-scorecard/{vendor_id}")
async def get_vendor_scorecard_detail(vendor_id: str):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendors WHERE vendor_id=?", (vendor_id,))
    vendor = cursor.fetchone()
    if not vendor:
        conn.close()
        raise HTTPException(status_code=404, detail="Vendor tidak ditemukan")
    cursor.execute("SELECT * FROM kso_evaluations WHERE vendor_id=? ORDER BY evaluation_date DESC", (vendor_id,))
    evals = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "vendor": dict(vendor), "evaluations": evals}


# =============================================================================
# DASHBOARD KPI API
# =============================================================================

@app.get("/api/dashboard-kpi")
async def get_dashboard_kpi():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as cnt FROM requisitions WHERE status NOT IN ('approved_final','rejected','po_created')")
    active_reqs = cursor.fetchone()["cnt"]
    cursor.execute("SELECT COALESCE(SUM(total_amount),0) as total FROM purchase_orders WHERE status='issued'")
    total_po_value = cursor.fetchone()["total"]
    cursor.execute("SELECT COUNT(*) as cnt FROM vendors WHERE vendor_status='approved'")
    active_vendors = cursor.fetchone()["cnt"]
    cursor.execute("SELECT COUNT(*) as total, SUM(CASE WHEN status='approved_final' THEN 1 ELSE 0 END) as approved FROM requisitions WHERE status IN ('approved_final','rejected','po_created')")
    sla_row = cursor.fetchone()
    sla_pct = round((sla_row["approved"]/max(sla_row["total"],1))*100,1) if sla_row["total"] else 100.0
    cursor.execute("SELECT COUNT(*) as cnt FROM tenders WHERE status IN ('published','closed')")
    active_tenders = cursor.fetchone()["cnt"]
    cursor.execute("SELECT e.vendor_id, v.company_name, AVG(e.final_score) as avg_score FROM kso_evaluations e JOIN vendors v ON e.vendor_id=v.vendor_id WHERE e.final_score IS NOT NULL AND e.status NOT IN ('completed_penalty','disputed') GROUP BY e.vendor_id ORDER BY avg_score DESC LIMIT 1")
    tv = cursor.fetchone()
    top_vendor = dict(tv) if tv else None
    cursor.execute("SELECT req_number,title,sbu_name,total_amount,status,created_at FROM requisitions WHERE status NOT IN ('approved_final','rejected','po_created') ORDER BY created_at ASC")
    pending_all = [dict(r) for r in cursor.fetchall()]
    sla_alerts = []
    for r in pending_all:
        try:
            created = datetime.fromisoformat(str(r["created_at"]).split(".")[0])
            days = (datetime.now()-created).days
            r["days_elapsed"] = days
            if days >= 10: sla_alerts.append(r)
        except Exception:
            pass
    cursor.execute("SELECT strftime('%Y-%m',created_at) as month, COUNT(*) as cnt FROM requisitions GROUP BY month ORDER BY month DESC LIMIT 6")
    monthly = list(reversed([dict(r) for r in cursor.fetchall()]))
    conn.close()
    return {"status": "success", "kpi": {
        "active_requisitions": active_reqs, "total_po_value": total_po_value,
        "active_vendors": active_vendors, "sla_compliance_pct": sla_pct,
        "active_tenders": active_tenders, "top_vendor": top_vendor,
        "sla_alerts": sla_alerts, "monthly_trend": monthly,
    }}


# =============================================================================
# TENDERS MANAGEMENT API
# =============================================================================

class TenderCreate(BaseModel):
    title: str
    category: str
    description: str = ""
    specifications: str = ""
    budget_max: float
    bid_closing_date: str
    expected_delivery_date: str = ""
    created_by: str = "Kasie Pengadaan"

@app.get("/api/tenders")
async def get_tenders(status: str = None, category: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    q = "SELECT * FROM tenders WHERE 1=1"; params = []
    if status:   q += " AND status=?";   params.append(status)
    if category: q += " AND category=?"; params.append(category)
    q += " ORDER BY created_at DESC"
    cursor.execute(q, params)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": rows}

@app.post("/api/tenders")
async def create_tender(t: TenderCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) as cnt FROM tenders")
        cnt = cursor.fetchone()["cnt"]
        yr = datetime.now().strftime('%Y')
        number = f"TND-{yr}-{str(cnt+1).zfill(3)}"
        cursor.execute(
            "INSERT INTO tenders (tender_number,title,category,description,specifications,budget_max,bid_closing_date,expected_delivery_date,created_by) VALUES (?,?,?,?,?,?,?,?,?)",
            (number, t.title, t.category, t.description, t.specifications, t.budget_max, t.bid_closing_date, t.expected_delivery_date, t.created_by))
        conn.commit()
        return {"status": "success", "tender_number": number, "message": "Tender berhasil dibuat"}
    except Exception as e:
        conn.rollback(); raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.post("/api/tenders/{tender_number}/status")
async def update_tender_status(tender_number: str, request: Request):
    data = await request.json()
    ns = data.get("status")
    if ns not in ["draft","published","closed","awarded","cancelled"]:
        raise HTTPException(status_code=400, detail="Status tidak valid")
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tenders SET status=?,updated_at=? WHERE tender_number=?", (ns, datetime.now(), tender_number))
    if cursor.rowcount == 0:
        conn.close(); raise HTTPException(status_code=404, detail="Tender tidak ditemukan")
    conn.commit(); conn.close()
    return {"status": "success", "message": f"Status diubah ke '{ns}'"}


# ==========================================
# COMMAND CENTER FULL GRID API (FASE 8 & 4)
# ==========================================

import time
import random
from datetime import datetime, timedelta

@app.get("/api/cc/payment-pipeline")
def get_cc_payment_pipeline():
    # Simulasi data payment pipeline yang bergerak
    total_pipeline = 5200000000
    return {
        "status": "success",
        "data": {
            "awaiting_approval": [
                {"id": "INV-2025-001", "amount": 200000000, "status": "PENDING", "due": (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")},
                {"id": "INV-2025-002", "amount": 150000000, "status": "PENDING", "due": (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")},
                {"id": "INV-2025-003", "amount": 100000000, "status": "PENDING", "due": (datetime.now() + timedelta(days=8)).strftime("%Y-%m-%d")},
            ],
            "processing_count": 2,
            "processing_amount": 800000000,
            "paid_count": 12,
            "paid_amount": 3950000000,
            "total_pipeline": total_pipeline,
            "cashflow": {
                "expected_outflow_30d": 920000000,
                "current_cash": 1200000000,
                "status": "OK"
            }
        }
    }

@app.get("/api/cc/budget-tracker")
def get_cc_budget_tracker():
    total_budget = 5000000000
    spent = 4200000000
    
    # Fluktuasi kecil untuk simulasi live data
    base_spent = spent + random.randint(-5000000, 5000000)
    
    return {
        "status": "success",
        "data": {
            "total_budget": total_budget,
            "spent": base_spent,
            "remaining": total_budget - base_spent,
            "spent_pct": round((base_spent / total_budget) * 100, 1),
            "breakdown": [
                {"category": "RS PKT Bontang", "spent": 1500000000, "budget": 1800000000, "pct": 83, "alert": "OK"},
                {"category": "RS PKT Prima Sangatta", "spent": 950000000, "budget": 1100000000, "pct": 86, "alert": "OK"},
                {"category": "RS PKT MUP (Bpp)", "spent": 800000000, "budget": 1100000000, "pct": 72, "alert": "WARNING"},
                {"category": "PT KMG Group", "spent": 950000000, "budget": 1000000000, "pct": 95, "alert": "CRITICAL"}
            ],
            "projected_ye": 5400000000,
            "projected_variance": 8
        }
    }

@app.get("/api/cc/transaction-log")
def get_cc_transaction_log():
    # Menghasilkan log transaksi palsu tapi terkesan live
    actions = [
        "Invoice verified", "PO sent to vendor", "Quote extracted",
        "BAPB approved", "Payment approved", "Vendor signed PO",
        "Tender closed", "Payment processed", "Invoice received"
    ]
    
    logs = []
    now = datetime.now()
    for i in range(15):
        past_time = now - timedelta(minutes=random.randint(1, 120), seconds=random.randint(0, 59))
        logs.append({
            "time": past_time.strftime("%H:%M:%S"),
            "action": random.choice(actions),
            "timestamp": past_time.timestamp()
        })
    
    # Sort logs by timestamp desc
    logs.sort(key=lambda x: x["timestamp"], reverse=True)
    
    return {
        "status": "success",
        "data": logs[:10]
    }

@app.get("/api/cc/system-status")
def get_cc_system_status():
    return {
        "status": "success",
        "data": {
            "procurement_system": "OPERATIONAL",
            "database": "RESPONSIVE",
            "latency_ms": random.randint(15, 65),
            "websocket": "CONNECTED",
            "subscribers": random.randint(18, 45),
            "email_service": "SENDING",
            "payment_gateway": "CONNECTED",
            "gl_integration": "SYNCED",
            "last_update": datetime.now().strftime("%H:%M:%S")
        }
    }


# ==========================================
# COMMAND CENTER V2 (KOMUNIKASI & KONTRAK)
# ==========================================

@app.get("/api/cc/contracts")
def get_cc_contracts():
    now = datetime.now()
    
    # Generate some dummy contracts
    contracts = [
        {"vendor": "PT Medik Jaya", "item": "KSO Lab Kimia", "start_date": "2023-01-15", "end_date": "2026-08-20"},
        {"vendor": "PT Farma Indonesia", "item": "Reagen Lab", "start_date": "2024-05-01", "end_date": "2027-04-30"},
        {"vendor": "PT Supply Chain", "item": "BMHP Consumables", "start_date": "2022-10-10", "end_date": "2025-09-10"},
        {"vendor": "PT. BEM (Borneo Etam Mandiri)", "item": "KSO Lab", "start_date": "2020-03-01", "end_date": "2025-02-28"},
        {"vendor": "PT Global Health", "item": "Maintenance Alkes", "start_date": "2025-01-01", "end_date": "2025-12-31"},
    ]
    
    for c in contracts:
        ed = datetime.strptime(c["end_date"], "%Y-%m-%d")
        days_left = (ed - now).days
        c["days_left"] = days_left
        
        if days_left < 0:
            c["status"] = "EXPIRED"
            c["alert"] = "CRITICAL"
        elif days_left <= 90:
            c["status"] = f"{days_left} Days Left"
            c["alert"] = "WARNING: Initiate Renewal Talks"
        elif days_left <= 180:
            c["status"] = f"{days_left} Days Left"
            c["alert"] = "PREPARE"
        else:
            months = days_left // 30
            c["status"] = f"{months} Months Left"
            c["alert"] = "OK"
            
    # Sort by days left
    contracts.sort(key=lambda x: x["days_left"])
    
    return {
        "status": "success",
        "data": contracts
    }

@app.get("/api/cc/communications")
def get_cc_communications():
    actions = [
        {"vendor": "PT Medik Jaya", "msg": "Negosiasi harga term termin 2", "tag": "NEGOTIATION", "color": "purple"},
        {"vendor": "PT Farma Indonesia", "msg": "Klarifikasi BAPB bulan lalu", "tag": "CLARIFICATION", "color": "blue"},
        {"vendor": "PT Supply Chain", "msg": "Keterlambatan pengiriman batch 4", "tag": "URGENT", "color": "red"},
        {"vendor": "PT. BEM (Borneo Etam Mandiri)", "msg": "Update jadwal preventive maintenance", "tag": "INFO", "color": "emerald"},
        {"vendor": "PT Mitra Sehat", "msg": "Pertanyaan spesifikasi tender X-Ray", "tag": "Q&A", "color": "cyan"}
    ]
    
    logs = []
    now = datetime.now()
    for i in range(5):
        past_time = now - timedelta(minutes=random.randint(1, 45))
        action = random.choice(actions)
        
        state = random.choice(["Menunggu Respon Vendor", "Menunggu Respon Internal", "Selesai"])
        
        logs.append({
            "time": past_time.strftime("%H:%M"),
            "vendor": action["vendor"],
            "message": action["msg"],
            "tag": action["tag"],
            "color": action["color"],
            "state": state,
            "timestamp": past_time.timestamp()
        })
    
    # Sort logs by timestamp desc
    logs.sort(key=lambda x: x["timestamp"], reverse=True)
    
    return {
        "status": "success",
        "data": logs
    }


# ==========================================
# VENDOR PORTAL API (EXTERNAL)
# ==========================================

@app.get("/api/vendor-portal-data")
def get_vendor_portal_data():
    now = datetime.now()
    
    return {
        "status": "success",
        "data": {
            "vendor_info": {
                "name": "PT Medik Jaya",
                "id": "VND-1001",
                "tier": "A-Grade Partner",
                "since": "2018"
            },
            "performance": {
                "overall_score": 87.5,
                "radar": {
                    "Delivery": 90,
                    "Quality": 95,
                    "Responsiveness": 75, # Yellow area
                    "Pricing": 85,
                    "Compliance": 80,
                    "Financial Health": 95,
                    "Relationship": 92
                },
                "feedback": "Kinerja medis sangat baik, namun respons unggah dokumen administratif (SJPH/BAPB) sering mendekati batas waktu SLA."
            },
            "tasks": [
                {
                    "id": "TSK-001",
                    "title": "Upload Surat Jalan (SJPH) - Reagen Batch 4",
                    "po_number": "PO-2026-105",
                    "deadline": (now + timedelta(hours=14)).strftime("%Y-%m-%d %H:%M"),
                    "status": "PENDING UPLOAD",
                    "penalty_warning": "-5pts Delivery & Compliance if late"
                },
                {
                    "id": "TSK-002",
                    "title": "Tanda Tangan Digital BAPB - MRI",
                    "po_number": "PO-2026-092",
                    "deadline": (now + timedelta(days=2)).strftime("%Y-%m-%d %H:%M"),
                    "status": "PENDING SIGNATURE",
                    "penalty_warning": "Payment hold if delayed"
                }
            ],
            "payments": [
                {
                    "invoice": "INV/MJ/26/01",
                    "amount": 450000000,
                    "status": "VERIFIED",
                    "timeline": ["SJPH (Done)", "BAPB (Done)", "Invoice Uploaded (Done)", "KMU Verified (Done)", "Payment Queue (Pending)"],
                    "est_payment": (now + timedelta(days=5)).strftime("%d %b %Y")
                },
                {
                    "invoice": "INV/MJ/26/02",
                    "amount": 120000000,
                    "status": "WAITING INVOICE",
                    "timeline": ["SJPH (Done)", "BAPB (Done)", "Upload Invoice (Pending)"],
                    "est_payment": "TBD"
                }
            ]
        }
    }


# ==========================================
# FINANCE & REALIZATION SPENDING PLANS API
# ==========================================

class SpendingPlanCreate(BaseModel):
    month_target: str
    project_title: str
    category: str
    sbu_name: str
    negotiated_price: float
    installation_fee: float
    testing_fee: float
    tax_pct: float = 11.0
    tax_amount: float
    shipping_cost: float
    total_amount: float
    dp_pct: float
    dp_amount: float

class PaymentScheduleUpdate(BaseModel):
    po_number: str
    dp_percentage: float
    dp_status: str
    dp_planned_date: str = None
    dp_realized_date: str = None
    remaining_status: str
    remaining_planned_date: str = None
    remaining_realized_date: str = None

@app.get("/api/procurement/spending-plans")
def get_spending_plans():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM investment_spending_plans ORDER BY id DESC")
    plans = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": plans}

@app.post("/api/procurement/spending-plans")
def create_spending_plan(sp: SpendingPlanCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO investment_spending_plans (
                month_target, project_title, category, sbu_name, negotiated_price,
                installation_fee, testing_fee, tax_pct, tax_amount, shipping_cost, total_amount, dp_pct, dp_amount
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            sp.month_target, sp.project_title, sp.category, sp.sbu_name, sp.negotiated_price,
            sp.installation_fee, sp.testing_fee, sp.tax_pct, sp.tax_amount, sp.shipping_cost,
            sp.total_amount, sp.dp_pct, sp.dp_amount
        ))
        conn.commit()
        return {"status": "success", "message": "Rencana belanja realisasi investasi berhasil disimpan"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/finance/pending-schedules")
def get_finance_schedules():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payment_schedules ORDER BY (dp_planned_date IS NULL) DESC, po_number DESC")
    schedules = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": schedules}

@app.post("/api/finance/save-schedule")
def save_finance_schedule(s: PaymentScheduleUpdate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            UPDATE payment_schedules SET
                dp_percentage = ?,
                dp_status = ?,
                dp_planned_date = ?,
                dp_realized_date = ?,
                remaining_status = ?,
                remaining_planned_date = ?,
                remaining_realized_date = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE po_number = ?
        ''', (
            s.dp_percentage, s.dp_status, s.dp_planned_date, s.dp_realized_date,
            s.remaining_status, s.remaining_planned_date, s.remaining_realized_date,
            s.po_number
        ))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="PO number tidak ditemukan")
        conn.commit()
        return {"status": "success", "message": "Jadwal dan progres pembayaran berhasil disimpan oleh Keuangan"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


# --- KSO MANAGEMENT & FINANCE BLOCKER ---

class KSODailyLog(BaseModel):
    vendor_id: str
    machine_id: str
    log_date: str
    high_control: str
    low_control: str
    technician_present: bool
    qc_verified_by_user: bool
    downtime_hours: int
    remarks: str

@app.get("/api/kso/contracts")
def get_kso_contracts():
    contracts = [
        {"id": "KSO-2026-001", "vendor_id": "VND-001", "vendor_name": "PT. BEM (Borneo Etam Mandiri)", "holding_agreement_valid": True, "expiry_date": "2026-08-15", "days_remaining": 64, "machine_count": 5, "score_current": 95.5},
        {"id": "KSO-2026-003", "vendor_id": "VND-008", "vendor_name": "PT. Global Medika", "holding_agreement_valid": True, "expiry_date": "2027-12-31", "days_remaining": 567, "machine_count": 8, "score_current": 92.5},
        {"id": "KSO-2026-008", "vendor_id": "VND-004", "vendor_name": "PT. EH Syam", "holding_agreement_valid": False, "expiry_date": "2026-05-30", "days_remaining": -13, "machine_count": 4, "score_current": 40.5}
    ]
    return {"status": "success", "data": contracts}

@app.post("/api/kso/daily-logs")
def submit_kso_daily_log(log: KSODailyLog):
    status = "Verified OK" if log.qc_verified_by_user else "Pending User Verification"
    return {"status": "success", "message": f"Log harian KSO tersimpan. Status: {status}"}

@app.get("/api/kso/daily-logs")
def get_kso_daily_logs(vendor_id: str = None):
    logs = [
        {"id": 1, "vendor_id": "VND-001", "machine_id": "HEMA-01 (Hematology)", "log_date": "2026-06-12", "high_control": "Pass", "low_control": "Pass", "technician_present": True, "qc_verified_by_user": True, "downtime_hours": 0, "remarks": "Mesin optimal"},
        {"id": 2, "vendor_id": "VND-008", "machine_id": "CHEM-01 (Chemistry)", "log_date": "2026-06-12", "high_control": "Pass", "low_control": "Pass", "technician_present": True, "qc_verified_by_user": True, "downtime_hours": 0, "remarks": "Mesin optimal"},
        {"id": 3, "vendor_id": "VND-009", "machine_id": "IMMU-01 (Immunoassay)", "log_date": "2026-06-12", "high_control": "Warning", "low_control": "Pass", "technician_present": False, "qc_verified_by_user": False, "downtime_hours": 4, "remarks": "Tidak ada teknisi standby (Mangkir)"}
    ]
    if vendor_id:
        logs = [l for l in logs if l["vendor_id"] == vendor_id]
    return {"status": "success", "data": logs}

@app.get("/api/kso/machines")
def get_kso_machines(vendor_id: str = None):
    machines = [
        {"id": "MCH-001", "vendor_id": "VND-009", "branch": "RS PKT Bontang", "agreed_count": 2, "actual_count": 4, "unapproved_additions": 2, "unapproved_reductions": 0, "status": "Violation Detected: Kesepakatan Diam-diam"},
        {"id": "MCH-002", "vendor_id": "VND-008", "branch": "Klinik Utama", "agreed_count": 1, "actual_count": 1, "unapproved_additions": 0, "unapproved_reductions": 0, "status": "Compliant"},
        {"id": "MCH-003", "vendor_id": "VND-001", "branch": "RS PKT Prima Sangatta", "agreed_count": 3, "actual_count": 3, "unapproved_additions": 0, "unapproved_reductions": 0, "status": "Compliant"}
    ]
    if vendor_id:
        machines = [m for m in machines if m["vendor_id"] == vendor_id]
    return {"status": "success", "data": machines}

@app.get("/api/finance/validate-payment")
def validate_finance_payment(vendor_id: str):
    if vendor_id == "VND-009":
        return {"status": "error", "blocked": True, "reason": "Dua Pelanggaran Berat: (1) Kontrak payung (Holding Agreement) tidak aktif. (2) Terdeteksi penambahan 2 alat diam-diam di RS PKT Bontang tanpa izin Holding. Pembayaran diblokir otomatis oleh Sistem Integritas."}
    return {"status": "success", "blocked": False, "message": "Kontrak tervalidasi."}


# =============================================================================
# PROKER BULANAN API (Rencana Realisasi — Bagian Umum → GM → Keuangan → Pengadaan)
# =============================================================================

class ProkerItemCreate(BaseModel):
    item_title: str
    kategori: str           # barang / jasa / kso
    bidang_pekerjaan: str   # lab / farmasi / bmhp / alkes / umum / jasa
    rkap_ref: str = ""
    estimasi_nilai: float
    target_bulan: str       # YYYY-MM
    target_vendor: str = ""
    keterangan: str = ""
    submitted_by: str

@app.get("/api/proker")
def get_proker(status: str = None, bulan: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    q = "SELECT * FROM proker_items WHERE 1=1"
    params = []
    if status:
        q += " AND status = ?"
        params.append(status)
    if bulan:
        q += " AND target_bulan = ?"
        params.append(bulan)
    q += " ORDER BY id DESC"
    cursor.execute(q, params)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": rows}

@app.post("/api/proker")
def create_proker_item(item: ProkerItemCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) as cnt FROM proker_items")
        cnt = cursor.fetchone()["cnt"]
        bulan_short = item.target_bulan.replace("-", "")
        code = f"PRK-{bulan_short}-{str(cnt + 1).zfill(3)}"
        cursor.execute('''
            INSERT INTO proker_items (item_code, item_title, kategori, bidang_pekerjaan,
                rkap_ref, estimasi_nilai, target_bulan, target_vendor, keterangan, submitted_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (code, item.item_title, item.kategori, item.bidang_pekerjaan,
              item.rkap_ref, item.estimasi_nilai, item.target_bulan,
              item.target_vendor, item.keterangan, item.submitted_by))
        conn.commit()
        return {"status": "success", "item_code": code, "message": "Item proker berhasil ditambahkan"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.post("/api/proker/{item_id}/status")
async def update_proker_status(item_id: int, request: Request):
    data = await request.json()
    action = data.get("action")   # gm_approve / keuangan_clear / reject
    actor  = data.get("actor", "System")
    catatan = data.get("catatan", "")

    valid_actions = {"gm_approve", "keuangan_clear", "reject"}
    if action not in valid_actions:
        raise HTTPException(status_code=400, detail="Action tidak valid")

    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM proker_items WHERE id = ?", (item_id,))
        item = cursor.fetchone()
        if not item:
            raise HTTPException(status_code=404, detail="Proker item tidak ditemukan")

        now = datetime.now()
        if action == "gm_approve":
            cursor.execute(
                "UPDATE proker_items SET status='approved_gm', approved_gm_by=?, approved_gm_at=? WHERE id=?",
                (actor, now, item_id))
        elif action == "keuangan_clear":
            cursor.execute(
                "UPDATE proker_items SET status='ready_pengadaan', cleared_keuangan_by=?, cleared_keuangan_at=?, catatan_keuangan=? WHERE id=?",
                (actor, now, catatan, item_id))
            # Kirim notifikasi ke vendor bidang terkait
            bidang = item["bidang_pekerjaan"]
            title = f"Peluang Pengadaan: {item['item_title']}"
            msg = (f"PT KMU membuka peluang pengadaan untuk bidang {bidang.upper()}. "
                   f"Estimasi nilai: Rp {item['estimasi_nilai']:,.0f}. "
                   f"Target realisasi: {item['target_bulan']}. "
                   f"Siapkan penawaran Anda melalui portal ini.")
            cursor.execute(
                "INSERT INTO vendor_notifications (vendor_category, title, message, priority, related_proker_id) VALUES (?, ?, ?, ?, ?)",
                (bidang, title, msg, "normal", item_id))
        elif action == "reject":
            cursor.execute("UPDATE proker_items SET status='rejected' WHERE id=?", (item_id,))

        conn.commit()
        return {"status": "success", "message": f"Status proker diubah: {action}"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()


# =============================================================================
# VENDOR NOTIFICATIONS API
# =============================================================================

@app.get("/api/notifications")
def get_notifications(vendor_category: str = None, unread_only: bool = False):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    q = "SELECT * FROM vendor_notifications WHERE 1=1"
    params = []
    if vendor_category:
        q += " AND vendor_category = ?"
        params.append(vendor_category)
    if unread_only:
        q += " AND is_read = 0"
    q += " ORDER BY created_at DESC LIMIT 20"
    cursor.execute(q, params)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": rows, "unread_count": len([r for r in rows if not r["is_read"]])}

@app.post("/api/notifications/{notif_id}/read")
def mark_notification_read(notif_id: int):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE vendor_notifications SET is_read = 1 WHERE id = ?", (notif_id,))
    conn.commit()
    conn.close()
    return {"status": "success"}


# =============================================================================
# BAPB API (Berita Acara Penerimaan Barang)
# =============================================================================

class BAPBCreate(BaseModel):
    po_number: str
    vendor_id: str
    received_date: str
    received_by: str
    items_json: str   # JSON string list of received items
    condition: str = "good"  # good / partial / rejected
    notes: str = ""

@app.get("/api/bapb")
def get_bapb(po_number: str = None, status: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    q = "SELECT * FROM bapb WHERE 1=1"
    params = []
    if po_number:
        q += " AND po_number = ?"
        params.append(po_number)
    if status:
        q += " AND status = ?"
        params.append(status)
    q += " ORDER BY id DESC"
    cursor.execute(q, params)
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": rows}

@app.post("/api/bapb")
def create_bapb(b: BAPBCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) as cnt FROM bapb")
        cnt = cursor.fetchone()["cnt"]
        bapb_number = f"BAPB-{datetime.now().strftime('%Y%m')}-{str(cnt + 1).zfill(3)}"
        cursor.execute('''
            INSERT INTO bapb (bapb_number, po_number, vendor_id, received_date, received_by,
                items_json, condition, notes, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'submitted')
        ''', (bapb_number, b.po_number, b.vendor_id, b.received_date,
              b.received_by, b.items_json, b.condition, b.notes))
        conn.commit()
        return {"status": "success", "bapb_number": bapb_number, "message": "BAPB berhasil disimpan"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# --- ARSIP DIGITAL & UPLOAD API ---

@app.post("/api/documents/upload")
async def upload_document(file: UploadFile = File(...), category: str = Form("Uncategorized")):
    try:
        cat_dir = os.path.join(UPLOADS_DIR, category)
        os.makedirs(cat_dir, exist_ok=True)
        safe_filename = file.filename.replace(" ", "_")
        file_path = os.path.join(cat_dir, safe_filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        relative_path = f"/uploads/{category}/{safe_filename}"
        
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO documents (file_name, file_path, category)
            VALUES (?, ?, ?)
        ''', (file.filename, relative_path, category))
        conn.commit()
        conn.close()
        return {"status": "success", "message": "File berhasil diupload", "path": relative_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/rkap/import-csv")
async def import_rkap_csv(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        decoded = contents.decode('utf-8')
        csv_reader = csv.reader(StringIO(decoded))
        headers = next(csv_reader, None)
        row_count = sum(1 for row in csv_reader)
        
        cat_dir = os.path.join(UPLOADS_DIR, "RKAP")
        os.makedirs(cat_dir, exist_ok=True)
        safe_filename = file.filename.replace(" ", "_")
        file_path = os.path.join(cat_dir, safe_filename)
        with open(file_path, "wb") as f:
            f.write(contents)
            
        relative_path = f"/uploads/RKAP/{safe_filename}"
        conn = database.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO documents (file_name, file_path, category)
            VALUES (?, ?, ?)
        ''', (file.filename, relative_path, "RKAP"))
        conn.commit()
        conn.close()
        
        return {
            "status": "success", 
            "message": f"Berhasil membaca {row_count} baris data RKAP",
            "rows_processed": row_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================================
# E-KATALOG INTERNAL & MLM COMPARISON API
# =============================================================================

@app.get("/api/catalogs")
def get_catalogs(vendor: str = None, q: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM internal_catalogs WHERE 1=1"
    params = []
    if vendor:
        query += " AND vendor_name = ?"
        params.append(vendor)
    if q:
        query += " AND item_name LIKE ?"
        params.append(f"%{q}%")
    query += " ORDER BY id DESC"
    cursor.execute(query, params)
    data = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": data}

@app.get("/api/finance/mlm-comparison")
def get_mlm_comparison():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mlm_price_comparisons ORDER BY id DESC")
    data = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": data}

# =============================================================================
# PROCUREMENT KPI & BOTTLENECK TRACKING
# =============================================================================

@app.get("/api/procurement/kpi-report")
def get_kpi_report():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    
    # Total Planned Items (RKAP)
    cursor.execute("SELECT COUNT(*) as count FROM proker_items")
    row = cursor.fetchone()
    total_planned = row['count'] if row else 0
    
    # Total Realized Items (PO with BAPB)
    cursor.execute("SELECT COUNT(DISTINCT po_number) as count FROM bapb")
    row = cursor.fetchone()
    total_realized = row['count'] if row else 0
    
    # Delayed Items due to Finance (Late DP > 30 days or Overdue)
    cursor.execute("SELECT po_number, project_title, dp_planned_date, dp_realized_date, dp_status FROM payment_schedules")
    schedules = cursor.fetchall()
    
    delayed_items = []
    
    for sched in schedules:
        po_num = sched['po_number']
        title = sched['project_title']
        planned = sched['dp_planned_date']
        realized = sched['dp_realized_date']
        status = sched['dp_status']
        
        if not planned: continue
            
        cursor.execute("SELECT id FROM bapb WHERE po_number = ?", (po_num,))
        if cursor.fetchone():
            continue
            
        reason = "Menunggu Proses Pengadaan"
        
        try:
            p_date = datetime.strptime(planned, "%Y-%m-%d")
            
            if status == "Belum Dibayar":
                if p_date < datetime.now():
                    reason = "Keterlambatan Pembayaran DP (Keuangan)"
                    delayed_items.append({"po": po_num, "item": title, "reason": reason, "planned_date": planned, "realized_date": "-"})
            elif status == "Sudah Dibayar" and realized:
                r_date = datetime.strptime(realized, "%Y-%m-%d")
                if (r_date - p_date).days > 30:
                    reason = "Keterlambatan Pembayaran DP (Keuangan) -> Pengiriman Mundur"
                    delayed_items.append({"po": po_num, "item": title, "reason": reason, "planned_date": planned, "realized_date": realized})
        except:
            pass

    conn.close()
    
    return {
        "status": "success",
        "data": {
            "total_planned": total_planned,
            "total_realized": total_realized,
            "total_delayed": len(delayed_items),
            "delayed_items": delayed_items
        }
    }

@app.post("/api/vendor-portal/upload-catalog")
async def upload_vendor_catalog(file: UploadFile = File(...), vendor_name: str = Form(...)):
    try:
        contents = await file.read()
        decoded = contents.decode('utf-8')
        csv_reader = csv.reader(StringIO(decoded))
        headers = next(csv_reader, None)
        
        conn = database.get_db_connection()
        cursor = conn.cursor()
        
        row_count = 0
        for row in csv_reader:
            if len(row) < 7: continue
            if not row[0].isdigit(): continue
            item_name = row[1]
            unit = row[2]
            sbu_name = row[3]
            # Clean price
            price_str = row[4]
            cleaned = re.sub(r'[^\d]', '', price_str)
            price = float(cleaned) if cleaned else 0.0
            brand = row[5]
            availability = row[6]
            
            cursor.execute('''
                INSERT INTO internal_catalogs (vendor_name, item_name, unit, sbu_name, price, brand, availability_status, year)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (vendor_name, item_name, unit, sbu_name, price, brand, availability, 2026))
            row_count += 1
            
        conn.commit()
        conn.close()
        return {"status": "success", "message": f"Berhasil mengimpor {row_count} item ke E-Katalog Internal."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class QuotationCreate(BaseModel):
    item_name: str
    target_realization_date: str

@app.post("/api/quotations")
def create_quotation(q: QuotationCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) as cnt FROM quotation_requests")
        cnt = cursor.fetchone()["cnt"]
        req_number = f"QUOT-{datetime.now().strftime('%Y%m')}-{str(cnt + 1).zfill(3)}"
        cursor.execute('''
            INSERT INTO quotation_requests (req_number, item_name, target_realization_date, status)
            VALUES (?, ?, ?, 'open')
        ''', (req_number, q.item_name, q.target_realization_date))
        quot_id = cursor.lastrowid
        conn.commit()
        return {"status": "success", "quotation_id": quot_id, "req_number": req_number}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/api/quotations")
def get_quotations():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quotation_requests ORDER BY id DESC")
    quotations = [dict(r) for r in cursor.fetchall()]
    for q in quotations:
        cursor.execute("SELECT * FROM quotation_bids WHERE quotation_id = ?", (q['id'],))
        q['bids'] = [dict(b) for b in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": quotations}

class BidCreate(BaseModel):
    vendor_name: str
    bid_price: float

@app.post("/api/quotations/{quot_id}/bids")
def add_bid(quot_id: int, b: BidCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO quotation_bids (quotation_id, vendor_name, bid_price)
            VALUES (?, ?, ?)
        ''', (quot_id, b.vendor_name, b.bid_price))
        conn.commit()
        return {"status": "success", "message": "Bid vendor berhasil ditambahkan"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

class ScoreUpdate(BaseModel):
    score_price: int
    score_quality: int
    score_service: int
    score_needs: int
    score_brand: int
    is_winner: bool = False

@app.put("/api/quotations/{quot_id}/bids/{bid_id}/score")
def update_score(quot_id: int, bid_id: int, s: ScoreUpdate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        total_score = s.score_price + s.score_quality + s.score_service + s.score_needs + s.score_brand
        cursor.execute('''
            UPDATE quotation_bids 
            SET score_price=?, score_quality=?, score_service=?, score_needs=?, score_brand=?, total_score=?, is_winner=?
            WHERE id=? AND quotation_id=?
        ''', (s.score_price, s.score_quality, s.score_service, s.score_needs, s.score_brand, total_score, s.is_winner, bid_id, quot_id))
        
        if s.is_winner:
            cursor.execute("SELECT vendor_name FROM quotation_bids WHERE id=?", (bid_id,))
            vendor = cursor.fetchone()["vendor_name"]
            cursor.execute("UPDATE quotation_requests SET status='awarded', awarded_vendor=? WHERE id=?", (vendor, quot_id))
            
        conn.commit()
        return {"status": "success", "message": "Skor berhasil diupdate"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# =============================================================================
# VENDOR APPROVE (endpoint unik, bukan duplikat)
# =============================================================================

@app.put("/api/vendors/{vendor_id}/approve")
def approve_vendor(vendor_id: str):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE vendors SET vendor_status = 'active' WHERE vendor_id = ?", (vendor_id,))
        conn.commit()
        return {"status": "success", "message": "Vendor berhasil disetujui"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# =============================================================================
# KSO CONTRACTS — path berbeda dari /api/kso/contracts (unik)
# =============================================================================

@app.get("/api/kso-contracts")
def get_kso_contracts_alt():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kso_contracts ORDER BY id DESC")
    contracts = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": contracts}

# =============================================================================
# RKAP DASHBOARD (Fase 1)
# =============================================================================

@app.get("/api/rkap/dashboard")
def get_rkap_dashboard():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rkap_sbu")
    sbus = [dict(r) for r in cursor.fetchall()]
    cursor.execute("SELECT * FROM rkap_categories")
    categories = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": {"sbu": sbus, "categories": categories}}

# =============================================================================
# INVOICES 3-WAY MATCH API (Fase 7)
# =============================================================================

class InvoiceCreate(BaseModel):
    inv_number: str
    po_number: str
    bapb_number: str
    inv_date: str
    inv_due_date: str = ""
    amount: float
    notes: str = ""

@app.get("/api/invoices")
def get_invoices():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT i.*, p.total_amount as po_amount, v.company_name as vendor_name
        FROM invoices i
        JOIN purchase_orders p ON i.po_number = p.po_number
        LEFT JOIN vendors v ON i.vendor_id = v.vendor_id
        ORDER BY i.id DESC
    ''')
    rows = [dict(r) for r in cursor.fetchall()]
    conn.close()
    formatted = []
    for r in rows:
        formatted.append({
            "inv": r["inv_number"], "po": r["po_number"], "bapb": r["bapb_number"],
            "vendor": r["vendor_name"] or "Unknown Vendor",
            "inv_amount": r["amount"], "po_amount": r["po_amount"],
            "status": "matched" if (r["match_po"] and r["match_bapb"]) else ("mismatch" if r["bapb_number"] else "pending")
        })
    return {"status": "success", "data": formatted}

@app.post("/api/invoices")
def create_invoice(inv: InvoiceCreate):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM purchase_orders WHERE po_number = ?", (inv.po_number,))
        po = cursor.fetchone()
        cursor.execute("SELECT * FROM bapb WHERE bapb_number = ?", (inv.bapb_number,))
        bapb = cursor.fetchone()
        if not po:
            raise HTTPException(status_code=404, detail="PO tidak ditemukan")
        vendor_id = po["vendor_id"]
        po_amount = po["total_amount"]
        match_po = (inv.amount == po_amount)
        match_bapb = (bapb is not None and bapb["po_number"] == inv.po_number)
        status = "matched" if (match_po and match_bapb) else ("mismatch" if inv.bapb_number else "pending")
        cursor.execute('''
            INSERT INTO invoices (inv_number, po_number, bapb_number, vendor_id, inv_date,
                inv_due_date, amount, notes, status, match_po, match_bapb)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (inv.inv_number, inv.po_number, inv.bapb_number, vendor_id, inv.inv_date,
              inv.inv_due_date, inv.amount, inv.notes, status, match_po, match_bapb))
        conn.commit()
        return {"status": "success", "message": "Invoice berhasil diproses 3-Way Match",
                "match_po": match_po, "match_bapb": match_bapb, "final_status": status}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

# =============================================================================
# RENCANA PEMBAYARAN VENDOR API (Laporan Finance)
# =============================================================================

@app.get("/api/finance/rencana-pembayaran")
def get_rencana_pembayaran(kategori: str = None, periode: str = None, status: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM rencana_pembayaran WHERE 1=1"
    params = []
    if kategori:
        query += " AND kategori = ?"
        params.append(kategori)
    if periode:
        query += " AND periode = ?"
        params.append(periode)
    if status:
        query += " AND status = ?"
        params.append(status)
    query += " ORDER BY CASE status WHEN 'URGENT' THEN 1 WHEN 'PRIORITAS' THEN 2 ELSE 3 END, id"
    cursor.execute(query, params)
    data = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": data}

@app.get("/api/finance/rencana-pembayaran/summary")
def get_rencana_pembayaran_summary(periode: str = "Juni 2026"):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT kategori,
               COUNT(*) as jumlah_item,
               SUM(jumlah) as total_nilai,
               SUM(CASE WHEN status = 'URGENT' THEN 1 ELSE 0 END) as urgent_count,
               SUM(CASE WHEN status = 'PRIORITAS' THEN 1 ELSE 0 END) as prioritas_count
        FROM rencana_pembayaran
        WHERE periode = ?
        GROUP BY kategori
    """, (periode,))
    rows = [dict(r) for r in cursor.fetchall()]
    cursor.execute("SELECT SUM(jumlah) as grand_total FROM rencana_pembayaran WHERE periode = ?", (periode,))
    grand = cursor.fetchone()
    conn.close()
    return {"status": "success", "periode": periode, "by_kategori": rows,
            "grand_total": grand["grand_total"] or 0}

@app.get("/api/finance/program-berjalan")
def get_program_berjalan():
    """Jasa Non Rutin ongoing — untuk proker, legal, ksu"""
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM rencana_pembayaran
        WHERE kategori IN ('jasa_non_rutin', 'kso_rutin', 'rental')
        ORDER BY link_legal DESC, link_ksu DESC, jumlah DESC
    """)
    data = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": data}

# =============================================================================
# RUP ITEMS API (RKAP Fase 1 — DataRUP)
# =============================================================================

@app.get("/api/rkap/rup-items")
def get_rup_items(metabisnis: str = None, kategori: str = None, bulan: str = None):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM rup_items WHERE 1=1"
    params = []
    if metabisnis:
        query += " AND metabisnis = ?"
        params.append(metabisnis)
    if kategori:
        query += " AND kategori = ?"
        params.append(kategori)
    if bulan:
        query += " AND bulan_target = ?"
        params.append(bulan)
    query += " ORDER BY trimester, no_item"
    cursor.execute(query, params)
    data = [dict(r) for r in cursor.fetchall()]
    conn.close()
    return {"status": "success", "data": data}

@app.get("/api/rkap/rup-summary")
def get_rup_summary():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT bulan_target,
               COUNT(*) as jumlah_item,
               SUM(nilai_total) as total_anggaran
        FROM rup_items
        GROUP BY bulan_target
        ORDER BY trimester, bulan_target
    """)
    by_bulan = [dict(r) for r in cursor.fetchall()]
    cursor.execute("""
        SELECT kategori, COUNT(*) as jumlah_item, SUM(nilai_total) as total_anggaran
        FROM rup_items GROUP BY kategori ORDER BY total_anggaran DESC
    """)
    by_kategori = [dict(r) for r in cursor.fetchall()]
    cursor.execute("SELECT SUM(nilai_total) as grand_total, COUNT(*) as total_item FROM rup_items")
    grand = dict(cursor.fetchone())
    conn.close()
    return {"status": "success", "by_bulan": by_bulan, "by_kategori": by_kategori,
            "grand_total": grand["grand_total"] or 0, "total_item": grand["total_item"] or 0}

# =============================================================================
# ANALITIK DASHBOARD (Fase 9) — dinamis dari rup_items + rencana_pembayaran
# =============================================================================

@app.get("/api/analytics/dashboard")
def get_analytics_dashboard():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as total_po FROM purchase_orders")
    total_po = cursor.fetchone()["total_po"] or 0

    cursor.execute("""
        SELECT bulan_target, SUM(nilai_total) as total
        FROM rup_items GROUP BY bulan_target ORDER BY trimester, bulan_target
    """)
    rup_rows = cursor.fetchall()

    cursor.execute("""
        SELECT kategori, SUM(nilai_total) as total
        FROM rup_items GROUP BY kategori ORDER BY total DESC
    """)
    kat_rows = cursor.fetchall()

    cursor.execute("SELECT SUM(jumlah) as total FROM rencana_pembayaran WHERE periode = 'Juni 2026'")
    realisasi_juni = cursor.fetchone()["total"] or 0
    conn.close()

    bulan_labels = [r["bulan_target"] for r in rup_rows] if rup_rows else ['Jan','Feb','Mar','Apr','Mei','Jun']
    anggaran_data = [round((r["total"] or 0) / 1_000_000) for r in rup_rows] if rup_rows else [500,600,550,700,650,800]
    kat_labels = [r["kategori"] for r in kat_rows] if kat_rows else ['Alat Kesehatan / KSO','Obat & Farmasi','IT & Infrastruktur','Umum & Jasa']
    kat_data = [round((r["total"] or 0) / 1_000_000) for r in kat_rows] if kat_rows else [45,25,15,15]

    return {
        "status": "success",
        "data": {
            "metrics": {
                "total_efficiency": 1200000000,
                "efficiency_pct": 8.5,
                "avg_lead_time": 14,
                "budget_realized_pct": 65,
                "total_po": total_po if total_po else 342,
                "realisasi_pembayaran_juni": realisasi_juni
            },
            "chartAnggaran": {"labels": bulan_labels, "anggaran": anggaran_data, "realisasi": anggaran_data},
            "chartKategori": {"labels": kat_labels, "data": kat_data}
        }
    }

# =============================================================================
# AUTH ENDPOINTS — Google OAuth + Vendor Verify
# =============================================================================

@app.post("/api/auth/google")
async def google_auth(request: Request):
    """
    Terima Google ID token dari frontend (GSI callback).
    Verifikasi ke Google tokeninfo, optional cek email vendor di DB.
    check_vendor=true → cari contact_person_email / email di tabel vendors.
    """
    import urllib.request as urllib_req
    body = await request.json()
    credential = body.get("credential", "")
    check_vendor = body.get("check_vendor", False)

    if not credential:
        raise HTTPException(status_code=400, detail="Token tidak ditemukan")

    try:
        loop = asyncio.get_event_loop()
        def _verify():
            url = f"https://oauth2.googleapis.com/tokeninfo?id_token={credential}"
            with urllib_req.urlopen(url, timeout=8) as r:
                return json.loads(r.read())

        info = await loop.run_in_executor(None, _verify)
        email = info.get("email", "")

        result = {
            "status": "success",
            "user": {
                "email": email,
                "name": info.get("name", ""),
                "picture": info.get("picture", ""),
                "email_verified": info.get("email_verified") == "true"
            },
            "vendor": None
        }

        if check_vendor and email:
            conn = database.get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT vendor_id, company_name, vendor_status, vendor_category
                   FROM vendors
                   WHERE contact_person_email = ? OR email = ?
                   LIMIT 1""",
                (email, email)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                result["vendor"] = dict(row)

        return result

    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Token Google tidak valid: {str(e)}")


@app.get("/api/vendors/verify/{vendor_id}")
async def verify_vendor_by_id(vendor_id: str):
    """Verifikasi Vendor ID spesifik — tidak expose data vendor lain."""
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """SELECT vendor_id, company_name, vendor_status, vendor_type, vendor_category
           FROM vendors WHERE vendor_id = ?""",
        (vendor_id.upper(),)
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Vendor ID tidak ditemukan")

    vendor = dict(row)
    if vendor["vendor_status"] != "approved":
        raise HTTPException(
            status_code=403,
            detail=f"Akun vendor belum aktif (status: {vendor['vendor_status']})"
        )

    return {"status": "success", "data": vendor}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000)


from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import sqlite3
import json
from datetime import datetime
import os
import database

app = FastAPI(title="Sistem Pengadaan Terintegrasi PT KMU", version="1.0")

@app.get("/")
def root():
    return RedirectResponse(url="/frontend/portal_hub.html")

# Mount frontend folder
frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')
app.mount("/frontend", StaticFiles(directory=frontend_path, html=True), name="frontend")

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


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
        {"id": "KSO-2026-003", "vendor_id": "VND-008", "vendor_name": "PT. EH Syam", "holding_agreement_valid": True, "expiry_date": "2027-12-31", "days_remaining": 567, "machine_count": 8, "score_current": 92.5},
        {"id": "KSO-2026-004", "vendor_id": "VND-009", "vendor_name": "PT. Rosche", "holding_agreement_valid": False, "expiry_date": "2026-05-30", "days_remaining": -13, "machine_count": 4, "score_current": 60.5}
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


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)

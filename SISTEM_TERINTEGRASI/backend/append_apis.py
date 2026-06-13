"""Script to append new API endpoints to main.py"""

new_code = r'''

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
'''

with open("main.py", "a", encoding="utf-8") as f:
    f.write(new_code)

with open("main.py", "r", encoding="utf-8") as f:
    total = len(f.readlines())
print(f"Done. main.py now has {total} lines.")

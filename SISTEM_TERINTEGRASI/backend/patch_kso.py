with open('c:/Users/Petugas/Claude/Projects/Pengadaan/04_SISTEM_TERINTEGRASI/backend/main.py', 'a', encoding='utf-8') as f:
    f.write('''

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
''')

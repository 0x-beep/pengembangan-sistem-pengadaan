import os

MAIN_PY = "main.py"

NEW_ENDPOINTS = """

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
"""

def main():
    if not os.path.exists(MAIN_PY):
        print(f"Error: {MAIN_PY} not found.")
        return

    with open(MAIN_PY, "r", encoding="utf-8") as f:
        content = f.read()

    if "/api/vendor-portal-data" in content:
        print("API endpoints already exist in main.py. Skipping.")
        return

    # Let's just append it to the end of the file
    with open(MAIN_PY, "a", encoding="utf-8") as f:
        f.write(NEW_ENDPOINTS)

    print("Successfully added Vendor Portal API endpoint to main.py")

if __name__ == "__main__":
    main()

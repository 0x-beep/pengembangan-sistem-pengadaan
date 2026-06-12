import os

MAIN_PY = "main.py"

NEW_ENDPOINTS = """

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
                {"category": "Equipment", "pct": 45, "alert": "OK"},
                {"category": "Medicine", "pct": 30, "alert": "WARNING"},
                {"category": "Services", "pct": 20, "alert": "CRITICAL"},
                {"category": "Other", "pct": 5, "alert": "OK"}
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
"""

def main():
    if not os.path.exists(MAIN_PY):
        print(f"Error: {MAIN_PY} not found.")
        return

    with open(MAIN_PY, "r", encoding="utf-8") as f:
        content = f.read()

    if "/api/cc/payment-pipeline" in content:
        print("API endpoints already exist in main.py. Skipping.")
        return

    # Let's just append it to the end of the file
    with open(MAIN_PY, "a", encoding="utf-8") as f:
        f.write(NEW_ENDPOINTS)

    print("Successfully added Command Center API endpoints to main.py")

if __name__ == "__main__":
    main()

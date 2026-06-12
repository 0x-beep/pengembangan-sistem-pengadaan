import os

MAIN_PY = "main.py"

NEW_ENDPOINTS = """

# ==========================================
# COMMAND CENTER V2 (KOMUNIKASI & KONTRAK)
# ==========================================

@app.get("/api/cc/contracts")
def get_cc_contracts():
    now = datetime.now()
    
    # Generate some dummy contracts
    contracts = [
        {"vendor": "PT Medik Jaya", "item": "KSO CT Scan", "start_date": "2023-01-15", "end_date": "2026-08-20"},
        {"vendor": "PT Farma Indonesia", "item": "Reagen Lab", "start_date": "2024-05-01", "end_date": "2027-04-30"},
        {"vendor": "PT Supply Chain", "item": "BMHP Consumables", "start_date": "2022-10-10", "end_date": "2025-09-10"},
        {"vendor": "PT Indo Medika", "item": "KSO MRI", "start_date": "2020-03-01", "end_date": "2025-02-28"},
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
        {"vendor": "PT Indo Medika", "msg": "Update jadwal preventive maintenance", "tag": "INFO", "color": "emerald"},
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
"""

def main():
    if not os.path.exists(MAIN_PY):
        print(f"Error: {MAIN_PY} not found.")
        return

    with open(MAIN_PY, "r", encoding="utf-8") as f:
        content = f.read()

    if "/api/cc/contracts" in content:
        print("API endpoints already exist in main.py. Skipping.")
        return

    # Let's just append it to the end of the file
    with open(MAIN_PY, "a", encoding="utf-8") as f:
        f.write(NEW_ENDPOINTS)

    print("Successfully added CC V2 API endpoints to main.py")

if __name__ == "__main__":
    main()

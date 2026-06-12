import json
import os
import glob
from datetime import datetime
import time
import pandas as pd

# Path configurations
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
INBOX_DIR = os.path.join(BASE_DIR, "Inbox_Data_KSO")
DASHBOARD_JSON = os.path.join(DATA_DIR, "dashboard_state.json")
RAPORT_JSON = os.path.join(DATA_DIR, "raport_state.json")

# Pastikan folder ada
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(INBOX_DIR, exist_ok=True)

def format_rupiah(value):
    try:
        return f"Rp {float(value):,.0f}".replace(",", ".")
    except:
        return "Rp 0"

def clean_col_name(cols):
    # Membersihkan nama kolom untuk antisipasi spasi atau huruf besar/kecil dari file asli
    return [str(c).strip().lower() for c in cols]

def process_evaluations():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Memindai folder Inbox: {INBOX_DIR}")
    
    # Cari semua file excel dan csv di dalam folder Inbox
    files_to_process = glob.glob(os.path.join(INBOX_DIR, "*.xlsx")) + glob.glob(os.path.join(INBOX_DIR, "*.csv"))
    
    if not files_to_process:
        print("[INFO] Tidak ada file data di dalam folder Inbox_Data_KSO. Menunggu file asli...")
        return

    dashboard_data = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_vendors": 0,
        "alarms": [],
        "resolved_logs": [],
        "vendors_overview": []
    }
    raports = {}

    try:
        for file_path in files_to_process:
            print(f"[INFO] Membaca file: {os.path.basename(file_path)}")
            
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            # Mapping nama kolom agar lebih fleksibel
            df.columns = clean_col_name(df.columns)
            
            # Cari kolom yang mirip
            col_vendor = next((c for c in df.columns if 'vendor' in c or 'kso' in c or 'nama' in c), None)
            col_bulan = next((c for c in df.columns if 'bulan' in c or 'periode' in c), 'Bulan')
            col_target_rp = next((c for c in df.columns if 'target' in c and ('rp' in c or 'uang' in c or 'finansial' in c or 'keuangan' in c)), None)
            if not col_target_rp: col_target_rp = next((c for c in df.columns if 'target' in c and 'vol' not in c), None)
            col_realisasi_rp = next((c for c in df.columns if 'realisasi' in c and ('rp' in c or 'uang' in c or 'finansial' in c or 'keuangan' in c)), None)
            if not col_realisasi_rp: col_realisasi_rp = next((c for c in df.columns if 'realisasi' in c and 'vol' not in c), None)
            
            col_target_vol = next((c for c in df.columns if 'target' in c and ('vol' in c or 'test' in c or 'pemeriksaan' in c)), None)
            col_realisasi_vol = next((c for c in df.columns if 'realisasi' in c and ('vol' in c or 'test' in c or 'pemeriksaan' in c)), None)
            
            col_tarif_kontrak = next((c for c in df.columns if 'tarif' in c and ('kontrak' in c or 'sepakat' in c or 'awal' in c)), None)
            col_tarif_aktual = next((c for c in df.columns if 'tarif' in c and ('aktual' in c or 'tagihan' in c or 'real' in c)), None)

            if not col_vendor:
                print(f"[WARNING] Tidak bisa menemukan kolom Vendor di file {os.path.basename(file_path)}. Melewati file ini.")
                continue

            for _, row in df.iterrows():
                vendor = str(row[col_vendor]).strip()
                if pd.isna(row[col_vendor]) or not vendor: continue
                
                bulan = str(row[col_bulan]).strip() if col_bulan in df.columns else "Periode Ini"
                
                target_rp = float(row[col_target_rp]) if col_target_rp and not pd.isna(row[col_target_rp]) else 0
                realisasi_rp = float(row[col_realisasi_rp]) if col_realisasi_rp and not pd.isna(row[col_realisasi_rp]) else 0
                target_vol = float(row[col_target_vol]) if col_target_vol and not pd.isna(row[col_target_vol]) else 0
                realisasi_vol = float(row[col_realisasi_vol]) if col_realisasi_vol and not pd.isna(row[col_realisasi_vol]) else 0
                tarif_kontrak = float(row[col_tarif_kontrak]) if col_tarif_kontrak and not pd.isna(row[col_tarif_kontrak]) else 0
                tarif_aktual = float(row[col_tarif_aktual]) if col_tarif_aktual and not pd.isna(row[col_tarif_aktual]) else 0

                dashboard_data["total_vendors"] += 1

                # 1. Kausalitas: Defisit Keuangan
                defisit_pct = 0
                if target_rp > 0 and realisasi_rp < target_rp:
                    defisit_pct = ((target_rp - realisasi_rp) / target_rp) * 100

                # 2. Kausalitas: Penurunan Volume
                vol_defisit_pct = 0
                if target_vol > 0 and realisasi_vol < target_vol:
                    vol_defisit_pct = ((target_vol - realisasi_vol) / target_vol) * 100

                # 3. Kausalitas: Anomali Harga
                anomali_harga = tarif_aktual > tarif_kontrak
                selisih_tarif = tarif_aktual - tarif_kontrak if anomali_harga else 0

                # -- Generate Alarms --
                if anomali_harga:
                    dashboard_data["alarms"].append({
                        "type": "CRITICAL",
                        "title": f"Kenaikan Tarif Tidak Terjadwal: {vendor}",
                        "desc": f"Ditemukan perbedaan tarif pada {vendor}. Tarif aktual {format_rupiah(tarif_aktual)} melebihi kontrak awal {format_rupiah(tarif_kontrak)}."
                    })
                
                if defisit_pct > 10:
                    dashboard_data["alarms"].append({
                        "type": "WARNING",
                        "title": f"Vendor {vendor} Melemah",
                        "desc": f"Realisasi {vendor} periode {bulan} baru mencapai {format_rupiah(realisasi_rp)} dari target {format_rupiah(target_rp)} (Defisit {defisit_pct:.0f}%)."
                    })
                
                if vol_defisit_pct > 15:
                    dashboard_data["alarms"].append({
                        "type": "INFO",
                        "title": f"Penurunan Volume Pemeriksaan: {vendor}",
                        "desc": f"Volume pemeriksaan {vendor} melambat. Realisasi {realisasi_vol} test dari target {target_vol} test."
                    })

                # -- Hitung Raport / Score --
                score_fin = min(50, (realisasi_rp / target_rp * 50)) if target_rp > 0 else 0
                score_vol = min(20, (realisasi_vol / target_vol * 20)) if target_vol > 0 else 0
                score_harga = 0 if anomali_harga else 30

                total_score = score_fin + score_vol + score_harga
                
                if total_score >= 90: grade = "A"; status = "Aman / Lanjutkan"
                elif total_score >= 80: grade = "B"; status = "Pantau Kinerja"
                elif total_score >= 60: grade = "C"; status = "Evaluasi (SP 1)"
                elif total_score >= 40: grade = "D"; status = "Sangat Kritis (SP 2)"
                else: grade = "E"; status = "Rekomendasi Putus Kontrak"

                raport_entry = {
                    "vendor": vendor,
                    "bulan": bulan,
                    "grade": grade,
                    "score": round(total_score, 1),
                    "status": status,
                    "metrics": {
                        "target_rp": format_rupiah(target_rp),
                        "realisasi_rp": format_rupiah(realisasi_rp),
                        "pencapaian_rp": f"{(realisasi_rp/target_rp*100) if target_rp > 0 else 0:.1f}%",
                        "target_vol": f"{target_vol} test",
                        "realisasi_vol": f"{realisasi_vol} test",
                        "pencapaian_vol": f"{(realisasi_vol/target_vol*100) if target_vol > 0 else 0:.1f}%",
                        "tarif_kontrak": format_rupiah(tarif_kontrak),
                        "tarif_aktual": format_rupiah(tarif_aktual),
                        "anomali_harga": anomali_harga
                    },
                    "scores": {
                        "finansial": round(score_fin, 1),
                        "volume": round(score_vol, 1),
                        "kepatuhan_harga": score_harga
                    }
                }

                raports[vendor] = raport_entry
                
                # Overview for dashboard
                dashboard_data["vendors_overview"].append({
                    "vendor": vendor,
                    "realisasi_rp": format_rupiah(realisasi_rp),
                    "target_rp": format_rupiah(target_rp),
                    "grade": grade,
                    "has_anomaly": anomali_harga
                })

        # Save to JSON
        with open(DASHBOARD_JSON, "w") as f:
            json.dump(dashboard_data, f, indent=4)
        
        with open(RAPORT_JSON, "w") as f:
            json.dump(raports, f, indent=4)
            
        print("[SUCCESS] Data dari Inbox berhasil diproses dan disimpan ke Dashboard.")

    except Exception as e:
        print(f"[ERROR] Engine gagal memproses data dari Inbox: {e}")

if __name__ == "__main__":
    print("========================================")
    print("KSO LAB EVALUATOR ENGINE")
    print(f"Folder Inbox: {INBOX_DIR}")
    print("Silakan COPY-PASTE file Excel/CSV asli Anda ke folder tersebut.")
    print("========================================")
    while True:
        process_evaluations()
        time.sleep(10)

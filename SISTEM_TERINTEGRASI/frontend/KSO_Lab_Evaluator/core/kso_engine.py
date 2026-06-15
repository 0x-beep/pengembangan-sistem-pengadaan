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
    return [str(c).strip().lower() for c in cols]

def process_evaluations():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Memindai folder Inbox: {INBOX_DIR}")
    
    # We also check DATA_DIR just in case for this demo
    files_to_process = glob.glob(os.path.join(INBOX_DIR, "*.xlsx")) + glob.glob(os.path.join(INBOX_DIR, "*.csv"))
    if not files_to_process:
        files_to_process = glob.glob(os.path.join(DATA_DIR, "data_input_kso.csv"))
        
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
    
    parsed_vendors = []

    try:
        for file_path in files_to_process:
            print(f"[INFO] Membaca file: {os.path.basename(file_path)}")
            
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            df.columns = clean_col_name(df.columns)

            for _, row in df.iterrows():
                if pd.isna(row.get('vendor')) or not str(row['vendor']).strip(): continue
                parsed_vendors.append(row)

        # Cross vendor analysis for inefficiency
        cheapest_vendor = None
        min_price = float('inf')
        for v in parsed_vendors:
            t = float(v.get('tarif_kontrak', 0))
            if t > 0 and t < min_price:
                min_price = t
                cheapest_vendor = str(v['vendor']).strip()

        for row in parsed_vendors:
            vendor = str(row['vendor']).strip()
            bulan = str(row.get('bulan', 'Periode Ini')).strip()
            cabang = str(row.get('cabang', 'Semua Cabang')).strip()
            pemeriksaan = str(row.get('pemeriksaan', 'General')).strip()
            
            kehadiran = float(row.get('kehadiran_teknisi_pct', 0))
            reagen = float(row.get('ketersediaan_reagen_pct', 0))
            telat_bayar = str(row.get('keterlambatan_bayar_kmu', 'FALSE')).upper() == 'TRUE'
            
            tarif_kontrak = float(row.get('tarif_kontrak', 0))
            tarif_aktual = float(row.get('tarif_aktual', 0))
            vol = float(row.get('volume_pemeriksaan', 0))
            
            tagihan_ilegal = str(row.get('tagihan_alat_ilegal', 'FALSE')).upper() == 'TRUE'
            sla_rusak = str(row.get('sla_rusak_lebih_2hari', 'FALSE')).upper() == 'TRUE'

            dashboard_data["total_vendors"] += 1

            # 1. Kausalitas Harga (Kepatuhan Kontrak)
            anomali_harga = tarif_aktual > tarif_kontrak
            if anomali_harga:
                dashboard_data["alarms"].append({
                    "type": "CRITICAL",
                    "title": f"Anomali Tarif: {vendor}",
                    "desc": f"Tarif aktual {format_rupiah(tarif_aktual)} melebihi kesepakatan kontrak {format_rupiah(tarif_kontrak)}."
                })
                
            # 2. Inefisiensi Harga Lintas Vendor
            if cheapest_vendor and vendor != cheapest_vendor and vol > 1000:
                dashboard_data["alarms"].append({
                    "type": "WARNING",
                    "title": f"Inefisiensi Distribusi Volume: {vendor} di {cabang}",
                    "desc": f"Cabang {cabang} memakai alat {vendor} lebih banyak ({vol} test) padahal tarif {cheapest_vendor} lebih murah untuk pemeriksaan {pemeriksaan}. Perlu penjelasan dari Kasie Lab {cabang}."
                })

            # 3. Kepatuhan Maintenance / Teknisi
            if kehadiran < 80:
                dashboard_data["alarms"].append({
                    "type": "WARNING",
                    "title": f"Kehadiran Teknisi Rendah: {vendor}",
                    "desc": f"Teknisi {vendor} jarang melakukan kontrol alat (hanya {kehadiran}% kehadiran)."
                })

            # 4. Ketersediaan Reagen
            if reagen < 90:
                if telat_bayar:
                    dashboard_data["alarms"].append({
                        "type": "INFO",
                        "title": f"Stok Reagen Rendah (Dimaklumi): {vendor}",
                        "desc": f"Ketersediaan reagen {vendor} menurun ({reagen}%), namun ini akibat keterlambatan pembayaran dari pihak KMU."
                    })
                else:
                    dashboard_data["alarms"].append({
                        "type": "CRITICAL",
                        "title": f"Krisis Stok Reagen: {vendor}",
                        "desc": f"Ketersediaan reagen {vendor} kritis di {reagen}% tanpa alasan keterlambatan bayar."
                    })
                    
            # 5. Tagihan Alat Ilegal
            if tagihan_ilegal:
                dashboard_data["alarms"].append({
                    "type": "CRITICAL",
                    "title": f"Tagihan Alat Ilegal Terdeteksi: {vendor}",
                    "desc": f"Ditemukan tagihan untuk alat yang belum terdaftar di kontrak PKS KSO. Butuh investigasi Legal & SPI."
                })
                
            # 6. SLA Kerusakan
            if sla_rusak:
                dashboard_data["alarms"].append({
                    "type": "CRITICAL",
                    "title": f"Pelanggaran SLA Perbaikan: {vendor}",
                    "desc": f"Alat rusak lebih dari 2x24 jam tanpa solusi perbaikan yang jelas. Operasional terganggu!"
                })

            # -- Hitung Raport / Score --
            # Bobot: Teknisi(40%), Reagen(40%), Kepatuhan Harga(20%)
            score_teknisi = kehadiran * 0.40
            
            # Jika telat bayar KMU = TRUE, maka jangan penalti reagen, anggap 100% (atau setidaknya tetap full score 40)
            reagen_calc = 100 if telat_bayar else reagen
            score_reagen = reagen_calc * 0.40
            
            score_harga = 0 if anomali_harga else 20
            
            # Pengurangan Pinalti Tambahan
            if sla_rusak: score_teknisi -= 15 # Penalti berat
            if tagihan_ilegal: score_harga = 0
            
            # Batasi minimal 0
            score_teknisi = max(0, score_teknisi)
            score_reagen = max(0, score_reagen)
            score_harga = max(0, score_harga)

            total_score = score_teknisi + score_reagen + score_harga
            
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
                    "kehadiran": f"{kehadiran}%",
                    "reagen": f"{reagen}%",
                    "telat_bayar": telat_bayar,
                    "tarif_kontrak": format_rupiah(tarif_kontrak),
                    "tarif_aktual": format_rupiah(tarif_aktual),
                    "anomali_harga": anomali_harga,
                    "tagihan_ilegal": tagihan_ilegal,
                    "sla_rusak": sla_rusak,
                    "volume_info": f"{vol} test (Utk Analisa Efisiensi)"
                },
                "scores": {
                    "teknisi": round(score_teknisi, 1),
                    "reagen": round(score_reagen, 1),
                    "harga": round(score_harga, 1)
                }
            }

            raports[vendor] = raport_entry
            
            dashboard_data["vendors_overview"].append({
                "vendor": vendor,
                "info_kehadiran": f"Teknisi: {kehadiran}%",
                "info_reagen": f"Reagen: {reagen}%",
                "grade": grade,
                "has_anomaly": anomali_harga or tagihan_ilegal or sla_rusak
            })

        with open(DASHBOARD_JSON, "w") as f:
            json.dump(dashboard_data, f, indent=4)
        
        with open(RAPORT_JSON, "w") as f:
            json.dump(raports, f, indent=4)
            
        print("[SUCCESS] Data berhasil diproses dan disimpan ke Dashboard.")

    except Exception as e:
        print(f"[ERROR] Engine gagal memproses data: {e}")

if __name__ == "__main__":
    process_evaluations()

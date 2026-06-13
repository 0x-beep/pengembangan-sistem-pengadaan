# PEDOMAN INTEGRASI & HANDOFF SISTEM (TIM IT PT KMU)

Dokumen ini disusun sebagai **Blueprint Teknis** yang harus diacu oleh Tim IT PT KMU dalam melakukan *coding*, *bridging*, dan *deployment* Sistem Ekosistem Digitalisasi Terintegrasi KMU.

Dokumen ini memuat *hardcode logic* (Aturan GCG) yang **tidak boleh diubah tanpa persetujuan BOD**, karena menyangkut kepatuhan (*compliance*) dan tata kelola perusahaan.

---

## 1. Arsitektur Multi-Portal
Aplikasi ini dipecah menjadi 3 (tiga) gerbang utama (*entry point*) untuk memastikan isolasi data dan keamanan. Tim IT wajib melakukan pemisahan *routing* dan otentikasi (JWT/Session) berdasarkan *Role* berikut:

1. **Portal Internal (Holding)** `(/holding)`
   - *Akses:* BOD, SPI, GM Operasional, Manager Pengadaan, Kasie, Finance, Komite Anggaran.
   - *Fungsi:* Approval berjenjang (Fase 1-9), Peta Keuangan (Swimlane), Audit Investigasi.
2. **Portal Unit Bisnis** `(/unit-bisnis)`
   - *Akses:* Kepala RS (Bontang, Prima, MUP), PT KMG, PT KMUS.
   - *Fungsi:* Keranjang E-Catalogue (PR), BAPB (Penerimaan), Lapor Volume Pasien KSO harian.
3. **Portal Vendor B2B** `(/vendor)`
   - *Akses:* Vendor KSO, Vendor Farmasi, Vendor Umum.
   - *Fungsi:* Input *Maintenance* KSO, Upload Bukti *Expired Date* (ED) dan CoA Farmasi, *Generate* Tagihan.

---

## 2. Hardcode Aturan GCG (Otonom)
*Logic* berikut wajib diimplementasikan di level *backend* (API) untuk memastikan tidak ada intervensi manusia (Sistem Otonom).

### A. Algoritma Sentralisasi & Desentralisasi (Routing PR)
Sistem harus mendeteksi total nilai pesanan (PR) dari keranjang E-Catalogue Unit Bisnis:
- **Kategori Alkes:**
  - Jika $\le$ Rp 5.000.000 $\rightarrow$ Status: `DESENTRALISASI` (Oto-Approval Kepala Cabang, langsung lempar PO ke Vendor).
  - Jika $>$ Rp 5.000.000 $\rightarrow$ Status: `SENTRALISASI` (PR dialihkan ke *Inbox* Manager Pengadaan Holding untuk dieksekusi terpusat).
- **Kategori Non-Alkes (Umum):**
  - Jika $\le$ Rp 2.000.000 $\rightarrow$ `DESENTRALISASI`.
  - Jika $>$ Rp 2.000.000 $\rightarrow$ `SENTRALISASI`.

### B. Pemblokiran Expired Date (Farmasi)
- Saat Vendor menekan tombol **"Kirim Barang"**, sistem *wajib* memvalidasi input `expired_date`.
- Jika `expired_date` < 6 bulan dari tanggal pengiriman, *throw error* dan matikan tombol (Blokir).

### C. Raport Kinerja Vendor KSO (Skoring Otomatis)
Nilai Vendor bukan input manual, melainkan kalkulasi dari:
1. **SLA Response Time:** Waktu dari pelaporan *trouble* di Portal RS hingga Vendor merespons/klik "Perbaikan Selesai" di Portal Vendor. Target KSU = 95%.
2. **Kepatuhan Kalibrasi:** Apakah Vendor meng-upload Bukti Sertifikat Kalibrasi pada bulan jatuh temponya. Jika lewat bulan, skor minus.

---

## 3. Kamus Data & Database Schema
Tim IT wajib menyediakan/menyesuaikan skema tabel (RDBMS: PostgreSQL/MySQL) berikut:

1. **`tb_requisitions` (Tabel PR/Permintaan)**
   - `routing_type` (Enum: `SENTRALISASI`, `DESENTRALISASI`)
   - `sbu_id` (Relasi ke entitas cabang, misal PT KMG)
   - `total_amount` (Dasar kalkulasi *routing*)

2. **`tb_kso_contracts` (Tabel Kontrak Alat KSO)**
   - `schema_type` (Enum: `COST_PER_TEST`, `REVENUE_SHARING`)
   - `unit_price` / `sharing_percentage` (Sesuai kesepakatan KSU)
   - `penalty_clause` (JSON object opsi denda fleksibel)

3. **`tb_kso_daily_logs` (Tabel Log Harian Alat)**
   - Diisi oleh vendor: `activity_type` (Maintenance, Kalibrasi, Perbaikan).
   - Diisi oleh RS: `patient_volume` (Jumlah utilisasi hari itu).

---

## 4. Panduan Bridging ke SIM RS (Existing)
Agar sistem tidak berdiri sendiri, integrasikan dengan SIM RS melalui REST API:
1. **Endpoint Tarik Data Pasien KSO:** `/api/simrs/utilisasi-alat` (Untuk *auto-fill* jumlah volume di `rs_klinik_dashboard.html`).
2. **Endpoint Tarik Data Hutang Piutang (BPJS):** `/api/finance/receivables` (Untuk diumpankan ke Node Peta Keuangan Swimlane *Holding* agar Komite Anggaran tahu posisi uang masuk).

---
*Dokumen ini bersifat teknikal-final. Tim Pengembang diinstruksikan untuk menggunakan _mockup_ HTML di folder `/frontend/` sebagai panduan UI/UX mutlak.*

# MASTER BLUEPRINT
# SISTEM DIGITALISASI PENGADAAN KMU TERINTEGRASI
## PT Kaltim Medika Utama (Holding) — RS PKT Group

**Versi:** 1.0 — Master Architecture  
**Tanggal:** Juni 2026  
**Status:** DOKUMEN INDUK — SUMBER KEBENARAN TUNGGAL SISTEM  
**Pemilik:** Departemen Pengadaan Umum dan Jasa PT KMU

---

## FILOSOFI SISTEM

> **"Pengadaan bukan transaksi. Pengadaan adalah siklus hidup yang tidak pernah berhenti."**

Sistem ini bukan kumpulan aplikasi yang berdiri sendiri. Ini adalah satu organisme digital yang bernapas: setiap output dari satu fase menjadi input fase berikutnya, dan setiap akhir siklus langsung memulai siklus berikutnya — tanpa henti, semakin cerdas, semakin efisien dari waktu ke waktu.

---

## ARSITEKTUR MASTER: SIKLUS PENGADAAN KMU

```
╔══════════════════════════════════════════════════════════════════════════════════╗
║           SISTEM DIGITALISASI PENGADAAN KMU — MASTER LOOP                       ║
║                                                                                  ║
║   ┌─────────────────────────────────────────────────────────────────────────┐   ║
║   │              [LAPISAN AI PENJAGA KEPATUHAN SPO]                         │   ║
║   │   Memvalidasi SETIAP aksi di SETIAP modul secara real-time             │   ║
║   └─────────────────────────────────────────────────────────────────────────┘   ║
║   ┌─────────────────────────────────────────────────────────────────────────┐   ║
║   │              [LAPISAN COMMAND CENTER DASHBOARD]                         │   ║
║   │   Memantau SEMUA modul secara real-time — satu layar untuk Direksi     │   ║
║   └─────────────────────────────────────────────────────────────────────────┘   ║
║   ┌─────────────────────────────────────────────────────────────────────────┐   ║
║   │              [LAPISAN AUDIT TRAIL & PELAPORAN]                          │   ║
║   │   Merekam SEMUA kejadian — dasar laporan & keputusan strategis         │   ║
║   └─────────────────────────────────────────────────────────────────────────┘   ║
║                                                                                  ║
║                        ╔═══════════════════╗                                     ║
║              ┌─────────║   [0] DIREKSI     ║─────────┐                          ║
║              │         ║   Kebijakan &     ║         │                          ║
║              │  Arahan ║   Keputusan       ║ Laporan │                          ║
║              │         ║   Strategis       ║         │                          ║
║              ↓         ╚═══════════════════╝         ↑                          ║
║   ┌──────────────────┐               ┌───────────────────────┐                  ║
║   │ [1] PERENCANAAN  │               │ [9] PELAPORAN &       │                  ║
║   │ & ANGGARAN       │               │ ANALITIK              │                  ║
║   │                  │               │                       │                  ║
║   │ RKAP, RAB,       │               │ Laporan Bulanan/      │                  ║
║   │ Kebutuhan SBU,   │               │ Triwulan/Tahunan,     │                  ║
║   │ Budget Ceiling   │               │ Financial Impact,     │                  ║
║   └────────┬─────────┘               │ Audit Trail           │                  ║
║            │                         └───────────┬───────────┘                  ║
║            │ Kebutuhan & Budget                  ↑ Data Semua Transaksi          ║
║            ↓                                     │                              ║
║   ┌──────────────────┐               ┌───────────────────────┐                  ║
║   │ [2] REGISTRASI & │               │ [8] EVALUASI VENDOR   │                  ║
║   │ DATABASE VENDOR  │               │                       │                  ║
║   │                  │               │ 7 Dimensi Scoring:    │                  ║
║   │ Kualifikasi,     │               │ Delivery, Kualitas,   │                  ║
║   │ Checklist Legal, │               │ Harga, Kepatuhan,     │                  ║
║   │ Master Database, │               │ Finansial, Respons,   │                  ║
║   │ Status Vendor    │               │ Kemitraan             │                  ║
║   └────────┬─────────┘               └───────────┬───────────┘                  ║
║            │                                     │                              ║
║            │ Pool Vendor Terverifikasi            │ Feedback: Renewal/           ║
║            │                                     │ Blacklist/Improvement        ║
║            ↓                                     ↑                              ║
║   ┌──────────────────┐               ┌───────────────────────┐                  ║
║   │ [3] PERMINTAAN   │               │ [7] PEMBAYARAN &      │                  ║
║   │ PENGADAAN        │               │ INVOICE               │                  ║
║   │                  │               │                       │                  ║
║   │ IMT (investasi)  │               │ DP & Pelunasan,       │                  ║
║   │ PP (barang umum) │               │ 3-Way Match           │                  ║
║   │ SPPJ (jasa)      │               │ (PO-BAPB-Invoice),    │                  ║
║   │ dari SBU/Unit    │               │ GL Posting Keuangan   │                  ║
║   └────────┬─────────┘               └───────────┬───────────┘                  ║
║            │                                     ↑                              ║
║            │ Trigger Proses Pengadaan            │ Invoice Terverifikasi         ║
║            ↓                                     │                              ║
║   ┌──────────────────┐               ┌───────────────────────┐                  ║
║   │ [4] PELAKSANAAN  │               │ [6] PENERIMAAN &      │                  ║
║   │ PENGADAAN        │               │ VERIFIKASI            │                  ║
║   │ (PROSES TENDER)  │               │                       │                  ║
║   │                  │               │ BAPB, QC Barang/Jasa, │                  ║
║   │ SPPH→Aanwijzing  │               │ 3-Way Match Check,    │                  ║
║   │ →SJPH→Bidding    │               │ Konfirmasi Selesai    │                  ║
║   │ →Negosiasi       │               │ ke Unit yang Meminta  │                  ║
║   │ →PO/SPK/PKS      │               └───────────┬───────────┘                  ║
║   └────────┬─────────┘                           ↑                              ║
║            │                                     │                              ║
║            │ Kontrak Aktif                       │ Barang/Jasa Diterima          ║
║            ↓                                     │                              ║
║   ┌──────────────────────────────────────────────┘                              ║
║   │ [5] PELAKSANAAN KONTRAK & PORTAL VENDOR KSO                                 ║
║   │                                                                             ║
║   │ • Vendor self-report via Portal KMU: maintenance harian/bulanan/tahunan    ║
║   │ • Tracking konsumabel: BHP, BMHP, Reagen — sesuai jadwal KSO              ║
║   │ • KMU verifikasi laporan vendor secara digital                             ║
║   │ • Eskalasi otomatis jika kewajiban vendor tidak terpenuhi                 ║
║   └─────────────────────────────────────────────────────────────────────────────║
╚══════════════════════════════════════════════════════════════════════════════════╝
```

---

## PENJELASAN 9 FASE SIKLUS

### ════ FASE 0: DIREKSI — PUSAT KENDALI STRATEGIS ════

**Posisi dalam siklus:** Puncak dan penutup siklus — menerima laporan, mengeluarkan arahan.

**Input yang diterima:**
- Laporan bulanan/triwulan/tahunan dari Modul 9 (Pelaporan)
- Hasil evaluasi vendor dari Modul 8
- Alert kritis dari Command Center Dashboard
- Rekomendasi dari Manager Pengadaan

**Keputusan yang dihasilkan:**
- Pengesahan RKAP untuk siklus berikutnya → masuk Modul 1
- Kebijakan baru / perubahan SPO → masuk AI Penjaga Kepatuhan
- Keputusan strategis vendor (KSO lanjut/putus, blacklist) → masuk Modul 2
- Prioritas pengadaan investasi → masuk Modul 1

**Kenapa ini looping:** Setiap keputusan Direksi langsung menjadi input untuk siklus berikutnya.

---

### ════ FASE 1: PERENCANAAN & ANGGARAN ════

**Dokumen referensi:** PROCUREMENT_PLATFORM_BLUEPRINT_v2.0.md (Business Context)  
**Pengelola:** Manager Pengadaan + Komite Anggaran + Kepala SBU

**Input yang masuk:**
- Keputusan strategis Direksi (Fase 0)
- Hasil evaluasi vendor siklus sebelumnya (Fase 8) — vendor mana yang masih andal
- Laporan realisasi anggaran siklus lalu (Fase 9)

**Proses:**
```
Semua SBU/Unit ajukan kebutuhan tahunan
           ↓
Kompilasi master kebutuhan (barang & jasa)
           ↓
Kategorisasi: Reguler / Urgent / Investasi
           ↓
RKAP disusun → Komite Anggaran review
           ↓
Direksi sahkan → Budget ceiling per kategori ditetapkan
```

**Output yang keluar:**
- RKAP yang disahkan → jadi batas atas semua pengadaan
- RAB per proyek/kebutuhan → syarat proses SPPJ
- Daftar prioritas pengadaan investasi → trigger Fase 3

**Pengaruh ke modul lain:**
- Budget ceiling membatasi nilai PO/SPK di Fase 4
- Perencanaan jasa besar trigger evaluasi vendor lebih awal di Fase 2

---

### ════ FASE 2: REGISTRASI & DATABASE VENDOR ════

**Dokumen referensi:** VENDOR_MASTER_DATABASE_KSO_MODULE.md, VENDOR_REGISTRATION_REQUIREMENTS_CHECKLIST_KALTIM.md, VENDOR_FORM_USAGE_GUIDE.md  
**Pengelola:** Kasie Pengadaan Jasa + Kasie Pengadaan Barang

**Input yang masuk:**
- Keputusan Direksi tentang vendor (Fase 0)
- Hasil evaluasi vendor siklus sebelumnya → update status (Fase 8)
- Vendor baru yang mengajukan registrasi mandiri

**Proses:**
```
Vendor ajukan registrasi (Excel/JSON/Portal)
           ↓
Checklist kualifikasi: legal, keuangan, operasional, regional Kaltim
           ↓
Site visit jika diperlukan (4-6 minggu proses)
           ↓
Keputusan: Approve → masuk Database Master KMU
           ↓
Klasifikasi vendor: Barang (Alkes/Farmasi/Umum) atau Jasa (Konstruksi/Konsultan/Outsourcing)
           ↓
Status aktif di Database → siap dipanggil di Fase 4
```

**Output yang keluar:**
- Daftar Vendor Terverifikasi KMU → pool yang bisa diundang tender di Fase 4
- Update status vendor (aktif/suspend/daftar vendor bermasalah) berdasarkan Fase 8
- Data KSO obligations yang harus dipenuhi vendor → masuk Fase 5

**Pengaruh ke modul lain:**
- Pool vendor yang tersedia langsung menentukan kompetisi di Fase 4
- KSO obligations yang tercatat menjadi checklist monitoring di Fase 5

---

### ════ FASE 3: PERMINTAAN PENGADAAN ════

**Dokumen referensi:** PROCUREMENT_PLATFORM_BLUEPRINT_v2.0.md (Workflow), Pedoman Pengadaan KMU  
**Pengelola:** SBU/Unit yang Meminta → Admin Pengadaan Barang/Jasa

**Input yang masuk:**
- Anggaran yang sudah disetujui dari RKAP (Fase 1)
- Kebutuhan operasional SBU yang muncul sepanjang tahun

**Proses:**
```
Jenis Pengadaan menentukan dokumen pemicu:

BARANG UMUM:    IMT → diproses menjadi PP oleh Departemen Umum
BARANG INVESTASI: IMT + FS (jika >100 juta) → PP
JASA:           JOR dari unit → SPPJ dari Departemen Umum
                (dilengkapi RAB, BOQ, DED untuk jasa konstruksi)
```

**Output yang keluar:**
- PP (Permintaan Pembelian) yang sudah disetujui Komite Anggaran → trigger Fase 4
- SPPJ yang lengkap dengan RAB/BOQ/DED → trigger Fase 4 jalur jasa

**AI Penjaga Kepatuhan aktif di sini:**
- Validasi: apakah PP sudah ada di RKAP?
- Validasi: apakah investasi >100 juta sudah ada FS?
- Validasi: apakah SPPJ sudah dilengkapi BOQ/DED?

---

### ════ FASE 4: PELAKSANAAN PENGADAAN (PROSES TENDER) ════

**Dokumen referensi:** PROCUREMENT_PLATFORM_BLUEPRINT_v2.0.md (CORE), SPO Pengadaan 2026 (semua)  
**Pengelola:** Kasie Pengadaan Barang / Kasie Pengadaan Jasa + Panitia Pengadaan (SKD)

**Input yang masuk:**
- PP atau SPPJ yang sudah disetujui (Fase 3)
- Pool vendor terverifikasi (Fase 2)
- Budget ceiling dari RKAP (Fase 1)

**Proses — Jalur Barang:**
```
PP diterima
    ↓
SPPH dikirim ke min. 2 vendor (estimasi jawab 2 hari)
    ↓
SJPH diterima dari vendor
    ↓
Bidding Tabulasi dibuat (1 hari)
    ↓
Negosiasi: harga, waktu, garansi, after-sales
    ↓
PO dibuat (1 hari) → Otorisasi sesuai nilai
    ↓
PO dikirim ke vendor → barang dikirim ke gudang
```

**Proses — Jalur Jasa:**
```
SPPJ + BOQ/DED diterima
    ↓
Aanwijzing Internal (1 hari) — unit peminta + tim pengadaan + keuangan
    ↓
SPPH dikirim ke min. 2 kontraktor/konsultan/vendor
    ↓
Aanwijzing Eksternal — briefing ke seluruh peserta
    ↓
SJPH diterima (skala kecil: 1 minggu | sedang: 10 hari | besar: 1 bulan)
    ↓
Bidding Tabulasi (1 hari)
    ↓
Negosiasi → Pemenang ditetapkan
    ↓
PKS + SPK dibuat → Otorisasi sesuai nilai
    ↓
BASTL (Serah Terima Lokasi) → pekerjaan dimulai
```

**Jalur Khusus:**
- Penunjukan Langsung: tanpa tender, langsung ke vendor terpilih (syarat ketat)
- Swakelola: dikerjakan sendiri oleh tim internal KMU

**Output yang keluar:**
- PO yang ditandatangani → trigger pengiriman barang (Fase 6)
- PKS + SPK yang ditandatangani → trigger pelaksanaan jasa (Fase 5)
- Data tender tersimpan di sistem → feed ke Pelaporan (Fase 9)

**AI Penjaga Kepatuhan aktif di sini:**
- Validasi jumlah vendor minimum di SPPH
- Cek apakah Aanwijzing sudah dilakukan sebelum SJPH diterima
- Blokir PO jika nilai melebihi budget RKAP tanpa persetujuan
- Validasi otorisasi sesuai kewenangan nilai PO/SPK

---

### ════ FASE 5: PELAKSANAAN KONTRAK & PORTAL VENDOR KSO ════

**Dokumen referensi:** VENDOR_PORTAL_KSO_OBLIGATIONS_SYSTEM.md  
**Pengelola:** Kasie Pengadaan Jasa + Tim Teknis + Vendor (via portal)

**Input yang masuk:**
- PKS + SPK yang sudah ditandatangani (Fase 4)
- KSO obligations dari kontrak vendor di Database (Fase 2)

**Proses:**
```
PKS/SPK aktif → Vendor login ke Portal Vendor KMU
           ↓
Vendor self-report kewajiban KSO:

  MAINTENANCE:
  ├─ Harian: laporan inspeksi visual, power-on test
  ├─ Bulanan: kalibrasi, penggantian suku cadang
  └─ Tahunan: overhaul, sertifikasi ulang

  KONSUMABEL:
  ├─ BHP: ATK, cleaning supply → jadwal bulanan
  ├─ BMHP: jarum suntik, sarung tangan → jadwal mingguan
  └─ Reagen: bahan lab/diagnostik → jadwal sesuai kontrak

           ↓
KMU verifikasi laporan via sistem (bukan manual)
           ↓
Jika kewajiban tidak terpenuhi → eskalasi otomatis ke Kasie/Manager
           ↓
Tim Teknis KMU pantau progress pekerjaan (untuk jasa konstruksi)
           ↓
Pekerjaan selesai → BAPP dibuat → trigger Fase 6
```

**Output yang keluar:**
- Data kinerja vendor real-time → feed ke Evaluasi Vendor (Fase 8)
- BAPP (Berita Acara Penyelesaian Pekerjaan) → trigger Fase 6
- Log kewajiban KSO → feed ke Pelaporan (Fase 9)

**AI Penjaga Kepatuhan aktif di sini:**
- Alert jika maintenance terlambat dari jadwal
- Flag jika vendor tidak upload laporan sesuai tenggat
- Eskalasi otomatis ke Manager Pengadaan jika kewajiban melebihi toleransi

---

### ════ FASE 6: PENERIMAAN & VERIFIKASI ════

**Dokumen referensi:** PROCUREMENT_PLATFORM_BLUEPRINT_v2.0.md (Payment & Delivery)  
**Pengelola:** Unit yang Meminta + Staf Pemeriksa Barang + Admin Pengadaan

**Input yang masuk:**
- Barang datang ke gudang (Fase 4 → pengiriman vendor)
- BAPP dari vendor jasa (Fase 5)

**Proses:**
```
Barang/jasa datang
    ↓
Pengecekan fisik: kuantitas, kualitas, spesifikasi sesuai PO/SPK?
    ↓
Jika sesuai → BAPB ditandatangani (Berita Acara Penerimaan Barang)
Jika tidak sesuai → Notifikasi ke vendor → revisi/penggantian
    ↓
3-Way Match: PO ↔ BAPB ↔ Invoice harus cocok
    ↓
Jika cocok → Invoice disetujui → trigger Fase 7
Jika tidak cocok → Invoice ditolak → Vendor diberi tahu
    ↓
Konfirmasi ke Unit yang Meminta: barang/jasa siap digunakan
```

**Output yang keluar:**
- BAPB yang ditandatangani → bukti penerimaan resmi
- 3-Way Match result → clearance untuk pembayaran (Fase 7)
- Data kualitas barang → feed ke Evaluasi Vendor (Fase 8)

**AI Penjaga Kepatuhan aktif di sini:**
- Blokir proses pembayaran jika BAPB belum ada
- Alert jika Invoice melebihi nilai BAPB
- Validasi 3-Way Match sebelum dokumen lanjut ke Fase 7

---

### ════ FASE 7: PEMBAYARAN & INVOICE ════

**Dokumen referensi:** PROCUREMENT_PLATFORM_BLUEPRINT_v2.0.md (Payment Milestones), COMMAND_CENTER_DASHBOARD_SPEC.md (Payment Pipeline)  
**Pengelola:** Bagian Keuangan + Manager Pengadaan + Otorisasi Direksi (nilai tertentu)

**Input yang masuk:**
- 3-Way Match yang sudah clear (Fase 6)
- Invoice dari vendor
- Syarat pembayaran sesuai PKS/PO (DP + pelunasan)

**Proses:**
```
Invoice masuk ke sistem
    ↓
Auto-validasi 3-Way Match (PO ↔ BAPB ↔ Invoice)
    ↓
Jika matched → masuk antrian approval pembayaran
    ↓
Approval bertingkat sesuai nilai (sama dengan otorisasi PO/SPK)
    ↓
Pembayaran diproses: DP terlebih dahulu (jika ada), lalu pelunasan
    ↓
GL Posting otomatis ke sistem keuangan KMU
    ↓
Vendor menerima pembayaran → konfirmasi di Portal Vendor KMU
    ↓
Status kontrak: LUNAS → trigger Fase 8
```

**Catatan:** Untuk pekerjaan >1 Miliar → Bank Guarantee 5% dicairkan setelah masa retensi selesai.

**Output yang keluar:**
- Rekaman pembayaran → feed ke Pelaporan (Fase 9)
- Status pembayaran vendor → data untuk Evaluasi Vendor (Fase 8)
- GL posting → integrasi dengan sistem keuangan KMU

**AI Penjaga Kepatuhan aktif di sini:**
- Blokir pembayaran tanpa 3-Way Match clear
- Alert jika pembayaran melebihi nilai kontrak
- Validasi masa retensi Bank Guarantee sebelum pencairan

---

### ════ FASE 8: EVALUASI VENDOR ════

**Dokumen referensi:** COMPREHENSIVE_VENDOR_EVALUATION_REPORTING_SYSTEM.md, SPO Evaluasi Vendor (KMU-SPO-DAN-07)  
**Pengelola:** Kasie Pengadaan Jasa/Umum + Manager Pengadaan

**Input yang masuk:**
- Data kinerja real-time dari Portal KSO (Fase 5)
- Data penerimaan barang/jasa (Fase 6) — kualitas, ketepatan waktu
- Data pembayaran (Fase 7) — konsistensi vendor
- Akumulasi semua transaksi dalam periode evaluasi

**7 Dimensi Scoring:**
```
1. DELIVERY PERFORMANCE    → On-time %, rata-rata keterlambatan
2. KUALITAS                → Defect rate, kesesuaian spesifikasi
3. RESPONSIVITAS           → Kecepatan SJPH, respon isu
4. HARGA & TERMS           → Kompetitivitas, konsistensi, diskon
5. KEPATUHAN SPO           → % kepatuhan prosedur KMU
6. KESEHATAN FINANSIAL     → Stabilitas, dampak ke modal kerja KMU
7. KEMITRAAN               → Kolaborasi, problem-solving, inovasi

TOTAL SKOR → Rating ⭐ (1-5)
```

**Keputusan berdasarkan skor:**
```
⭐⭐⭐⭐⭐ (4.5-5.0) → Preferred Vendor → Prioritas di tender berikutnya
⭐⭐⭐⭐   (3.5-4.4) → Good Vendor → Lanjut normal
⭐⭐⭐     (2.5-3.4) → Vendor Perlu Improvement → Peringatan + coaching
⭐⭐       (1.5-2.4) → Vendor Bermasalah → Suspensi sementara
⭐         (<1.5)    → Daftar Vendor Bermasalah → Dikeluarkan ±2 tahun
```

**Output yang keluar:**
- Update status vendor di Database Master (Fase 2) → langsung mempengaruhi siapa yang bisa diundang tender
- Laporan evaluasi → feed ke Pelaporan (Fase 9)
- Rekomendasi strategis → feed ke Direksi (Fase 0) untuk keputusan KSO lanjut/putus
- Improvement plan untuk vendor rating rendah

---

### ════ FASE 9: PELAPORAN & ANALITIK ════

**Dokumen referensi:** COMPREHENSIVE_REPORTING_ANALYTICS_SYSTEM.md  
**Pengelola:** Manager Pengadaan + SPI (Satuan Pengawasan Internal)

**Input yang masuk:**
- SEMUA data dari Fase 1-8 — setiap transaksi, dokumen, keputusan
- Audit trail dari AI Penjaga Kepatuhan SPO
- Data vendor dari Fase 8
- Data keuangan dari Fase 7

**Output yang dihasilkan:**
```
LAPORAN BULANAN (otomatis tanggal 1 tiap bulan):
├─ Realisasi pengadaan vs RKAP
├─ Status PO/SPK aktif
├─ Kinerja vendor bulan berjalan
├─ Isu dan eskalasi yang terjadi
└─ Compliance rate SPO

LAPORAN TRIWULAN (otomatis setiap akhir kuartal):
├─ Trend analisis 3 bulan
├─ Financial impact analysis
├─ Vendor performance ranking
└─ Rekomendasi perbaikan proses

LAPORAN TAHUNAN (otomatis 31 Januari):
├─ Comprehensive performance review
├─ Audit-ready dengan full trail
├─ ROI pengadaan terhadap RKAP
└─ Rekomendasi strategis untuk RKAP berikutnya
```

**Output yang keluar — menutup dan membuka loop:**
- Laporan ke Direksi (Fase 0) → dasar keputusan strategis dan RKAP siklus berikutnya
- Data historis → memperkaya AI Penjaga Kepatuhan SPO (semakin akurat dari waktu ke waktu)
- Benchmarking → input Fase 1 (perencanaan lebih realistis)

---

## TIGA LAPISAN LINTAS FASE

Tiga komponen ini tidak berada di satu fase — mereka **berjalan di SEMUA fase secara bersamaan:**

### LAPISAN 1: AI PENJAGA KEPATUHAN SPO
```
Cara kerja: Setiap aksi yang dilakukan di sistem → dicek otomatis terhadap SPO

Contoh aksi yang dicek:
├─ Fase 3: "Apakah PP sudah disetujui Komite Anggaran?"
├─ Fase 4: "Apakah jumlah vendor SPPH minimal 2?"
├─ Fase 4: "Apakah Aanwijzing sudah dilakukan sebelum SJPH?"
├─ Fase 6: "Apakah BAPB ada sebelum Invoice diproses?"
├─ Fase 7: "Apakah 3-Way Match sudah clear?"
└─ Fase 5: "Apakah laporan maintenance vendor terlambat?"

Jika ada pelanggaran:
├─ Pelanggaran ringan → Alert + panduan langkah benar
├─ Pelanggaran sedang → Warning + harus ada override approval
└─ Pelanggaran berat → BLOKIR + eskalasi ke Manager/Direksi

Chatbot 24/7: Staff bisa tanya "Apa langkah selanjutnya untuk SPPJ konstruksi?"
→ AI jawab berdasarkan SPO KMU yang sudah diingesti
```

### LAPISAN 2: COMMAND CENTER DASHBOARD
```
Siapa yang melihat:
├─ Direksi PT KMU → layar besar, KPI tingkat tinggi
├─ GM Operasi → semua tender aktif, alert
├─ Manager Pengadaan → operasional harian lengkap
└─ Bagian Keuangan → payment pipeline, budget tracker

Yang ditampilkan real-time:
├─ KPI Board: total pengadaan YTD, on-time delivery %, compliance rate
├─ Active Tender Wall: semua tender aktif + SLA countdown
├─ Alert Center: 🔴 kritis / 🟡 warning / ℹ️ info
├─ Payment Pipeline: invoice pending, total outstanding
├─ Vendor Performance: top/bottom performers real-time
├─ Budget Tracker: realisasi vs RKAP per kategori
└─ Audit Log: setiap aksi tercatat dengan timestamp + user
```

### LAPISAN 3: AUDIT TRAIL & PELAPORAN
```
Setiap kejadian di sistem dicatat:
[TIMESTAMP] [USER] [MODUL] [AKSI] [DOKUMEN] [NILAI] [STATUS]

Contoh:
2026-06-05 09:31 | Kasie.DaanJasa | Fase4 | SPPH Terkirim | SPPH-2026-089 | - | ✅
2026-06-05 14:22 | Admin.DaanUmum | Fase4 | Bidding Tabulasi | BT-2026-089 | 250.000.000 | ✅
2026-06-05 15:45 | Mgr.Pengadaan  | Fase4 | PO Ditandatangani | PO-2026-089 | 247.500.000 | ✅

Feed ke:
├─ Laporan otomatis (Fase 9)
├─ SPI untuk keperluan audit kapan saja
└─ AI Penjaga Kepatuhan SPO untuk pattern learning
```

---

## MATRIX KONEKTIVITAS ANTAR MODUL

| Output dari → | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F0 |
|---|---|---|---|---|---|---|---|---|---|---|
| **F0 Direksi** | ✅ RKAP | ✅ Kebijakan | | | | | | | | |
| **F1 Perencanaan** | | | ✅ Budget | | | | | | | ✅ Laporan |
| **F2 Vendor DB** | | | | ✅ Pool Vendor | ✅ KSO | | | | | |
| **F3 Permintaan** | | | | ✅ PP/SPPJ | | | | | | |
| **F4 Tender** | | | | | ✅ PKS/SPK | ✅ PO → Kirim | | | | |
| **F5 Kontrak** | | | | | | ✅ BAPP | | ✅ Kinerja | ✅ Log | |
| **F6 Penerimaan** | | | | | | | ✅ 3WM | ✅ Kualitas | ✅ Data | |
| **F7 Pembayaran** | | | | | | | | ✅ Perilaku | ✅ Keuangan | |
| **F8 Evaluasi** | | ✅ Status | | | | | | | ✅ Report | ✅ Rekomendasi |
| **F9 Pelaporan** | ✅ Historis | | | | | | | | | ✅ Laporan |

---

## TRIGGER YANG MEMULAI SETIAP FASE

| Fase | Trigger | Yang Memulai |
|---|---|---|
| F1 Perencanaan | Setiap awal tahun anggaran / arahan Direksi | Direksi + Manager Pengadaan |
| F2 Vendor DB | Vendor baru mendaftar / hasil evaluasi F8 | Vendor sendiri / Kasie Pengadaan |
| F3 Permintaan | Kebutuhan operasional SBU muncul | Kepala SBU / Unit yang Meminta |
| F4 Tender | PP atau SPPJ yang sudah disetujui masuk | Admin Pengadaan |
| F5 Kontrak | PKS/SPK sudah ditandatangani kedua pihak | Kasie Pengadaan Jasa |
| F6 Penerimaan | Barang tiba di gudang / BAPP diterima | Staf Pemeriksa + Unit |
| F7 Pembayaran | 3-Way Match clear + Invoice masuk | Bagian Keuangan |
| F8 Evaluasi | Kontrak selesai / periode evaluasi berakhir | Kasie Pengadaan |
| F9 Pelaporan | Otomatis: tanggal 1 bulanan, akhir kuartal, 31 Jan | Sistem (otomatis) |
| F0 Direksi | Laporan masuk dari F9 / Alert kritis dari Dashboard | Manager Pengadaan |

---

## KENAPA INI SIKLUS YANG TIDAK PERNAH BERHENTI

```
Siklus Pengadaan KMU tidak berhenti karena:

1. WAKTU TIDAK SINKRON: Fase-fase berjalan paralel, bukan serial.
   Sementara F4 (Tender) sedang berjalan untuk proyek A,
   F5 (Kontrak) sudah berjalan untuk proyek B,
   F8 (Evaluasi) sudah selesai untuk proyek C.

2. DATA MENGALIR TERUS: Setiap detik ada transaksi baru yang
   langsung masuk ke Audit Trail, Command Center, dan AI Guardian.

3. FEEDBACK LANGSUNG: Hasil evaluasi vendor hari ini langsung
   mengubah status vendor di database besok — tanpa menunggu
   siklus tahunan.

4. AI BELAJAR TERUS: Semakin banyak data transaksi, semakin
   akurat AI Penjaga Kepatuhan SPO dalam mendeteksi anomali.

5. LAPORAN MEMICU PERENCANAAN: Laporan akhir tahun langsung
   menjadi bahan RKAP tahun berikutnya — perencanaan tidak
   dimulai dari nol, tapi dari data aktual.
```

---

## PETA DOKUMEN KE MODUL SISTEM

| Dokumen | Modul/Fase | Status |
|---|---|---|
| PROCUREMENT_PLATFORM_BLUEPRINT_v2.0.md | F3, F4, F6, F7 (core platform) | ✅ Ada |
| AI_PROCEDURE_COMPLIANCE_GUARDIAN.md | Lapisan AI (cross-cutting) | ✅ Ada |
| COMMAND_CENTER_DASHBOARD_SPEC.md | Lapisan Dashboard (cross-cutting) | ✅ Ada |
| COMPREHENSIVE_REPORTING_ANALYTICS_SYSTEM.md | F9 Pelaporan | ✅ Ada |
| COMPREHENSIVE_VENDOR_EVALUATION_REPORTING_SYSTEM.md | F8 Evaluasi Vendor | ✅ Ada |
| STAKEHOLDER_CAUSAL_LOGIC_ANALYSIS.md | Governance layer (semua fase) | ✅ Ada |
| VENDOR_MASTER_DATABASE_KSO_MODULE.md | F2 Database Vendor | ✅ Ada |
| VENDOR_PORTAL_KSO_OBLIGATIONS_SYSTEM.md | F5 Portal Vendor KSO | ✅ Ada |
| VENDOR_REGISTRATION_REQUIREMENTS_CHECKLIST_KALTIM.md | F2a Registrasi | ✅ Ada |
| VENDOR_FORM_USAGE_GUIDE.md + JSON + CSV | F2b Form Registrasi | ✅ Ada |
| IMPLEMENTATION_CODE_READY.md | Technical layer (semua fase) | ✅ Ada |
| SOP_UPLOAD_GUIDE.md | Foundation AI Guardian | ✅ Ada |
| GLOSARIUM_ISTILAH_KMU.md | Standar terminologi seluruh sistem | ✅ Ada |
| **MASTER_BLUEPRINT ini** | **Induk — menyatukan semua** | ✅ **Dokumen ini** |

**Gap yang perlu diisi (dokumen belum ada):**
| Yang Dibutuhkan | Fase | Prioritas |
|---|---|---|
| Blueprint F1: Modul Perencanaan & RKAP Digital | F1 | Tinggi |
| Blueprint F3: Modul Permintaan (IMT/PP/SPPJ Digital) | F3 | Tinggi |
| Blueprint F6: Modul Penerimaan & Verifikasi Digital | F6 | Sedang |
| Blueprint F7: Modul Pembayaran & Invoice Tracking | F7 | Sedang |
| User Manual: Panduan Pengguna per Jabatan | Semua | Rendah |

---

## ARSITEKTUR IT: 5 LAPISAN SISTEM DIGITAL

Sistem digitalisasi pengadaan KMU dibangun dalam **5 Lapisan IT** yang saling menopang. Setiap lapisan punya tanggung jawab berbeda tapi bekerja sebagai satu kesatuan.

```
╔══════════════════════════════════════════════════════════════════╗
║           5 LAPISAN SISTEM IT PENGADAAN KMU                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  LAPISAN 1 — MANAJEMEN & TATA KELOLA                            ║
║  ─────────────────────────────────────────────────────────────  ║
║  • Modul E-Procurement: pengajuan kebutuhan, approval           ║
║    berjenjang, tender atau penunjukan langsung                   ║
║  • Workflow otomatis: Unit → Dept. Pengadaan → Komite           ║
║    Anggaran → Direktur → Vendor                                  ║
║  • AI Penjaga Kepatuhan SPO: rule enforcement real-time         ║
║  • Regulatory Compliance: LKPP + Permenkes                      ║
║                                                                  ║
║  LAPISAN 2 — OPERASIONAL                                        ║
║  ─────────────────────────────────────────────────────────────  ║
║  • Manajemen Vendor: registrasi, verifikasi legalitas,          ║
║    penilaian kinerja                                             ║
║  • Katalog Pengadaan: daftar barang/jasa standar,               ║
║    harga acuan, integrasi E-Katalog                              ║
║  • Manajemen Kontrak: drafting PKS/SPK, tanda tangan            ║
║    digital, monitoring masa berlaku kontrak                      ║
║  • Portal Vendor KSO: self-reporting kewajiban                  ║
║                                                                  ║
║  LAPISAN 3 — INTEGRASI                                          ║
║  ─────────────────────────────────────────────────────────────  ║
║  • SIMRS: tarik kebutuhan dari Farmasi, Alkes, Lab, KSO        ║
║  • Finance/ERP: cek anggaran real-time, eksekusi pembayaran,   ║
║    pencatatan ke General Ledger                                  ║
║  • Gudang/Inventori: stok real-time, reorder point,            ║
║    buffer safety stock                                           ║
║                                                                  ║
║  LAPISAN 4 — ANALITIK & TRANSPARANSI                           ║
║  ─────────────────────────────────────────────────────────────  ║
║  • Command Center Dashboard: KPI real-time, SLA tracking,      ║
║    nilai kontrak, vendor performance                             ║
║  • Analisis Belanja: efisiensi, identifikasi pemborosan,       ║
║    benchmarking vendor                                           ║
║  • Audit Trail Digital: rekam jejak lengkap setiap aksi,       ║
║    pengawasan SPI + eksternal                                    ║
║                                                                  ║
║  LAPISAN 5 — INFRASTRUKTUR & KEAMANAN                          ║
║  ─────────────────────────────────────────────────────────────  ║
║  • Deployment: Cloud/Hybrid (server RS + cloud)                 ║
║  • Single Sign-On (SSO): akses berbasis jabatan (RBAC)         ║
║  • Keamanan Data: enkripsi, backup, disaster recovery          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

### Pemetaan Lapisan ke Fase Siklus

| Lapisan | Fase yang Dicakup |
|---|---|
| Lapisan 1 — Tata Kelola | F1, F3, F4 (inti governance) + cross-cutting |
| Lapisan 2 — Operasional | F2, F4, F5 (vendor & kontrak) |
| Lapisan 3 — Integrasi | F3, F6, F7 (data dari/ke sistem lain) |
| Lapisan 4 — Analitik | F8, F9 + Lapisan Command Center |
| Lapisan 5 — Infrastruktur | Fondasi semua fase |

---

## SLA (TARGET WAKTU PROSES) PER TAHAP

Seluruh SLA dinyatakan dalam **hari kerja** (Senin–Jumat, kecuali libur nasional).

```
TAHAP                          SLA          KETERANGAN
──────────────────────────────────────────────────────────────────
Pengajuan IMT/PP/SPPJ          ≤ 1 hari     Unit → Dept. Umum
Review & Penentuan Metode      ≤ 2 hari     Dept. Pengadaan review
──────────────────────────────────────────────────────────────────
JALUR TENDER (Kompetitif):
  SPPH → SJPH → Bidding        ≤ 14 hari    Barang & Jasa
  (PP → PO, keseluruhan)       ≤ 14 hari    Sesuai Pedoman Rev
──────────────────────────────────────────────────────────────────
JALUR PENUNJUKAN LANGSUNG:
  Seleksi + PO                 ≤ 3 hari     Kondisi khusus/urgent
──────────────────────────────────────────────────────────────────
Terbitkan PO/SPK               ≤ 1 hari     Setelah pemenang
Pengiriman Barang              ≤ 7 hari     Vendor kirim ke gudang
QC & Pembuatan BAPB            ≤ 2 hari     Gudang + unit penerima
Submission Invoice             ≤ 3 hari     Setelah BAPB ditanda
Validasi 3-Way Match           ≤ 5 hari     PO ↔ BAPB ↔ Invoice
PEMBAYARAN                     ≤ 30 hari    Dari tanggal invoice
──────────────────────────────────────────────────────────────────
TOTAL SIKLUS (Tender path):    ~45–55 hari
TOTAL SIKLUS (Penunjukan):     ~15–20 hari
```

### Eskalasi Otomatis jika SLA Terlampaui

| Batas Pelanggaran | Tindakan Sistem |
|---|---|
| SLA + 1 hari | Notifikasi otomatis ke PIC & atasan langsung |
| SLA + 3 hari | Alert di Command Center + eskalasi ke Manager |
| SLA + 7 hari | Eskalasi ke GM Operasi + laporan SPI |
| SLA + 14 hari | Eskalasi ke Direksi + Komite Anggaran |

---

## INTEGRASI SISTEM EKSTERNAL

Sistem Pengadaan KMU **tidak berdiri sendiri** — wajib terintegrasi dengan 3 sistem utama:

### INTEGRASI SISTEM EKSTERNAL

| Sistem | Arah | Yang Dipertukarkan | Manfaat |
|---|---|---|---|
| **SIMRS** | SIMRS → Pengadaan | Kebutuhan Farmasi, Lab, Alkes, KSO | Tidak input manual, data akurat dari klinis |
| **Finance / ERP** | ↔ Dua arah | Konfirmasi budget, GL posting, status bayar | Tidak ada pembayaran tanpa clearance sistem |
| **Gudang / Inventori** | ↔ Dua arah | Stok real-time, reorder trigger, konfirmasi BAPB | Pengadaan hanya dipicu jika stok di bawah reorder point |

---

## KEPATUHAN REGULASI

| Regulasi | Berlaku untuk | Implikasi ke Sistem |
|---|---|---|
| **Permenkes** | Semua pengadaan alkes & obat | Vendor wajib punya izin Kemenkes, barang tersertifikasi |
| **LKPP / Perpres No.12/2021** | Semua pengadaan | Dasar hukum jenis & prosedur tender |
| **Audit BPK** | Jika BUMN/anak BUMN | Audit trail digital wajib lengkap & tidak bisa dimanipulasi |
| **SPO KMU (internal)** | Semua proses | AI Penjaga Kepatuhan SPO memvalidasi setiap aksi |

---

## SKORING VENDOR: DUA KERANGKA BERBEDA TUJUAN

### Kerangka A — Skoring Pemilihan Vendor Barang (Saat Bidding — Fase 4)
*Sumber: Template_Skoring_Pengadaan.xlsx (dokumen resmi KMU)*

| Kriteria | Bobot | Keterangan |
|---|---|---|
| Harga Penawaran | **25%** | Mendekati HPS — bukan selalu termurah |
| Kualitas Barang | **20%** | Spesifikasi teknis, standar mutu, sertifikasi |
| Maintenance & Sparepart | **20%** | Ketersediaan, response time, biaya servis |
| Kesesuaian Kebutuhan User | **20%** | Fit to clinical requirements, kemudahan pakai |
| Orientasi Merek / Track Record | **15%** | Reputasi vendor, pengalaman di RS lain, Populasi |

**Interpretasi skor:**

| Total Skor | Kategori | Tindakan |
|---|---|---|
| ≥ 400 | Rekomendasi Utama | Award kontrak |
| 350–399 | Rekomendasi Alternatif | Award jika utama tidak tersedia |
| 300–349 | Pertimbangan Bersyarat | Negosiasi atau lewati |
| < 300 | Tidak Direkomendasikan | Tolak |

### Kerangka B — Evaluasi Kinerja Vendor Pasca-Kontrak (Fase 8)
*Sumber: SPO Evaluasi Vendor KMU (KMU-SPO-DAN-07)*

| Dimensi | Fokus Penilaian |
|---|---|
| Ketepatan Pengiriman | On-time %, rata-rata keterlambatan |
| Kualitas | Defect rate, kesesuaian spesifikasi |
| Responsivitas | Kecepatan SJPH, respon isu |
| Harga & Termin | Kompetitivitas, konsistensi |
| Kepatuhan SPO | % kepatuhan prosedur KMU |
| Kesehatan Finansial | Stabilitas, dampak ke modal kerja |
| Kemitraan | Kolaborasi, inovasi, problem-solving |

**Perbedaan fungsi penting:**

| | Kerangka A | Kerangka B |
|---|---|---|
| Digunakan | Saat memilih pemenang tender (Fase 4) | Setelah kontrak berjalan (Fase 8) |
| Input | Dokumen penawaran & spesifikasi | Data aktual transaksi & kinerja |
| Output | Pemenang tender | Keputusan renewal / blacklist / improvement |
| Pelaksana | Kasie Pengadaan Barang + Panitia | Kasie Pengadaan Barang/Jasa + Manager |

---

## JENIS KSO (KERJASAMA OPERASIONAL)

KSO adalah mitra operasional berkelanjutan — **bukan vendor biasa**. Kewajiban terikat kontrak dan dipantau setiap hari melalui Portal Vendor KSO.

| Jenis KSO | Layanan | Kewajiban Utama | Monitoring |
|---|---|---|---|
| **KSO Laboratorium** | Alat lab, reagen, teknisi | Maintenance harian/bulanan, supply reagen terjadwal, kalibrasi | Laporan harian via Portal |
| **KSO Farmasi** | Sediaan farmasi | Supply obat terjadwal, ketersediaan stok darurat | Laporan stok mingguan |
| **KSO BMHP** | Bahan Medis Habis Pakai | Supply rutin (jarum, sarung tangan, kateter, dll) | Konfirmasi pengiriman per batch |

KSO dikelola di **Fase 5 (Portal Vendor KSO)** dan dievaluasi di **Fase 8** dengan mempertimbangkan sifat partnership-nya, bukan sekadar transaksi jual-beli.

---

## KESIMPULAN

Sistem Digitalisasi Pengadaan KMU adalah **satu ekosistem hidup** — bukan 9 aplikasi terpisah.

Setiap rupiah yang dibelanjakan melalui sistem ini meninggalkan jejak digital yang lengkap: dari kebutuhan SBU yang pertama diajukan, sampai vendor dievaluasi setelah barang/jasa diterima, sampai laporan dibaca Direksi, sampai RKAP tahun depan disusun berdasarkan data aktual.

Tidak ada black box. Tidak ada keputusan tanpa jejak. Tidak ada vendor yang bisa lolos evaluasi tanpa data. Tidak ada pembayaran yang bisa diproses tanpa dokumen lengkap.

**Ini adalah tata kelola pengadaan yang sesungguhnya — digital, transparan, akuntabel, dan tidak pernah berhenti belajar.**

# BLUEPRINT FASE 3: PERMINTAAN PENGADAAN (IMT/PP/SPPJ DIGITAL)
## PT Kaltim Medika Utama (Holding) — RS PKT Group

**Dokumen Bagian:** Modul F3 - Permintaan & Pemicu Siklus  
**Status:** DRAFT FINAL  
**Terkait dengan Master:** MASTER_BLUEPRINT_SISTEM_PENGADAAN_KMU_TERINTEGRASI.md  

---

## 1. DESKRIPSI MODUL
Fase 3 adalah pintu masuk resmi dimulainya siklus eksekusi pengadaan. Setelah kebutuhan disahkan secara gelondongan di RKAP (Fase 1), Fase 3 mengonversi kebutuhan tersebut menjadi dokumen spesifik (Permintaan Pembelian/PP untuk Barang dan Surat Permintaan Pekerjaan Jasa/SPPJ untuk Jasa). Modul ini mentransformasi proses *paper-based* yang memakan waktu menjadi alur digital dengan *auto-routing* persetujuan.

## 2. PENGGUNA MODUL (STAKEHOLDERS)
- **Unit Peminta (User):** Dokter, Kepala Perawat, Kepala Departemen yang membutuhkan barang/jasa.
- **Departemen Umum / PIC Logistik:** Pembuat dokumen PP/SPPJ berdasarkan nota internal (IMT / JOR) dari Unit Peminta.
- **Komite Anggaran & Direktur Terkait:** Otorisator dokumen PP/SPPJ sebelum dapat dilelang oleh Bagian Pengadaan.
- **Admin Pengadaan (Bagian Daan):** Penerima dokumen final yang akan memproses lelang di Fase 4.

## 3. ALUR KERJA (WORKFLOW) DIGITAL
1. **Trigger Permintaan:**
   - Kebutuhan muncul (bisa dari *alert* batas *reorder point* Gudang, atau permintaan mendadak / insidental SBU).
   - SBU mengunggah / mengisi IMT (Instruksi Mutasi Transaksi) untuk barang, atau JOR (Job Order Request) untuk jasa.
2. **Validasi Plafon Anggaran (Sistematis):**
   - Begitu IMT diinput, sistem langsung menarik data dari Fase 1 (RKAP). 
   - Jika sisa anggaran mencukupi -> Proses lanjut.
   - Jika sisa anggaran tidak mencukupi -> *Hard Stop*. Unit harus mengajukan revisi anggaran.
3. **Penyusunan PP / SPPJ:**
   - PIC Logistik mengonversi IMT menjadi PP. 
   - Untuk jasa konstruksi/konsultan, PIC mengunggah dokumen pendukung teknis (BOQ, RAB, DED, KAK/TOR) ke dalam draft SPPJ.
4. **Auto-Routing Approval:**
   - Sistem merutekan dokumen persetujuan secara otomatis hierarkis berdasarkan threshold nilai.
   - Contoh: < 50 Juta cukup Manager Umum. > 500 Juta harus sampai Direktur Utama.
   - Persetujuan menggunakan Digital Signature atau klik persetujuan ber-PIN.
5. **Serah Terima ke Pengadaan:**
   - PP / SPPJ yang berstatus "Approved" akan langsung muncul secara *real-time* di Papan Kanban Bagian Pengadaan (Dashboard Fase 4) tanpa perlu serah terima fisik (kertas).

## 4. INTEGRASI SISTEM EKSTERNAL
- **Integrasi SIMRS (Modul Intra-Pengadaan):** Permintaan obat-obatan dan alkes tidak lagi diinput manual, melainkan ditarik langsung (API pull) dari daftar menipisnya stok (buffer stock) di sistem Farmasi SIMRS.

## 5. PENJAGA KEPATUHAN SPO (AI GUARDIAN RULES)
- **Rule F3-1:** Blokir otomatis pembuatan PP untuk Investasi Medis (> Rp 100 Juta) jika form tidak melampirkan Dokumen *Feasibility Study (FS)* dan estimasi *Payback Period*.
- **Rule F3-2:** Blokir otomatis pembuatan SPPJ Konstruksi jika dokumen RAB dan *Bill of Quantities (BOQ)* belum diunggah.
- **Rule F3-3:** Pemecahan PP (Splitting). AI Guardian akan mendeteksi jika ada dua PP untuk item serupa dalam selang waktu berdekatan dengan nilai tepat di bawah batas persetujuan Direksi. Jika terdeteksi *fraud splitting*, PP akan difreeze dan dilaporkan ke SPI.

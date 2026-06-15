# BLUEPRINT FASE 6: PENERIMAAN & VERIFIKASI (BAPB DIGITAL)
## PT Kaltim Medika Utama (Holding) — RS PKT Group

**Dokumen Bagian:** Modul F6 - Penerimaan Barang & Jasa  
**Status:** DRAFT FINAL  
**Terkait dengan Master:** MASTER_BLUEPRINT_SISTEM_PENGADAAN_KMU_TERINTEGRASI.md  

---

## 1. DESKRIPSI MODUL
Fase 6 merupakan titik kritis (chokepoint) di mana barang atau jasa yang diserahkan oleh vendor diverifikasi secara fisik dan administratif sebelum hak tagih (invoice) dapat diproses. Modul ini mendigitalisasi proses Berita Acara Penerimaan Barang/Pekerjaan (BAPB/BAPP) dan memastikan bahwa kualitas, kuantitas, serta spesifikasi sesuai dengan PO (Purchase Order) atau SPK (Surat Perintah Kerja).

## 2. PENGGUNA MODUL (STAKEHOLDERS)
- **Staf Pemeriksa (Gudang/Logistik):** Menerima barang, melakukan pengecekan fisik, mencatat kondisi barang.
- **Unit Peminta (SBU/Klinik/RS):** Memberikan validasi akhir bahwa jasa/barang yang diterima sesuai kebutuhan (terutama untuk BAPP Jasa dan Investasi Medis).
- **Vendor:** Mengirimkan surat jalan, memantau status penerimaan barang secara *real-time* via Vendor Portal.
- **Admin Pengadaan:** Memantau ketepatan waktu pengiriman terhadap SLA PO.

## 3. ALUR KERJA (WORKFLOW) DIGITAL
1. **Prapenerimaan (Pre-Arrival):**
   - Vendor mengunggah Surat Jalan (Delivery Order) di Vendor Portal.
   - Gudang KMU mendapat notifikasi estimasi kedatangan barang.
2. **Inspeksi Fisik (On-Site):**
   - Barang tiba, Staf Pemeriksa membuka Modul F6.
   - Sistem menampilkan detail PO (Kuantitas, Spesifikasi, Harga).
   - Staf melakukan *checklist* inspeksi (Cacat, Expired Date, Kesesuaian Merk).
3. **Penerbitan BAPB Digital:**
   - Jika 100% Sesuai: Staf menekan "Terima Penuh" -> BAPB di-generate.
   - Jika Sebagian (Parsial): Staf memasukkan kuantitas yang diterima. Sistem membuat *Backorder* untuk sisa barang. BAPB Parsial diterbitkan.
   - Jika Ditolak: Staf memasukkan alasan penolakan dan bukti foto. Notifikasi retur dikirim ke Vendor.
4. **Distribusi Dokumen:**
   - BAPB Digital ditandatangani secara elektronik.
   - Dokumen langsung diteruskan ke Fase 7 (sebagai syarat 3-Way Match).
   - Status diubah menjadi "Barang Diterima" -> Auto-update di Command Center.

## 4. INTEGRASI 3-WAY MATCH (PRE-CHECK)
Fase 6 bertanggung jawab atas "kaki kedua" dari 3-Way Match:
- **Kaki 1:** Purchase Order (Fase 4)
- **Kaki 2:** BAPB (Fase 6) -> *Kuantitas yang diakui*
- **Kaki 3:** Invoice (Fase 7)

**Validasi Sistem:** Sistem di Fase 6 akan mengunci kuantitas maksimal yang bisa diklaim oleh vendor di Fase 7. Vendor tidak akan bisa submit Invoice untuk 100 item jika BAPB di Fase 6 hanya mengakui 90 item lulus QC.

## 5. FITUR UTAMA UI/UX
- **QR Code Scanner / Barcode:** Untuk mempercepat pencarian data PO di Gudang.
- **Photo Attachment:** Wajib mengunggah foto barang cacat/rusak jika melakukan penolakan.
- **Dashboard Gudang:** Menampilkan jadwal pengiriman harian berdasarkan SLA vendor.

## 6. PENJAGA KEPATUHAN SPO (AI GUARDIAN RULES)
- **Rule F6-1:** Mencegah penerbitan BAPB jika tanggal pengiriman melebihi masa berlaku PO tanpa ada Adendum.
- **Rule F6-2:** Memaksa Staf Pemeriksa untuk mengisi *field* Expired Date (ED) untuk barang kategori Farmasi/Reagen. ED < 6 bulan akan otomatis memicu peringatan (Warning) atau penolakan.
- **Rule F6-3:** BAPP Jasa bernilai > Rp 100 Juta wajib melampirkan *digital signature* dari Kepala SBU terkait.

# BLUEPRINT FASE 7: PEMBAYARAN & INVOICE TRACKING
## PT Kaltim Medika Utama (Holding) — RS PKT Group

**Dokumen Bagian:** Modul F7 - Finance & Invoice  
**Status:** DRAFT FINAL  
**Terkait dengan Master:** MASTER_BLUEPRINT_SISTEM_PENGADAAN_KMU_TERINTEGRASI.md  

---

## 1. DESKRIPSI MODUL
Fase 7 adalah gerbang terakhir sebelum siklus pengadaan diakhiri. Modul ini menjembatani antara kewajiban perusahaan (Hutang Usaha / Account Payable) dan penyelesaian pembayaran ke vendor. Fokus utamanya adalah menegakkan sistem *3-Way Matching* yang sangat ketat dan mengelola termin pembayaran (DP, Termin, Pelunasan, Retensi) secara sistematis tanpa toleransi kesalahan manusia.

## 2. PENGGUNA MODUL (STAKEHOLDERS)
- **Bagian Keuangan (Finance & AP):** Melakukan verifikasi akhir, menyetujui invoice, memproses pembayaran (atau GL Posting *mock*).
- **Vendor:** Mengajukan E-Invoice, memasukkan faktur pajak, memonitor status pencairan dana.
- **Manager Pengadaan & Direksi:** Melakukan otorisasi final (Approval) untuk pembayaran bernilai besar.
- **SPI (Satuan Pengawasan Internal):** Melakukan *audit trail* terhadap kesesuaian nilai yang ditransfer dengan dokumen kontrak.

## 3. ALUR KERJA (WORKFLOW) DIGITAL
1. **Invoice Submission (Oleh Vendor):**
   - Vendor login ke Portal Eksternal KMU.
   - Sistem secara otomatis menampilkan daftar BAPB/BAPP yang sudah "Clear" di Fase 6 dan siap ditagih.
   - Vendor mengunggah E-Invoice, Faktur Pajak, dan Bukti Potong (jika ada).
2. **Sistem 3-Way Matching (Otomatis oleh Sistem):**
   - **PO (Fase 4)** vs **BAPB (Fase 6)** vs **Invoice (Fase 7)**.
   - Sistem mencocokkan: (1) Item Barang, (2) Kuantitas, (3) Harga Satuan.
   - Jika *Matched*, status berubah menjadi "Ready for Payment".
   - Jika *Unmatched*, Invoice otomatis ditolak kembali ke vendor dengan alasan yang digenerate AI (misal: "Kuantitas tagihan melebihi BAPB").
3. **Approval Keuangan & Direksi:**
   - Bagian AP memverifikasi kelengkapan perpajakan.
   - Approval bertingkat sesuai Threshold (Misal: > Rp 500 Juta wajib Approval Direktur Keuangan).
4. **Proses Pencairan & GL Posting:**
   - Sistem merekam tanggal jatuh tempo (Due Date).
   - Saat dibayarkan, sistem memicu *GL Posting* (jurnal akuntansi) ke sistem ERP Finance (sementara menggunakan modul *intra-pengadaan* / *mock server*).
   - Status invoice berubah menjadi "Paid".
5. **Manajemen Retensi & Bank Guarantee:**
   - Untuk proyek konstruksi atau jasa KSO bernilai besar (> Rp 1 Miliar), sistem secara otomatis menahan 5% dari nilai tagihan akhir sebagai masa retensi (misal: 6 bulan).
   - Vendor baru bisa menagih sisa 5% tersebut setelah masa retensi berakhir dan BAST Kedua ditandatangani.

## 4. INTEGRASI SISTEM (ERP FINANCE)
- **Modul Intra-Pengadaan (Standalone Mode):** Apabila integrasi dengan IT KMU ERP belum siap, sistem mencatat status pembayaran secara internal. Pengadaan dapat melanjutkan operasional siklus ke Fase 8.
- **Modul Eksternal (Full Integration Mode):** API *endpoint* sudah disiapkan untuk mengirimkan JSON *payload* berisikan data hutang dan menerima *webhook callback* "PAYMENT_SUCCESS" dari sistem ERP utama KMU.

## 5. PENJAGA KEPATUHAN SPO (AI GUARDIAN RULES)
- **Rule F7-1:** Kunci absolut (Absolute Lock) pada 3-Way Match. Tidak ada satupun *user* (termasuk Direktur) yang dapat mem-bypass pembayaran jika nilai Invoice > Nilai BAPB.
- **Rule F7-2:** Penundaan pembayaran (Payment Hold) jika terdapat *Bank Guarantee* yang belum diserahkan oleh vendor untuk proyek terkait.
- **Rule F7-3:** Notifikasi otomatis ke Bagian Keuangan 3 hari sebelum *Due Date* untuk menjaga performa likuiditas namun menghindari denda keterlambatan bayar ke vendor.

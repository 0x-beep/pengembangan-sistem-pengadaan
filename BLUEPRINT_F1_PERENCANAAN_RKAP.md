# BLUEPRINT FASE 1: PERENCANAAN & ANGGARAN (RKAP DIGITAL)
## PT Kaltim Medika Utama (Holding) — RS PKT Group

**Dokumen Bagian:** Modul F1 - Perencanaan Budgeting & Ceiling  
**Status:** DRAFT FINAL  
**Terkait dengan Master:** MASTER_BLUEPRINT_SISTEM_PENGADAAN_KMU_TERINTEGRASI.md  

---

## 1. DESKRIPSI MODUL
Fase 1 adalah hulu dari seluruh aliran darah pengadaan PT KMU. Modul ini digunakan untuk menyusun, mereview, dan mengesahkan Rencana Kerja dan Anggaran Perusahaan (RKAP). Output dari modul ini adalah "Budget Ceiling" (Plafon Anggaran) yang bersifat mengikat dan akan membatasi eksekusi pengadaan pada Fase 3 dan Fase 4.

## 2. PENGGUNA MODUL (STAKEHOLDERS)
- **Komite Anggaran (Budgeting Committee):** Meriview dan menyetujui usulan RKAP dari masing-masing unit bisnis.
- **Kepala SBU / Kepala Unit:** Mengajukan kebutuhan pengadaan (Capex & Opex) untuk tahun berjalan.
- **Direksi:** Melakukan pengesahan final Master RKAP.
- **Manager Pengadaan:** Melakukan kompilasi kebutuhan barang dan merumuskan strategi *procurement* (contoh: *bulk buying*, tender konsolidasi).

## 3. ALUR KERJA (WORKFLOW) DIGITAL
1. **Pengajuan Kebutuhan (Bottom-Up):**
   - Kepala SBU (misal: RS PKT Bontang, Klinik KMU, Lab Biomedik) memasukkan usulan kebutuhan barang/jasa tahunan (Draft RAB).
   - Pengajuan dibedakan menjadi Kategori Opex (Operasional seperti Obat, BMHP, ATK) dan Capex (Investasi seperti Alkes Besar).
2. **Kompilasi & Review:**
   - Sistem secara otomatis mengkonsolidasi semua usulan per kategori.
   - Manager Pengadaan menganalisis volume (contoh: jika 3 Klinik meminta Paracetamol, sistem merekomendasikan tender terpusat / konsolidasi).
3. **Pengesahan RKAP & Penetapan Plafon:**
   - Komite Anggaran melakukan penyesuaian nilai (Cuts/Approvals).
   - RKAP Final disahkan oleh Direksi.
   - Sistem menetapkan (Lock) *Budget Ceiling* di *database* untuk setiap SBU dan setiap Kategori Barang.
4. **Monitoring Serapan Berjalan:**
   - Dashboard F1 menampilkan Realisasi (YTD) berbanding dengan RKAP.
   - Warna indikator Hijau (<80%), Kuning (80%-95%), Merah (>95% Overbudget Warning).

## 4. INTEGRASI DENGAN FASE 3 (PERMINTAAN)
Modul F1 merupakan dasar bagi Fase 3 (Permintaan Pengadaan - PP/SPPJ).
- **Hard Block Limit:** Apabila sebuah SBU membuat IMT (Instruksi Mutasi Transaksi) atau PP di Fase 3 yang menyebabkan estimasi biaya melampaui sisa *Budget Ceiling* di Fase 1, maka sistem akan menolak formulir PP tersebut secara otomatis.
- **Real-time Deduct:** Setiap PO yang terbit di Fase 4 secara otomatis mengurangi saldo plafon anggaran di Fase 1.

## 5. PENJAGA KEPATUHAN SPO (AI GUARDIAN RULES)
- **Rule F1-1:** Pembatasan (Locking) pembuatan PP untuk kategori Capex (Investasi) yang tidak tercantum secara spesifik dan nominal dalam nomenklatur RKAP, kecuali memiliki dokumen Persetujuan *Cito/Urgent* dari Direksi.
- **Rule F1-2:** Sistem menolak pengajuan anggaran baru jika pelaporan utilitas aset tahun sebelumnya (terutama alkes KSO) masih berada pada performa di bawah standar efisiensi yang ditetapkan.

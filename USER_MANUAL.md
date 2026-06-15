# BUKU PANDUAN PENGGUNA (USER MANUAL)
**Sistem Digitalisasi Pengadaan Terintegrasi PT KMU**

---

## DAFTAR ISI
1. [Pendahuluan](#pendahuluan)
2. [Panduan untuk Direksi (Dashboard Executive)](#panduan-untuk-direksi)
3. [Panduan untuk Manager / Kepala Seksi Pengadaan](#panduan-untuk-manager--kasie-pengadaan)
4. [Panduan untuk Vendor / Mitra](#panduan-untuk-vendor--mitra)
5. [Panduan untuk Bagian Keuangan (Finance)](#panduan-untuk-bagian-keuangan)
6. [Panduan untuk SPI / Auditor](#panduan-untuk-spi--auditor)

---

## PENDAHULUAN
Sistem Digitalisasi Pengadaan Terintegrasi dirancang untuk menghubungkan seluruh stakeholder dalam proses pengadaan di lingkungan PT KMU (Karya Medika Utama). Mulai dari perencanaan anggaran (RKAP), permintaan (PR), tender (PO), penerimaan barang (BAPB), hingga pembayaran (Invoice 3-Way Match).

Sistem ini didukung oleh **AI Guardian**, sebuah middleware kecerdasan buatan yang bertugas menjaga kepatuhan terhadap SOP dan memberikan peringatan dini (*early warning*) apabila terjadi anomali pengadaan.

---

## PANDUAN UNTUK DIREKSI
**Peran:** Memantau kinerja pengadaan, efisiensi anggaran, dan memberikan persetujuan strategis.

**Cara Menggunakan Sistem:**
1. **Login:** Akses melalui Command Center atau Portal Direksi.
2. **Dashboard Utama:**
   - Di halaman utama, Anda dapat melihat **KPI Efisiensi Pengadaan** secara *real-time*.
   - Grafik serapan anggaran akan menunjukkan performa SBU dibandingkan dengan RKAP tahun berjalan.
3. **Persetujuan (Approval):**
   - Transaksi pengadaan yang nilainya melebihi kewenangan Kasie/Manager (misalnya > Rp 1 Miliar) akan muncul di kotak masuk *Approval Direksi*.
   - Anda dapat menekan tombol **Setujui** atau **Tolak** yang dilengkapi dengan analisis prediktif AI terkait kelayakan harga.
4. **Command Center:**
   - Gunakan fitur ini di layar besar untuk melihat *live feed* aktivitas vendor, tender berjalan, dan *alert* lintas unit yang terindikasi anomali (misalnya: *Bottleneck* pembayaran di Finance atau keterlambatan *delivery* BAPB).

---

## PANDUAN UNTUK MANAGER / KASIE PENGADAAN
**Peran:** Mengelola tender, memilih vendor, memverifikasi BAPB, dan memantau performa KSO.

**Cara Menggunakan Sistem:**
1. **Proker Bulanan:**
   - Ajukan *Purchase Requisition* (PR) atau Rencana Proker dari unit (misal: Unit Umum/IMT).
   - Pastikan spesifikasi teknis dan estimasi harga sudah diinput sebelum dikirim ke Keuangan untuk verifikasi ketersediaan *budget*.
2. **E-Katalog Internal & Quotation:**
   - Gunakan fitur E-Katalog untuk membandingkan harga antar SBU.
   - Untuk item non-katalog, buat *Quotation Request*. Sistem akan mengundang vendor-vendor terdaftar untuk mengajukan *bid* harga.
3. **Scoring & Tunjuk Pemenang:**
   - Sistem menyediakan fitur *Scoring* berbasis harga, kualitas, layanan, dan merk.
   - Tandai vendor sebagai pemenang dan otomatis *Purchase Order* (PO) akan terbuat dengan status *Draft*.
4. **Evaluasi KSO & SLA (Fase 8):**
   - Buka menu *Vendor Scorecard* secara berkala untuk mengevaluasi performa vendor KSO. 
   - Nilai dari QC (User) dan Nilai Finansial/Compliance akan digabungkan menjadi skor berbobot (0-100). Vendor di bawah 70 berisiko ditinjau ulang kontraknya.

---

## PANDUAN UNTUK VENDOR / MITRA
**Peran:** Merespons tender, memantau PO, mengunggah katalog, dan menagihkan invoice.

**Cara Menggunakan Sistem:**
1. **Registrasi & Portal Vendor:**
   - Buka **Portal Vendor SBU**.
   - Login menggunakan akun Vendor yang telah disetujui (Status: *Active*).
2. **Dashboard Vendor:**
   - Anda dapat melihat semua *Purchase Order* (PO) aktif, status pembayaran (Tepat waktu, Terlambat), dan pengumuman *Tender* terbaru.
3. **Upload E-Katalog:**
   - Masuk ke menu E-Katalog. Anda dapat mengunggah file CSV/Excel berisi daftar harga barang, diskon SBU, dan ketersediaan (*availability*).
4. **Penagihan (Invoicing) & 3-Way Match:**
   - Saat barang/jasa telah diterima pihak PT KMU (dibuktikan dengan nomor BAPB), buat Invoice.
   - Input No. Invoice Anda, lalu tautkan dengan No. PO dan No. BAPB.
   - Sistem akan melakukan verifikasi **3-Way Match** secara otomatis. Jika nilai di PO, BAPB, dan Invoice cocok, pembayaran akan langsung masuk antrian persetujuan *Finance*.
   - **Retensi KSO:** Untuk proyek KSO/Konstruksi > Rp 1 Miliar, sistem otomatis menahan retensi sebesar 5%.

---

## PANDUAN UNTUK BAGIAN KEUANGAN (FINANCE)
**Peran:** Memvalidasi anggaran, melakukan pembayaran, dan merekonsiliasi GL.

**Cara Menggunakan Sistem:**
1. **Verifikasi Anggaran (Budget Clearance):**
   - Setiap permintaan (PR/Proker) yang diajukan oleh Bagian Umum akan masuk ke dashboard Keuangan.
   - Verifikasi apakah anggaran RKAP masih tersedia. Jika tersedia, setujui (Clear) agar proses pengadaan dapat berjalan.
2. **Antrian Pembayaran (Payable Pipeline):**
   - Buka menu **Finance & Pembayaran**.
   - Invoice yang telah lolos sistem *3-Way Match* akan muncul di daftar antrian siap bayar.
   - Proses pelunasan sesuai *Term of Payment* (ToP) dan tanggal jatuh tempo. SLA pembayaran akan terhitung otomatis oleh *Command Center*.
3. **MLM Comparison & Penghematan:**
   - Anda dapat menggunakan fitur Analitik Finance untuk melihat *Cost Avoidance* atau selisih penghematan pembelian e-katalog vs harga pasar.

---

## PANDUAN UNTUK SPI / AUDITOR
**Peran:** Memastikan transparansi, memonitor kepatuhan (compliance), dan mengecek *flag* anomali.

**Cara Menggunakan Sistem:**
1. **Log Aktivitas (*Audit Trail*):**
   - Seluruh perubahan data (misalnya: Perubahan harga penawaran setelah *closing bid*) dicatat oleh sistem dengan *timestamp* dan *user id*.
   - Buka menu **SPI & Audit Dashboard** untuk melihat jejak digital.
2. **AI Guardian Alert:**
   - Auditor akan menerima notifikasi otomatis bila AI Guardian menemukan:
     - Tender dengan peserta tunggal (*Single Bidder Alert*).
     - Pembelian item yang harganya >20% di atas *average price* E-Katalog.
     - Penahanan pembayaran yang melebihi SLA 14 hari tanpa alasan sah (Potensi *Fraud* / Kesengajaan).
3. **Arsip Digital:**
   - Seluruh dokumen legal (Kontrak KSO, BAPB, Dokumen Legalitas Vendor) tersimpan secara digital dan dapat diunduh kapan saja untuk keperluan verifikasi bukti.

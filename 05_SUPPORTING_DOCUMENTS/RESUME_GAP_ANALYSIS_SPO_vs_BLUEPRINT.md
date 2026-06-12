# RESUME GAP ANALYSIS
# SPO & Pedoman Rev vs Blueprint Sistem Digitalisasi Pengadaan KMU
**Tanggal:** Juni 2026
**Tujuan:** Bahan diskusi Tim Daan dan Atasan — finalisasi sebelum sistem dibangun
**Status:** DRAFT v2 — Perlu konfirmasi Tim Daan untuk gap yang tersisa

---

## CATATAN PENTING: REFERENSI DOKUMEN

> **Dokumen 2022 (SPO lama) = TIDAK BERLAKU.**
> Seluruh analisis ini mengacu pada **Pedoman Rev** dan **SPO Rev1** sebagai satu-satunya referensi yang sah.

**Struktur organisasi yang berlaku sekarang (hasil konfirmasi):**
- **GM Operasi** membawahi 4 departemen: Pengadaan, Umum, IT, PUM
- **Kasie Pengadaan Barang** = nama jabatan resmi (bukan Kasie Pengadaan Umum)
- **KSU** = bagian dari Departemen PUM, bukan unit terpisah
- **Departemen Umum** = departemen sendiri di bawah GM Operasi, bukan bagian Pengadaan

Glosarium dan semua blueprint sudah diupdate sesuai struktur ini.

---

## RINGKASAN EKSEKUTIF

Ditemukan **8 gap** antara Pedoman Rev + SPO Rev1 dan Blueprint Sistem yang sudah disusun. Gap-gap ini bukan masalah teknis semata — sebagian besar adalah **kebijakan yang belum didefinisikan** yang kalau dibiarkan akan jadi konflik di lapangan saat sistem hidup.

**Tingkat urgensi:**
- 🔴 **KRITIS** — Harus diputuskan sebelum coding dimulai
- 🟡 **PENTING** — Harus diselesaikan sebelum go-live
- 🟢 **PENYEMPURNAAN** — Bisa diselesaikan di iterasi berikutnya

---

## GAP 1 🔴 — ARM (Anjungan Rekanan Mandiri) BELUM ADA DI BLUEPRINT

**Sumber:** Pedoman Rev Bab X, Poin 3

**Kutipan langsung dari Pedoman Rev:**
> *"Membuat dan mengirimkan SPPH melalui ARM (Anjungan Rekanan Mandiri) kepada para PBAK/distributor yang sudah terdaftar dalam ARM"*

**Masalah:**
Pedoman Rev secara eksplisit menyebutkan SPPH dikirim **melalui ARM** — sebuah portal/sistem rekanan. Blueprint kita tidak menyebut ARM sama sekali. Tiga kemungkinan:
- ARM sudah ada sebagai sistem yang harus diintegrasikan
- ARM = nama lain untuk Portal Vendor KMU yang sedang kita rancang
- ARM adalah sistem paralel yang berjalan bersamaan

**Dampak ke blueprint:** Jika ARM sudah ada, sistem baru harus **terintegrasi atau menggantikan ARM**, bukan berdiri paralel. Ini mengubah arsitektur secara fundamental — database vendor, mekanisme SPPH, dan notifikasi semua berubah.

**Yang harus dikonfirmasi Tim Daan:**
- ARM itu sistem apa? Sudah berjalan atau masih rencana?
- Apakah ARM = Portal Vendor KMU yang kita rancang? (jika ya, gap ini hilang)
- Jika ARM sudah ada: berapa vendor sudah terdaftar? Data apa yang tersimpan di sana?

**Rekomendasi:** Klarifikasi ARM sebelum apapun dibangun. Ini adalah fondasi Portal Vendor.

---

## GAP 2 🔴 — SENTRALISASI vs DESENTRALISASI BELUM DIPETAKAN DI BLUEPRINT

**Sumber:** Pedoman Rev Bab X, SPO DAAN Sentralisasi.pdf, SPO DAAN Disentralisasi.pdf

**Yang ditemukan di Pedoman Rev:**

*Prosedur Sentralisasi (5 langkah ringkas):*
1. Identifikasi kebutuhan
2. Pemilihan pemasok, negosiasi JPH
3. Pembelian sesuai PO
4. Pengawasan dan Pengendalian
5. Pelaporan dan evaluasi oleh **"Meta Bisnis"**

*Prosedur Desentralisasi (5 langkah ringkas):*
1. Perencanaan kebutuhan oleh unit kerja
2. Pemilihan Penyedia
3. Pelaksanaan Kontrak
4. Pengawasan dan Pengendalian
5. Pelaporan dan evaluasi oleh **"Meta Bisnis"**

**Masalah:**
Blueprint kita hanya punya **satu jalur** (semua melalui Departemen Pengadaan). Pedoman Rev mengakui dua model yang berbeda secara struktural. Plus ada entitas **"Meta Bisnis"** yang disebut di keduanya tapi tidak pernah didefinisikan di dokumen manapun.

SPO Sentralisasi dan Desentralisasi adalah file scan — isinya detail belum bisa dibaca.

**Pertanyaan kritis untuk Tim Daan:**
- Kapan pakai sentralisasi? Kapan desentralisasi? Apa batas nilai/jenis barang/jasa?
- Apakah desentralisasi berarti unit kerja bisa pengadaan sendiri di luar Departemen Pengadaan?
- **"Meta Bisnis" itu apa?** Unit? Sistem? Tim khusus? Ini kunci karena muncul di kedua prosedur.
- Kalau desentralisasi diizinkan, siapa yang approve dan siapa yang bertanggung jawab?

**Dampak ke blueprint:** Jika dua jalur ini berbeda, sistem harus punya dua workflow approval terpisah. Ini bukan perubahan kecil — ini perubahan arsitektur besar.

---

## GAP 3 🟡 — ISTILAH JPH vs SJPH TIDAK SERAGAM

**Sumber:** Pedoman Rev, Alur Pengadaan Barang

**Temuan:**

| Dokumen | Istilah Jawaban Penawaran | Istilah Permintaan Penawaran |
|---|---|---|
| Pedoman Rev (Bab X barang) | **SJPH** | SPPH |
| Pedoman Rev (Bidding Tabulasi) | **JPH** | SPPH |
| Alur Pengadaan Barang | **JPH** | PH |
| Glosarium KMU kita | **SJPH** | SPPH |

Dalam satu pedoman yang sama muncul dua istilah berbeda untuk dokumen yang sama. "PH" juga muncul sebagai singkatan alternatif untuk SPPH.

**Dampak:** Label di form digital, notifikasi sistem, dan laporan akan tidak konsisten dengan dokumen cetak yang dipakai di lapangan.

**Rekomendasi untuk Tim Daan:** Pilih satu istilah resmi dan konsisten:
- [ ] **SJPH** (Surat Jawaban Penawaran Harga) — lebih formal, sesuai istilah jasa
- [ ] **JPH** (Jawaban Penawaran Harga) — lebih singkat, sudah dipakai di beberapa SPO baru

---

## GAP 4 🟡 — EVALUASI VENDOR BARANG BELUM ADA DI BLUEPRINT

**Sumber:** Pedoman Rev Bab X — Prosedur Evaluasi Vendor Pengadaan Barang

**Yang ada di Pedoman Rev (sangat ringkas):**
- Evaluasi Kualitas: mutu, spesifikasi teknis, standar mutu, jaminan kualitas
- Evaluasi Harga: dibanding anggaran dan harga pasar, diskon, biaya tambahan

**Yang ada di Alur Pengadaan Barang (lebih lengkap):**
- Harga terbaik, Spek barang, Waktu penyediaan
- Jaminan/garansi/sparepart availability
- Company Profile
- **Populasi** (khusus Alkes Investasi — belum didefinisikan apa artinya)

**Masalah:**
Blueprint kita hanya punya Evaluasi Vendor **Jasa** (7 dimensi, SPO KMU-SPO-DAN-07). Tidak ada sistem evaluasi untuk vendor **barang**. Kriteria di Pedoman Rev terlalu singkat untuk dijadikan sistem — perlu dikembangkan.

**Rekomendasi:** Tim Daan perlu menyusun SPO Evaluasi Vendor Barang yang lebih lengkap. Ini jadi input untuk blueprint Fase 8.

---

## GAP 5 🟡 — "FRANKO BARANG" DAN "POPULASI" PERLU DIDEFINISIKAN

**Sumber:** Alur Pengadaan Barang

**Temuan:**
- **Franko Barang** — disebut sebagai poin konfirmasi saat negosiasi, tapi tidak ada di prosedur manapun. Franko = kondisi pengiriman (siapa menanggung ongkir). Apakah KMU yang tanggung atau vendor? Harus ada standar.
- **Populasi** — kriteria tambahan khusus penyedia Alkes dan Investasi. Tidak pernah didefinisikan. Kemungkinan arti: jumlah unit alat yang sudah terpasang di RS lain, atau market share vendor di industri.

**Dampak:** Form SPPH dan checklist negosiasi di sistem tidak lengkap tanpa dua poin ini.

**Pertanyaan untuk Tim Daan:**
- Franko barang: standar KMU itu seperti apa? Selalu franco gudang? Atau tergantung negosiasi?
- Populasi: definisinya apa? Cara verifikasinya bagaimana?

---

## GAP 6 🟡 — SLA 14 HARI KERJA BELUM DIKUNCI DENGAN JELAS

**Sumber:** Pedoman Rev Bab X, Poin 6

**Kutipan:**
> *"Proses Pengadaan Barang dimulai dari PP ke PO membutuhkan waktu 14 hari kerja."*

**Masalah:**
- Blueprint menyebut target IMT→PO ≤14 hari, tapi tidak spesifik **hari kerja atau kalender**
- 14 hari kerja ≠ 14 hari kalender (beda ±4 hari jika ada libur/weekend)
- SLA jasa: skala kecil 1 minggu, sedang 10 hari, besar 1 bulan — tidak jelas hari kerja/kalender
- Command Center Dashboard countdown timer harus diprogram berdasarkan satuan yang benar

**Rekomendasi:** Tetapkan standar: semua SLA dalam **hari kerja** (hari senin-jumat, kecuali libur nasional). Ini berlaku untuk semua jenis pengadaan, bukan hanya barang.

---

## GAP 7 🟡 — SPO PENUNJUKAN LANGSUNG TIDAK ADA DI PAKET BARU

**Sumber:** Perbandingan daftar SPO

| SPO | Paket Lama (2022) | Paket Baru (Rev) |
|---|---|---|
| Evaluasi Vendor Jasa | ✅ | ✅ |
| Jasa Konstruksi | ✅ | ✅ |
| Jasa Konsultan | ✅ | ✅ |
| Jasa Outsourcing | ✅ | ✅ |
| Jasa Swakelola | ✅ | ✅ |
| **Penunjukan Langsung** | **✅** | **❌** |
| Sentralisasi | ❌ | ✅ |
| Desentralisasi | ❌ | ✅ |
| Investasi & Non Investasi | ❌ | ✅ |

**Pertanyaan:** Apakah Penunjukan Langsung masih berlaku? Kalau masih ada, SPO-nya di mana? Kalau tidak ada, bagaimana handle kondisi darurat/urgent yang hanya bisa dipenuhi satu vendor?

---

## GAP 8 🟢 — METODE PEMBAYARAN VENDOR BELUM DIDETAILKAN

**Sumber:** Alur Pengadaan Barang

Alur menyebut tiga metode pembayaran ke vendor: **Invoice** (termin), **Kredit**, **Cash**. Blueprint Fase 7 kita hanya cover DP + pelunasan. Tidak ada SOP untuk:
- Kapan boleh cash? Siapa otorisasi? Batas nilai?
- Bagaimana rekonsiliasi cash ke GL Keuangan?

**Rekomendasi:** Tambahkan ke blueprint Fase 7 saat dikerjakan.

---

## CATATAN: FILE SCAN YANG BELUM TERBACA

File-file berikut adalah PDF scan — isinya belum diketahui:

| File | Relevansi |
|---|---|
| SPO DAAN Sentralisasi.pdf | Detail prosedur sentralisasi (kritis untuk Gap 2) |
| SPO DAAN Disentralisasi.pdf | Detail prosedur desentralisasi (kritis untuk Gap 2) |
| SPO DAAN Investasi & Non Investasi rev1.pdf | Mungkin ada batasan nilai/kriteria baru |
| SPO DAAN Aanwijding rev1.pdf | Mungkin ada perubahan prosedur Aanwijzing |
| SPO Daan Bidding Tabulasi rev1.pdf | Mungkin ada perubahan kriteria bidding |
| SPO Pengadaan Jasa Swakelola.pdf | Prosedur swakelola belum terbaca |

**Tindakan:** Upload ulang dalam format digital (bukan scan), atau lakukan OCR, agar bisa dimasukkan ke sistem AI Penjaga Kepatuhan SPO.

---

## TASK LIST TINDAK LANJUT

### 🔴 SEBELUM CODING DIMULAI

| # | Task | Siapa |
|---|---|---|
| T1 | Klarifikasi ARM: sistem apa, sudah ada atau belum, relasinya ke Portal Vendor KMU | Manager Pengadaan + IT |
| T2 | Definisikan Sentralisasi vs Desentralisasi: kapan, siapa, batas nilai, otorisasi | Tim Daan + Direksi |
| T3 | Jelaskan "Meta Bisnis": apa itu, siapa yang kelola | Tim Daan |

### 🟡 SEBELUM GO-LIVE

| # | Task | Siapa |
|---|---|---|
| T4 | Pilih satu istilah resmi: SJPH atau JPH | Tim Daan |
| T5 | Susun SPO Evaluasi Vendor Barang yang lengkap | Kasie Pengadaan Barang |
| T6 | Definisikan Franko Barang dan Populasi secara resmi | Tim Daan |
| T7 | Standardisasi SLA: hari kerja untuk semua proses pengadaan | Tim Daan + Direksi |
| T8 | Konfirmasi status SPO Penunjukan Langsung | Manager Pengadaan |
| T9 | Digitisasi 6 file SPO scan (upload ulang sebagai teks digital) | Tim Daan + IT/Admin |

### 🟢 ITERASI BERIKUTNYA

| # | Task | Siapa |
|---|---|---|
| T10 | Tambahkan SOP Pembayaran Cash ke Blueprint Fase 7 | Tim Daan + Keuangan |

---

## REKOMENDASI AGENDA DISKUSI

**Sesi 1 — Keputusan Kebijakan (dengan Atasan/Direksi):**
- Gap 1: ARM dan arsitektur sistem
- Gap 2: Model Sentralisasi vs Desentralisasi + "Meta Bisnis"
- Gap 7: Nasib SPO Penunjukan Langsung

**Sesi 2 — Penyeragaman Operasional (Tim Daan):**
- Gap 3: SJPH atau JPH
- Gap 4: Kriteria Evaluasi Vendor Barang
- Gap 5: Franko Barang dan Populasi
- Gap 6: Standardisasi SLA hari kerja
- Catatan: Digitisasi 6 file scan

---

*Dokumen ini mengacu pada Pedoman Rev dan SPO Rev1 sebagai referensi sah. Dokumen 2022 tidak digunakan sebagai pembanding.*

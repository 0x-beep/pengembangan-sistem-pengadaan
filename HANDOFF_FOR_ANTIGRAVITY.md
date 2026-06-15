# HANDOFF DOKUMEN — Sistem Digitalisasi Pengadaan PT KMU
**Dari:** Tim Proyek Digitalisasi Pengadaan  
**Kepada:** Tim IT Implementasi  
**Tanggal:** 2026-06-13  
**Status:** Prototype selesai, siap handoff ke Tim IT

---

## APA YANG SUDAH SELESAI

1. ✅ **Reorganisasi folder** — `04_SISTEM_TERINTEGRASI` → `SISTEM_TERINTEGRASI`, `04_REFERENCE_DOCUMENTS` → `REFERENCE_DOCUMENTS`
2. ✅ **rs_klinik_dashboard.html** — Logika otonom Sentralisasi/Desentralisasi (Alkes > Rp5Jt, Umum > Rp2Jt)
3. ✅ **approval_dashboard.html** — Inbox Sentralisasi untuk Holding
4. ✅ **PEDOMAN_SISTEM_IT_HANDOFF.md** — Blueprint teknis final untuk Tim IT PT KMU
5. ✅ **portal_hub.html** — Landing page (pintu masuk 3 portal)
6. ✅ **vendor_kso_dashboard.html** — Portal vendor KSO dengan skema cost-per-test & revenue sharing
7. ✅ **vendor_hub.html** — Sub-hub Vendor B2B, 6 kategori: KSO Lab · KSO Farmasi · KSO BMHP · Alkes · Umum · Jasa
8. ✅ **proker_bulanan.html** — Rencana realisasi bulanan: Kasie konfirmasi dari daftar RKAP tahunan (bukan input dari nol)
9. ✅ **fase3_imt_pp_sppj.html** — Panel "Proker Cleared" auto-pull item siap tindak lanjut
10. ✅ **vendor_portal.html** — Notifikasi vendor otomatis saat item proker cleared
11. ✅ **MVP Tahap 1 (Core Internal)** — Akses Jaringan Lokal (0.0.0.0), Gudang Arsip Digital (Tabel `documents` & Folder `uploads/`), Endpoint Import RKAP CSV.
12. ✅ **Fix Logo** — Seluruh 28 file HTML sudah dikembalikan ke `logo_kmu.png` yang asli agar seragam dan rapi.
13. ✅ **Rencana Integrasi Email (Tahap Selanjutnya)** — Merancang skenario integrasi IMAP untuk `pengadaan@rspkt.id` otomatis menarik data PDF BAPB, Invoice, PO, dan Penawaran.

---

## STATUS GIT

**Semua perubahan SUDAH STAGED tapi BELUM COMMIT.**

Yang sudah bersih dari staging:
- `__pycache__/*.pyc` → sudah di-unstage
- `robocopy_log.txt` → sudah di-unstage
- `.gitignore` → sudah dibuat dan di-stage

**Kapan commit:** Lakukan SATU commit bersih setelah semua pekerjaan Tim IT selesai dan siap, bukan bertahap.

---

## STATUS BACKEND

**Cara start backend:**
```
cd D:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\backend
python main.py
```
atau via bat:
```
cd D:\digitalisasi_pengadan\SISTEM_TERINTEGRASI
START_BACKEND.bat
```

**Setelah backend jalan, buka browser:**
```
http://127.0.0.1:8000
```
Akan langsung redirect ke `portal_hub.html`.

**Endpoint yang sudah tersedia di `main.py`:**
- `GET/POST /api/proker` — rencana realisasi bulanan
- `POST /api/proker/{id}/status` — update status item (keuangan_clear → trigger notifikasi vendor)
- `GET /api/notifications` — notifikasi vendor per kategori
- `POST /api/notifications/{id}/read` — tandai notifikasi sudah dibaca
- `GET/POST /api/bapb` — Berita Acara Penerimaan Barang
- `GET /api/purchase-orders` — daftar PO

---

## BACKLOG — YANG MASIH PERLU DIKERJAKAN

### ✅ Prioritas 1 — Fix RAM/Freeze (command_center.html) (SELESAI)
- `command_center.html` punya `setInterval(fetchAll, 3000)` yang polling backend setiap 3 detik
- Masalah: DOM di-append tanpa di-trim + Tailwind Play CDN JIT scanner = RAM naik terus → laptop freeze
- Fix yang dilakukan: membatasi array data, membandingkan DOM sebelum re-render, mengurangi interval ke 5 detik.

### ✅ Prioritas 2 — Invoice 3-Way Match (Fase 7) (SELESAI)
- `fase7_invoice_3waymatch.html` sudah ada backend
- Endpoint `/api/invoices` dan logika matching: Invoice ↔ PO ↔ BAPB telah dibuat
- Status blok pembayaran otomatis jika tiga dokumen tidak cocok sudah diimplementasikan (status mismatch atau pending BAPB)

### Prioritas 3 — Halaman yang belum ada
- `FASE_1` s/d `FASE_9` — masing-masing ada `.mm` panduan interface
- Beberapa modul masih placeholder, cek folder masing-masing fase

### Prioritas 4 — Navigasi
- `portal_hub.html` sudah ada, pastikan semua link menuju halaman yang tepat

---

## ARSITEKTUR SISTEM (RINGKAS)

```
portal_hub.html                 → Landing page, pilih portal
  ├─ rs_klinik_dashboard.html       → Unit Bisnis (RS & Klinik)
  ├─ approval_dashboard.html        → Holding/Internal Pengadaan
  │    └─ proker_bulanan.html       → Rencana realisasi bulanan
  └─ vendor_hub.html                → Sub-hub Vendor B2B (6 kategori)
       ├─ vendor_kso_lab_portal.html    → KSO Laboratorium
       ├─ vendor_portal.html            → KSO Farmasi / Alkes / Umum / Jasa
       └─ vendor_kso_dashboard.html     → KSO BMHP

Backend: SISTEM_TERINTEGRASI/backend/main.py (FastAPI, port 8000)
DB:      SISTEM_TERINTEGRASI/backend/kmu_procurement.db (SQLite)
```

**3 Aturan GCG yang sudah di-hardcode:**
1. Alkes > Rp5Jt → Sentralisasi | ≤ Rp5Jt → Desentralisasi
2. Non-Alkes > Rp2Jt → Sentralisasi | ≤ Rp2Jt → Desentralisasi
3. Expired date farmasi < 6 bulan → blok otomatis

**Alur proker bulanan:**
```
[Awal Tahun] Bagian Umum input RKAP tahunan ke sistem
    → item terjadwal per bulan, disetujui GM + dikonfirmasi Keuangan

[Tiap Akhir Bulan — tgl 26-31]
Kasie Barang & Kasie Jasa:
    → Pilih/konfirmasi item RKAP yang jadwalnya bulan depan
    → Tambah catatan operasional jika perlu
    → Jika ada perubahan → ajukan via tab "Perubahan/Switching" (diproses Bagian Umum → GM)
    → Manager approve → Keuangan siapkan likuiditas

[Downstream]
    → Pengadaan proses PP (fase3_imt_pp_sppj.html)
    → Vendor dapat notifikasi alert di portal mereka
```

---

## INTEGRASI SIM EXISTING — KEPUTUSAN UNTUK TIM IT

### Konteks
Data RKAP sudah ada di SIM existing PT KMU: **`https://hormon.rspkt.com/`**

Di sistem pengadaan ini, data RKAP tahunan saat ini di-mock di frontend (`RKAP_TAHUNAN` object di `proker_bulanan.html`). Di production, data ini harus diambil langsung dari SIM existing — bukan di-input ulang.

---

### Dua Opsi Implementasi

#### Opsi A — Bridge API (Rekomendasi, paling cepat)
Backend FastAPI pengadaan tambah satu endpoint proxy:
```
GET /api/rkap-bridge?bulan=YYYY-MM
```
Yang di dalamnya memanggil SIM existing dan meneruskan hasilnya ke frontend pengadaan.

**Cocok jika:** SIM existing bisa expose JSON endpoint (REST API).

**Yang dibutuhkan dari Tim IT SIM existing:**
- URL endpoint data RKAP per bulan — contoh: `https://hormon.rspkt.com/api/rkap?tahun=2026`
- Format response JSON-nya (nama field, struktur data)
- Mekanisme autentikasi (API key / token / session)

**Contoh implementasi di `main.py`:**
```python
import httpx

@app.get("/api/rkap-bridge")
async def rkap_bridge(bulan: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://hormon.rspkt.com/api/rkap",
            params={"bulan": bulan},
            headers={"Authorization": "Bearer <TOKEN_SIM>"}
        )
        return r.json()
```

Di `proker_bulanan.html`, ganti `RKAP_TAHUNAN[bulan]` dengan:
```javascript
const items = await fetch(`${API_URL}/rkap-bridge?bulan=${bulan}`).then(r => r.json());
```

---

#### Opsi B — Sistem Pengadaan Jadi Bagian SIM Existing
Frontend pengadaan di-deploy langsung ke server `hormon.rspkt.com` — satu sistem, satu auth, satu domain.

**Cocok jika:** Tim IT ingin unified platform jangka panjang.

**Yang dibutuhkan:**
- Akses ke codebase SIM existing (tech stack apa? PHP/Laravel/Django/dll)
- Deploy backend FastAPI di server yang sama atau subdomain (misal: `api.hormon.rspkt.com`)
- Migrasi DB dari SQLite → MySQL/PostgreSQL (kemungkinan besar SIM existing sudah pakai ini)

---

### Yang Perlu Dijawab Tim IT Sebelum Implementasi

| Pertanyaan | Dampak ke Sistem Pengadaan |
|---|---|
| SIM existing punya REST API? | Opsi A langsung bisa jalan |
| Tech stack backend SIM? (PHP/Laravel/dll) | Tentukan apakah FastAPI bisa berdampingan |
| Database SIM pakai apa? (MySQL/PostgreSQL) | Perlu migrasi dari SQLite atau tidak |
| Auth SIM pakai apa? (SSO/JWT/session) | Bisa di-share ke frontend pengadaan |
| RKAP data ada di tabel apa di DB SIM? | Tentukan query/endpoint yang perlu diekspos |

---

### Solusi Sementara (Sebelum Integrasi Selesai)
Sambil menunggu keputusan arsitektur, `RKAP_TAHUNAN` di `proker_bulanan.html` bisa diganti dengan **import CSV/Excel** — Tim Pengadaan export RKAP dari SIM existing, upload ke sistem ini. Endpoint sudah bisa ditambah:
```
POST /api/rkap/import-csv
```

---

## FILE REFERENSI WAJIB SEBELUM MULAI
- `GLOSARIUM_ISTILAH_KMU.md` — terminologi PT KMU, jangan pakai istilah generik
- `MASTER_BLUEPRINT_SISTEM_PENGADAAN_KMU_TERINTEGRASI.md` — blueprint utama
- `PEDOMAN_SISTEM_IT_HANDOFF.md` — panduan teknis lengkap untuk Tim IT

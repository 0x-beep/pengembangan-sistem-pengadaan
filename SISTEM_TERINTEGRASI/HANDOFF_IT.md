# Handoff IT — Sistem Digitalisasi Pengadaan PT KMU

## Stack Frontend
- HTML/CSS/JS murni (Tailwind CDN, Font Awesome CDN)
- Tidak ada framework JS (React/Vue dll)
- Semua API call via `fetch()` ke `http://127.0.0.1:8000`

## Stack Backend (existing, bisa diganti)
- Python + FastAPI (tanpa pin versi)
- SQLite database: `kmu_procurement.db`
- Jalankan: `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

> **Jika IT menggunakan stack lain (Node/Laravel/Django dll):**
> Frontend tidak perlu diubah. Cukup implement endpoint-endpoint di bawah
> dengan response format yang sama. Base URL bisa disesuaikan di konstanta
> `API` / `API_URL` di masing-masing file HTML.

---

## Endpoint Auth yang Perlu Diimplementasi

### 1. `POST /api/auth/google`
Terima Google ID token dari frontend (Google Identity Services callback).
Verifikasi ke Google, optional lookup email vendor di database.

**Request body:**
```json
{
  "credential": "<google_id_token_string>",
  "check_vendor": true
}
```

**Response sukses:**
```json
{
  "status": "success",
  "user": {
    "email": "user@gmail.com",
    "name": "Nama User",
    "picture": "https://...",
    "email_verified": true
  },
  "vendor": {
    "vendor_id": "VND-001",
    "company_name": "PT Contoh",
    "vendor_status": "approved",
    "vendor_category": "KSO Lab"
  }
}
```
> `vendor` = `null` jika email tidak terdaftar di DB vendor.
> Jika `check_vendor: false`, cukup return `user`, `vendor` boleh `null`.

**Cara verifikasi token Google (backend):**
```
GET https://oauth2.googleapis.com/tokeninfo?id_token=<credential>
```
Response Google berisi `email`, `name`, `picture`, `email_verified`.

**Response error (401):**
```json
{ "detail": "Token Google tidak valid: ..." }
```

---

### 2. `GET /api/vendors/verify/{vendor_id}`
Cek apakah Vendor ID valid dan statusnya `approved`.
Dipakai sebagai fallback login di vendor_hub.html dan arm_portal.html.

**Path param:** `vendor_id` — contoh: `VND-001` (case-insensitive, normalize ke uppercase)

**Response sukses (200):**
```json
{
  "status": "success",
  "data": {
    "vendor_id": "VND-001",
    "company_name": "PT Contoh",
    "vendor_status": "approved",
    "vendor_type": "Barang",
    "vendor_category": "KSO Lab"
  }
}
```

**Response error:**
- `404` jika vendor_id tidak ditemukan
- `403` jika vendor_status bukan `approved`

```json
{ "detail": "Akun vendor belum aktif (status: submitted)" }
```

---

## Setup Google OAuth (untuk IT)

1. Buka [console.cloud.google.com](https://console.cloud.google.com)
2. Buat project baru (atau pakai existing)
3. APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID
4. Application type: **Web application**
5. Authorized JavaScript Origins:
   - `http://localhost` (development)
   - `http://localhost:8000`
   - `https://domain-prod.kmu.co.id` (production)
6. Salin **Client ID** yang dihasilkan
7. Cari `YOUR_GOOGLE_CLIENT_ID_HERE` di 3 file berikut dan ganti:
   - `frontend/portal_hub.html` (baris ~230)
   - `frontend/vendor_hub.html` (baris ~262)
   - `frontend/arm_portal.html` (baris ~122)

---

## Struktur Database (SQLite)

File: `backend/kmu_procurement.db`
Schema: `backend/database.py` fungsi `init_db()`

Tabel utama:
- `vendors` — data vendor (vendor_id, company_name, contact_person_email, vendor_status, ...)
- `users` — user internal (username, password_hash, role, vendor_id)
- `purchase_orders`, `tenders`, `requisitions`, `kso_evaluations`, dll

---

## File Frontend yang Perlu Perhatian

| File | Keterangan |
|------|-----------|
| `portal_hub.html` | Gerbang utama, ada Google Auth overlay |
| `vendor_hub.html` | Hub portal vendor, Google Auth + fallback VND-XXX |
| `arm_portal.html` | ARM (Anjungan Rekanan Mandiri), Google Auth + fallback |
| `pengadaan_dashboard.html` | Kanban board tim pengadaan |
| `command_center.html` | Dashboard KPI real-time (polling 15 detik) |
| `finance_dashboard.html` | Rencana pembayaran dari DB |
| `fase9_laporan_analitik.html` | Chart dari `/api/analytics/dashboard` |

Semua file frontend menggunakan `http://127.0.0.1:8000` sebagai base URL.
**Ganti ke URL prod** dengan cari-ganti `http://127.0.0.1:8000` di semua HTML.

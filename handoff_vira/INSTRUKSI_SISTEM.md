# INSTRUKSI SISTEM PROCUREMENT PT. KMU
## Single Source of Truth - Untuk Semua Session (Chat & Cowork)

**Last Updated:** 2026-06-05  
**Status:** ACTIVE - Reference untuk semua pekerjaan  
**Scope:** Pengadaan Barang & Jasa + Vendor Management PT. KMU

---

## 1️⃣ MANDATORY ALIGNMENT

### Setiap output WAJIB sesuai dengan:
- ✅ **Pedoman Pengadaan PT. KMU** (dari `SISTEM_PROCUREMENT.docx`)
- ✅ **Template Skoring Vendor** (dari `Template_Skoring_Pengadaan.xlsx`)
- ✅ **Terminologi PT. KMU** (bukan istilah generic)
- ✅ **Struktur RS** dengan KSO: Laboratorium, Farmasi, BMHP
- ✅ **SLA yang berlaku:**
  - Approval PO: ≤ 2 hari
  - Tender: ≤ 14 hari
  - Penerimaan Barang (BAPB): ≤ 7 hari
  - Pembayaran: ≤ 30 hari

### Integrasi dengan sistem:
- SIMRS (Sistem Informasi RS)
- Finance/ERP (Budgeting, Pembayaran)
- Warehouse/Inventory (Stok, Reorder)

### Compliance:
- LKPP (Lembaga Kebijakan Pengadaan Pemerintah)
- Permenkes (Peraturan Menteri Kesehatan)
- Audit trail untuk pengawasan internal & BPK

---

## 2️⃣ DOKUMEN SOURCE YANG SUDAH ADA

### Files di `/mnt/user-data/uploads/`:

| File | Tipe | Size | Konten |
|------|------|------|--------|
| SISTEM_PROCUREMENT.docx | Word | 11 KB | Pedoman & Framework 5 Lapisan |
| Template_Skoring_Pengadaan.xlsx | Excel | 8.5 KB | Kriteria Vendor Selection |
| 1780561275361_image.png | Image | 118 KB | (Diagram/Screenshot tertentu) |

### Info Penting dari dokumen:

#### SISTEM_PROCUREMENT.docx:
- **5 Lapisan IT Procurement:**
  1. Manajemen & Tata Kelola (E-Procurement, Workflow, Compliance)
  2. Operasional (Vendor Mgmt, Catalog, Contract Lifecycle)
  3. Integrasi (SIMRS, Finance, Warehouse)
  4. Analitik & Transparansi (Dashboard, Spend Analysis, Audit Trail)
  5. Infrastruktur & Keamanan (Cloud/Hybrid, SSO, Data Security)

- **Process Flow:** Requisition → Approval → Tender/Direct → Vendor → PO → Delivery → BAPB → Invoice → Payment

- **Risiko Misleading yang diperhatikan:**
  - Over-teknologi tanpa SDM readiness
  - Tidak account regulasi pemerintah
  - Kurang integrasi dengan SIMRS
  - Vendor resistance terhadap digital
  - Cash flow impact

#### Template_Skoring_Pengadaan.xlsx:
- **Kriteria Penilaian Vendor** (2 sheets):
  
  Sheet "Skoring":
  ```
  Harga Penawaran        → 25% bobot
  Kualitas Barang        → 20% bobot
  Maintenance & Sparepart → 20% bobot
  Kebutuhan User         → 20% bobot
  Orientasi Merek        → 15% bobot
  
  Total skor: 1-5 per kriteria, weighted calculation
  ```
  
  Sheet "Interpretasi":
  ```
  ≥ 400 poin → Rekomendasi Utama
  350-399 poin → Rekomendasi Alternatif
  300-349 poin → Pertimbangan dengan catatan
  < 300 poin → Tidak direkomendasikan
  ```

---

## 3️⃣ DELIVERABLES YANG DIMINTA

### Output yang akan dibuat:

```
TARGET OUTPUTS:

1. INSTRUKSI_SISTEM.md ← File ini (permanent reference)

2. KOORDINASI_SHEET.md (checklist & coordination notes)

3. SUMMARY_FINDINGS.md (ringkasan dari dokumen yang sudah dibaca)

4. MIND MAPS (untuk setiap module)
   ├─ Format: .mmap (MindManager), .xmind (XMind), .mm (FreeMind)
   ├─ Scope: 12 modules procurement system
   ├─ Detail: Aligned dengan 5 lapisan + flow PT. KMU
   └─ Status: [PENDING - dikerjakan di Cowork]

5. MATRIX/TABULASI (untuk pemetaan relasi)
   ├─ Responsibility Matrix (RACI)
   ├─ Vendor Scoring Matrix
   ├─ Process × Risk Matrix
   ├─ Authority Approval Matrix (per amount)
   ├─ Module × Stakeholder Matrix
   └─ Status: [PENDING - dikerjakan di Cowork]

6. VISUAL DIAGRAMS (Flow, Relationships)
   ├─ Process flow (swimlane)
   ├─ System architecture (5 lapisan)
   ├─ Vendor lifecycle
   └─ Status: [PENDING - dikerjakan di Cowork]

STRUKTUR FOLDER OUTPUT:
/mnt/user-data/outputs/
├─ INSTRUKSI_SISTEM.md (ini)
├─ KOORDINASI_SHEET.md
├─ SUMMARY_FINDINGS.md
├─ MINDMAPS/
│  ├─ 01_Module_1_Procurement_Platform.mmap
│  ├─ 01_Module_1_Procurement_Platform.xmind
│  ├─ 02_Module_2_Vendor_Management.mmap
│  └─ ... (dst 12 modules)
├─ MATRIX/
│  ├─ RACI_Matrix.xlsx
│  ├─ Vendor_Scoring_Matrix.xlsx
│  ├─ Process_Risk_Matrix.xlsx
│  └─ ...
├─ DIAGRAMS/
│  ├─ System_Architecture_5Layers.pdf
│  ├─ Process_Flow_Swimlane.pdf
│  └─ ...
└─ [Original 17 files dari blueprint sebelumnya]
```

---

## 4️⃣ EFISIENSI & STRATEGY

### Prinsip Kerja:

✅ **SINGLE PASS EXECUTION**
- Kerja sekali jadi, bukan template + refine
- Data Pedoman/SPO jadi guideline
- Output langsung final-ready

✅ **KOORDINASI CROSS-SESSION**
- Chat session (tablet): Koordinasi & planning
- Cowork session (PC): Execution & implementation
- File ini jadi "jembatan" komunikasi

✅ **HEMAT TOKEN & WAKTU**
- Tidak ada pekerjaan duplikat
- Clear checklist apa yg perlu dikerjakan
- Notes & findings siap dibawa ke Cowork

---

## 5️⃣ PERTANYAAN BELUM TERJAWAB

### Data yang mungkin masih diperlukan (optional):

```
❓ Struktur Organisasi PT. KMU
   → Untuk mapping stakeholder & approval authority
   
❓ Daftar Kategori Barang/Jasa detail
   → Untuk mapping product categories
   
❓ Template PO/BAPB/Invoice yg sudah ada
   → Untuk alignment dengan existing process
   
❓ Thresholds & Approval limits spesifik PT. KMU
   → Untuk mapping authority matrix
```

**Status:** Bisa ambil asumsi dari best practice RS standard jika belum available.

---

## 6️⃣ RENCANA KERJA (COWORK)

### Fase 1: PREPARATION (SUDAH SELESAI)
- ✅ Baca SISTEM_PROCUREMENT.docx
- ✅ Analisis Template_Skoring_Pengadaan.xlsx
- ✅ Dokumentasi findings & requirements
- ✅ Buat instruksi permanent (file ini)

### Fase 2: MIND MAP & MATRIX (NEXT - di Cowork)
- [ ] Bikin Mind Map untuk 12 modules
- [ ] Bikin Master Mind Map (overview keseluruhan)
- [ ] Bikin 5+ matrix/tabulasi
- [ ] Export ke berbagai format (.mmap, .xlsx, .xmind, .pdf)

### Fase 3: REFINEMENT (Jika ada feedback)
- [ ] Review dengan dokumen asli
- [ ] Adjust terminology & struktur
- [ ] Final validation

### Timeline:
```
Session Cowork 1: Mind Map Module 1-4 + Matrix utama
Session Cowork 2: Mind Map Module 5-8 + Matrix lanjut
Session Cowork 3: Mind Map Module 9-12 + Master Map
Session Cowork 4: Refinement & Final Export
```

---

## 7️⃣ ISTILAH & SINGKATAN (dari dokumen)

| Istilah | Arti | Konteks |
|---------|------|---------|
| KSO | Kerjasama Operasional | Laboratorium, Farmasi, BMHP |
| SIMRS | Sistem Informasi RS | Integrasi sistem |
| LKPP | Lembaga Kebijakan Pengadaan Pemerintah | Compliance |
| Permenkes | Peraturan Menteri Kesehatan | Compliance |
| BAPB | Berita Acara Penerimaan Barang | Penerimaan barang |
| PO | Purchase Order | Order ke vendor |
| SLA | Service Level Agreement | Timeframe per tahap |
| 3-Way Match | PO ↔ BAPB ↔ Invoice | Validasi pembayaran |

---

## 8️⃣ CATATAN PENTING

### Yang HARUS diperhatikan:
1. **RS ≠ Organisasi generik** → Kompleksitas lebih tinggi (barang medis, regulasi ketat)
2. **KSO = partnership penting** → Bukan vendor biasa (lab, farmasi, BMHP)
3. **SLA ketat** → Approval 2h, tender 14h, deliver 7h (timeline important)
4. **Multi-layer integration** → Tidak bisa standalone, harus integrasi dengan SIMRS/Finance
5. **Vendor readiness** → Tidak semua vendor siap digital procurement
6. **Compliance mandatory** → LKPP, Permenkes bukan optional

### Yang BISA flexible:
- Technology stack (cloud/hybrid/on-premise)
- UI/UX design approach
- Automation level detail
- Reporting format & frequency

---

## 9️⃣ NEXT STEPS

### Immediate Actions:
1. ✅ **Chat Session:** Baca instruksi ini, confirm understanding
2. ✅ **Chat Session:** Ambil KOORDINASI_SHEET.md & SUMMARY_FINDINGS.md
3. ✅ **Cowork Session:** Baca semua 3 file itu sebagai konteks
4. → **Cowork Session:** Mulai bikin Mind Maps & Matrix

### Contact Points:
- **File Koordinasi:** KOORDINASI_SHEET.md (checklist & notes)
- **File Reference:** INSTRUKSI_SISTEM.md (ini)
- **File Summary:** SUMMARY_FINDINGS.md (ringkasan findings)

---

## 📌 FINAL NOTES

**File ini adalah REFERENCE PERMANENT untuk semua session.**

Kalau ada perubahan requirement:
1. Update file ini
2. Notify session yang bersangkutan
3. Ensure consistency across semua work

**Tujuan:** Eliminate redundant explanations, speed up execution, maintain consistency.

---

**STATUS: READY FOR COWORK SESSION** ✅


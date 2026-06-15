# SUMMARY FINDINGS - PT. KMU PROCUREMENT SYSTEM
## Ringkasan Detail dari Source Documents

**Created:** 2026-06-05  
**From:** SISTEM_PROCUREMENT.docx + Template_Skoring_Pengadaan.xlsx  
**Purpose:** Quick reference untuk implementation di Cowork  

---

## 📄 DOKUMEN SOURCE

### File 1: SISTEM_PROCUREMENT.docx
**Size:** 11 KB  
**Type:** Word document (Pedoman/Framework)  
**Key Author Intent:** Describe system architecture & requirements for PT. KMU procurement digitalization

### File 2: Template_Skoring_Pengadaan.xlsx
**Size:** 8.5 KB  
**Type:** Excel spreadsheet (Vendor Scoring Template)  
**Sheets:** 2 (Skoring + Interpretasi)

---

## 🏥 KONTEKS ORGANISASI: PT. KMU (Rumah Sakit)

### Karakteristik Unik:
```
1. ORGANISASI KESEHATAN (Rumah Sakit)
   ├─ Tidak seperti organisasi komersial biasa
   ├─ Barang & jasa vital untuk patient care
   ├─ Regulasi ketat dari pemerintah
   └─ Integrasi dengan clinical systems

2. KOMPLEKSITAS BARANG/JASA
   ├─ Barang Medis (obat, alat kesehatan, BHP)
   ├─ Jasa Pendukung (maintenance, cleaning, sewa kendaraan, SDM outsourcing, konsultasi)
   ├─ KSO (Kerjasama Operasional) khusus:
   │  ├─ Laboratorium (Lab)
   │  ├─ Farmasi (Pharmacy)
   │  └─ BMHP (Barang Medis Habis Pakai)
   └─ Kebutuhan emergency/urgent (patient care cannot wait)

3. REGULASI & COMPLIANCE
   ├─ Permenkes (Peraturan Menteri Kesehatan)
   ├─ LKPP (Lembaga Kebijakan Pengadaan Pemerintah) - jika RS negeri
   ├─ Regulasi pemerintah lainnya
   └─ Audit internal + eksternal (BPK jika BUMN)

4. INTEGRASI SISTEM CRITICAL
   ├─ SIMRS (Sistem Informasi Manajemen Rumah Sakit)
   ├─ Finance/ERP (Budgeting, Pembayaran, Akuntansi)
   ├─ Warehouse/Inventory (Stok Barang, Reorder Point)
   └─ Clinical systems (Farmasi, Lab, dll)
```

---

## 🏗️ SISTEM ARCHITECTURE: 5 LAPISAN

### Dari SISTEM_PROCUREMENT.docx → Framing Section

Sistem IT Procurement dibagi menjadi **5 Lapisan**:

```
LAPISAN 1: MANAJEMEN & TATA KELOLA (Management & Governance)
├─ Modul E-Procurement
│  ├─ Pengajuan kebutuhan (requisition)
│  ├─ Approval berjenjang (hierarchical workflow)
│  └─ Tender atau penunjukan langsung (direct PO)
├─ Workflow Otomatis
│  ├─ User → Departemen Pengadaan → Komite Anggaran → Direktur → Vendor
│  └─ Tracking real-time per tahap
└─ Regulatory Compliance Engine
   ├─ Memastikan setiap proses sesuai LKPP/Permenkes
   ├─ Automated rule enforcement
   └─ Audit trail complete

LAPISAN 2: OPERASIONAL (Operational)
├─ Vendor Management System
│  ├─ Registrasi vendor
│  ├─ Verifikasi legalitas
│  └─ Penilaian kinerja (performance rating)
├─ Catalog Management
│  ├─ Daftar barang/jasa standar
│  ├─ Harga acuan (reference pricing)
│  └─ E-catalog LKPP integration
└─ Contract Lifecycle Management
   ├─ Drafting contract
   ├─ Digital signature
   └─ Monitoring contract validity

LAPISAN 3: INTEGRASI (Integration)
├─ Integrasi dengan SIMRS
│  ├─ Pull kebutuhan dari Farmasi, Alat, KSO
│  └─ Real-time visibility ke clinical needs
├─ Integrasi dengan Finance/ERP
│  ├─ Budgeting (budget available check)
│  ├─ Pembayaran (payment execution)
│  └─ Pencatatan akuntansi (general ledger)
└─ Integrasi dengan Warehouse/Inventory
   ├─ Stok gudang real-time
   ├─ Reorder point tracking
   └─ Buffer safety management

LAPISAN 4: ANALITIK & TRANSPARANSI (Analytics & Transparency)
├─ Dashboard Pengadaan
│  ├─ Status real-time
│  ├─ SLA approval tracking
│  ├─ Nilai kontrak berjalan
│  └─ KPI visualization (Command Center)
├─ Spend Analysis
│  ├─ Analisis efisiensi
│  ├─ Identifikasi potensi pemborosan
│  └─ Vendor performance benchmarking
└─ Audit Trail Digital
   ├─ Rekam jejak lengkap
   ├─ Pengawasan internal
   └─ Pengawasan eksternal + BPK

LAPISAN 5: INFRASTRUKTUR & KEAMANAN (Infrastructure & Security)
├─ Cloud/Hybrid Deployment
│  ├─ Server internal RS
│  ├─ Cloud option (flexibility)
│  └─ Disaster recovery plan
├─ Single Sign-On (SSO)
│  ├─ Akses terkendali per jabatan
│  └─ Role-based access control
└─ Data Security
   ├─ Enkripsi data
   ├─ Backup management
   └─ Disaster recovery infrastructure
```

---

## ⏱️ SLA (SERVICE LEVEL AGREEMENT) - TIMELINE KRITIS

### Dari SISTEM_PROCUREMENT.docx → Process Section

Proses pengadaan RS memiliki SLA per tahap:

```
TAHAP 1: PENGAJUAN KEBUTUHAN (Requisition)
├─ Actor: Unit RS (Departemen/Klinik)
├─ Action: Ajukan permintaan barang/jasa
├─ SLA: ≤ 1 hari
└─ System tracking: Requisition entry timestamp

TAHAP 2: REVIEW & APPROVAL PENGADAAN (Procurement review)
├─ Actor: Tim Departemen Pengadaan
├─ Action: Review permintaan, tentukan metode pengadaan
├─ Decision: 
│  ├─ Gunakan E-Catalog (direct PO)
│  ├─ Proses Tender (competitive)
│  └─ Penunjukan Langsung (direct assignment)
└─ SLA: ≤ 2 hari

TAHAP 3A: PROSES TENDER (If competitive bidding)
├─ Actor: Pengadaan Team + Vendor
├─ Actions:
│  ├─ Tender announcement
│  ├─ Vendor submissions
│  ├─ Quote evaluation
│  └─ Vendor selection
└─ SLA: ≤ 14 hari

TAHAP 3B: PENUNJUKAN LANGSUNG (If direct or catalog)
├─ Actor: Pengadaan Team
├─ Actions:
│  ├─ Select vendor
│  └─ Verify & prepare PO
└─ SLA: ≤ 3 hari

TAHAP 4: TERBITKAN PO (Purchase Order)
├─ Actor: Pengadaan Team
├─ Action: Generate & send PO to vendor
├─ SLA: ≤ 1 hari
└─ System: PO issued timestamp

TAHAP 5: PENGIRIMAN BARANG (Delivery)
├─ Actor: Vendor
├─ Action: Manufacture/prepare & deliver goods
├─ SLA: ≤ 7 hari (setelah PO)
└─ Tracking: Delivery timestamp, tracking #

TAHAP 6: PENERIMAAN & QC (BAPB - Berita Acara Penerimaan Barang)
├─ Actor: Gudang/Unit Penerima + QA
├─ Actions:
│  ├─ Receive barang
│  ├─ Quality check
│  ├─ Count verification
│  └─ Buat BAPB (jika lulus QC) or Rejection
├─ SLA: ≤ 2 hari
└─ System: BAPB timestamp, quality data logged

TAHAP 7: INVOICE & PEMBAYARAN (Invoice & Payment)
├─ Vendor submits invoice
│  ├─ Should match PO & BAPB (3-Way Match)
│  ├─ SLA Invoice submission: ≤ 3 hari setelah BAPB
│  └─ System: Invoice received timestamp
│
├─ Finance validates
│  ├─ 3-Way Match: PO ↔ BAPB ↔ Invoice
│  ├─ SLA validation: ≤ 5 hari
│  └─ System: 3-Way Match validation logged
│
└─ Payment executed
   ├─ Due date: Net 30 dari invoice date
   ├─ Timing: Pay 2-3 hari sebelum due date
   ├─ SLA Payment: ≤ 30 hari
   └─ System: Payment timestamp, bank transfer confirmation

TOTAL CYCLE TIME: ~47-60 hari (worst case, tender path)
FAST TRACK: ~15-20 hari (direct PO or catalog)
```

### SLA Importance:
```
✅ Audit internal requirement
✅ Regulatory compliance (LKPP, Permenkes)
✅ Performance measurement
✅ Vendor accountability
✅ Cash flow planning
✅ Patient care continuity
```

---

## 🎯 VENDOR SCORING CRITERIA

### Dari Template_Skoring_Pengadaan.xlsx

#### Sheet "Skoring" (Penilaian):

```
KRITERIA PENILAIAN VENDOR: 5 Dimensi

1. HARGA PENAWARAN
   ├─ Bobot: 25%
   ├─ Scoring: 1-5 (1=termahal, 5=termurah)
   ├─ Calculation: Bobot × Score / 100 = Weighted score
   ├─ Rationale: Cost control important tapi bukan satu-satunya faktor
   └─ Note: Jangan pilih harga termurah jika kualitas rendah

2. KUALITAS BARANG
   ├─ Bobot: 20%
   ├─ Scoring: 1-5 (1=poor quality, 5=excellent quality)
   ├─ Assessment: Material, durability, standards compliance
   ├─ Calculation: Bobot × Score / 100
   └─ Rationale: RS critical → quality tidak boleh compromised

3. MAINTENANCE & SPAREPART
   ├─ Bobot: 20%
   ├─ Scoring: 1-5 (1=difficult to service, 5=excellent support)
   ├─ Assessment: Availability, response time, cost of maintenance
   ├─ Calculation: Bobot × Score / 100
   └─ Rationale: Equipment durability & serviceability vital for RS operations

4. KEBUTUHAN USER
   ├─ Bobot: 20%
   ├─ Scoring: 1-5 (1=doesn't meet needs, 5=exceeds expectations)
   ├─ Assessment: Fit to clinical requirements, usability, training
   ├─ Calculation: Bobot × Score / 100
   └─ Rationale: End user satisfaction = patient care quality

5. ORIENTASI MEREK (Brand/Vendor Preference)
   ├─ Bobot: 15%
   ├─ Scoring: 1-5 (1=unknown/unreliable, 5=trusted brand)
   ├─ Assessment: Vendor reputation, track record with RS
   ├─ Calculation: Bobot × Score / 100
   └─ Rationale: Established vendors = lower risk

TOTAL CALCULATION:
Score = (25% × Harga Score) + (20% × Kualitas Score) + 
         (20% × Maintenance Score) + (20% × User Score) + 
         (15% × Brand Score)

Maximum Score: 100 poin (jika semua kriteria score 5)
Minimum Score: 20 poin (jika semua kriteria score 1)
```

#### Sheet "Interpretasi" (Interpretation):

```
RECOMMENDATION CATEGORIES (Berdasarkan Total Score):

Score ≥ 400 poin (80% dari max 500)
├─ Category: REKOMENDASI UTAMA (Primary Recommendation)
├─ Action: AWARD CONTRACT → Vendor ini pilihan terbaik
└─ Reason: Excellent across all criteria

Score 350-399 poin (70-79%)
├─ Category: REKOMENDASI ALTERNATIF (Alternative Recommendation)
├─ Action: AWARD IF PRIMARY UNAVAILABLE → Vendor backup option
└─ Reason: Good enough, tapi ada area untuk improvement

Score 300-349 poin (60-69%)
├─ Category: PERTIMBANGAN DENGAN CATATAN (Proceed with Caution)
├─ Action: NEGOTIATE TERMS atau SKIP → Approval with conditions
└─ Reason: Several criteria below expectations

Score < 300 poin (<60%)
├─ Category: TIDAK DIREKOMENDASIKAN (Not Recommended)
├─ Action: REJECT → Don't award contract to vendor ini
└─ Reason: Failed to meet minimum acceptable standards

INTERPRETATION NOTES:
- Scoring bukan rigid, bisa disesuaikan per kategori barang
- Alat kesehatan critical: Bobot Quality lebih tinggi
- Jasa layanan: Bobot User Need & Maintenance lebih penting
- Vendor yang sama untuk berbagai category: Maintain history/track record
```

---

## 🔄 PROCESS FLOW - SWIMLANE OVERVIEW

### Dari SISTEM_PROCUREMENT.docx → Flowchart Section

```
DIAGRAM SWIMLANE (Simplified):

Unit RS          Pengadaan Team          Vendor            Gudang            Finance
   │                  │                    │                 │                 │
   │─ Pengajuan       │                    │                 │                 │
   │  Kebutuhan       │                    │                 │                 │
   │──────────────────►│                    │                 │                 │
   │ (≤1 hari)        │                    │                 │                 │
   │                  │─ Review &          │                 │                 │
   │                  │  Decide Metode     │                 │                 │
   │                  │ (≤2 hari)          │                 │                 │
   │                  │                    │                 │                 │
   │                  ├─ Tender atau       │                 │                 │
   │                  │  Direct PO         │                 │                 │
   │                  │ (≤14 hari or ≤3h)  │                 │                 │
   │                  │                    │                 │                 │
   │                  │─ Terbitkan PO      │                 │                 │
   │                  │ (≤1 hari)          │                 │                 │
   │                  │────────────────────►│                 │                 │
   │                  │                    │─ Kirim Barang   │                 │
   │                  │                    │ (≤7 hari)       │                 │
   │                  │                    │──────────────────►│                 │
   │                  │                    │                 │─ QC & BAPB       │
   │                  │                    │                 │ (≤2 hari)       │
   │                  │                    │                 │ [Buat BAPB]    │
   │                  │                    │─── Invoice ─────────────────────────►│
   │                  │                    │ (≤3 hari        │                 │
   │                  │                    │  setelah BAPB)   │                 │
   │                  │                    │                 │─ 3-way Match   │
   │                  │                    │                 │ (≤5 hari)       │
   │                  │                    │                 │─ Payment       │
   │                  │                    │                 │ (≤30 hari)     │
   │                  │                    │                 │                 │

CYCLE TIME CALCULATION:
Fast Track (Direct PO):    1+2+3+1+7+2+3+5+30 = ~54 days
Tender Path (Competitive): 1+2+14+1+7+2+3+5+30 = ~65 days
Ideal Case (with parallelization): ~35-45 days
```

---

## ⚠️ RISIKO & MITIGASI

### Dari SISTEM_PROCUREMENT.docx → Risk Misleading Section

```
RISIKO 1: Over-teknologi tanpa kesiapan SDM
├─ Issue: Sistem canggih tapi staff tidak siap pakai
├─ Consequence: System adoption failure, manual workarounds continue
└─ Mitigation:
   ├─ Extensive training program
   ├─ Change management (process reengineering)
   └─ Phased rollout dengan support team

RISIKO 2: Tidak memperhitungkan regulasi pemerintah
├─ Issue: RS swasta vs RS negeri punya rule berbeda
├─ Consequence: Non-compliance, audit findings
└─ Mitigation:
   ├─ Clear regulatory mapping (LKPP, Permenkes)
   ├─ Compliance engine built-in
   └─ Legal review sebelum go-live

RISIKO 3: Kurang integrasi dengan SIMRS
├─ Issue: Hanya standalone app, tidak connected ke clinical systems
├─ Consequence: Data silos, manual re-entry, inefficiency
└─ Mitigation:
   ├─ API integration dengan SIMRS mandatory
   ├─ Real-time data sync
   └─ Single source of truth

RISIKO 4: Vendor Resistance (tidak siap digital)
├─ Issue: Vendor lama terbiasa paper-based PO & invoicing
├─ Consequence: Slow adoption, delayed payments, complaints
└─ Mitigation:
   ├─ Vendor onboarding program
   ├─ Support & training for digital procurement
   ├─ Phased rollout (large vendors first)
   └─ Fallback to manual if needed (at cost)

RISIKO 5: Biaya awal tinggi (cash flow impact)
├─ Issue: Development & implementation cost significant
├─ Consequence: Budget pressure, might delay project
└─ Mitigation:
   ├─ ROI calculation (cost savings justify investment)
   ├─ Phased implementation (spread cost over time)
   ├─ Cloud option (OpEx vs CapEx)
   └─ Grant/subsidy opportunities
```

---

## 📊 MAPPING KE 12 MODULES

### Bagaimana 5 Lapisan & Requirements memetakan ke 12 Modules:

```
MODULE 1: Procurement Platform
├─ Covers: Lapisan 1 (Management & Governance)
├─ Focus: Requisition → Approval → Tender/Direct → PO
├─ SLA: Most critical (approval ≤2h)
└─ Integration: SIMRS requisition input

MODULES 2, 7, 10: Vendor Management
├─ Covers: Lapisan 2 (Operational)
├─ Focus: Registration → Verification → Database → KSO
├─ KSO: Lab, Farmasi, BMHP
└─ Integration: Vendor master data

MODULE 3: Vendor Portal
├─ Covers: Lapisan 2 (Operational)
├─ Focus: Self-service vendor platform
├─ KSO Obligation tracking
└─ Communication channel

MODULE 4: AI Compliance Guardian
├─ Covers: Lapisan 1 (Governance) + Lapisan 4 (Audit Trail)
├─ Focus: SOP enforcement, rule engine
├─ Compliance: LKPP, Permenkes
└─ Automation: Violation detection

MODULES 5-8: Execution (Delivery, Quality, Invoice, Payment)
├─ Covers: All 5 Lapisan (integration point)
├─ Focus: BAPB → QC → Invoice → 3-way Match → Payment
├─ SLA: Receive ≤7h, QC ≤2h, Invoice ≤3h, Payment ≤30h
└─ Integration: Finance/ERP, Warehouse

MODULE 9: Reporting & Analytics
├─ Covers: Lapisan 4 (Analytics & Transparency)
├─ Focus: Dashboard, Spend analysis, Vendor performance
├─ SLA visibility: Track all stages
└─ Command Center: Executive dashboard

MODULE 11: Master Database & Compliance
├─ Covers: Lapisan 5 (Infrastructure) + Lapisan 2 (Data)
├─ Focus: Data structure, security, KSO contracts
└─ Integration: Data warehouse

MODULE 12: Vendor Evaluation
├─ Covers: Lapisan 4 (Analytics) + Lapisan 2 (Vendor Mgmt)
├─ Focus: 7-dimension scoring, contracts renewal
├─ Scoring: Based on Template_Skoring_Pengadaan criteria
└─ Frequency: Monthly, Quarterly, Annual
```

---

## 🗂️ KEY DOCUMENTS & ARTIFACTS

### Artifacts dari Dokumen Source:

```
FROM SISTEM_PROCUREMENT.docx:
├─ 5-Layer Architecture (Lapisan)
├─ Process Flow (Swimlane diagram)
├─ SLA Timeline (per stage)
├─ Risiko & Mitigasi (5 main risks)
├─ Integration Points (SIMRS, Finance, Warehouse)
└─ Compliance Requirements (LKPP, Permenkes)

FROM Template_Skoring_Pengadaan.xlsx:
├─ 5 Vendor Scoring Criteria
├─ Bobot per Criteria (25%, 20%, 20%, 20%, 15%)
├─ Scoring Scale (1-5 points)
├─ Recommendation Categories (≥400, 350-399, 300-349, <300)
└─ Calculation Formula (Weighted scoring)

IMPLICIT/TO-BE-CLARIFIED:
├─ Exact vendor scoring sub-criteria detail
├─ KSO specific requirements (Lab, Farmasi, BMHP)
├─ SIMRS integration API details
├─ Finance/ERP integration points
├─ Approval authority matrix (by amount)
└─ Stakeholder roles per process
```

---

## 💡 KEY INSIGHTS FOR MIND MAP CREATION

### What to emphasize:

```
1. KSO is NOT regular vendor
   └─ Laboratorium, Farmasi, BMHP = Special partnerships
   └─ Own evaluation criteria
   └─ Different approval process

2. SLA is CRITICAL
   └─ Every stage has timeline
   └─ Delays cascade (if approve late → delivery late → payment late)
   └─ Track & measure strictly

3. Integration is MANDATORY
   └─ Cannot be standalone system
   └─ SIMRS feeds requirements
   └─ Finance tracks payments
   └─ Warehouse tracks inventory

4. Compliance is Non-negotiable
   └─ LKPP + Permenkes must be satisfied
   └─ Audit trail mandatory
   └─ Every decision must be documented

5. Vendor Scoring is Balanced
   └─ Not just price (25%) - quality (20%), service (20%), fit (20%), brand (15%)
   └─ Multi-criteria decision making
   └─ Prevents "cheapest vendor" trap

6. 5 Layers is Architecture Blueprint
   └─ Layer 1-5 each has specific responsibility
   └─ Integration between layers critical
   └─ Security & compliance in Layer 5
```

---

## ✅ VALIDATION CHECKLIST

When creating Mind Maps & Matrices, ensure:

```
FROM SISTEM_PROCUREMENT.docx:
- [ ] All 5 Lapisan (Layers) represented
- [ ] Process flow matches swimlane diagram
- [ ] All SLA timelines included (1h, 2h, 14h, 3h, 7h, 2h, 3h, 5h, 30h)
- [ ] Integration points marked (SIMRS, Finance, Warehouse)
- [ ] Compliance requirements noted (LKPP, Permenkes)
- [ ] KSO structure included (Lab, Farmasi, BMHP)
- [ ] Risiko & Mitigasi considerations included

FROM Template_Skoring_Pengadaan.xlsx:
- [ ] 5 Scoring Criteria correct (Harga 25%, Kualitas 20%, Maintenance 20%, User 20%, Brand 15%)
- [ ] Scoring scale is 1-5
- [ ] Recommendation categories correct (≥400, 350-399, 300-349, <300)
- [ ] Weighted formula is correct
- [ ] Interpretation guide matches

GENERAL:
- [ ] Terminology matches PT. KMU usage
- [ ] No generic procurement terminology
- [ ] Readable & understandable
- [ ] Color-coded for clarity
- [ ] All stakeholders identified
- [ ] No missing critical information
```

---

## 📌 FINAL NOTES FOR COWORK

This summary contains:
✅ Organizational context (RS with complexity)  
✅ 5-layer architecture breakdown  
✅ Complete SLA timeline  
✅ Vendor scoring detail  
✅ Process flow overview  
✅ Risk mapping  
✅ Module allocation  
✅ Validation checklist  

**Use this as reference while creating Mind Maps & Matrices in Cowork.**

Everything is documented. Everything is clear.

**Ready to execute!** 🚀

---

**Summary Created:** 2026-06-05  
**For:** Cowork Session Preparation  
**Status:** COMPLETE & READY FOR USE


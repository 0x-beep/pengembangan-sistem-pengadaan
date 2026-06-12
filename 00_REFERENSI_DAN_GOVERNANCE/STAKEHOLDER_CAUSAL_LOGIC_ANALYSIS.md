# STAKEHOLDER ANALYSIS & CAUSAL LOGIC MAP
## PT KMU Comprehensive Procurement & Vendor Management System

**Purpose:** Identify all stakeholders across system modules, show overlaps, define roles, causality, risk mitigation, and benefits  
**Scope:** All 14 modules + integrated system  
**Analysis Type:** Stakeholder mapping with functional dependencies  

---

## TABLE OF CONTENTS

1. [Complete Stakeholder List](#complete-stakeholder-list)
2. [Stakeholder Overlap Analysis (Beririsan)](#stakeholder-overlap-analysis)
3. [Causal Logic & Dependencies](#causal-logic--dependencies)
4. [Stakeholder Roles & Functions](#stakeholder-roles--functions)
5. [Risk Mitigation By Stakeholder](#risk-mitigation-by-stakeholder)
6. [Benefits By Stakeholder](#benefits-by-stakeholder)
7. [Decision Authority & Accountability](#decision-authority--accountability)

---

## COMPLETE STAKEHOLDER LIST

### Internal Stakeholders (PT KMU)

```
1. PROCUREMENT OFFICER
   ├─ Appears in: 9 modules (1,2,3,5,6,7,8,11,12)
   ├─ Reporting To: Manager Pengadaan
   └─ Primary: Day-to-day procurement execution

2. PROCUREMENT MANAGER
   ├─ Appears in: 9 modules (1,2,3,5,6,7,8,11,12)
   ├─ Reporting To: GM Operasi
   └─ Primary: Procurement operations & team leadership

3. VENDOR MANAGER
   ├─ Appears in: 8 modules (2,3,5,7,8,9,10,12)
   ├─ Reporting To: Manager Pengadaan or GM Operasi
   └─ Primary: Vendor relationships & performance

4. VENDOR Direktur Operasi & PengembanganRDINATOR
   ├─ Appears in: 5 modules (3,5,7,8,9)
   ├─ Reporting To: Kasie Pengadaan Jasa
   └─ Primary: Day-to-day vendor communication

5. COMPLIANCE OFFICER
   ├─ Appears in: 4 modules (4,5,6,11)
   ├─ Reporting To: GM Operasi or Audit
   └─ Primary: SOP compliance & enforcement

6. FINANCE MANAGER (Procurement Finance)
   ├─ Appears in: 7 modules (1,2,5,6,8,9,10)
   ├─ Reporting To: Direktur Keuangan, SDM dan Umum
   └─ Primary: Payment processing & budget approval

7. Direktur Keuangan, SDM dan Umum (Direktur Keuangan, SDM dan Umum)
   ├─ Appears in: 5 modules (1,2,9,10,12)
   ├─ Reporting To: Direksi PT KMU
   └─ Primary: Strategic financial decisions

8. VP OPERATIONS
   ├─ Appears in: 12 modules (nearly all)
   ├─ Reporting To: Direktur Utama / Direksi PT KMU
   └─ Primary: Executive operations leadership

9. UNIT MANAGER (Departmental Heads)
   ├─ Appears in: 3 modules (1,5,7)
   ├─ Reporting To: GM Operasi
   └─ Primary: Departmental requirements

10. QUALITY ASSURANCE STAFF
    ├─ Appears in: 3 modules (1,5,12)
    ├─ Reporting To: Operations Manager
    └─ Primary: Goods inspection & quality check

11. BOARD OF DIRECTORS
    ├─ Appears in: 6 modules (1,2,3,9,10,12)
    ├─ Reporting To: Shareholders
    └─ Primary: Governance & strategic decisions

12. FINANCE ANALYST
    ├─ Appears in: 3 modules (9,10,12)
    ├─ Reporting To: Kepala Bagian Keuangan/Direktur Keuangan, SDM dan Umum
    └─ Primary: Financial analysis & reporting

13. IT INFRASTRUCTURE TEAM
    ├─ Appears in: All modules (technical)
    ├─ Reporting To: CIO/GM Operasi
    └─ Primary: System implementation & maintenance

14. AI CHATBOT (Penjaga Kepatuhan SPO)
    ├─ Appears in: 1 module (4)
    ├─ Reporting To: N/A (automated system)
    └─ Primary: Automated SOP guidance
```

### External Stakeholders

```
15. VENDORS (Suppliers)
    ├─ Appears in: 8 modules (2,3,5,7,8,9,10,12)
    ├─ Relationship: Commercial partnership
    └─ Primary: Good/service delivery

16. CUSTOMERS/PATIENTS (Indirect)
    ├─ Appears in: 4 modules (1,3,5,12)
    ├─ Relationship: Beneficiary
    └─ Primary: End-user of procured items

17. GOVERNMENT/REGULATORY BODIES
    ├─ Appears in: 6 modules (3,4,5,6,8,10)
    ├─ Relationship: Compliance requirement
    └─ Primary: Regulatory oversight

18. AUDIT FIRM (External Auditors)
    ├─ Appears in: 6 modules (1,5,6,9,10,11)
    ├─ Relationship: Third-party verification
    └─ Primary: Independent audit & verification
```

---

## STAKEHOLDER OVERLAP ANALYSIS (BERIRISAN)

### Who Overlaps with Whom?

```
HIGHEST OVERLAP STAKEHOLDERS (5+ modules):

1. VP OPERATIONS (12 modules)
   ├─ Overlaps with: Everyone (central hub)
   ├─ Critical decision-maker
   └─ Touch all major processes

2. PROCUREMENT MANAGER (9 modules)
   ├─ Overlaps with: Admin Pengadaan Barang, Kasie Pengadaan Jasa, 
   │                 Kepala Bagian Keuangan, GM Operasi, Direksi PT KMU
   ├─ Operational coordinator
   └─ Central operational hub

3. VENDOR MANAGER (8 modules)
   ├─ Overlaps with: Manager Pengadaan, Kepala Bagian Keuangan,
   │                 Admin Pengadaan Jasa, Staf SPI
   ├─ Vendor relationship owner
   └─ Vendor-side central hub

4. VENDORS (External) (8 modules)
   ├─ Overlaps with: Kasie Pengadaan Jasa, Coordinator, 
   │                 Kepala Bagian Keuangan, QA Staff
   ├─ Service delivery partner
   └─ External-side central hub

5. FINANCE MANAGER (7 modules)
   ├─ Overlaps with: Manager Pengadaan, Staf Keuangan,
   │                 Direktur Keuangan, SDM dan Umum, Kasie Pengadaan Jasa, QA Staff
   ├─ Financial gatekeeper
   └─ Financial-side central hub

MEDIUM OVERLAP (3-4 modules):

6. BOARD OF DIRECTORS (6 modules)
   ├─ Executive governance
   └─ High-value decisions

7. COMPLIANCE OFFICER (4 modules)
   ├─ Compliance enforcement
   └─ SOP adherence

8. QUALITY ASSURANCE STAFF (3 modules)
   ├─ Quality validation
   └─ Delivery inspection

INTERSECTION POINTS (Where Stakeholders Meet):

Point 1: TENDER & PO CREATION (Module 1)
├─ Stakeholders: Admin Pengadaan Barang, Manager Pengadaan, Kepala Bagian Keuangan
├─ Logic: Officer creates → Manager approves → Finance validates budget
└─ Decision: Proceed or reject

Point 2: VENDOR SELECTION & REGISTRATION (Modules 2,10)
├─ Stakeholders: Manager Pengadaan, Kasie Pengadaan Jasa, Kepala Bagian Keuangan, Direktur Keuangan, SDM dan Umum
├─ Logic: Manager selects → Finance checks viability → Direktur Keuangan, SDM dan Umum decides (big deals)
└─ Decision: Approve or reject vendor

Point 3: INVOICE & PAYMENT PROCESSING (Modules 5,8)
├─ Stakeholders: Kepala Bagian Keuangan, Admin Pengadaan Jasa, Quality Assurance, Vendor
├─ Logic: QA confirms delivery → Finance validates invoice → Pays vendor
└─ Decision: Pay or query invoice

Point 4: PERFORMANCE EVALUATION (Module 12)
├─ Stakeholders: Kasie Pengadaan Jasa, Manager Pengadaan, Kepala Bagian Keuangan, Direksi PT KMU
├─ Logic: Kasie Pengadaan Jasa scores → PM reviews → Finance analyzes impact → 
│         Board decides renewal
└─ Decision: Renew, improve, or terminate

Point 5: COMPLIANCE & SOP (Modules 4,6,11)
├─ Stakeholders: Staf SPI, Manager Pengadaan, GM Operasi, 
│                Audit Firm, Direksi PT KMU
├─ Logic: Compliance ensures SOPs → Officer enforces → GM Operasi reviews → 
│         Auditors verify → Board approves
└─ Decision: Approve or penalize violations

Point 6: FINANCIAL REPORTING (Modules 9,10)
├─ Stakeholders: Kepala Bagian Keuangan, Staf Keuangan, Direktur Keuangan, SDM dan Umum, GM Operasi, Direksi PT KMU
├─ Logic: Analyst calculates → Manager reviews → Direktur Keuangan, SDM dan Umum validates → 
│         GM Operasi/ Direksi PT KMU approves
└─ Decision: Report findings to board
```

---

## CAUSAL LOGIC & DEPENDENCIES

### How Actions Trigger Actions (Causal Chain)

```
CAUSAL FLOW EXAMPLE: COMPLETE PROCUREMENT CYCLE

TRIGGER 1: Kepala Unit yang Meminta Creates Permintaan Pembelian (PP)
├─ WHO: Kepala Unit yang Meminta (Department)
├─ MODULE: 1 - Platform Digitalisasi Pengadaan KMU
├─ ACTION: Submits requirement for supplies
└─ SYSTEM RECORDS: Requisition entry → Activity Log

    ↓ CAUSALLY TRIGGERS ↓

TRIGGER 2: Admin Pengadaan Barang Processes Requisition
├─ WHO: Admin Pengadaan Barang
├─ TRIGGERED BY: Requisition received (event)
├─ ACTION: Reviews, determines procurement method
├─ LOGIC: IF urgent → Direct PO; IF competitive → Tender
├─ DECISION POINT: Tender or Direct Purchase?
└─ OUTPUT: Tender Created OR Direct PO Created

    ↓ IF TENDER PATH (Competitiveness) ↓

TRIGGER 3: Vendors Submit Quotes
├─ WHO: Multiple VENDORS (External)
├─ TRIGGERED BY: Tender published in system
├─ ACTION: Submit pricing & capability quotes
├─ MODULE: 2 - Vendor Management Database
├─ TIME: Within tender deadline (7-14 days)
└─ OUTPUT: Multiple quotes received

TRIGGER 4: Manager Pengadaan Evaluates & Awards
├─ WHO: Manager Pengadaan
├─ TRIGGERED BY: Quotes received from vendors
├─ ACTION: Evaluate price, quality, delivery timeline
├─ LOGIC: 
│  ├─ Price: Lowest cost? Reasonable?
│  ├─ Quality: Meets standards?
│  ├─ Delivery: Can they meet timeline?
│  └─ Vendor: Is vendor certified/approved?
├─ DECISION: Award to which vendor?
└─ OUTPUT: PO created to selected vendor

    ↓ BOTH PATHS CONVERGE ↓

TRIGGER 5: Kepala Bagian Keuangan Reviews PO for Approval
├─ WHO: Kepala Bagian Keuangan
├─ TRIGGERED BY: PO created in system
├─ CHECK 1: Is budget available? (Check Module 9 data)
├─ CHECK 2: Is vendor approved? (Check Module 2 database)
├─ CHECK 3: Is amount within authority limits?
├─ LOGIC TREE:
│  ├─ IF amount ≤100M IDR → AUTO-APPROVE
│  ├─ IF 100M < amount ≤500M → Manager approval needed
│  ├─ IF amount >500M → Director approval needed
│  └─ IF NO budget → REJECT PO
├─ DECISION: Approve or Reject?
└─ OUTPUT: PO Approved/Rejected Status

    ↓ IF APPROVED ↓

TRIGGER 6: Admin Pengadaan Barang Sends PO to Vendor
├─ WHO: Admin Pengadaan Barang (on behalf of FM approval)
├─ TRIGGERED BY: Kepala Bagian Keuangan approved PO
├─ ACTION: Sends PO document to vendor
├─ METHOD: Email, formal document
├─ VENDOR RECEIVES: Official order confirmation
└─ SYSTEM RECORDS: PO sent timestamp

    ↓ CAUSALLY TRIGGERS (Vendor side) ↓

TRIGGER 7: Vendor Manufactures & Prepares Goods
├─ WHO: VENDOR (External)
├─ TRIGGERED BY: PO received from KMU
├─ ACTION: Manufactures/prepares goods per PO specs
├─ OBLIGATION: Deliver by promised date (KSO contract term)
├─ MODULE: 3 - Portal Vendor KMU (if applicable)
├─ RISK: 
│  ├─ IF delayed → Impacts KMU operations (cost impact)
│  ├─ Vendor score in Module 12 affected
│  └─ May trigger emergency purchasing
└─ OUTPUT: Goods ready for shipping

TRIGGER 8: Vendor Delivers Goods to KMU
├─ WHO: VENDOR (External)
├─ TRIGGERED BY: Goods manufactured & ready
├─ ACTION: Transports goods to KMU location (Balikpapan, etc)
├─ TIMING: Target = promised delivery date
├─ METRICS TRACKED:
│  ├─ Actual delivery date vs promised
│  ├─ Number of units delivered
│  ├─ Condition on arrival
│  └─ All recorded in Module 12 (Evaluation)
└─ SYSTEM RECORDS: Delivery event logged

    ↓ CAUSALLY TRIGGERS ↓

TRIGGER 9: Quality Assurance Inspects Goods
├─ WHO: Staf Pemeriksa Barang + Admin Pengadaan Jasa
├─ TRIGGERED BY: Goods arrival notification in system
├─ ACTIONS (Checks):
│  ├─ Check 1: Count matches PO? (Count vs PO line items)
│  ├─ Check 2: Quality meets standards? (Visual + test)
│  ├─ Check 3: Delivery on-time? (Date vs promised date)
│  ├─ Check 4: Documentation complete? (Packing slip, certs)
│  └─ Check 5: No damage in transit?
├─ LOGIC DECISION:
│  ├─ IF all checks PASS → Create BAPB (BAPB (Berita Acara Penerimaan Barang))
│  ├─ IF count mismatch → Partial BAPB + note shortage
│  ├─ IF quality issue → Create Rejection notice
│  └─ IF late delivery → Record in Module 12 (vendor score)
├─ MODULES: Records in 1, 5, 12 (Evaluation impacts)
└─ OUTPUT: BAPB OR Rejection/Return Notice

    ↓ CAUSALLY TRIGGERS (Finance side) ↓

TRIGGER 10: Vendor Submits Invoice
├─ WHO: VENDOR (External)
├─ TRIGGERED BY: BAPB created (goods confirmed received)
├─ ACTION: Submit invoice matching:
│  ├─ PO number & items
│  ├─ Kuantitas di BAPB
│  ├─ Agreed pricing
│  └─ Applicable taxes/discounts
├─ TIMING: Should arrive within 10 days of delivery
├─ MODULE: 5 - Invoice Processing
├─ METRICS:
│  ├─ Invoice arrival timeliness (for vendor score)
│  ├─ Invoice accuracy (Module 12 quality metric)
│  └─ Invoice delay cost analysis (Module 9)
└─ OUTPUT: Invoice received in system

    ↓ CAUSALLY TRIGGERS ↓

TRIGGER 11: Kepala Bagian Keuangan Processes Invoice (3-Way Match)
├─ WHO: Kepala Bagian Keuangan or Accounts Payable staff
├─ TRIGGERED BY: Invoice received in system
├─ MATCHING CHECKS:
│  ├─ Does invoice amount match PO amount?
│  ├─ Do quantities match BAPB quantities?
│  ├─ Are taxes calculated correctly?
│  ├─ Are discounts applied correctly?
│  └─ Are all required vendor docs attached?
├─ LOGIC:
│  ├─ IF all 3-way match → APPROVE for payment
│  ├─ IF amount mismatch → QUERY vendor (pause payment)
│  ├─ IF missing docs → REQUEST docs (pause payment)
│  └─ IF quality issue → Negotiate credit memo
├─ MODULE UPDATES:
│  ├─ Module 5: Invoice status = Approved/On-Hold
│  ├─ Module 12: Invoice accuracy metric updated
│  └─ Module 9: Financial impact calculation updated
└─ OUTPUT: Invoice Approved OR On Hold

    ↓ IF APPROVED ↓

TRIGGER 12: Payment Scheduled & Processed
├─ WHO: Kepala Bagian Keuangan or Accounts Payable
├─ TRIGGERED BY: Invoice approved for payment
├─ PAYMENT CALCULATION:
│  ├─ Due date: Per payment terms (Net 30 = 30 days from invoice)
│  ├─ Early pay discount?: Check if vendor offers 1% for 10-day pay
│  ├─ Should we pay early? (Cost-benefit vs cash position)
│  └─ Amount to pay: Invoice - discount (if early) = final amount
├─ MODULE: 8 - Payment Processing
├─ METRICS TRACKED:
│  ├─ Payment timeliness (Module 12: vendor score)
│  ├─ Discount captured or missed (Module 9: financial impact)
│  ├─ Working capital impact (how long cash tied up)
│  └─ Payment reliability (Module 12: financial health score)
└─ OUTPUT: Payment made to vendor

    ↓ CAUSALLY TRIGGERS (Vendor side) ↓

TRIGGER 13: Vendor Receives Payment
├─ WHO: VENDOR (External)
├─ TRIGGERED BY: Payment processed from KMU
├─ ACTION: Receives payment, confirms in their system
├─ METRIC: Payment reliability (Module 12: vendor relationship score)
└─ OUTCOME: Vendor-KMU relationship strengthened or maintained

    ↓ PARALLEL TRACKING ↓

TRIGGER 14: Data Aggregates for Monthly Evaluation (Module 12)
├─ WHO: Kasie Pengadaan Jasa + Staf Keuangan
├─ TRIGGERED BY: End of month (automatic aggregation)
├─ DATA COMPILED FROM:
│  ├─ Module 1: PO timeliness, approval time
│  ├─ Module 5: Delivery timeliness (data from Trigger 9)
│  ├─ Module 5: Invoice accuracy (data from Trigger 11)
│  ├─ Module 8: Payment timeliness (data from Trigger 12)
│  ├─ Module 3: KSO compliance (if applicable)
│  └─ Other: Quality issues, communication, pricing
├─ CALCULATION: All metrics → 7-dimensional scoring
├─ OUTPUT: Vendor scorecard (0-100, ⭐ 1-5 rating)
└─ MODULES UPDATED: Module 12 (Vendor Evaluation)

    ↓ QUARTERLY AGGREGATION ↓

TRIGGER 15: Quarterly Report Generated (Module 12)
├─ WHO: System (automated) + Kasie Pengadaan Jasa
├─ TRIGGERED BY: End of quarter
├─ DATA: 3-month average of all metrics
├─ ANALYSIS:
│  ├─ Trend: Improving? Declining? Stable?
│  ├─ Comparison: Rank vs other vendors
│  ├─ Risk: Any concerns?
│  └─ Financial: What's the ROI with this vendor?
├─ OUTPUT: 20-page quarterly report
└─ DISTRIBUTION: GM Operasi, Procurement, Kasie Pengadaan Jasa

    ↓ ANNUALLY (Dec 31) ↓

TRIGGER 16: Annual Evaluation & Contract Renewal Decision
├─ WHO: Kasie Pengadaan Jasa, Manager Pengadaan, GM Operasi, Direksi PT KMU
├─ TRIGGERED BY: 12-month evaluation complete
├─ ANALYSIS:
│  ├─ Annual score: Excellent? Good? Poor?
│  ├─ Trend: Getting better or worse?
│  ├─ Financial impact: ROI calculated
│  ├─ Risk: Any concerns for next year?
│  └─ Strategic: Still aligned with goals?
├─ DECISION OPTIONS:
│  ├─ RENEW: Continue as is
│  ├─ RENEW WITH CONDITIONS: Improve or lose contract
│  ├─ RENEGOTIATE: Change terms (price, volume, etc)
│  └─ TERMINATE: Find new vendor
├─ MODULE: 12 (Evaluation) + Module 2 (Vendor database)
└─ FINAL APPROVAL: Direksi PT KMU

═══════════════════════════════════════════════════════════════

KEY CAUSAL OBSERVATIONS:

1. LINEAR CAUSALITY: 
   Each trigger flows logically to next (A→B→C pattern)

2. GATING DEPENDENCIES:
   Some triggers only occur IF prior trigger approved
   Example: Invoice only processed IF BAPB created

3. TIMING CAUSALITY:
   Delays at one stage cascade to next stage
   Example: Late delivery → Late invoice → Late payment

4. DATA CAUSALITY:
   Metrics collected at early triggers feed into later evaluations
   Example: Delivery data (Trigger 9) feeds into Trigger 15 decision

5. QUALITY CAUSALITY:
   Quality issue at one stage impacts vendor score (Module 12)
   Which impacts contract renewal (Trigger 16)

6. FINANCIAL CAUSALITY:
   Financial decisions at Kepala Bagian Keuangan level (Trigger 5)
   Impact vendor behavior & KMU cash position (Module 9)
```

---

## STAKEHOLDER ROLES & FUNCTIONS

### By Module - Who Does What

```
MODULE 1: PROCUREMENT PLATFORM (Tender → Quote → PO → Payment)

ROLES & FUNCTIONS:
1. Admin Pengadaan Barang
   ├─ Function: Creates tenders, reviews quotes
   ├─ Authority: Recommend vendor (no final approval)
   ├─ Risk Mitigation: Ensures competitive process, documentation
   └─ Benefit: Efficient procurement, best pricing

2. Manager Pengadaan
   ├─ Function: Approves tender decisions, awards contracts
   ├─ Authority: Final award (unless high-value → escalate)
   ├─ Risk Mitigation: Verifies vendor capability, pricing reasonableness
   └─ Benefit: Ensures quality vendor selection

3. Kepala Bagian Keuangan
   ├─ Function: Reviews PO, approves based on budget
   ├─ Authority: Approve/reject based on amount limits
   ├─ Risk Mitigation: Budget control, unauthorized spending prevention
   └─ Benefit: Financial discipline, cash management

4. Director (for >500M orders)
   ├─ Function: Final approval for large POs
   ├─ Authority: Can override Kepala Bagian Keuangan recommendation
   ├─ Risk Mitigation: Governance over strategic spending
   └─ Benefit: Executive oversight of major commitments

5. GM Operasi
   ├─ Function: Strategic direction, escalation authority
   ├─ Authority: Final decision on disputes
   ├─ Risk Mitigation: Alignment with operational strategy
   └─ Benefit: Operational coherence

6. Direksi PT KMU
   ├─ Function: Governance over very large purchases
   ├─ Authority: Approval for contracts >500M affecting strategy
   ├─ Risk Mitigation: Shareholder protection
   └─ Benefit: Strategic alignment

─────────────────────────────────────────────────────

MODULE 2: VENDOR MANAGEMENT (Registration, KSO, Database)

ROLES & FUNCTIONS:
1. Kasie Pengadaan Jasa
   ├─ Function: Vendor registration, KSO creation, relationship mgmt
   ├─ Authority: Approve/reject vendor registration
   ├─ Risk Mitigation: Vendor capability verification, due diligence
   └─ Benefit: Quality vendor base, risk reduction

2. Manager Pengadaan
   ├─ Function: Reviews vendor suitability, approves major vendors
   ├─ Authority: Final approval for tier-1 vendors
   ├─ Risk Mitigation: Strategic vendor fit assessment
   └─ Benefit: Vendor quality assurance

3. Kepala Bagian Keuangan
   ├─ Function: Financial viability check
   ├─ Authority: Can reject vendor if financially unstable
   ├─ Risk Mitigation: Credit risk assessment
   └─ Benefit: Financial stability of supply chain

4. Direktur Keuangan, SDM dan Umum
   ├─ Function: Large contract approvals
   ├─ Authority: Final approval for strategic vendors
   ├─ Risk Mitigation: Financial exposure management
   └─ Benefit: Large commitment oversight

─────────────────────────────────────────────────────

MODULE 3: VENDOR PORTAL & KSO OBLIGATIONS

ROLES & FUNCTIONS:
1. Vendor (External)
   ├─ Function: Self-reporting of KSO obligations
   ├─ Authority: Can only submit own data
   ├─ Risk Mitigation: Accountability through self-reporting
   └─ Benefit: Real-time compliance tracking

2. Admin Pengadaan Jasa
   ├─ Function: Manages vendor portal, answers questions
   ├─ Authority: Can approve/reject submissions
   ├─ Risk Mitigation: Validates vendor submissions
   └─ Benefit: Compliance verification

3. Kasie Pengadaan Jasa
   ├─ Function: Reviews vendor obligations, performance
   ├─ Authority: Escalates non-compliance
   ├─ Risk Mitigation: Monitors KSO adherence
   └─ Benefit: Ensures vendor accountability

─────────────────────────────────────────────────────

MODULE 4: AI COMPLIANCE GUARDIAN (SOP Enforcement)

ROLES & FUNCTIONS:
1. AI Chatbot (Automated System)
   ├─ Function: Guides users through SOP, prevents violations
   ├─ Authority: Can block non-SOP actions
   ├─ Risk Mitigation: Automated SOP enforcement
   └─ Benefit: Prevents compliance violations

2. Staf SPI
   ├─ Function: Uploads SOPs, reviews violations
   ├─ Authority: Can modify SOP rules
   ├─ Risk Mitigation: Monitors compliance violations
   └─ Benefit: Governance of operations

3. GM Operasi
   ├─ Function: Approves SOP changes
   ├─ Authority: Final approval of SOP modifications
   ├─ Risk Mitigation: Ensures SOPs serve strategic goals
   └─ Benefit: Operational consistency

─────────────────────────────────────────────────────

MODULE 5-8: EXECUTION (Delivery, Quality, Invoice, Payment)

ROLES & FUNCTIONS:
1. Staf Pemeriksa Barang
   ├─ Function: Inspects goods on delivery
   ├─ Authority: Can reject goods that don't meet standards
   ├─ Risk Mitigation: Quality control gateway
   └─ Benefit: Only quality goods accepted

2. Admin Pengadaan Jasa
   ├─ Function: Communication hub with vendor
   ├─ Authority: Can escalate issues to Kasie Pengadaan Jasa
   ├─ Risk Mitigation: Issue tracking and follow-up
   └─ Benefit: Quick issue resolution

3. Kepala Bagian Keuangan
   ├─ Function: Invoice validation, payment processing
   ├─ Authority: Approve/reject invoices
   ├─ Risk Mitigation: 3-way match validation
   └─ Benefit: Error prevention, fraud control

4. Staf Keuangan
   ├─ Function: Data analysis, report preparation
   ├─ Authority: Prepares data for decisions
   ├─ Risk Mitigation: Ensures data accuracy
   └─ Benefit: Informed decision-making

─────────────────────────────────────────────────────

MODULE 9: COMPREHENSIVE REPORTING

ROLES & FUNCTIONS:
1. Kepala Bagian Keuangan
   ├─ Function: Supervises report generation
   ├─ Authority: Approves financial reports
   ├─ Risk Mitigation: Ensures accuracy
   └─ Benefit: Accurate financial picture

2. Staf Keuangan
   ├─ Function: Analyzes financial data
   ├─ Authority: Calculates metrics, identifies trends
   ├─ Risk Mitigation: Detailed analysis
   └─ Benefit: Insights for decision-making

3. Direktur Keuangan, SDM dan Umum
   ├─ Function: Reviews financial reports
   ├─ Authority: Final approval of reports
   ├─ Risk Mitigation: Executive oversight
   └─ Benefit: Board-ready reporting

4. GM Operasi
   ├─ Function: Reviews operational impact
   ├─ Authority: Interprets findings for operations
   ├─ Risk Mitigation: Operational context
   └─ Benefit: Operational insights

5. Direksi PT KMU
   ├─ Function: Reviews summary reports
   ├─ Authority: Makes strategic decisions based on reports
   ├─ Risk Mitigation: Governance oversight
   └─ Benefit: Strategic alignment

─────────────────────────────────────────────────────

MODULE 10: VENDOR MASTER DATABASE & KSO

ROLES & FUNCTIONS:
1. Kasie Pengadaan Jasa
   ├─ Function: Manages vendor master data
   ├─ Authority: Updates vendor information
   ├─ Risk Mitigation: Data accuracy
   └─ Benefit: Single source of truth for vendor data

2. Kepala Bagian Keuangan
   ├─ Function: Reviews financial data in KSO
   ├─ Authority: Validates payment terms
   ├─ Risk Mitigation: Financial terms accuracy
   └─ Benefit: Correct payment processing

3. Staf SPI
   ├─ Function: Monitors KSO compliance
   ├─ Authority: Flags non-compliant vendors
   ├─ Risk Mitigation: Contract adherence
   └─ Benefit: Risk control

─────────────────────────────────────────────────────

MODULE 11: COMMAND CENTER DASHBOARD

ROLES & FUNCTIONS:
1. GM Operasi
   ├─ Function: Monitors real-time KPIs
   ├─ Authority: Makes decisions based on dashboard
   ├─ Risk Mitigation: Early problem detection
   └─ Benefit: Real-time visibility

2. Manager Pengadaan
   ├─ Function: Monitors procurement KPIs
   ├─ Authority: Manages team based on metrics
   ├─ Risk Mitigation: Performance tracking
   └─ Benefit: Team accountability

3. Kepala Bagian Keuangan
   ├─ Function: Monitors financial KPIs
   ├─ Authority: Manages cash position
   ├─ Risk Mitigation: Cash flow control
   └─ Benefit: Financial stability

─────────────────────────────────────────────────────

MODULE 12: VENDOR EVALUATION & REPORTING

ROLES & FUNCTIONS:
1. Kasie Pengadaan Jasa
   ├─ Function: Compiles vendor performance data
   ├─ Authority: Inputs evaluation metrics
   ├─ Risk Mitigation: Ensures evaluation accuracy
   └─ Benefit: Objective vendor assessment

2. Staf Keuangan
   ├─ Function: Calculates financial impact
   ├─ Authority: Determines ROI per vendor
   ├─ Risk Mitigation: Financial analysis
   └─ Benefit: Quantified vendor value

3. Manager Pengadaan
   ├─ Function: Reviews evaluations
   ├─ Authority: Recommends actions
   ├─ Risk Mitigation: Performance interpretation
   └─ Benefit: Action recommendations

4. GM Operasi
   ├─ Function: Reviews strategic implications
   ├─ Authority: Makes renewal/termination decisions
   ├─ Risk Mitigation: Strategic alignment
   └─ Benefit: Strategic vendor management

5. Direksi PT KMU
   ├─ Function: Final approval on major vendor decisions
   ├─ Authority: Approves/rejects vendor continuation
   ├─ Risk Mitigation: Governance
   └─ Benefit: Strategic oversight
```

---

## RISK MITIGATION BY STAKEHOLDER

### How Each Stakeholder Mitigates Risk

```
PROCUREMENT OFFICER
Risk 1: Non-competitive procurement (favoring certain vendors)
├─ Mitigation: Tender process ensures competition
├─ Control: Multiple vendors invited to bid
└─ Monitoring: Manager Pengadaan reviews

Risk 2: Vendor selection based on relationships (not quality)
├─ Mitigation: Objective scoring criteria
├─ Control: Price, quality, delivery all weighted equally
└─ Monitoring: Transparent vendor scorecard

─────────────────────────────────────────────────────

PROCUREMENT MANAGER
Risk 1: Over-spending beyond budget
├─ Mitigation: Kepala Bagian Keuangan approval gate
├─ Control: Cannot PO without budget validation
└─ Monitoring: Budget tracking in Module 9

Risk 2: Approving low-quality vendors
├─ Mitigation: Vendor scorecard (Module 12)
├─ Control: Only approved vendors can be selected
└─ Monitoring: Performance evaluation required

Risk 3: Vendor relationships bias decisions
├─ Mitigation: Objective evaluation criteria
├─ Control: Data-driven scoring (not subjective)
└─ Monitoring: Board review of large contracts

─────────────────────────────────────────────────────

FINANCE MANAGER
Risk 1: Over-commitment of budget
├─ Mitigation: Real-time budget tracking
├─ Control: Cannot approve if budget unavailable
└─ Monitoring: Weekly budget reporting

Risk 2: Paying incorrect invoices (fraud risk)
├─ Mitigation: 3-way match validation (PO, BAPB, Invoice)
├─ Control: Automated validation rules
└─ Monitoring: Exception reporting of mismatches

Risk 3: Vendor insolvency (non-delivery risk)
├─ Mitigation: Vendor credit check (Module 2)
├─ Control: Financial viability assessment
└─ Monitoring: Quarterly vendor financial review

Risk 4: Overpayment through early discounts missed
├─ Mitigation: Early discount tracking
├─ Control: Automated identification of discount opportunities
└─ Monitoring: Monthly report on discounts captured vs missed

─────────────────────────────────────────────────────

QUALITY ASSURANCE STAFF
Risk 1: Accepting defective goods
├─ Mitigation: Protokol inspeksi sebelum BAPB
├─ Control: Goods must pass QC before acceptance
└─ Monitoring: Defect rate tracking (Module 12)

Risk 2: Accepting wrong quantities
├─ Mitigation: Count verification against PO
├─ Control: BAPB quantity must match PO quantity
└─ Monitoring: Discrepancy reporting

Risk 3: Accepting late deliveries without escalation
├─ Mitigation: Delivery date validation
├─ Control: Late deliveries flagged automatically
└─ Monitoring: On-time delivery % tracked (Module 12)

─────────────────────────────────────────────────────

VENDOR MANAGER
Risk 1: Vendor performance degradation unnoticed
├─ Mitigation: Monthly performance reporting (Module 12)
├─ Control: Automated scorecard generation
└─ Monitoring: Monthly review meetings with vendors

Risk 2: Vendor contract violations not caught
├─ Mitigation: KSO obligation tracking (Module 3)
├─ Control: Automated compliance checking
└─ Monitoring: Daily obligation status

Risk 3: Strategic vendor relationship too dependent
├─ Mitigation: Multi-KSO strategy (multiple vendors per service)
├─ Control: No single vendor >70% allocation
└─ Monitoring: Vendor concentration analysis

Risk 4: Vendor insolvency affecting supply chain
├─ Mitigation: Quarterly financial stability review
├─ Control: Credit monitoring
└─ Monitoring: Financial health score (Module 12)

─────────────────────────────────────────────────────

COMPLIANCE OFFICER
Risk 1: SOP violations not detected
├─ Mitigation: AI Penjaga Kepatuhan SPO (Module 4)
├─ Control: Automated SOP enforcement blocks violations
└─ Monitoring: Violation log (Module 11)

Risk 2: Unauthorized variations to process
├─ Mitigation: SOP documentation in system
├─ Control: AI Chatbot provides guidance, prevents variations
└─ Monitoring: Audit trail of all deviations

Risk 3: Audit findings not addressed
├─ Mitigation: Audit tracking & follow-up
├─ Control: Issues tracked to resolution
└─ Monitoring: Compliance dashboard

─────────────────────────────────────────────────────

VP OPERATIONS
Risk 1: Procurement process misalignment with strategy
├─ Mitigation: Strategic oversight of procurement
├─ Control: Approval authority over major contracts
└─ Monitoring: Quarterly business reviews

Risk 2: Vendor relationship creating bottleneck
├─ Mitigation: Multi-vendor strategy (Module 2)
├─ Control: Backup vendors for critical services
└─ Monitoring: Supply chain risk assessment

Risk 3: Compliance violations at lower levels
├─ Mitigation: SOP enforcement (Module 4)
├─ Control: AI Chatbot prevents violations
└─ Monitoring: Compliance dashboard

Risk 4: Financial mismanagement affecting operations
├─ Mitigation: Financial oversight
├─ Control: Direktur Keuangan, SDM dan Umum partnership on large spending
└─ Monitoring: Weekly financial reports

─────────────────────────────────────────────────────

BOARD OF DIRECTORS
Risk 1: Large vendor commitment without governance
├─ Mitigation: Approval authority for >500M contracts
├─ Control: Board vote on strategic vendors
└─ Monitoring: Annual vendor assessment

Risk 2: Vendor failure affecting hospital operations
├─ Mitigation: Financial viability assessment
├─ Control: Backup vendors identified
└─ Monitoring: Supply chain contingency planning

Risk 3: Fraud in procurement process
├─ Mitigation: Audit oversight
├─ Control: Annual audit by external firm
└─ Monitoring: Audit findings & corrective actions

─────────────────────────────────────────────────────

VENDORS (External)
Risk 1: Non-payment by KMU
├─ Mitigation: KSO contract with payment terms
├─ Control: Bank reference & credit check on KMU
└─ Monitoring: Payment timeliness (get rated Module 12)

Risk 2: Scope creep (changing requirements)
├─ Mitigation: PO specification documentation
├─ Control: Written PO defines exactly what's required
└─ Monitoring: Change order process

Risk 3: Relationship deterioration
├─ Mitigation: Regular vendor communication
├─ Control: Quarterly business reviews
└─ Monitoring: Performance feedback
```

---

## BENEFITS BY STAKEHOLDER

### What Each Stakeholder Gains

```
PROCUREMENT OFFICER
✅ Benefit 1: Clear Process & Authority
   └─ Knows exactly what decisions they own (tender/PO creation)

✅ Benefit 2: Workload Management
   └─ System handles administrative tasks (AI Penjaga Kepatuhan SPO)

✅ Benefit 3: Performance Visibility
   └─ Can see their approval efficiency (Module 11 dashboard)

✅ Benefit 4: Vendor Feedback
   └─ Vendor scorecards show quality of their vendor selections

─────────────────────────────────────────────────────

PROCUREMENT MANAGER
✅ Benefit 1: Strategic Control
   └─ Can shape vendor strategy, multi-KSO approach

✅ Benefit 2: Team Accountability
   └─ Clear metrics for officer performance (Module 12)

✅ Benefit 3: Decision Support
   └─ Data-driven recommendations (Module 12 evaluations)

✅ Benefit 4: Risk Management
   └─ Early warning on vendor problems (monthly reports)

✅ Benefit 5: Cost Optimization
   └─ Identifies cost-saving opportunities (early discounts, etc)

─────────────────────────────────────────────────────

FINANCE MANAGER
✅ Benefit 1: Budget Control
   └─ Real-time visibility of spending (Module 9)

✅ Benefit 2: Prevention of Fraud
   └─ 3-way match catches errors before payment

✅ Benefit 3: Working Capital Optimization
   └─ Data on DPO, WC impact helps management

✅ Benefit 4: Cost Reduction
   └─ Identifies missed discounts, payment delays costing money

✅ Benefit 5: Payment Accuracy
   └─ Automated invoice validation prevents overpayment

✅ Benefit 6: Vendor Financial Stability
   └─ Credit checks reduce insolvency risk

─────────────────────────────────────────────────────

Direktur Keuangan, SDM dan Umum
✅ Benefit 1: Strategic Financial Decisions
   └─ Annual vendor assessment supports contract renewal decisions

✅ Benefit 2: ROI Visibility
   └─ Financial impact per vendor quantified (Module 12)

✅ Benefit 3: Capital Planning
   └─ Working capital impact analysis (Module 9)

✅ Benefit 4: Large Commitment Control
   └─ Board approval authority protects shareholder interests

✅ Benefit 5: Audit Readiness
   └─ Complete audit trail proves financial controls

─────────────────────────────────────────────────────

VP OPERATIONS
✅ Benefit 1: Complete Operational Visibility
   └─ Real-time command center dashboard (Module 11)

✅ Benefit 2: Strategic Vendor Management
   └─ Multi-KSO strategy reduces supply chain risk

✅ Benefit 3: Compliance Assurance
   └─ AI Penjaga Kepatuhan SPO prevents violations

✅ Benefit 4: Risk Mitigation
   └─ Early warning system for operational problems

✅ Benefit 5: Decision Data
   └─ Annual evaluations support strategic decisions

✅ Benefit 6: Team Performance
   └─ KPI dashboard shows team effectiveness

─────────────────────────────────────────────────────

COMPLIANCE OFFICER
✅ Benefit 1: Automated SOP Enforcement
   └─ AI Chatbot reduces manual compliance checking

✅ Benefit 2: Violation Prevention
   └─ System blocks non-SOP actions before they happen

✅ Benefit 3: Audit Trail
   └─ Complete documentation for external auditors

✅ Benefit 4: Risk Reduction
   └─ Compliance violations dramatically reduced

✅ Benefit 5: Scalable Compliance
   └─ System scales without adding compliance staff

─────────────────────────────────────────────────────

QUALITY ASSURANCE STAFF
✅ Benefit 1: Clear Quality Standards
   └─ System defines what's acceptable before delivery

✅ Benefit 2: Issue Tracking
   └─ Defects logged, tracked to resolution

✅ Benefit 3: Performance Accountability
   └─ Vendor quality scores visible to everyone

✅ Benefit 4: Reduced Rework
   └─ Early detection prevents bad goods acceptance

─────────────────────────────────────────────────────

VENDOR MANAGER
✅ Benefit 1: Performance Data
   └─ Automated scorecards remove subjectivity

✅ Benefit 2: Relationship Intelligence
   └─ Know which vendors are top performers

✅ Benefit 3: Strategic Vendor Expansion
   └─ Data supports adding new product categories with vendors

✅ Benefit 4: Issue Escalation Path
   └─ Clear process for vendor problem resolution

✅ Benefit 5: Vendor Development
   └─ Performance data helps vendors improve

✅ Benefit 6: Contract Renewal Decisions
   └─ Annual assessment provides clear renew/replace decision

─────────────────────────────────────────────────────

BOARD OF DIRECTORS
✅ Benefit 1: Governance & Control
   └─ Approval authority over large vendor commitments

✅ Benefit 2: Strategic Insights
   └─ Annual vendor assessment shows strategic fit

✅ Benefit 3: Risk Management
   └─ Multi-KSO approach reduces supply chain risk

✅ Benefit 4: Financial Transparency
   └─ Vendor ROI analysis shows value creation

✅ Benefit 5: Audit Readiness
   └─ Complete documentation supports external audits

─────────────────────────────────────────────────────

VENDORS (External)
✅ Benefit 1: Clear Requirements
   └─ PO specifies exactly what's expected

✅ Benefit 2: Fair Evaluation
   └─ Objective scorecard (no favoritism)

✅ Benefit 3: Performance Feedback
   └─ Monthly reports show how they're doing

✅ Benefit 4: Opportunity for Improvement
   └─ Performance gaps identified with suggestions

✅ Benefit 5: Transparency
   └─ Know exactly why they got contract or why they're being replaced

✅ Benefit 6: Increased Volume Opportunity
   └─ Top-performing vendors get more business

✅ Benefit 7: Self-Reporting Portal
   └─ Easy way to submit KSO obligations, reduces manual coordination

─────────────────────────────────────────────────────

CUSTOMERS/PATIENTS (Indirect Benefit)
✅ Benefit 1: Quality Goods
   └─ Quality assurance ensures only good products purchased

✅ Benefit 2: Availability
   └─ Multi-KSO strategy ensures supplies available

✅ Benefit 3: Cost Control
   └─ Efficient procurement keeps costs manageable

─────────────────────────────────────────────────────

AUDIT FIRM (External)
✅ Benefit 1: Complete Documentation
   └─ Full audit trail available for verification

✅ Benefit 2: Clear Controls
   └─ Procurement controls documented and enforced

✅ Benefit 3: Easy Audit
   └─ Systematic approach makes auditing efficient
```

---

## DECISION AUTHORITY & ACCOUNTABILITY

### Who Decides What & Who's Accountable

```
DECISION AUTHORITY MATRIX:

Amount Threshold    Who Decides           Accountability
──────────────────────────────────────────────────────────
≤100M IDR          Kepala Bagian Keuangan      Kepala Bagian Keuangan
                   (Auto-approve)        to GM Operasi

100M-500M IDR      Kepala Bagian Keuangan      Kepala Bagian Keuangan
                   + Procurement Mgr     to GM Operasi

>500M IDR          Director/Direktur Keuangan, SDM dan Umum          Director ke Direksi PT KMU
                   + Board vote          of Directors

VENDOR SELECTION:
- <3 vendors      Admin Pengadaan Barang    Manager Pengadaan
- 3+ vendors      Manager Pengadaan    GM Operasi
- Strategic       GM Operasi          Direksi PT KMU
  (>1B annual)

VENDOR TERMINATION:
- Performance     Kasie Pengadaan Jasa         GM Operasi
  issues
- Major issues    GM Operasi          Direksi PT KMU
- Fraud/legal     Direktur Keuangan, SDM dan Umum + Legal            Direksi PT KMU

CONTRACT RENEWAL:
- Annual          Kasie Pengadaan Jasa +       GM Operasi
- Strategic       GM Operasi          Direksi PT KMU
  changes

COMPLIANCE:
- Violations      Staf SPI     Staf SPI
- Escalations     GM Operasi          Direksi PT KMU

ACCOUNTABILITY CHAIN:

Admin Pengadaan Barang
        ↓ Reports to
Manager Pengadaan
        ↓ Reports to
GM Operasi
        ↓ Reports to
Direktur Utama
        ↓ Reports to
Direksi PT KMU

Same pattern for:
- Kasie Pengadaan Jasa → Manager Pengadaan/GM Operasi
- Kepala Bagian Keuangan → Direktur Keuangan, SDM dan Umum
- Staf SPI → GM Operasi/Audit
```

---

## INTEGRATION POINTS & DEPENDENCIES

### Where Stakeholders Interact

```
CRITICAL INTERACTION POINT 1: TENDER DECISION
Stakeholders: Admin Pengadaan Barang, Manager Pengadaan, Kepala Bagian Keuangan
Interaction: "Can we afford this tender?"
Process: Officer drafts → Manager reviews → Finance checks budget
Dependency: Finance must approve budget before Manager awards

CRITICAL INTERACTION POINT 2: VENDOR SELECTION
Stakeholders: Manager Pengadaan, Kasie Pengadaan Jasa, Kepala Bagian Keuangan
Interaction: "Is this vendor suitable?"
Process: Manager recommends → Vendor Mgr checks capability → Finance checks viability
Dependency: All three must agree

CRITICAL INTERACTION POINT 3: PAYMENT PROCESSING
Stakeholders: Quality Assurance, Kepala Bagian Keuangan, Admin Pengadaan Jasa
Interaction: "Has delivery been confirmed? Is invoice correct?"
Process: QA approves delivery → Coordinator confirms → Finance processes
Dependency: All must sign off before payment

CRITICAL INTERACTION POINT 4: VENDOR RENEWAL
Stakeholders: Kasie Pengadaan Jasa, Manager Pengadaan, Staf Keuangan, GM Operasi, Direksi PT KMU
Interaction: "Should we continue with this vendor?"
Process: Manager compiles data → Analyst calculates ROI → GM Operasi reviews → Board decides
Dependency: Each step builds on prior step

CRITICAL INTERACTION POINT 5: ISSUE ESCALATION
Stakeholders: Admin Pengadaan Jasa, Kasie Pengadaan Jasa, GM Operasi
Interaction: "This vendor is not meeting commitments"
Process: Coordinator reports → Manager escalates → GM Operasi decides action
Dependency: Clear escalation path prevents issues from falling through cracks
```

---

**END OF STAKEHOLDER ANALYSIS**

This comprehensive analysis shows:
✅ All 18 stakeholders identified
✅ Where they overlap (beririsan) in responsibilities
✅ Complete causal logic of how actions trigger actions
✅ Specific roles and functions in each module
✅ Risk mitigation strategies by stakeholder
✅ Benefits each stakeholder receives
✅ Clear decision authority and accountability
✅ Integration points where stakeholders interact

Result: **Complete transparency of who does what, why, how they interact, and what they gain from the system.**


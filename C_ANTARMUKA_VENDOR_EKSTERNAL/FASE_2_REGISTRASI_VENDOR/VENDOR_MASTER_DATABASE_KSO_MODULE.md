# VENDOR MASTER DATABASE MODULE
## Comprehensive Vendor Management with KSO (Kerja Sama Operasional) System

**Purpose:** Single source of truth for all vendor/supplier data with partnership management  
**Scope:** Register, categorize, track, and manage all vendor partnerships  
**Integration:** Platform Digitalisasi Pengadaan KMU + Purchasing Module  

---

## TABLE OF CONTENTS

1. [Database Schema](#database-schema)
2. [Vendor Categorization](#vendor-categorization)
3. [Registrasi Vendor KMU Process](#vendor-registration-process)
4. [KSO Management](#kso-management)
5. [Multi-KSO Strategy](#multi-kso-strategy)
6. [Vendor Dashboard](#vendor-dashboard)
7. [Performance Tracking](#performance-tracking)
8. [Implementation Guide](#implementation-guide)

---

## DATABASE SCHEMA

### 1. Vendor Master Table

```sql
CREATE TABLE vendors (
  id SERIAL PRIMARY KEY,
  vendor_id VARCHAR(50) UNIQUE,              -- VND-001, VND-002, etc
  
  -- Basic Information
  company_name VARCHAR(255) NOT NULL,
  company_name_short VARCHAR(50),            -- PT Medik (for reports)
  vendor_status VARCHAR(50) DEFAULT 'active', -- active, inactive, suspended, blacklist
  
  -- Vendor Type/Category
  vendor_type VARCHAR(50) NOT NULL,          -- 'barang', 'jasa'
  vendor_category VARCHAR(100) NOT NULL,     -- 'alkes', 'farmasi', 'umum', 'sewa', etc
  service_type TEXT[],                       -- ['alkes_equipment', 'diagnostic_tools', ...]
  
  -- Contact Information
  phone VARCHAR(20),
  email VARCHAR(100),
  website VARCHAR(255),
  
  -- Address
  address_street VARCHAR(255),
  address_city VARCHAR(100),
  address_province VARCHAR(100),
  address_postal_code VARCHAR(10),
  address_country VARCHAR(100),
  
  -- Legal/Financial Information
  npwp VARCHAR(20),                          -- Tax ID
  sio VARCHAR(50),                           -- Business License
  business_license_expiry DATE,
  
  -- Banking Information
  bank_name VARCHAR(100),
  bank_account_number VARCHAR(50),
  bank_account_holder VARCHAR(255),
  
  -- Vendor Characteristics
  is_distributor BOOLEAN DEFAULT false,      -- Distributor or direct supplier?
  is_manufacturer BOOLEAN DEFAULT false,     -- Manufacture or reseller?
  is_local_kaltim BOOLEAN DEFAULT false,     -- Local to Kalimantan Timur?
  spare_parts_availability VARCHAR(50),      -- none, limited, available, excellent
  
  -- Key Contact Person
  contact_person_name VARCHAR(255),
  contact_person_title VARCHAR(100),
  contact_person_phone VARCHAR(20),
  contact_person_email VARCHAR(100),
  
  -- Metadata
  registration_date DATE DEFAULT CURRENT_DATE,
  registered_by INT REFERENCES users(id),
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_by INT REFERENCES users(id),
  
  notes TEXT,
  
  CONSTRAINT vendor_type_valid CHECK (vendor_type IN ('barang', 'jasa'))
);

CREATE INDEX idx_vendor_id ON vendors(vendor_id);
CREATE INDEX idx_vendor_status ON vendors(vendor_status);
CREATE INDEX idx_vendor_category ON vendors(vendor_category);
CREATE INDEX idx_vendor_type ON vendors(vendor_type);
CREATE INDEX idx_vendor_service_type ON vendors USING GIN(service_type);

-- ============================================
-- KSO (Kerja Sama Operasional) TABLE
-- ============================================

CREATE TABLE kso_partnerships (
  id SERIAL PRIMARY KEY,
  kso_id VARCHAR(50) UNIQUE,                 -- KSO-001, KSO-002, etc
  
  -- Partnership Identification
  vendor_id INT NOT NULL REFERENCES vendors(id) ON DELETE RESTRICT,
  partnership_name VARCHAR(255),             -- "Lab Equipment Supply Contract"
  partnership_status VARCHAR(50) DEFAULT 'active', -- active, inactive, suspended, expired
  
  -- Contract Period
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  renewal_date DATE,                         -- Automatic renewal date if applicable
  is_auto_renewal BOOLEAN DEFAULT false,
  renewal_notice_days INT DEFAULT 30,        -- Notify X days before expiry
  
  -- Partnership Details
  service_type VARCHAR(100) NOT NULL,        -- alkes, farmasi, sewa, construc, renovasi, umum
  service_description TEXT,                  -- Detailed description of services/goods
  
  product_list TEXT[],                       -- Array of products supplied
  -- Example: ['EKG Machine', 'Ultrasound Probe', 'ECG Leads']
  
  coverage_area VARCHAR(50),                 -- 'all_branches', 'main_only', 'kaltim_only', specific
  
  -- Commercial Terms
  payment_terms VARCHAR(100),                -- 'Net 30', 'COD', 'DP 50% + Milestones'
  currency VARCHAR(10) DEFAULT 'IDR',
  discount_rate DECIMAL(5,2),                -- % discount from list price
  minimum_order_value BIGINT,                -- Minimum order amount
  
  -- Contract Details
  contract_document_path VARCHAR(500),       -- Path to uploaded contract
  contract_notes TEXT,
  
  -- KSO Efficiency/Utilization Tracking
  expected_annual_value BIGINT,              -- Expected annual spending (for forecasting)
  actual_ytd_value BIGINT DEFAULT 0,         -- YTD actual spending
  utilization_rate DECIMAL(5,2),             -- % of expected (calculated)
  
  -- Performance Metrics
  on_time_delivery_percentage DECIMAL(5,2),
  quality_rating DECIMAL(3,2),               -- 1.0-5.0
  response_time_hours INT,                   -- How fast do they respond to inquiries?
  spare_parts_availability_score DECIMAL(3,2),
  price_competitiveness_score DECIMAL(3,2),
  
  -- Multi-KSO Management
  is_exclusive BOOLEAN DEFAULT false,        -- Is this the only supplier for this service?
  competing_vendors TEXT[],                  -- Other KSOs for same service
  priority_level VARCHAR(50),                -- 'primary', 'secondary', 'backup'
  
  -- Contact for this KSO
  kso_contact_person VARCHAR(255),
  kso_contact_phone VARCHAR(20),
  kso_contact_email VARCHAR(100),
  
  -- Metadata
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_by INT REFERENCES users(id),
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_by INT REFERENCES users(id),
  
  notes TEXT
);

CREATE INDEX idx_kso_id ON kso_partnerships(kso_id);
CREATE INDEX idx_kso_vendor ON kso_partnerships(vendor_id);
CREATE INDEX idx_kso_status ON kso_partnerships(partnership_status);
CREATE INDEX idx_kso_service ON kso_partnerships(service_type);
CREATE INDEX idx_kso_dates ON kso_partnerships(start_date, end_date);

-- ============================================
-- VENDOR DOCUMENTS TABLE
-- ============================================

CREATE TABLE vendor_documents (
  id SERIAL PRIMARY KEY,
  doc_id VARCHAR(50) UNIQUE,
  
  vendor_id INT NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
  kso_id INT REFERENCES kso_partnerships(id) ON DELETE CASCADE,
  
  document_type VARCHAR(100),                -- 'tax_id', 'business_license', 'contract', 'insurance', 'certification'
  document_name VARCHAR(255),
  file_path VARCHAR(500),
  file_size BIGINT,
  
  issue_date DATE,
  expiry_date DATE,
  
  is_verified BOOLEAN DEFAULT false,
  verified_by INT REFERENCES users(id),
  verified_date TIMESTAMP,
  
  upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  uploaded_by INT REFERENCES users(id),
  
  notes TEXT
);

CREATE INDEX idx_vendor_docs ON vendor_documents(vendor_id);
CREATE INDEX idx_vendor_docs_type ON vendor_documents(document_type);

-- ============================================
-- VENDOR PERFORMANCE TRACKING
-- ============================================

CREATE TABLE vendor_performance (
  id SERIAL PRIMARY KEY,
  performance_id VARCHAR(50) UNIQUE,
  
  kso_id INT NOT NULL REFERENCES kso_partnerships(id) ON DELETE CASCADE,
  vendor_id INT NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
  
  period_year INT,
  period_month INT,
  
  -- Delivery Performance
  orders_placed INT DEFAULT 0,
  orders_on_time INT DEFAULT 0,
  orders_late INT DEFAULT 0,
  on_time_percentage DECIMAL(5,2) GENERATED ALWAYS AS (
    CASE WHEN orders_placed = 0 THEN 0 
    ELSE (orders_on_time::numeric / orders_placed) * 100 
    END
  ) STORED,
  
  -- Quality Metrics
  orders_with_defects INT DEFAULT 0,
  defect_rate DECIMAL(5,2),
  rejection_rate DECIMAL(5,2),
  
  -- Responsiveness
  avg_response_time_hours DECIMAL(5,2),
  support_ticket_count INT DEFAULT 0,
  support_resolved_count INT DEFAULT 0,
  
  -- Financial Performance
  total_orders BIGINT DEFAULT 0,
  total_spend BIGINT DEFAULT 0,
  avg_order_value BIGINT GENERATED ALWAYS AS (
    CASE WHEN total_orders = 0 THEN 0 ELSE total_spend / total_orders END
  ) STORED,
  
  -- Price Compliance
  price_variance_percentage DECIMAL(5,2),    -- vs agreed price
  
  -- Overall Rating (calculated)
  overall_score DECIMAL(5,2),
  rating_stars DECIMAL(3,1),                 -- 1.0-5.0
  
  notes TEXT,
  recorded_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_perf_kso ON vendor_performance(kso_id);
CREATE INDEX idx_perf_period ON vendor_performance(period_year, period_month);
CREATE INDEX idx_perf_rating ON vendor_performance(overall_score);

-- ============================================
-- MULTI-KSO MAPPING TABLE
-- ============================================

CREATE TABLE multi_kso_services (
  id SERIAL PRIMARY KEY,
  service_code VARCHAR(100),                 -- 'lab_equipment', 'pharmacy_supply', etc
  service_name VARCHAR(255),
  
  primary_kso_id INT REFERENCES kso_partnerships(id),
  secondary_kso_id INT REFERENCES kso_partnerships(id),
  tertiary_kso_id INT REFERENCES kso_partnerships(id),
  
  -- Multi-sourcing strategy
  why_multiple_vendors TEXT,                 -- Why we use multiple vendors
  -- Example: "Risk mitigation, price competition, ensure availability"
  
  allocation_primary_percentage INT,         -- % of orders to primary
  allocation_secondary_percentage INT,       -- % to secondary
  allocation_tertiary_percentage INT,        -- % to tertiary
  
  usage_notes TEXT,
  effective_date DATE,
  
  CONSTRAINT allocation_sum CHECK (
    allocation_primary_percentage + allocation_secondary_percentage + 
    COALESCE(allocation_tertiary_percentage, 0) = 100
  )
);

CREATE INDEX idx_multi_kso_service ON multi_kso_services(service_code);

-- ============================================
-- VENDOR RATING & SCORECARDS
-- ============================================

CREATE TABLE vendor_scorecards (
  id SERIAL PRIMARY KEY,
  scorecard_id VARCHAR(50) UNIQUE,
  
  vendor_id INT NOT NULL REFERENCES vendors(id),
  kso_id INT REFERENCES kso_partnerships(id),
  
  evaluation_date DATE,
  evaluation_period VARCHAR(20),             -- 'monthly', 'quarterly', 'annual'
  
  -- Scoring Dimensions (1-5 scale)
  delivery_timeliness DECIMAL(3,2),
  product_quality DECIMAL(3,2),
  service_responsiveness DECIMAL(3,2),
  price_competitiveness DECIMAL(3,2),
  compliance_with_terms DECIMAL(3,2),
  spare_parts_support DECIMAL(3,2),
  communication_quality DECIMAL(3,2),
  
  -- Overall Score (weighted average)
  overall_score DECIMAL(3,2),
  
  -- Status Based on Score
  performance_status VARCHAR(50),            -- 'excellent', 'good', 'satisfactory', 'needs_improvement', 'critical'
  
  evaluator_name VARCHAR(255),
  evaluator_role VARCHAR(100),
  
  comments TEXT,
  recommendations TEXT,
  
  CONSTRAINT score_range CHECK (overall_score >= 1 AND overall_score <= 5)
);

CREATE INDEX idx_scorecard_vendor ON vendor_scorecards(vendor_id);
CREATE INDEX idx_scorecard_date ON vendor_scorecards(evaluation_date);
CREATE INDEX idx_scorecard_status ON vendor_scorecards(performance_status);

-- ============================================
-- VENDOR ALERTS & COMPLIANCE
-- ============================================

CREATE TABLE vendor_alerts (
  id SERIAL PRIMARY KEY,
  alert_id VARCHAR(50) UNIQUE,
  
  vendor_id INT NOT NULL REFERENCES vendors(id),
  kso_id INT REFERENCES kso_partnerships(id),
  
  alert_type VARCHAR(100),                   -- 'contract_expiry', 'poor_performance', 'blacklist', 'license_expiry'
  alert_severity VARCHAR(50),                -- 'critical', 'high', 'medium', 'low'
  
  alert_message TEXT,
  alert_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  action_required TEXT,
  action_deadline DATE,
  action_taken BOOLEAN DEFAULT false,
  action_notes TEXT,
  
  resolved_date TIMESTAMP
);

CREATE INDEX idx_alert_vendor ON vendor_alerts(vendor_id);
CREATE INDEX idx_alert_severity ON vendor_alerts(alert_severity);
CREATE INDEX idx_alert_date ON vendor_alerts(alert_date);

```

---

## VENDOR CATEGORIZATION

### Complete Vendor Type Taxonomy

```
1. BARANG (GOODS)
├─ Alkes (Medical Equipment)
│  ├─ Diagnostic Equipment (EKG, Ultrasound, X-Ray machines)
│  ├─ Life Support (Ventilators, Monitors, Infusion pumps)
│  ├─ Surgical Instruments
│  ├─ Lab Equipment
│  ├─ Furniture & Fixtures
│  └─ Safety Equipment
│
├─ Farmasi (Pharmacy)
│  ├─ Medicines (by category)
│  ├─ Supplements & Vitamins
│  ├─ Vaccines
│  ├─ Biological Products
│  └─ OTC Medications
│
├─ Bahan Habis Pakai (General Consumables)
│  ├─ Office Supplies
│  ├─ Cleaning Supplies
│  ├─ Packaging Materials
│  ├─ IT Equipment (non-critical)
│  └─ Maintenance Supplies
│
└─ Bahan Medis Habis Pakai (Medical Consumables)
   ├─ PPE (Masks, Gloves, Gowns)
   ├─ Syringes & Needles
   ├─ Infusion Sets
   ├─ Wound Care (Dressings, Bandages)
   ├─ Catheters & Tubes
   ├─ Specimen Containers
   ├─ Diagnostic Test Kits
   └─ Laboratory Supplies

2. JASA (SERVICES)
├─ Sewa (Rental/Leasing)
│  ├─ Equipment Rental
│  ├─ Vehicle Rental
│  ├─ Space Rental (Office, Storage)
│  └─ Software Licensing
│
├─ Proyek Pembangunan (Construction Projects)
│  ├─ Building Construction
│  ├─ Extension/Addition
│  ├─ Infrastructure Development
│  └─ Renovation (Major)
│
├─ Renovasi (Renovation/Maintenance)
│  ├─ Interior Renovation
│  ├─ Equipment Maintenance
│  ├─ Facility Maintenance
│  ├─ Cleaning Services
│  └─ Pest Control
│
└─ Layanan Profesional (Professional Services)
   ├─ Consulting (Management, Technical)
   ├─ Auditing & Compliance
   ├─ Training & Development
   ├─ IT Services (Support, Development)
   ├─ Medical Services (Visiting specialists)
   ├─ Transportation & Logistics
   ├─ Catering
   └─ Security Services
```

---

## VENDOR REGISTRATION PROCESS

### Step-by-Step Registration Flow

```
VENDOR WANTS TO WORK WITH KMU
        ↓
[STEP 1] INITIAL INQUIRY
├─ Vendor submits vendor inquiry form
├─ Procurement team reviews
└─ If interested: Proceed to Step 2

[STEP 2] VENDOR QUALIFICATION
├─ Request Company Documents:
│  ├─ Business License (SIU)
│  ├─ Tax ID (NPWP)
│  ├─ Bank Account Info
│  ├─ References (previous clients)
│  └─ Product/Service Specification
├─ Verify Legal Status
├─ Check Financial Viability (if high-value vendor)
└─ If qualified: Proceed to Step 3

[STEP 3] VENDOR REGISTRATION
├─ System creates:
│  ├─ Vendor ID (VND-001, VND-002, etc)
│  ├─ Vendor record in database
│  ├─ Initial performance tracking
│  └─ Document repository
├─ Assign procurement category
├─ Set up contact information
└─ If approved: Proceed to Step 4

[STEP 4] KSO (KERJA SAMA OPERASIONAL) SETUP
├─ Negotiate partnership terms:
│  ├─ Service/product scope
│  ├─ Payment terms
│  ├─ Pricing & discounts
│  ├─ SLA (Service Level Agreement)
│  ├─ Contract period (start/end dates)
│  └─ Renewal terms
├─ Create KSO record (KSO-001, etc)
├─ Upload signed contract
├─ Set performance expectations
└─ If confirmed: Proceed to Step 5

[STEP 5] ACTIVATION & ONBOARDING
├─ Activate vendor in system
├─ Assign order codes/account numbers
├─ Set up payment method
├─ Notify Finance of new vendor
├─ Brief procurement team on vendor details
└─ Vendor READY TO RECEIVE ORDERS

[ONGOING] PERFORMANCE MONITORING
├─ Monthly scorecard evaluation
├─ Track delivery, quality, responsiveness
├─ Update utilization metrics
├─ Monitor contract expiry dates
├─ Handle alerts & compliance issues
└─ Annual review & renewal decision
```

### Example Registration Data

```
VENDOR REGISTRATION EXAMPLE:

Vendor ID:                      VND-001
Company Name:                   PT Medik Jaya Indonesia
Vendor Type:                    Barang (Goods)
Vendor Category:                Alkes (Medical Equipment)
Service Type:                   ['Diagnostic Equipment', 'Life Support']

Legal Status:
├─ Business License:            SIU-123456 (Valid until 2026-12-31)
├─ Tax ID (NPWP):               98.765.432.1.098.765
├─ Business License Expiry:     2026-12-31

Contact Information:
├─ Phone:                       021-123-4567
├─ Email:                       sales@medikjaya.co.id
├─ Website:                     www.medikjaya.co.id

Location:
├─ Address:                     Jl. Sudirman No. 123, Jakarta
├─ City:                        Jakarta
├─ Province:                    Jakarta
├─ Local to Kalimantan Timur:   No

Key Contact:
├─ Person:                      Budi Santoso
├─ Title:                       Sales Manager
├─ Phone:                       0812-3456-7890
├─ Email:                       budi@medikjaya.co.id

Banking:
├─ Bank:                        Bank Mandiri
├─ Account Number:              1234567890
├─ Account Holder:              PT Medik Jaya Indonesia

Vendor Characteristics:
├─ Is Distributor:              Yes
├─ Is Manufacturer:             No
├─ Spare Parts Availability:    Available (Most items in stock)

Registration Date:              2024-06-15
Status:                         ACTIVE
```

---

## KSO MANAGEMENT

### KSO (Kerja Sama Operasional) Structure

```
KSO = OFFICIAL PARTNERSHIP AGREEMENT

What is KSO?
├─ Formal contract/agreement between KMU & Vendor
├─ Specifies:
│  ├─ What goods/services will be supplied
│  ├─ Quality standards
│  ├─ Pricing & payment terms
│  ├─ Contract period (start - end dates)
│  ├─ Renewal conditions
│  └─ Performance expectations
├─ Duration-based (typically 1-3 years)
└─ Can be renewed or terminated

Example KSO Structure:

KSO-001: PT Medik Jaya - Lab Equipment
├─ Vendor:                      PT Medik Jaya Indonesia (VND-001)
├─ Service Type:                Alkes - Diagnostic Equipment
├─ Product List:
│  ├─ EKG Machines
│  ├─ Ultrasound Machines
│  ├─ Portable Monitor
│  └─ ECG Leads & Accessories
├─ Contract Period:
│  ├─ Start Date:               2024-06-15
│  ├─ End Date:                 2025-06-14
│  ├─ Auto Renewal:             Yes
│  └─ Renewal Notice Period:    30 days
├─ Payment Terms:
│  ├─ Method:                   Net 30 (Invoice due 30 days after delivery)
│  ├─ Currency:                 IDR
│  ├─ Discount:                 5% for orders > 50M
│  └─ Minimum Order:            10M IDR
├─ Coverage Area:               All KMU Branches
├─ Expected Annual Value:       500M IDR
├─ Contact for This KSO:
│  ├─ Person:                   Budi Santoso
│  ├─ Phone:                    0812-3456-7890
│  └─ Email:                    budi@medikjaya.co.id
├─ Priority Level:              PRIMARY (main supplier for lab equipment)
├─ Competing KSOs:              KSO-002 (PT Medik Indo), KSO-003 (PT Alat Medis)
└─ Status:                      ACTIVE
```

### KSO Renewal Process

```
3 MONTHS BEFORE KSO EXPIRY:

Day 1: System Alert
├─ Alert: "KSO-001 expires in 90 days (2025-06-14)"
├─ Notify: Manager Pengadaan, Vendor
└─ Action: Review partnership performance

Day 15: Performance Review
├─ Pull YTD performance metrics:
│  ├─ Utilization rate: 95% (Excellent - used more than expected)
│  ├─ On-time delivery: 98% (Excellent)
│  ├─ Quality rating: 4.8/5.0 (Excellent)
│  ├─ Price competitiveness: 4.5/5.0 (Good)
│  └─ Overall score: 4.7/5.0 (Excellent)
├─ Decision: RENEW
└─ Notify vendor of renewal intent

Day 30: Renewal Negotiation
├─ Contact vendor:
│  ├─ "We want to renew for another year"
│  ├─ "Current terms satisfactory"
│  └─ "Any changes needed?"
├─ Discuss:
│  ├─ Price adjustment (inflation, volume discounts?)
│  ├─ Contract adjustments (any new products?)
│  ├─ SLA improvements (delivery speed?)
│  └─ New terms if needed
└─ Finalize terms

Day 45: Contract Update
├─ New end date: 2026-06-14 (1 year extension)
├─ Update terms if any changes
├─ Both parties sign
└─ Update KSO record in system

Day 60: Activation
├─ New KSO active
├─ Notify all departments
├─ Reset performance metrics for new period
└─ Continue operations
```

---

## MULTI-KSO STRATEGY

### Why Multiple KSOs for Same Service?

```
Example: LABORATORY EQUIPMENT

Problem:
- Single vendor creates dependency
- If vendor out of stock → can't get equipment
- No price competition
- Quality issues not caught early
- Risk if vendor goes bankrupt

Solution: Multiple KSOs for Laboratory Equipment

KSO-001: PT Medik Jaya (PRIMARY - 60%)
├─ Supplier of: EKG, Ultrasound, Portable Monitors
├─ Allocation: 60% of orders
├─ Priority: PRIMARY
├─ Why: Best price, fastest delivery, excellent quality
└─ Location: Jakarta (good reach)

KSO-002: PT Medik Indo (SECONDARY - 30%)
├─ Supplier of: EKG, Ultrasound, ECG Monitors
├─ Allocation: 30% of orders
├─ Priority: SECONDARY (backup)
├─ Why: Competitive pricing, local representative
└─ Location: Surabaya

KSO-003: PT Alat Medis Profesional (TERTIARY - 10%)
├─ Supplier of: All lab equipment types
├─ Allocation: 10% of orders
├─ Priority: BACKUP (emergency only)
├─ Why: Ensures availability, competition
└─ Location: Balikpapan

Multi-KSO Benefits:
✅ Risk Mitigation:        If primary vendor fails, we have secondary/tertiary
✅ Price Competition:      Multiple vendors push prices down
✅ Availability:           If primary is out of stock, we can use secondary
✅ Quality Assurance:      Multiple suppliers = better quality control
✅ Service Redundancy:     If one vendor has slow response, use another
✅ Negotiating Power:      Can leverage one against another
✅ Innovation:             Multiple suppliers bring different solutions

Multi-KSO Rules:
├─ Primary gets 60%+ of orders (main relationship)
├─ Secondary gets 20-40% (backup + price negotiation tool)
├─ Tertiary gets <20% (emergency only)
├─ Review allocation quarterly
├─ If primary underperforms, promote secondary
└─ If secondary outperforms, negotiate better terms
```

### Multi-KSO Dashboard

```
LABORATORY EQUIPMENT SUPPLY MANAGEMENT

Total Spend YTD: 450M IDR
Expected Annual: 600M IDR

PRIMARY SUPPLIER - KSO-001: PT Medik Jaya
├─ YTD Spend: 270M (60% of total) ✅ Target: 60%
├─ On-Time: 98% (Excellent)
├─ Quality: 4.8/5.0 (Excellent)
├─ Price Competitiveness: 4.5/5.0
├─ Overall Score: 4.7/5.0
└─ Status: PERFORMING WELL - Continue as primary

SECONDARY SUPPLIER - KSO-002: PT Medik Indo
├─ YTD Spend: 135M (30% of total) ✅ Target: 30%
├─ On-Time: 94% (Good)
├─ Quality: 4.3/5.0 (Good)
├─ Price Competitiveness: 4.7/5.0 (Best price!)
├─ Overall Score: 4.4/5.0
└─ Status: GOOD BACKUP - Monitor for promotion to primary

TERTIARY SUPPLIER - KSO-003: PT Alat Medis Profesional
├─ YTD Spend: 45M (10% of total) ✅ Target: 10%
├─ On-Time: 89% (Satisfactory)
├─ Quality: 3.9/5.0 (Acceptable)
├─ Price Competitiveness: 3.5/5.0 (Most expensive)
├─ Overall Score: 3.8/5.0
└─ Status: EMERGENCY BACKUP - Use only if primary/secondary unavailable

QUARTERLY REVIEW ACTION ITEMS:
┌──────────────────────────────────────────────────────┐
│ 1. PT Medik Jaya (Primary) - Continue current terms  │
│    Action: Annual review meeting in Q3               │
│                                                       │
│ 2. PT Medik Indo (Secondary) - Monitor for growth    │
│    Action: Negotiate to 35% allocation next quarter  │
│    Reason: Better price, catching up on quality      │
│                                                       │
│ 3. PT Alat Medis Prof (Tertiary) - Consider removal  │
│    Action: Meeting to improve quality/price or end   │
│    Reason: Poor performance, rarely used             │
└──────────────────────────────────────────────────────┘
```

---

## VENDOR DASHBOARD

### Real-Time Vendor Management Portal

```
VENDOR MASTER DATABASE DASHBOARD

═══════════════════════════════════════════════════════════════════

QUICK STATS
┌─────────────────────────────────────────────────────────────────┐
│ Total Active Vendors:       87 vendors                          │
│ Total Active KSOs:          156 partnerships                    │
│ Vendors with Multi-KSO:     23 service types                    │
│ Vendor Compliance Rate:      96.8% ✅                          │
│ Average Vendor Rating:       4.4/5.0                            │
│ KSOs Expiring (90 days):     12 partnerships                    │
│ Vendors on Alert:            3 (action required)                │
└─────────────────────────────────────────────────────────────────┘

VENDOR SEARCH & FILTER
┌─────────────────────────────────────────────────────────────────┐
│ [Search by vendor name/ID]                                      │
│                                                                  │
│ Filter by:                                                      │
│ Category: [Alkes ▼] [Farmasi ▼] [Umum ▼] [Jasa ▼]             │
│ Status: [Active ▼] [Inactive ▼] [All ▼]                       │
│ Rating: [4+ Stars ▼] [3+ Stars ▼] [All ▼]                    │
│                                                                  │
│ [SEARCH] [CLEAR FILTERS] [EXPORT LIST]                        │
└─────────────────────────────────────────────────────────────────┘

VENDOR DIRECTORY (Table View)
┌─────────────────────────────────────────────────────────────────┐
│ ID    │ Vendor Name      │ Category │ KSOs │ Rating │ Status  │
├─────────────────────────────────────────────────────────────────┤
│ VND-001│ PT Medik Jaya   │ Alkes   │ 1   │ 4.7★  │ Active  │
│        └─ [View Details] [Manage KSOs] [Edit] [View Docs]      │
│                                                                  │
│ VND-002│ PT Pharma Indo  │ Farmasi │ 2   │ 4.4★  │ Active  │
│        └─ [View Details] [Manage KSOs] [Edit] [View Docs]      │
│                                                                  │
│ VND-003│ PT Supply Chain │ Umum    │ 3   │ 4.1★  │ Active  │
│        └─ [View Details] [Manage KSOs] [Edit] [View Docs]      │
│                                                                  │
│ VND-004│ Sewa Genset PT  │ Jasa    │ 1   │ 3.8★  │ Active  │
│        └─ [View Details] [Manage KSOs] [Edit] [View Docs]      │
│                                                                  │
│ VND-005│ PT Konstruksi   │ Jasa    │ 1   │ 4.2★  │ Inactive│
│        └─ [View Details] [Manage KSOs] [Reactivate] [Docs]    │
└─────────────────────────────────────────────────────────────────┘

KSO EXPIRY MONITOR
┌──────────────────────────────────────────────────────────────┐
│ 🔴 CRITICAL (Expires < 30 days): 3 KSOs                     │
│ ├─ KSO-045: PT Medik Jaya Lab Equipment (Expires: Jun 20)    │
│ │  Status: NEEDS RENEWAL DECISION                           │
│ │  YTD Performance: 4.7/5.0 (Excellent - RECOMMEND RENEW)  │
│ │  [RENEW] [TERMINATE] [RENEGOTIATE]                       │
│ │                                                            │
│ ├─ KSO-067: PT Pharma Indo Medicine Supply (Expires: Jun 25)│
│ │  Status: VENDOR REQUESTED TERMS CHANGE                   │
│ │  YTD Performance: 4.4/5.0 (Good)                         │
│ │  [REVIEW PROPOSAL] [APPROVE] [REJECT]                    │
│ │                                                            │
│ └─ KSO-089: PT Supply Genral (Expires: Jun 28)              │
│    Status: UNDER REVIEW - POOR PERFORMANCE                 │
│    YTD Performance: 2.8/5.0 (Needs Improvement)             │
│    [RENEW WITH CONDITIONS] [TERMINATE] [REPLACE]            │
│                                                              │
│ 🟡 WARNING (30-90 days): 9 KSOs                             │
│ └─ [See list] [Manage renewals]                             │
│                                                              │
│ 🟢 NORMAL (90+ days): 144 KSOs                              │
│ └─ [See list]                                               │
└──────────────────────────────────────────────────────────────┘

VENDOR ALERTS & ISSUES
┌──────────────────────────────────────────────────────────────┐
│ 🔴 CRITICAL (3 alerts - Requires immediate action)          │
│                                                              │
│ Alert #1: Poor Delivery Performance                         │
│ Vendor: PT Supply Chain Corp (VND-003)                      │
│ Issue: Last 3 orders late (avg 5 days late)                 │
│ Impact: Affecting hospital operations                       │
│ Action Required: Contact vendor, discuss remediation        │
│ Deadline: Today                                             │
│ [CONTACT VENDOR] [ESCALATE] [MARK RESOLVED]                │
│                                                              │
│ Alert #2: License Expiry                                    │
│ Vendor: PT Construction Pro (VND-008)                       │
│ Issue: Business License expires in 15 days                  │
│ Action Required: Request renewed license documentation      │
│ Deadline: 2025-06-15                                        │
│ [REQUEST DOCS] [SUSPEND] [ACKNOWLEDGE]                     │
│                                                              │
│ Alert #3: Quality Issues                                    │
│ Vendor: PT Medis Murah (VND-012)                           │
│ Issue: 3 defective batches in last 60 days                  │
│ Action Required: Quality audit before next order            │
│ Deadline: 2025-06-30                                        │
│ [SCHEDULE AUDIT] [TERMINATE] [CONDITIONAL RENEWAL]         │
│                                                              │
│ 🟡 WARNING (2 alerts - Monitor closely)                     │
│ └─ [See list]                                               │
└──────────────────────────────────────────────────────────────┘

VENDOR UTILIZATION ANALYSIS
┌──────────────────────────────────────────────────────────────┐
│ Top 10 Vendors by Spend (YTD)                               │
│                                                              │
│ 1. PT Medik Jaya          320M IDR (↑ 15% vs last year)     │
│    Utilization: 95% of expected annual budget ✅            │
│    Status: Primary for Lab Equipment                        │
│                                                              │
│ 2. PT Pharma Indo         280M IDR (↑ 8% vs last year)      │
│    Utilization: 105% of expected (EXCEEDING)                │
│    Status: Primary for Pharmacy                             │
│    Action: Consider increasing annual budget                │
│                                                              │
│ 3. PT Construction Pro    150M IDR (NEW)                    │
│    Utilization: 75% of expected annual budget               │
│    Status: Primary for Building Renovation                  │
│                                                              │
│ ... (7 more vendors)                                        │
│                                                              │
│ [VIEW FULL RANKING] [EXPORT REPORT] [DRILL DOWN]           │
└──────────────────────────────────────────────────────────────┘

VENDOR ACTIONS
┌──────────────────────────────────────────────────────────────┐
│ [+ NEW VENDOR]          Register new vendor                  │
│ [+ NEW KSO]             Create new partnership               │
│ [BULK IMPORT]           Import vendors from Excel            │
│ [COMPLIANCE AUDIT]      Run vendor compliance check          │
│ [PERFORMANCE REPORT]    Generate monthly scorecard           │
│ [CONTRACT MANAGEMENT]   View/manage KSO contracts            │
│ [RENEWAL WORKFLOW]      Manage KSO renewals                  │
│ [MULTI-KSO SETUP]       Configure multi-vendor services      │
│ [EXPORT VENDOR LIST]    Excel/PDF vendor directory           │
│ [VENDOR COMMUNICATION]  Send email to vendors                │
└──────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════
```

---

## PERFORMANCE TRACKING

### Vendor Scorecard System

```
VENDOR PERFORMANCE SCORECARD

═════════════════════════════════════════════════════════════════

Vendor: PT Medik Jaya Indonesia (VND-001)
KSO: KSO-001 - Laboratory Equipment Supply
Evaluation Period: May 2025 (Monthly)
Evaluation Date: 2025-06-01

DELIVERY PERFORMANCE
├─ Orders Placed This Month: 5
├─ Orders On Time: 5 (100%)
├─ Orders Late: 0
├─ Average Delay: 0 days
├─ On-Time Delivery Rate: ✅ 100%
│  Target: ≥95%
│  Status: EXCEEDS TARGET
└─ Trend: ↑ Consistent excellence

QUALITY METRICS
├─ Total Items Received: 47 units
├─ Items with Defects: 0
├─ Defect Rate: ✅ 0%
│  Target: <2%
│  Status: EXCELLENT
├─ Rejected Items: 0
├─ Rejection Rate: 0%
│  Target: <1%
│  Status: EXCELLENT
└─ Trend: ↑ No quality issues

RESPONSIVENESS
├─ Support Tickets This Month: 2
├─ Resolved Within SLA: 2 (100%)
├─ Average Response Time: ✅ 2.5 hours
│  Target: <4 hours
│  Status: EXCELLENT
├─ Customer Inquiries: 3
├─ Average Resolution Time: 1 day
│  Target: <2 days
│  Status: EXCEEDS TARGET
└─ Trend: ↑ Very responsive

FINANCIAL PERFORMANCE
├─ Total Orders Value: 95M IDR
├─ Average Order Value: 19M IDR
├─ Order Count: 5
├─ Price Variance: ✅ 0% (exactly per contract)
│  Target: Within ±2%
│  Status: EXCELLENT
└─ Discount Taken: 0 (under minimum 50M threshold)

SPARE PARTS & SUPPORT
├─ Spare Parts Requests: 2
├─ Parts Availability: ✅ 100% (2/2 available)
│  Target: ≥90%
│  Status: EXCELLENT
├─ Turnaround for Spare Parts: ✅ 1-2 days
│  Target: <5 days
│  Status: EXCELLENT
└─ Warranty Claims: 0

COMPLIANCE & DOCUMENTATION
├─ Contract Compliance: ✅ 100%
│  All terms followed
├─ Documentation Complete: ✅ Yes
│  All required documents attached
├─ Invoices Accurate: ✅ Yes (100%)
└─ Payment Terms Compliance: ✅ 100%
   All invoices paid on time

OVERALL SCORING
┌─────────────────────────────────────┐
│ Delivery Timeliness:    5.0/5.0 ⭐  │
│ Product Quality:        5.0/5.0 ⭐  │
│ Service Responsiveness: 5.0/5.0 ⭐  │
│ Price Competitiveness:  4.5/5.0 ⭐  │
│ Compliance with Terms:  5.0/5.0 ⭐  │
│ Spare Parts Support:    5.0/5.0 ⭐  │
│ Communication:          5.0/5.0 ⭐  │
│                                     │
│ OVERALL SCORE:          4.93/5.0    │
│ RATING:                 ⭐⭐⭐⭐⭐ │
│ PERFORMANCE STATUS:     EXCELLENT   │
└─────────────────────────────────────┘

PERFORMANCE TREND (Last 6 Months)
Jan: 4.8 → Feb: 4.85 → Mar: 4.9 → Apr: 4.92 → May: 4.93
Trend: ↑ IMPROVING - Vendor getting better each month

COMMENTS & NOTES
═════════════════════════════════════════════════════════════════
PT Medik Jaya continues to perform excellently across all metrics.
- Consistently on-time deliveries
- Zero quality issues
- Excellent responsiveness to support requests
- Good price competitiveness
- No compliance issues

RECOMMENDATION FOR RENEWAL
═════════════════════════════════════════════════════════════════
✅ STRONG RECOMMENDATION TO RENEW

Rationale:
- Excellent performance across all metrics
- Reliable partner for critical equipment
- Good communication and support
- No performance concerns

Suggested Action:
Renew KSO-001 with current terms (no price increase needed given
excellent performance). Consider expanding product list or service
scope in next negotiation.

EVALUATOR INFORMATION
═════════════════════════════════════════════════════════════════
Evaluated by: Manager Pengadaan (Ibu Siti)
Evaluation Date: 2025-06-01
Signature: [Digital Signature]

═════════════════════════════════════════════════════════════════
```

---

## IMPLEMENTATION GUIDE

### Database Setup

```sql
-- Run all schema creation scripts above

-- Add to existing procurement tables:

ALTER TABLE purchase_orders 
ADD COLUMN vendor_id INT REFERENCES vendors(id),
ADD COLUMN kso_id INT REFERENCES kso_partnerships(id);

ALTER TABLE tenders
ADD COLUMN vendor_category VARCHAR(100);

-- Grant permissions
GRANT SELECT, INSERT, UPDATE ON vendors TO procurement_team;
GRANT SELECT, INSERT, UPDATE ON kso_partnerships TO procurement_team;
GRANT SELECT ON vendor_scorecards TO management_dashboard;
```

### API Endpoints for Vendor Management

```javascript
// Vendor Management APIs

// Register new vendor
POST /api/vendors/register
{
  "company_name": "PT Medik Jaya",
  "vendor_type": "barang",
  "vendor_category": "alkes",
  "service_type": ["diagnostic_equipment", "life_support"],
  "contact_details": {...},
  "legal_documents": [...]
}

// Create/Update KSO
POST /api/kso/create
{
  "vendor_id": 1,
  "service_type": "alkes_diagnostic",
  "start_date": "2025-06-15",
  "end_date": "2026-06-14",
  "payment_terms": "Net 30",
  "contract_document": "..."
}

// Get vendor details
GET /api/vendors/:vendor_id

// List all vendors with filters
GET /api/vendors?category=alkes&status=active&rating=4+

// Get KSO details
GET /api/kso/:kso_id

// Update vendor scorecard
POST /api/vendor-scorecard/record
{
  "kso_id": 1,
  "evaluation_date": "2025-06-01",
  "scores": {
    "delivery_timeliness": 5.0,
    "product_quality": 5.0,
    ...
  }
}

// Multi-KSO configuration
POST /api/multi-kso/setup
{
  "service_code": "lab_equipment",
  "primary_kso_id": 1,
  "secondary_kso_id": 2,
  "allocation": [60, 40]
}

// Get vendor dashboard
GET /api/vendor-dashboard/summary

// KSO renewal workflow
POST /api/kso/:kso_id/renewal
{
  "action": "renew|terminate|renegotiate",
  "new_terms": {...}
}
```

---

**COMPLETE VENDOR MASTER DATABASE READY TO IMPLEMENT!** 🚀

This module integrates seamlessly with your Platform Digitalisasi Pengadaan KMU and handles:
✅ Vendor registration & categorization
✅ KSO management & renewal
✅ Multi-vendor strategy (multiple KSOs for same service)
✅ Performance tracking & scorecards
✅ Contract/partnership validity tracking
✅ Vendor alerts & compliance

Ready to build? 💪


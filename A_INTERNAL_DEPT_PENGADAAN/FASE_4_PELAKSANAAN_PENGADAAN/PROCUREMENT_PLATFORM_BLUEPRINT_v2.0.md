# PROCUREMENT PLATFORM BLUEPRINT v2.0
## KMU Holding Hospital Group - B2B Medical Equipment Procurement Portal

**Document Version:** 2.0  
**Date:** June 2025  
**Status:** READY FOR IT IMPLEMENTATION  
**Owner:** Departemen Pengadaan Umum dan Jasa  
**Target Deployment:** 4 weeks

---

## TABLE OF CONTENTS

1. [Executive Summary](#executive-summary)
2. [Business Context & Requirements](#business-context--requirements)
3. [System Architecture](#system-architecture)
4. [Database Design](#database-design)
5. [API Specifications](#api-specifications)
6. [Gemini AI Integration](#gemini-ai-integration)
7. [UI/UX Specifications](#uiux-specifications)
8. [Workflow & Process Design](#workflow--process-design)
9. [Security & Compliance](#security--compliance)
10. [Implementation Checklist](#implementation-checklist)
11. [Testing Strategy](#testing-strategy)
12. [Deployment Guide](#deployment-guide)

---

## EXECUTIVE SUMMARY

### Problem Statement
KMU Holding currently manages procurement manually across multiple hospital branches. Key pain points:
- **Long approval cycles** (>2 weeks for IMT-PO process)
- **Scattered vendor communications** (email, spreadsheet chaos)
- **Manual bid tabulation & scoring** (error-prone, time-consuming)
- **Payment tracking complexity** (DP + final payment across vendors)
- **No audit trail** for compliance & transparency

### Solution Overview
A **B2B Procurement Portal** that enables:
- ✅ Centralized tender management (1 year budget planning)
- ✅ Vendor self-service quote submission (any document format)
- ✅ AI-powered bid tabulation & scoring (using Google Gemini)
- ✅ Automated approval workflow (≤2 week SLA)
- ✅ Milestone-based payment tracking (DP + final)
- ✅ Closed-rank vendor bidding (fair, transparent)

### Key Success Metrics
| Metric | Current | Target |
|--------|---------|--------|
| IMT → PO Time | 14-21 days | ≤14 days |
| Bid Tabulation | 2-3 days (manual) | <2 hours (AI) |
| Vendor Query Response | 1-2 days | Real-time |
| Payment Accuracy | 85% | 99% |
| Audit Trail | Manual logs | 100% digital |

---

## BUSINESS CONTEXT & REQUIREMENTS

### Business Process Overview

```
ANNUAL PROCUREMENT CYCLE:

Q1: RAB (Rencana Anggaran Biaya)ning
├─ All branches submit yearly needs
├─ Compile master list (barang & jasa)
└─ Categorize by type (alkes, obat, jasa support)

Q2-Q4: Tender Execution (monthly/quarterly)
├─ Post tender to vendor portal
├─ Vendors login & submit quotes
├─ AI tabulates & scores
├─ Procurement approves winner
├─ PO issued with payment terms
└─ Payment tracking (DP + pelunasan)
```

### Key Stakeholders

**Internal Users:**
- **Procurement Team** (post tenders, review bids, issue PO)
- **Finance** (approve payment, 3-way match)
- **Clinical/User Units** (submit needs, validate specs)
- **Directors** (approve high-value tenders)
- **Audit** (review compliance, historical data)

**External Users:**
- **Vendors/Rekanan** (registered suppliers; submit quotes, negotiate, track orders)

### Critical Requirements

#### Functional Requirements

**FR1: Tender Management**
- Post tender with specifications
- Set bid closing date
- Define evaluation criteria with weightage
- Support multiple items per tender

**FR2: Quote Submission (Vendor)**
- Upload quotes in any format (PDF, Word, image, scanned)
- Include: Price, Delivery, Testing, Training, Commissioning
- Multiple revisions allowed (until closing date)
- Confidential bidding (vendors can't see others' bids)

**FR3: AI-Powered Bid Tabulation**
- Extract data from uploaded documents via Google Gemini
- Auto-populate comparison table
- Validate extracted data (sanity checks)
- Flag uncertain/conflicting data for human review

**FR4: Automated Scoring**
- 5 standard criteria: Harga (25%), Kualitas (20%), Maintenance (20%), User Need (20%), Brand (15%)
- Additional medical factors: Local presence (Kalimantan), spare parts availability, population served
- Auto-calculate weighted score
- Ranking with recommendation (Utama/Alternatif/Pertimbangan/Tidak)

**FR5: Approval Workflow**
- 2-week SLA countdown per tender
- Multi-level approval (Procurement → Finance → Director)
- Conditional auto-approval for ≤threshold amounts
- Escalation alerts if SLA breached
- Manual override capability (medical factors override AI score)

**FR6: PO Generation**
- Auto-generate from approved tender
- Include all terms: price, delivery, testing, training, commissioning
- Digital signature/approval
- PDF export & email to vendor

**FR7: Payment Tracking**
- Milestone-based payment (DP 30% → Delivery 40% → Testing 20% → Training+Comm 10%)
- Invoice matching (PO-BAPB-Invoice 3-way match)
- Payment status tracking
- Automatic notifications

**FR8: Dashboard & Reporting**
- Real-time SLA countdown
- Vendor performance metrics
- Budget vs. actual spend
- Payment status by vendor
- Historical audit trail

#### Non-Functional Requirements

**NFR1: Performance**
- Page load time: <2 seconds
- Bid tabulation: <5 minutes for 50 quotes
- Real-time dashboard updates

**NFR2: Scalability**
- Support 100+ vendors
- Handle 1000+ tenders/year
- 500+ concurrent users

**NFR3: Security**
- User authentication (email/password + optional 2FA)
- Role-based access control (RBAC)
- Data encryption (HTTPS + database)
- Audit logging of all actions
- GDPR-compliant data handling

**NFR4: Availability**
- 99.5% uptime
- Daily automated backups
- Disaster recovery plan

**NFR5: Usability**
- Responsive design (desktop + mobile)
- Intuitive UI for non-technical users
- Multi-language support (Indonesian default)

---

## SYSTEM ARCHITECTURE

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        INTERNET / VPN                           │
└──────────────────────┬──────────────────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
    ┌───▼─────┐              ┌───────▼────┐
    │ VENDOR  │              │  INTERNAL  │
    │ PORTAL  │              │  DASHBOARD │
    │(React)  │              │  (React)   │
    └───┬─────┘              └───────┬────┘
        │                            │
        └───────────┬────────────────┘
                    │
              ┌─────▼─────┐
              │  API GW   │
              │(Express)  │
              └─────┬─────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
    ┌───▼───┐  ┌───▼────┐  ┌──▼───┐
    │Auth   │  │Tender  │  │Quote │
    │Module │  │Module  │  │Module│
    └───┬───┘  └───┬────┘  └──┬───┘
        │          │          │
        └──────────┼──────────┘
                   │
            ┌──────▼──────┐
            │  Gemini API │◄─── (Document extraction)
            └──────┬──────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
    ┌───▼───┐  ┌──▼───┐  ┌───▼──┐
    │Score  │  │PO    │  │Pay   │
    │Module │  │Module│  │Module│
    └───┬───┘  └──┬───┘  └───┬──┘
        │         │          │
        └─────────┼──────────┘
                  │
           ┌──────▼──────────┐
           │ PostgreSQL DB   │
           │ (Primary)       │
           └─────────────────┘
                  │
           ┌──────▼──────────┐
           │   Redis Cache   │
           │ (Session + API) │
           └─────────────────┘
                  │
           ┌──────▼──────────┐
           │   File Storage  │
           │ (AWS S3 / Local)│
           └─────────────────┘
```

### Technology Stack

| Layer | Technology | Version | Notes |
|-------|-----------|---------|-------|
| **Frontend** | React.js | 18.x | SPA, responsive |
| | Tailwind CSS | 3.x | Styling |
| | Axios | 1.x | HTTP client |
| | Chart.js | 4.x | Dashboard charts |
| **Backend** | Node.js | 18.x+ | Runtime |
| | Express.js | 4.x | REST API framework |
| | Google Gemini API | Latest | Document extraction |
| **Database** | PostgreSQL | 13+ | Primary (recommended) |
| | SQLite | 3.x | Alternative (dev/small) |
| | Redis | 6.x | Cache & sessions |
| **Auth** | JWT | - | Token-based |
| | bcrypt | 5.x | Password hashing |
| **File Storage** | AWS S3 OR Local FS | - | Quote documents |
| **Logging** | Winston | 3.x | Application logs |
| **Email** | Nodemailer | 6.x | Notifications |

### Deployment Options

**Option A: Cloud (Recommended)**
```
Heroku/Railway (Backend) + Vercel (Frontend) + Supabase (Database)
├─ Easy scaling
├─ Minimal DevOps
├─ Pay-as-you-go pricing
└─ Built-in backups
```

**Option B: On-Premise (Local Server)**
```
Windows Server / Linux Box (Backend + DB) + Static hosting (Frontend)
├─ Full control
├─ No external dependencies
├─ Network isolation (internal only)
└─ Manual backup/maintenance
```

**Option C: Hybrid**
```
Local Backend + Cloud Frontend
├─ Frontend accessible globally
├─ Backend on internal network
├─ API Gateway with VPN
└─ Best of both worlds
```

---

## DATABASE DESIGN

### Database Schema (PostgreSQL)

#### 1. Users Table
```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  full_name VARCHAR(255) NOT NULL,
  role ENUM('vendor', 'procurement', 'finance', 'director', 'audit', 'admin'),
  user_type ENUM('internal', 'external') NOT NULL,
  status ENUM('active', 'inactive', 'suspended'),
  
  -- Vendor-specific
  vendor_id INT REFERENCES vendors(id),
  
  -- Internal user
  department VARCHAR(100),
  branch_id INT REFERENCES branches(id),
  
  -- Account settings
  two_factor_enabled BOOLEAN DEFAULT false,
  last_login TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  INDEX idx_email (email),
  INDEX idx_role (role),
  INDEX idx_vendor_id (vendor_id)
);
```

#### 2. Vendors Table
```sql
CREATE TABLE vendors (
  id SERIAL PRIMARY KEY,
  company_name VARCHAR(255) NOT NULL,
  tax_id VARCHAR(50) UNIQUE,
  email VARCHAR(255),
  phone VARCHAR(20),
  
  -- Address
  street_address VARCHAR(255),
  city VARCHAR(100),
  province VARCHAR(100),
  postal_code VARCHAR(10),
  country VARCHAR(100) DEFAULT 'Indonesia',
  
  -- Business info
  business_type VARCHAR(100), -- alkes, obat, jasa, etc
  specialization TEXT, -- comma-separated
  
  -- Local presence
  has_local_office BOOLEAN DEFAULT false,
  local_office_location VARCHAR(255), -- e.g., "Kalimantan Timur"
  local_office_population_served INT,
  
  -- Sparepart & support
  sparepart_availability VARCHAR(100), -- "excellent", "good", "fair"
  sparepart_price_level ENUM('low', 'medium', 'high'),
  support_rating DECIMAL(2,1), -- 1-5
  
  -- Status & compliance
  registration_date DATE,
  status ENUM('approved', 'pending', 'rejected', 'inactive'),
  certification_documents TEXT, -- JSON array of doc URLs
  
  -- Metrics
  total_bids INT DEFAULT 0,
  total_wins INT DEFAULT 0,
  avg_delivery_days DECIMAL(5,2),
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  INDEX idx_company_name (company_name),
  INDEX idx_status (status),
  INDEX idx_local_office (has_local_office)
);
```

#### 3. Tenders Table
```sql
CREATE TABLE tenders (
  id SERIAL PRIMARY KEY,
  tender_number VARCHAR(50) UNIQUE NOT NULL, -- e.g., "TND-2025-001"
  title VARCHAR(255) NOT NULL,
  description TEXT,
  
  -- Type & categorization
  category VARCHAR(100), -- alkes, obat, jasa, etc
  sub_category VARCHAR(100),
  
  -- Specifications
  specifications JSON, -- { "power": "220V", "weight": "50kg", ... }
  required_certifications TEXT, -- comma-separated
  
  -- Timeline
  posting_date DATE,
  bid_closing_date DATETIME NOT NULL,
  evaluation_period_days INT DEFAULT 7,
  expected_delivery_date DATE,
  
  -- Budget
  budget_min DECIMAL(15,2),
  budget_max DECIMAL(15,2),
  approval_threshold DECIMAL(15,2), -- auto-approve if below this
  
  -- Status
  status ENUM('draft', 'published', 'closed', 'awarded', 'completed'),
  
  -- Evaluation criteria (JSON for flexibility)
  evaluation_criteria JSON, -- {
                            --   "price": {"weight": 25, "type": "numeric"},
                            --   "quality": {"weight": 20, "type": "text"},
                            --   "local_presence": {"weight": 15, "type": "boolean"},
                            --   ...
                            -- }
  
  -- Additional factors
  medical_factor_override BOOLEAN DEFAULT false,
  medical_notes TEXT,
  
  -- User tracking
  created_by INT REFERENCES users(id),
  approved_by INT REFERENCES users(id),
  assigned_to INT REFERENCES users(id), -- procurement officer
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  INDEX idx_status (status),
  INDEX idx_closing_date (bid_closing_date),
  INDEX idx_category (category)
);
```

#### 4. Quotes (Bids) Table
```sql
CREATE TABLE quotes (
  id SERIAL PRIMARY KEY,
  tender_id INT NOT NULL REFERENCES tenders(id),
  vendor_id INT NOT NULL REFERENCES vendors(id),
  
  -- Quote upload & extraction
  document_url VARCHAR(255), -- S3/local path to uploaded file
  document_type VARCHAR(50), -- pdf, docx, image, etc
  upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  -- Extracted data (from Gemini AI)
  extracted_data JSON, -- {
                       --   "price": 5000000,
                       --   "price_currency": "IDR",
                       --   "delivery_days": 30,
                       --   "delivery_location": "...",
                       --   "testing_procedure": "...",
                       --   "training_hours": 8,
                       --   "training_days": 2,
                       --   "commissioning_days": 1,
                       --   "local_support": true,
                       --   "sparepart_availability": "excellent",
                       --   "confidence_score": 0.95
                       -- }
  
  -- Human review (if AI confidence low)
  requires_human_review BOOLEAN DEFAULT false,
  human_review_notes TEXT,
  reviewed_by INT REFERENCES users(id),
  reviewed_at TIMESTAMP,
  
  -- Vendor negotiation
  revision_number INT DEFAULT 1,
  negotiation_status ENUM('initial', 'revised', 'final'),
  negotiation_notes TEXT, -- offer/counter-offer history
  
  -- Scoring
  calculated_score DECIMAL(5,2), -- out of 500 (based on weightage)
  score_breakdown JSON, -- {
                        --   "price_score": 125,
                        --   "quality_score": 100,
                        --   "local_presence_score": 75,
                        --   ...
                        -- }
  recommendation ENUM('utama', 'alternatif', 'pertimbangan', 'tidak'), -- based on score
  
  -- Selection
  selected BOOLEAN DEFAULT false,
  selected_reason TEXT,
  
  -- Audit
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  UNIQUE(tender_id, vendor_id, revision_number),
  INDEX idx_tender_id (tender_id),
  INDEX idx_vendor_id (vendor_id),
  INDEX idx_calculated_score (calculated_score),
  INDEX idx_selected (selected)
);
```

#### 5. Purchase Orders (PO) Table
```sql
CREATE TABLE purchase_orders (
  id SERIAL PRIMARY KEY,
  po_number VARCHAR(50) UNIQUE NOT NULL, -- e.g., "PO-2025-001"
  tender_id INT NOT NULL REFERENCES tenders(id),
  vendor_id INT NOT NULL REFERENCES vendors(id),
  
  -- PO details
  po_date DATE NOT NULL,
  po_amount DECIMAL(15,2) NOT NULL,
  currency VARCHAR(10) DEFAULT 'IDR',
  
  -- Terms
  delivery_date DATE,
  payment_terms TEXT, -- "Net 30", "2/10 Net 30", etc
  
  -- Payment schedule (milestones)
  payment_milestones JSON, -- [
                           --   {"milestone": "DP", "percentage": 30, "trigger": "PO_ISSUED"},
                           --   {"milestone": "Delivery", "percentage": 40, "trigger": "GOODS_RECEIVED"},
                           --   {"milestone": "Testing Passed", "percentage": 20, "trigger": "QC_APPROVED"},
                           --   {"milestone": "Training+Commission", "percentage": 10, "trigger": "COMMISSIONED"}
                           -- ]
  
  -- Service requirements
  testing_required BOOLEAN DEFAULT true,
  testing_procedure TEXT,
  training_required BOOLEAN DEFAULT true,
  training_scope TEXT,
  commissioning_required BOOLEAN DEFAULT true,
  
  -- Status
  status ENUM('draft', 'issued', 'acknowledged', 'in_progress', 'delivered', 'completed', 'cancelled'),
  
  -- Approvals
  approved_by INT REFERENCES users(id),
  approved_date TIMESTAMP,
  
  -- Digital signature
  vendor_signature_url VARCHAR(255),
  vendor_signed_at TIMESTAMP,
  po_signature_url VARCHAR(255),
  po_signed_at TIMESTAMP,
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  INDEX idx_vendor_id (vendor_id),
  INDEX idx_tender_id (tender_id),
  INDEX idx_status (status)
);
```

#### 6. Payments Table
```sql
CREATE TABLE payments (
  id SERIAL PRIMARY KEY,
  po_id INT NOT NULL REFERENCES purchase_orders(id),
  vendor_id INT NOT NULL REFERENCES vendors(id),
  
  -- Invoice
  invoice_number VARCHAR(50),
  invoice_date DATE,
  invoice_amount DECIMAL(15,2),
  invoice_document_url VARCHAR(255),
  
  -- Milestone
  milestone_type ENUM('DP', 'delivery', 'testing', 'training_commission') NOT NULL,
  milestone_percentage DECIMAL(5,2),
  payment_amount DECIMAL(15,2),
  
  -- 3-Way Match
  po_matched BOOLEAN DEFAULT false,
  grn_matched BOOLEAN DEFAULT false, -- BAPB (Berita Acara Penerimaan Barang)
  invoice_matched BOOLEAN DEFAULT false,
  three_way_match_complete BOOLEAN DEFAULT false,
  match_date TIMESTAMP,
  
  -- Status & tracking
  status ENUM('pending', 'approved', 'processing', 'paid', 'cancelled'),
  approval_by INT REFERENCES users(id),
  approved_at TIMESTAMP,
  
  payment_date TIMESTAMP,
  payment_reference VARCHAR(100), -- bank transfer ref
  
  -- Notes
  payment_notes TEXT,
  rejection_reason TEXT,
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  INDEX idx_po_id (po_id),
  INDEX idx_vendor_id (vendor_id),
  INDEX idx_status (status),
  INDEX idx_milestone_type (milestone_type)
);
```

#### 7. Audit Log Table
```sql
CREATE TABLE audit_logs (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id),
  action VARCHAR(100), -- 'tender_created', 'quote_uploaded', 'po_approved', etc
  entity_type VARCHAR(50), -- 'tender', 'quote', 'po', 'payment'
  entity_id INT,
  
  old_value TEXT, -- JSON
  new_value TEXT, -- JSON
  
  ip_address VARCHAR(45),
  user_agent TEXT,
  
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  INDEX idx_user_id (user_id),
  INDEX idx_entity_type (entity_type),
  INDEX idx_timestamp (timestamp)
);
```

#### 8. Branches Table
```sql
CREATE TABLE branches (
  id SERIAL PRIMARY KEY,
  branch_name VARCHAR(255) NOT NULL,
  branch_code VARCHAR(50) UNIQUE,
  location VARCHAR(255),
  region VARCHAR(100), -- Kalimantan Timur, Jawa, etc
  contact_person VARCHAR(255),
  contact_phone VARCHAR(20),
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  INDEX idx_branch_code (branch_code)
);
```

### Database Indices & Performance Optimization

```sql
-- Critical indices for query performance
CREATE INDEX idx_quotes_tender_vendor ON quotes(tender_id, vendor_id);
CREATE INDEX idx_payments_po_vendor ON payments(po_id, vendor_id);
CREATE INDEX idx_audit_timestamp ON audit_logs(timestamp DESC);

-- Full-text search (optional)
ALTER TABLE tenders ADD COLUMN search_vector tsvector;
CREATE INDEX idx_tenders_search ON tenders USING gin(search_vector);
```

---

## API SPECIFICATIONS

### Base URL
```
Development: http://localhost:3000/api/v1
Production: https://procurement.kmuholding.com/api/v1
```

### Authentication

All endpoints require JWT token in header:
```
Authorization: Bearer <jwt_token>
```

**JWT Claims:**
```json
{
  "userId": 1,
  "email": "user@kmu.co.id",
  "role": "procurement",
  "userType": "internal",
  "vendorId": null,
  "branchId": 2,
  "iat": 1625097600,
  "exp": 1625184000
}
```

### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Detailed error description",
    "details": {}
  }
}
```

### API Endpoints

#### AUTH ENDPOINTS

**POST /auth/register**
```
Register new vendor

Request:
{
  "company_name": "PT Medik Jaya",
  "email": "contact@medikjaya.com",
  "password": "securePass123",
  "phone": "021-123456",
  "business_type": "alkes",
  "tax_id": "12.345.678.9-123.000"
}

Response (201):
{
  "success": true,
  "data": {
    "vendor_id": 42,
    "email": "contact@medikjaya.com",
    "status": "pending", // requires approval
    "message": "Registration successful. Awaiting admin approval."
  }
}
```

**POST /auth/login**
```
Login user

Request:
{
  "email": "user@kmu.co.id",
  "password": "password123"
}

Response (200):
{
  "success": true,
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": 1,
      "email": "user@kmu.co.id",
      "role": "procurement",
      "full_name": "Budi Santoso"
    }
  }
}

Response (401):
{
  "success": false,
  "error": {
    "code": "INVALID_CREDENTIALS",
    "message": "Email or password incorrect"
  }
}
```

**POST /auth/logout**
```
Logout (invalidate token)

Response (200):
{
  "success": true,
  "message": "Logged out successfully"
}
```

---

#### TENDER ENDPOINTS

**POST /tenders**
```
Create new tender (Internal only)

Request:
{
  "title": "Ultrasound Machine - 2D/3D",
  "description": "Mobile ultrasound for emergency dept",
  "category": "alkes",
  "sub_category": "imaging",
  "specifications": {
    "type": "2D/3D Color Doppler",
    "power_supply": "220V AC",
    "warranty": "2 years",
    "certification": "CE, FDA"
  },
  "budget_min": 400000000,
  "budget_max": 600000000,
  "bid_closing_date": "2025-06-30T23:59:59Z",
  "expected_delivery_date": "2025-08-15",
  "evaluation_criteria": {
    "price": {"weight": 25, "type": "numeric"},
    "quality": {"weight": 20, "type": "text"},
    "local_presence": {"weight": 15, "type": "boolean"},
    "maintenance": {"weight": 20, "type": "text"},
    "user_need": {"weight": 20, "type": "text"}
  }
}

Response (201):
{
  "success": true,
  "data": {
    "tender_id": 15,
    "tender_number": "TND-2025-0015",
    "status": "draft",
    "created_at": "2025-06-01T10:30:00Z"
  }
}
```

**GET /tenders**
```
List all tenders (with filters)

Query Parameters:
?status=published&category=alkes&page=1&limit=20

Response (200):
{
  "success": true,
  "data": {
    "tenders": [
      {
        "tender_id": 15,
        "tender_number": "TND-2025-0015",
        "title": "Ultrasound Machine",
        "category": "alkes",
        "status": "published",
        "bid_closing_date": "2025-06-30T23:59:59Z",
        "total_bids": 5,
        "sla_days_remaining": 21
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 47
    }
  }
}
```

**GET /tenders/{tender_id}**
```
Get tender details

Response (200):
{
  "success": true,
  "data": {
    "tender_id": 15,
    "tender_number": "TND-2025-0015",
    "title": "Ultrasound Machine",
    "description": "...",
    "specifications": {...},
    "status": "published",
    "bid_closing_date": "2025-06-30T23:59:59Z",
    "total_bids": 5,
    "evaluation_criteria": {...}
  }
}
```

**PATCH /tenders/{tender_id}**
```
Update tender (if still in draft)

Request:
{
  "title": "Updated title",
  "bid_closing_date": "2025-07-15T23:59:59Z"
}

Response (200): Updated tender object
```

**POST /tenders/{tender_id}/publish**
```
Publish tender (make visible to vendors)

Response (200):
{
  "success": true,
  "data": {
    "tender_id": 15,
    "status": "published",
    "published_at": "2025-06-01T11:00:00Z"
  }
}
```

---

#### QUOTE ENDPOINTS

**POST /quotes**
```
Submit quote for tender (Vendor only)

Form Data (multipart/form-data):
- tender_id: 15
- document: <binary file> (PDF/Word/Image)
- additional_notes: "Optional notes about the quote"

Response (201):
{
  "success": true,
  "data": {
    "quote_id": 42,
    "tender_id": 15,
    "vendor_id": 5,
    "document_url": "s3://bucket/quotes/TND-2025-0015-V5-R1.pdf",
    "upload_date": "2025-06-10T14:30:00Z",
    "status": "submitted",
    "extraction_status": "processing", // AI extraction in progress
    "revision_number": 1
  }
}
```

**GET /quotes/{quote_id}**
```
Get quote details (with extracted data)

Response (200):
{
  "success": true,
  "data": {
    "quote_id": 42,
    "tender_id": 15,
    "vendor_id": 5,
    "vendor_name": "PT Medik Jaya",
    "document_url": "...",
    "extracted_data": {
      "price": 500000000,
      "currency": "IDR",
      "delivery_days": 30,
      "delivery_location": "Jakarta",
      "testing_procedure": "2-hour functional test",
      "training_hours": 8,
      "training_days": 2,
      "commissioning_days": 1,
      "local_support": true,
      "sparepart_availability": "excellent",
      "confidence_score": 0.95
    },
    "calculated_score": 385,
    "recommendation": "alternatif",
    "requires_human_review": false,
    "status": "extracted"
  }
}
```

**GET /tenders/{tender_id}/quotes**
```
List all quotes for a tender (Internal only)

Query Parameters:
?sorted_by=score&order=desc&include_scores=true

Response (200):
{
  "success": true,
  "data": {
    "tender_id": 15,
    "total_quotes": 5,
    "quotes": [
      {
        "quote_id": 45,
        "vendor_name": "PT Medik Jaya",
        "price": 480000000,
        "delivery_days": 30,
        "calculated_score": 410,
        "recommendation": "utama",
        "extracted_data": {...}
      },
      // ... more quotes ordered by score
    ]
  }
}
```

**POST /quotes/{quote_id}/revise**
```
Vendor revise quote (negotiate)

Form Data:
- document: <binary file>
- negotiation_notes: "Reduced price per your request"

Response (201):
{
  "success": true,
  "data": {
    "quote_id": 42,
    "revision_number": 2,
    "status": "revised",
    "previous_extraction": {...},
    "new_extraction": {...},
    "change_summary": "Price reduced from 500M to 480M"
  }
}
```

**POST /quotes/{quote_id}/manual-review**
```
Trigger manual review (if AI uncertain)

Request:
{
  "review_notes": "AI could not extract price. Please verify."
}

Response (201):
{
  "success": true,
  "data": {
    "quote_id": 42,
    "review_status": "flagged_for_human_review",
    "assigned_to_user": 1,
    "priority": "high"
  }
}
```

---

#### SCORING & SELECTION ENDPOINTS

**POST /tenders/{tender_id}/calculate-scores**
```
Trigger AI scoring for all quotes in tender

Request:
{
  "override_medical_factors": false
}

Response (200):
{
  "success": true,
  "data": {
    "tender_id": 15,
    "scoring_timestamp": "2025-06-15T10:00:00Z",
    "quotes_scored": 5,
    "results": [
      {
        "quote_id": 45,
        "vendor_name": "PT Medik Jaya",
        "calculated_score": 410,
        "recommendation": "utama",
        "score_breakdown": {
          "price": 125,
          "quality": 95,
          "local_presence": 75,
          "maintenance": 80,
          "user_need": 35
        }
      },
      // ... more results
    ]
  }
}
```

**POST /tenders/{tender_id}/select-vendor**
```
Select winning vendor & create PO

Request:
{
  "quote_id": 45,
  "override_reason": "Medical team prefers superior training program",
  "medical_factor_override": true
}

Response (201):
{
  "success": true,
  "data": {
    "po_id": 100,
    "po_number": "PO-2025-0100",
    "tender_id": 15,
    "vendor_id": 5,
    "status": "draft",
    "created_at": "2025-06-15T10:30:00Z",
    "next_step": "Send for signature"
  }
}
```

---

#### PURCHASE ORDER ENDPOINTS

**GET /pos/{po_id}**
```
Get PO details

Response (200):
{
  "success": true,
  "data": {
    "po_id": 100,
    "po_number": "PO-2025-0100",
    "vendor_name": "PT Medik Jaya",
    "po_amount": 500000000,
    "po_date": "2025-06-15",
    "delivery_date": "2025-07-15",
    "status": "issued",
    "payment_milestones": [
      {
        "milestone": "DP",
        "percentage": 30,
        "amount": 150000000,
        "trigger": "PO_ISSUED",
        "status": "pending"
      },
      {
        "milestone": "Delivery",
        "percentage": 40,
        "amount": 200000000,
        "trigger": "GOODS_RECEIVED",
        "status": "pending"
      },
      {
        "milestone": "Testing Passed",
        "percentage": 20,
        "amount": 100000000,
        "trigger": "QC_APPROVED",
        "status": "pending"
      },
      {
        "milestone": "Training+Commission",
        "percentage": 10,
        "amount": 50000000,
        "trigger": "COMMISSIONED",
        "status": "pending"
      }
    ],
    "testing_required": true,
    "training_required": true,
    "commissioning_required": true,
    "signatures": {
      "vendor_signed": false,
      "po_signed": true,
      "signed_at": "2025-06-15T11:00:00Z"
    }
  }
}
```

**POST /pos/{po_id}/send-to-vendor**
```
Send PO to vendor for signature

Response (200):
{
  "success": true,
  "data": {
    "po_id": 100,
    "status": "sent_for_signature",
    "vendor_email": "contact@medikjaya.com",
    "signature_link": "https://procurement.kmuholding.com/sign/PO-2025-0100",
    "signature_deadline": "2025-06-22"
  }
}
```

**POST /pos/{po_id}/vendor-signature**
```
Vendor sign PO (via signature link)

Request:
{
  "signature_image_url": "s3://bucket/signatures/PO-100-vendor.png"
}

Response (200):
{
  "success": true,
  "data": {
    "po_id": 100,
    "status": "acknowledged",
    "vendor_signed_at": "2025-06-18T09:30:00Z",
    "next_step": "PO awaiting delivery"
  }
}
```

**POST /pos/{po_id}/mark-delivered**
```
Mark PO as delivered (trigger BAPB)

Request:
{
  "delivery_date": "2025-07-15",
  "goods_condition": "good",
  "grn_number": "BAPB-2025-001"
}

Response (200):
{
  "success": true,
  "data": {
    "po_id": 100,
    "status": "delivered",
    "delivery_date": "2025-07-15",
    "next_milestone": "Testing",
    "payment_ready": true,
    "payment_amount": 200000000
  }
}
```

---

#### PAYMENT ENDPOINTS

**GET /payments/po/{po_id}**
```
Get payment schedule for PO

Response (200):
{
  "success": true,
  "data": {
    "po_id": 100,
    "po_number": "PO-2025-0100",
    "vendor_name": "PT Medik Jaya",
    "total_po_amount": 500000000,
    "payments": [
      {
        "payment_id": 1,
        "milestone_type": "DP",
        "milestone_percentage": 30,
        "payment_amount": 150000000,
        "status": "paid",
        "payment_date": "2025-06-16",
        "payment_reference": "BCA-20250616-001"
      },
      {
        "payment_id": 2,
        "milestone_type": "delivery",
        "milestone_percentage": 40,
        "payment_amount": 200000000,
        "status": "approved",
        "three_way_match": true,
        "approval_date": "2025-07-16"
      },
      // ... more payments
    ]
  }
}
```

**POST /payments**
```
Create payment request

Request:
{
  "po_id": 100,
  "milestone_type": "delivery",
  "invoice_number": "INV-2025-001",
  "invoice_amount": 200000000,
  "invoice_document_url": "s3://bucket/invoices/INV-2025-001.pdf"
}

Response (201):
{
  "success": true,
  "data": {
    "payment_id": 2,
    "po_id": 100,
    "status": "submitted",
    "three_way_match_status": "in_progress",
    "approval_required": true
  }
}
```

**POST /payments/{payment_id}/approve**
```
Approve payment (Finance role)

Request:
{
  "approval_notes": "PO-BAPB-Invoice matched. Ready to process."
}

Response (200):
{
  "success": true,
  "data": {
    "payment_id": 2,
    "status": "approved",
    "approved_by": "Kepala Bagian Keuangan",
    "approved_at": "2025-07-17T10:00:00Z",
    "next_step": "Process payment in accounting system"
  }
}
```

---

#### DASHBOARD ENDPOINTS

**GET /dashboard/summary**
```
Get dashboard summary (Internal only)

Response (200):
{
  "success": true,
  "data": {
    "summary": {
      "total_tenders_active": 12,
      "total_tenders_closed": 45,
      "total_spend_ytd": 2500000000,
      "pending_approvals": 3,
      "overdue_deliveries": 1,
      "average_approval_time_days": 8
    },
    "sla_metrics": {
      "tenders_on_time": 42,
      "tenders_late": 3,
      "on_time_percentage": 93.3
    },
    "recent_activity": [
      {
        "timestamp": "2025-06-18T14:30:00Z",
        "action": "Quote submitted",
        "tender": "TND-2025-0015",
        "vendor": "PT Medik Jaya"
      }
    ]
  }
}
```

**GET /dashboard/vendor-performance**
```
Get vendor performance metrics

Query:
?period=last_12_months&sort_by=win_rate

Response (200):
{
  "success": true,
  "data": {
    "vendors": [
      {
        "vendor_id": 5,
        "vendor_name": "PT Medik Jaya",
        "total_bids": 12,
        "total_wins": 4,
        "win_rate": 33.3,
        "average_score": 395,
        "average_delivery_days": 28,
        "support_rating": 4.5
      }
    ]
  }
}
```

---

## GEMINI AI INTEGRATION

### Document Processing Pipeline

#### Step 1: Upload & Validation
```
Vendor Upload → File Validation → S3/Local Storage
   ↓
   └─ Check: PDF/Word/Image? Valid format? Size <50MB?
   └─ Store with metadata: tender_id, vendor_id, filename, timestamp
```

#### Step 2: Gemini Extraction Request
```javascript
// Backend service: gemini-extraction.js

const Anthropic = require("@anthropic-ai/sdk"); // Using Claude instead since user prefers

async function extractQuoteData(documentPath, documentType) {
  const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY
  });
  
  // Read document and encode to base64
  const fs = require("fs");
  const fileData = fs.readFileSync(documentPath);
  const base64Data = fileData.toString("base64");
  
  const prompt = `
    You are an expert procurement analyst for a medical equipment procurement system.
    
    A vendor has submitted a quote/proposal. Your task is to extract the following structured data from the document:
    
    INSTRUCTIONS:
    1. Read the entire document carefully
    2. Extract exact values where possible (numbers, dates)
    3. For text descriptions, provide clear, concise summaries
    4. If a field is not mentioned in the document, return null
    5. For confidence, rate 0-1 where 1 is certain the value is correct
    6. Flag any ambiguities or conflicting information
    
    FIELDS TO EXTRACT:
    {
      "price": {
        "value": number (in IDR),
        "currency": string ("IDR" or other),
        "unit_price": number (if per unit),
        "includes_tax": boolean or null,
        "confidence": 0-1
      },
      "delivery": {
        "delivery_days": number,
        "delivery_location": string,
        "includes_installation": boolean or null,
        "delivery_condition": string (e.g., "FOB", "CIF"),
        "confidence": 0-1
      },
      "testing": {
        "testing_procedure": string (description of how equipment will be tested),
        "testing_duration_hours": number or null,
        "testing_location": string or null,
        "equipment_warranty": string or null,
        "confidence": 0-1
      },
      "training": {
        "training_required": boolean,
        "training_scope": string (detailed description),
        "training_duration_hours": number or null,
        "training_duration_days": number or null,
        "trainee_capacity": number or null,
        "training_location": string or null,
        "confidence": 0-1
      },
      "commissioning": {
        "commissioning_required": boolean,
        "commissioning_procedure": string,
        "commissioning_duration_hours": number or null,
        "commissioning_duration_days": number or null,
        "on_site_support": boolean or null,
        "confidence": 0-1
      },
      "local_support": {
        "has_local_office": boolean or null,
        "local_office_location": string or null,
        "local_technician_available": boolean or null,
        "response_time_hours": number or null,
        "confidence": 0-1
      },
      "spareparts": {
        "sparepart_availability": string ("excellent", "good", "fair", "limited"),
        "sparepart_price_comment": string,
        "stock_location": string or null,
        "delivery_time": string (e.g., "same day", "3 days"),
        "confidence": 0-1
      },
      "additional_info": {
        "brand": string or null,
        "country_of_origin": string or null,
        "certifications": [string],
        "payment_terms": string (e.g., "Net 30", "50% DP, 50% upon delivery"),
        "warranty_months": number or null,
        "notes": string or null
      },
      "quality_assessment": {
        "overall_quality_impression": string,
        "technical_specs_completeness": "complete" | "partial" | "missing",
        "document_clarity": "clear" | "confusing" | "very_confusing"
      },
      "extraction_summary": {
        "confidence_score": 0-1 (overall confidence),
        "missing_critical_fields": [string],
        "ambiguous_sections": [string],
        "requires_human_review": boolean
      }
    }
    
    RESPOND WITH PURE JSON ONLY, NO MARKDOWN FORMATTING.
  `;
  
  try {
    const message = await client.messages.create({
      model: "claude-opus-4-20250514",
      max_tokens: 2000,
      messages: [
        {
          role: "user",
          content: [
            {
              type: "image",
              source: {
                type: "base64",
                media_type: getMimeType(documentType),
                data: base64Data
              }
            },
            {
              type: "text",
              text: prompt
            }
          ]
        }
      ]
    });
    
    const responseText = message.content[0].type === "text" 
      ? message.content[0].text 
      : "";
    
    const extractedData = JSON.parse(responseText);
    
    return {
      success: true,
      extractedData,
      confidence: extractedData.extraction_summary.confidence_score,
      requiresReview: extractedData.extraction_summary.requires_human_review
    };
    
  } catch (error) {
    console.error("Gemini extraction error:", error);
    return {
      success: false,
      error: error.message,
      requiresReview: true // Always require human review if AI fails
    };
  }
}

function getMimeType(docType) {
  const mimeTypes = {
    "pdf": "application/pdf",
    "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "doc": "application/msword",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "tiff": "image/tiff"
  };
  return mimeTypes[docType.toLowerCase()] || "application/octet-stream";
}

module.exports = { extractQuoteData };
```

#### Step 3: Data Validation
```javascript
// validation-rules.js

const ValidationRules = {
  price: {
    min: 100000, // IDR minimum
    max: 10000000000, // IDR maximum (10B)
    required: true,
    validate: (value) => value >= this.min && value <= this.max
  },
  delivery_days: {
    min: 1,
    max: 180,
    required: true,
    validate: (value) => Number.isInteger(value) && value >= this.min && value <= this.max
  },
  training_duration_hours: {
    min: 0,
    max: 200,
    required: false,
    validate: (value) => value === null || (Number.isInteger(value) && value >= this.min && value <= this.max)
  },
  // ... more rules
};

function validateExtractedData(data) {
  const errors = [];
  const warnings = [];
  
  for (const [field, rules] of Object.entries(ValidationRules)) {
    const value = data[field];
    
    if (rules.required && !value) {
      errors.push(`${field} is required but missing`);
    }
    
    if (value && !rules.validate(value)) {
      warnings.push(`${field} value ${value} seems unusual. Human review recommended.`);
    }
  }
  
  return {
    valid: errors.length === 0,
    errors,
    warnings,
    requiresHumanReview: errors.length > 0 || warnings.length > 0
  };
}

module.exports = { ValidationRules, validateExtractedData };
```

#### Step 4: Database Storage
```javascript
// Async function to save extracted data

async function saveExtractedQuote(quoteId, extractedData, confidenceScore) {
  const db = require("./database");
  
  const query = `
    UPDATE quotes
    SET 
      extracted_data = $1,
      requires_human_review = $2,
      updated_at = NOW()
    WHERE id = $3
  `;
  
  const requiresReview = confidenceScore < 0.8 || extractedData.extraction_summary.requires_human_review;
  
  return db.query(query, [
    JSON.stringify(extractedData),
    requiresReview,
    quoteId
  ]);
}
```

### Prompt Engineering for Better Extraction

**Key Principles:**
1. **Be specific** - Tell Gemini exactly what to extract
2. **Provide format** - JSON schema shows expected output
3. **Handle ambiguity** - Return null for missing fields, flag uncertainties
4. **Validate confidence** - Rate each extraction 0-1
5. **Fallback handling** - If AI uncertain, flag for human review

**Example refinements by document type:**

```javascript
// For medical equipment manuals
const medicalEquipmentPrompt = `
  Extract technical specifications that matter for medical procurement:
  - Power requirements (voltage, frequency, maximum load)
  - Connectivity options (WiFi, Ethernet, USB)
  - Accessories included vs. extra cost
  - Regulatory certifications (ISO, CE Mark, FDA approval status)
`;

// For price quotes
const priceQuotePrompt = `
  Look carefully for all pricing information:
  - Unit price vs. total price
  - Currency conversion if applicable
  - Hidden costs (installation, training, shipping)
  - Volume discounts if mentioned
  - Payment terms and conditions
`;
```

---

## UI/UX SPECIFICATIONS

### Page Structure Overview

```
VENDOR PORTAL                          INTERNAL PORTAL
├─ Dashboard                           ├─ Dashboard
│  ├─ Tenders Available                │  ├─ Summary (SLA, spend, approvals)
│  ├─ My Bids                          │  ├─ Active Tenders
│  └─ Order Status                     │  └─ Recent Activity
│                                       │
├─ Browse Tenders                      ├─ Tender Management
│  ├─ Filter by category               │  ├─ Create Tender
│  ├─ View Specifications              │  ├─ Edit/Publish
│  └─ Download SPPH                     │  └─ Close Tender
│                                       │
├─ Submit Quote                        ├─ Quote Evaluation
│  ├─ Upload Document                  │  ├─ View Tabulation
│  ├─ Add Notes                        │  ├─ AI Scoring Results
│  └─ Track Status                     │  ├─ Manual Override
│                                       │  └─ Select Winner
├─ Negotiate                            │
│  ├─ Revise Quote                     ├─ PO Management
│  └─ Counter-offer                    │  ├─ Generate PO
│                                       │  ├─ Send for Signature
├─ Track Orders                        │  └─ View Status
│  ├─ View PO                          │
│  ├─ Update Delivery Status           ├─ Payment Tracking
│  └─ Upload Invoice                   │  ├─ Payment Schedule
│                                       │  ├─ 3-Way Match
├─ Account Settings                    │  └─ Approve Payments
│  ├─ Profile                          │
│  ├─ Bank Details                     ├─ Reports & Analytics
│  └─ Certifications                   │  ├─ Spend Analysis
│                                       │  ├─ Vendor Performance
└─ Notifications                       │  └─ SLA Compliance
                                       │
                                       ├─ Audit Log
                                       │
                                       └─ Settings
                                          ├─ Vendor Management
                                          ├─ Approval Rules
                                          └─ User Management
```

### Key UI Components

#### 1. Quote Tabulation Table (Internal)
```
Tender: TND-2025-0015 - Ultrasound Machine
Closing Date: 2025-06-30 | Status: Open (21 days remaining)

┌─────────┬──────────┬──────────┬────────┬─────────┬────────────┬──────────┐
│ Vendor  │ Price    │ Delivery │ Test   │ Training│ Commission │ Score    │
├─────────┼──────────┼──────────┼────────┼─────────┼────────────┼──────────┤
│ V1      │ 500M IDR │ 30 days  │ 2h     │ 2 days  │ 1 day      │ 385 ⚠️  │
│ V2      │ 480M IDR │ 60 days  │ 3h     │ 3 days  │ 2 days     │ 365 ⚠️  │
│ V3      │ 520M IDR │ 20 days  │ 2h     │ 1 day   │ 1 day      │ 410 ✅  │
└─────────┴──────────┴──────────┴────────┴─────────┴────────────┴──────────┘

[Legends]
✅ Rekomendasi Utama (≥400)
⚠️  Rekomendasi Alternatif (350-399)
❌ Tidak Direkomendasikan (<300)

[Actions]
- Click row to view details
- [Select Winner] button for top candidate
- [Manual Review] for AI uncertain extractions
```

#### 2. Payment Milestone Tracker
```
PO: PO-2025-0100 | Vendor: PT Medik Jaya | Amount: 500M IDR

Timeline:
├─ DP (30%)
│  Amount: 150M IDR
│  Status: ✅ PAID (2025-06-16)
│  Reference: BCA-20250616-001
│
├─ Delivery (40%)
│  Amount: 200M IDR
│  Status: ⏳ APPROVED (awaiting payment processing)
│  Trigger: Barang diterima (BAPB-2025-001)
│  Approval Date: 2025-07-17
│
├─ Testing (20%)
│  Amount: 100M IDR
│  Status: ⏳ PENDING
│  Trigger: QC passed (expected 2025-07-22)
│
└─ Training+Commission (10%)
   Amount: 50M IDR
   Status: ⏳ PENDING
   Trigger: All activities completed (expected 2025-07-29)

Total Paid: 150M IDR (30%)
Total Outstanding: 350M IDR (70%)
```

#### 3. SLA Countdown Widget
```
ACTIVE TENDERS

┌─────────────────────────────────────────┐
│ TND-2025-0015: Ultrasound Machine       │
│ Posted: 2025-06-01                      │
│ Closing: 2025-06-30                     │
│ Days Remaining: 21 days 🟢               │
│ Status: 5 quotes submitted              │
│ Action: [View Quotes] [Score All]       │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ TND-2025-0012: Lab Equipment            │
│ Posted: 2025-05-20                      │
│ Closing: 2025-06-19                     │
│ Days Remaining: 0 days 🔴 (CLOSED)      │
│ Status: 8 quotes | Scoring complete    │
│ Action: [Select Winner]                 │
└─────────────────────────────────────────┘
```

### Responsive Design Breakpoints

```css
/* Mobile (320px - 640px) */
@media (max-width: 640px) {
  - Stack layout vertically
  - Simplified tables (carousel view)
  - Full-width buttons
  - Touch-friendly (44px min size)
}

/* Tablet (641px - 1024px) */
@media (max-width: 1024px) {
  - Two-column layout
  - Collapsible sections
  - Responsive tables
}

/* Desktop (1025px+) */
@media (min-width: 1025px) {
  - Multi-column layouts
  - Side-by-side comparisons
  - Full data visibility
}
```

---

## WORKFLOW & PROCESS DESIGN

### End-to-End Process Flow

```
┌──────────────────────────────────────────────────────────────────┐
│                    ANNUAL PLANNING PHASE                         │
└──────────────────────────────────────────────────────────────────┘
  Q1: All branches submit yearly needs
      ↓
  Finance compiles budget
      ↓
  Categorize by type (alkes, obat, jasa)
      ↓
  Master list created (data in system)

┌──────────────────────────────────────────────────────────────────┐
│                    TENDER EXECUTION PHASE                        │
└──────────────────────────────────────────────────────────────────┘
  
  STEP 1: Create Tender
  ┌─────────────────────────────────────────┐
  │ Procurement Team (Internal)             │
  │ ├─ Post tender with specs               │
  │ ├─ Set bid closing date                 │
  │ ├─ Define evaluation criteria           │
  │ └─ Publish to vendor portal             │
  └─────────────────────────────────────────┘
           ↓
  
  STEP 2: Vendor Bidding
  ┌─────────────────────────────────────────┐
  │ Vendors (External)                      │
  │ ├─ Login & view tender                  │
  │ ├─ Upload quote (any format)            │
  │ ├─ Can revise until closing date        │
  │ └─ Notifications via email              │
  └─────────────────────────────────────────┘
           ↓ (auto-triggered when bid uploaded)
  
  STEP 3: AI Extraction & Tabulation
  ┌─────────────────────────────────────────┐
  │ Gemini AI (Automated)                   │
  │ ├─ Read document (any format)           │
  │ ├─ Extract structured data              │
  │ ├─ Validate data (sanity checks)        │
  │ └─ Store in database                    │
  │ ↓ (if confidence <80%)                  │
  │ └─ Flag for human review                │
  └─────────────────────────────────────────┘
           ↓
  
  STEP 4: Scoring
  ┌─────────────────────────────────────────┐
  │ Scoring Engine (Automated)              │
  │ ├─ Calculate weighted scores            │
  │ ├─ Apply evaluation criteria            │
  │ ├─ Add medical factors (if applicable)  │
  │ ├─ Rank quotes (best to worst)          │
  │ └─ Generate recommendations             │
  └─────────────────────────────────────────┘
           ↓
  
  STEP 5: Evaluation & Selection
  ┌─────────────────────────────────────────┐
  │ Procurement Team (Internal)             │
  │ ├─ Review scoring results               │
  │ ├─ Check flagged items (human review)   │
  │ ├─ Can override score if needed         │
  │ │  (medical factors, local support)     │
  │ ├─ Select winning vendor                │
  │ └─ Route for approvals                  │
  └─────────────────────────────────────────┘
           ↓
  
  STEP 6: Approval Workflow
  ┌─────────────────────────────────────────┐
  │ Multi-level Approval (≤2 week SLA)      │
  │ ├─ Finance review: budget check         │
  │ │  └─ Auto-approve if ≤ threshold       │
  │ │  └─ Else route to Director            │
  │ ├─ Director approval: strategy check    │
  │ │  └─ If ≤ threshold: finance signs off │
  │ │  └─ If > threshold: director approves │
  │ └─ Status tracking (real-time)          │
  │    └─ Alerts if SLA breached            │
  └─────────────────────────────────────────┘
           ↓ (if approved)
  
  STEP 7: PO Generation & Signature
  ┌─────────────────────────────────────────┐
  │ System (Automated)                      │
  │ ├─ Generate PO document                 │
  │ ├─ Include all terms:                   │
  │ │  - Price, delivery, testing           │
  │ │  - Training, commissioning            │
  │ │  - Payment milestones (DP + 4 parts)  │
  │ ├─ Send to vendor for e-signature       │
  │ └─ Internal team signs                  │
  └─────────────────────────────────────────┘
           ↓
  
  STEP 8: Delivery & QC
  ┌─────────────────────────────────────────┐
  │ Vendor & Receiving Unit                 │
  │ ├─ Vendor delivers                      │
  │ ├─ Unit receives & QC inspection        │
  │ ├─ Generate BAPB (BAPB (Berita Acara Penerimaan Barang))   │
  │ └─ System triggers payment milestone #2 │
  └─────────────────────────────────────────┘
           ↓
  
  STEP 9: Testing & Commissioning
  ┌─────────────────────────────────────────┐
  │ Clinical Team & Vendor                  │
  │ ├─ Functional testing (per PO spec)     │
  │ ├─ If passed: QC approval               │
  │ ├─ Training execution                   │
  │ ├─ Commissioning                        │
  │ └─ System triggers payment milestone #3 │
  └─────────────────────────────────────────┘
           ↓
  
  STEP 10: Payment Processing
  ┌─────────────────────────────────────────┐
  │ Finance (Milestone-based)               │
  │ ├─ DP (30%) → Paid on PO issuance       │
  │ ├─ Delivery (40%) → On BAPB received     │
  │ ├─ Testing (20%) → On QC passed         │
  │ ├─ Training+Comm (10%) → On completion  │
  │ │                                        │
  │ For each payment:                       │
  │ ├─ 3-way match: PO ↔ BAPB ↔ Invoice     │
  │ ├─ Approval workflow                    │
  │ ├─ Process via accounting system        │
  │ └─ Update inventory                     │
  └─────────────────────────────────────────┘
           ↓
  
  STEP 11: Closure & Analytics
  ┌─────────────────────────────────────────┐
  │ System & Procurement                    │
  │ ├─ Mark PO as completed                 │
  │ ├─ Archive all documents                │
  │ ├─ Update vendor metrics:               │
  │ │  - Performance rating                 │
  │ │  - Delivery time                      │
  │ │  - Quality feedback                   │
  │ ├─ Generate audit trail                 │
  │ └─ Report for analytics                 │
  └─────────────────────────────────────────┘
```

### Approval Workflow Decision Tree

```
PO Amount: X IDR

Is X ≤ 100M?
├─ YES → Finance auto-approves ✅
│        └─ Sent directly for vendor signature
│
└─ NO → Route to Director
         ├─ Director reviews
         ├─ If approved ✅ → Vendor signature
         ├─ If rejected ❌ → Back to procurement
         │                  └─ Request revision or new bidding
         └─ If pending ⏳ → Escalation alert after 3 days

SLA: Decision should be made within 2 weeks from tender closing
```

---

## SECURITY & COMPLIANCE

### Authentication & Authorization

**User Roles & Permissions Matrix:**

| Feature | Vendor | Procurement | Finance | Director | Audit |
|---------|--------|------------|---------|----------|-------|
| View own quotes | ✅ | - | - | - | - |
| View all tenders | ✅ | ✅ | - | - | - |
| Create tender | - | ✅ | - | ✅ | - |
| Review quotes | - | ✅ | - | - | - |
| Approve quotes | - | ✅ | ✅ | ✅ | - |
| View payment status | ✅ | ✅ | ✅ | ✅ | ✅ |
| Approve payments | - | - | ✅ | ✅ | - |
| View audit logs | - | - | - | - | ✅ |
| Manage vendors | - | - | - | ✅ | - |

**Implementation:**
```javascript
// middleware/authorize.js

const authorize = (requiredRoles) => {
  return (req, res, next) => {
    const userRole = req.user.role;
    
    if (!requiredRoles.includes(userRole)) {
      return res.status(403).json({
        error: "Unauthorized - insufficient permissions"
      });
    }
    
    next();
  };
};

// Usage
router.post('/tenders', 
  authenticate,
  authorize(['procurement', 'director']),
  createTender
);
```

### Data Security

**Encryption:**
- **Transport:** HTTPS/TLS 1.3 (all endpoints)
- **At Rest:** PostgreSQL encryption (pgcrypto)
- **Sensitive Fields:** Password hashing (bcrypt), credit card tokens (tokenization)

**Password Policy:**
- Minimum 12 characters
- Must include: uppercase, lowercase, numbers, special characters
- Change every 90 days
- No reuse of last 5 passwords

**Session Management:**
- JWT tokens with 24-hour expiration
- Refresh tokens with 7-day expiration
- Secure httpOnly cookies (no JavaScript access)
- CSRF protection via double-submit cookies

### Audit Logging

**What gets logged:**
```sql
-- Every action is recorded
- User login/logout
- Document upload
- Data extraction by AI
- Quote scoring
- PO approval
- Payment processing
- User access to sensitive data
- Configuration changes
```

**Example audit log entry:**
```json
{
  "timestamp": "2025-06-15T10:30:00Z",
  "user_id": 5,
  "user_email": "budi@kmu.co.id",
  "action": "po_approved",
  "entity_type": "purchase_order",
  "entity_id": 100,
  "old_value": {"status": "draft"},
  "new_value": {"status": "issued"},
  "ip_address": "192.168.1.100",
  "user_agent": "Mozilla/5.0..."
}
```

### Compliance Considerations

**Data Privacy (GDPR/Local):**
- User data retention: 7 years (per Indonesian regulations)
- Right to be forgotten: Manual process (contact admin)
- Data export: Available via API endpoint

**Medical Equipment Standards:**
- Reference: WHO procurement guidelines
- Ensure all tenders include certification requirements
- Track compliance history per vendor

**Audit Trail:**
- 100% digital record of all transactions
- Immutable logs (append-only database)
- Regular compliance audits (quarterly)

---

## IMPLEMENTATION CHECKLIST

### Phase 1: Foundation (Week 1)

- [ ] Setup development environment
  - [ ] Node.js 18+ installed
  - [ ] PostgreSQL 13+ or SQLite for dev
  - [ ] Redis installed (optional for dev, required for prod)
  - [ ] Git repository initialized

- [ ] Database
  - [ ] Run migration scripts (see database schema above)
  - [ ] Create indexes
  - [ ] Seed initial data (branches, categories)
  - [ ] Verify schema integrity

- [ ] Backend skeleton
  - [ ] Express.js project structure
  - [ ] Environment variables (.env)
  - [ ] JWT authentication module
  - [ ] Database connection pooling
  - [ ] Error handling middleware

- [ ] Frontend skeleton
  - [ ] React project (Create React App or Vite)
  - [ ] Tailwind CSS setup
  - [ ] Basic routing structure
  - [ ] HTTP client setup (Axios)
  - [ ] Redux or Zustand state management

- [ ] Gemini AI Integration
  - [ ] API key setup
  - [ ] Document upload handler
  - [ ] Extraction function (see AI Integration section)
  - [ ] Test with sample documents

### Phase 2: Core Features (Week 2)

- [ ] Authentication & Authorization
  - [ ] User registration (vendor + internal)
  - [ ] Login/logout
  - [ ] Password reset
  - [ ] Role-based access control

- [ ] Tender Management (Internal)
  - [ ] Create tender form
  - [ ] Publish tender
  - [ ] View active/closed tenders
  - [ ] Dashboard with SLA countdown

- [ ] Quote Submission (Vendor)
  - [ ] Upload quote document
  - [ ] Document storage (S3/local)
  - [ ] Quote status tracking
  - [ ] Revision capability

- [ ] AI Extraction & Scoring
  - [ ] Gemini document processing pipeline
  - [ ] Data validation rules
  - [ ] Auto-scoring calculation
  - [ ] Tabulation view

### Phase 3: Workflow & Payments (Week 3)

- [ ] PO Generation
  - [ ] Auto-generate from selected quote
  - [ ] Digital signature flow
  - [ ] PDF export
  - [ ] Send to vendor

- [ ] Approval Workflow
  - [ ] Multi-level approval routing
  - [ ] Conditional approvals
  - [ ] SLA monitoring & escalation
  - [ ] Manual override capability

- [ ] Payment Tracking
  - [ ] Payment milestone schedule
  - [ ] 3-way match verification
  - [ ] Invoice processing
  - [ ] Payment approval workflow

- [ ] Notifications
  - [ ] Email notifications (bid closing soon, approval needed, payment ready)
  - [ ] In-app notifications
  - [ ] SMS alerts (for critical items)

### Phase 4: Polish & Deployment (Week 4)

- [ ] Testing
  - [ ] Unit tests (backend API endpoints)
  - [ ] Integration tests (workflows)
  - [ ] UI testing (vendor + internal portals)
  - [ ] Load testing (concurrent users)

- [ ] Documentation
  - [ ] API documentation (Swagger/OpenAPI)
  - [ ] User guides (vendor + internal)
  - [ ] Admin manual (system setup, troubleshooting)
  - [ ] Data backup/recovery procedures

- [ ] Deployment
  - [ ] Choose hosting (cloud or on-premise)
  - [ ] Configure CI/CD pipeline
  - [ ] SSL certificates
  - [ ] Database backups

- [ ] UAT (User Acceptance Testing)
  - [ ] With internal team (procurement, finance)
  - [ ] With sample vendors
  - [ ] Edge case testing
  - [ ] Performance verification

- [ ] Go-Live
  - [ ] Cutover plan
  - [ ] Support team training
  - [ ] 24/7 monitoring first week
  - [ ] Issue tracking & resolution

---

## TESTING STRATEGY

### Unit Tests

**Example: Scoring Calculation**
```javascript
// test/scoring.test.js

describe('Scoring Engine', () => {
  
  test('should calculate weighted score correctly', () => {
    const criteria = {
      price: { weight: 25, score: 100 },
      quality: { weight: 20, score: 90 },
      maintenance: { weight: 20, score: 80 },
      user_need: { weight: 20, score: 85 },
      brand: { weight: 15, score: 75 }
    };
    
    const expectedScore = (100 * 0.25) + (90 * 0.20) + (80 * 0.20) + (85 * 0.20) + (75 * 0.15);
    // = 25 + 18 + 16 + 17 + 11.25 = 87.25
    
    const actualScore = calculateScore(criteria);
    expect(actualScore).toBe(87.25);
  });
  
  test('should recommend "Utama" for score >= 400', () => {
    const score = 410;
    expect(getRecommendation(score)).toBe('utama');
  });
  
  test('should recommend "Tidak" for score < 300', () => {
    const score = 250;
    expect(getRecommendation(score)).toBe('tidak');
  });
});
```

### Integration Tests

**Example: Quote Upload to Scoring**
```javascript
// test/integration/quote-workflow.test.js

describe('Quote Submission to Scoring Workflow', () => {
  
  test('should extract, validate, and score a quote', async () => {
    // 1. Upload quote
    const uploadResponse = await request(app)
      .post('/api/v1/quotes')
      .attach('document', './test-fixtures/quote.pdf')
      .set('Authorization', `Bearer ${vendorToken}`)
      .expect(201);
    
    const quoteId = uploadResponse.body.data.quote_id;
    
    // 2. Wait for AI extraction (polling)
    let extractionComplete = false;
    let attempts = 0;
    
    while (!extractionComplete && attempts < 30) {
      await delay(1000); // wait 1 second
      const statusResponse = await request(app)
        .get(`/api/v1/quotes/${quoteId}`)
        .set('Authorization', `Bearer ${internalToken}`)
        .expect(200);
      
      if (statusResponse.body.data.extracted_data) {
        extractionComplete = true;
      }
      attempts++;
    }
    
    expect(extractionComplete).toBe(true);
    
    // 3. Verify scoring was calculated
    const scoreResponse = await request(app)
      .get(`/api/v1/quotes/${quoteId}`)
      .set('Authorization', `Bearer ${internalToken}`)
      .expect(200);
    
    expect(scoreResponse.body.data.calculated_score).toBeDefined();
    expect(scoreResponse.body.data.recommendation).toMatch(/utama|alternatif|pertimbangan|tidak/);
  });
});
```

### Performance Tests

```javascript
// test/performance/load-test.js

describe('Performance Tests', () => {
  
  test('should handle 50 simultaneous quote uploads', async () => {
    const startTime = Date.now();
    
    const uploads = Array(50).fill(null).map((_, i) =>
      request(app)
        .post('/api/v1/quotes')
        .attach('document', './test-fixtures/quote.pdf')
        .set('Authorization', `Bearer ${vendorToken}`)
    );
    
    const results = await Promise.all(uploads);
    const endTime = Date.now();
    
    const successCount = results.filter(r => r.status === 201).length;
    const duration = (endTime - startTime) / 1000;
    
    console.log(`✓ ${successCount}/50 uploads successful in ${duration}s`);
    expect(successCount).toBeGreaterThanOrEqual(45); // 90% success rate
    expect(duration).toBeLessThan(30); // complete in 30 seconds
  });
  
  test('API response time should be <2 seconds', async () => {
    const startTime = Date.now();
    
    await request(app)
      .get('/api/v1/tenders')
      .set('Authorization', `Bearer ${internalToken}`)
      .expect(200);
    
    const duration = Date.now() - startTime;
    expect(duration).toBeLessThan(2000);
  });
});
```

---

## DEPLOYMENT GUIDE

### Option A: Cloud Deployment (Recommended)

**Architecture: Heroku + Vercel + Supabase**

```
┌─────────────────┐
│ Vercel (Frontend)
│ - React SPA
│ - Auto-deploy from Git
│ - CDN globally
└────────┬────────┘
         │
         └──→ API → Heroku (Backend)
                    ├─ Node.js + Express
                    ├─ Auto-scale dynos
                    └─ Environment variables
                         │
                         └──→ Supabase (Database)
                              ├─ PostgreSQL
                              ├─ Backups
                              └─ Row-level security
```

**Step-by-step:**

1. **Prepare code for deployment**
   ```bash
   # Add Procfile for Heroku
   echo "web: npm start" > Procfile
   
   # Add .env template (no secrets)
   cp .env .env.example
   git add Procfile .env.example
   git commit -m "Add deployment config"
   ```

2. **Deploy Backend (Heroku)**
   ```bash
   # Install Heroku CLI
   # https://devcenter.heroku.com/articles/heroku-cli
   
   heroku login
   heroku create procurement-api
   
   # Set environment variables
   heroku config:set NODE_ENV=production
   heroku config:set DB_URL=<supabase-postgres-url>
   heroku config:set JWT_SECRET=<random-secret>
   heroku config:set GEMINI_API_KEY=<your-api-key>
   
   # Deploy
   git push heroku main
   
   # View logs
   heroku logs --tail
   ```

3. **Deploy Frontend (Vercel)**
   ```bash
   # Install Vercel CLI
   npm install -g vercel
   
   # Deploy
   vercel --prod
   
   # Configure environment variables in Vercel dashboard
   REACT_APP_API_URL=https://procurement-api.herokuapp.com/api/v1
   ```

4. **Setup Database (Supabase)**
   - Create Supabase project (https://supabase.com)
   - Get connection string
   - Run migrations:
   ```bash
   psql -U postgres -d <database> -f database/migrations/001-init.sql
   ```

### Option B: On-Premise Deployment

**Architecture: Windows Server / Linux Box**

```
┌───────────────────────────┐
│  Windows Server / Linux   │
├───────────────────────────┤
│ Node.js + Express (port 3000)
├───────────────────────────┤
│ PostgreSQL (port 5432)
├───────────────────────────┤
│ Redis (port 6379)
├───────────────────────────┤
│ Nginx Reverse Proxy (port 80/443)
├───────────────────────────┤
│ Static files (React SPA)
└───────────────────────────┘
```

**Step-by-step:**

1. **Server Setup (Linux)**
   ```bash
   # Update system
   sudo apt-get update && sudo apt-get upgrade
   
   # Install Node.js
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs
   
   # Install PostgreSQL
   sudo apt-get install -y postgresql postgresql-contrib
   
   # Install Redis
   sudo apt-get install -y redis-server
   
   # Install Nginx
   sudo apt-get install -y nginx
   ```

2. **Application Setup**
   ```bash
   # Create app directory
   sudo mkdir -p /var/www/procurement-api
   cd /var/www/procurement-api
   
   # Clone code
   git clone <your-repo> .
   
   # Install dependencies
   npm install --production
   
   # Create .env
   cp .env.example .env
   # Edit .env with server details
   
   # Setup PM2 (process manager)
   sudo npm install -g pm2
   pm2 start index.js --name "procurement-api"
   pm2 startup
   pm2 save
   ```

3. **Database Setup**
   ```bash
   sudo -u postgres createdb procurement
   sudo -u postgres psql procurement < database/migrations/001-init.sql
   ```

4. **Nginx Configuration**
   ```nginx
   # /etc/nginx/sites-available/procurement.conf
   
   server {
       listen 80;
       server_name procurement.kmuholding.com;
       
       # Redirect HTTP to HTTPS
       return 301 https://$server_name$request_uri;
   }
   
   server {
       listen 443 ssl http2;
       server_name procurement.kmuholding.com;
       
       ssl_certificate /etc/letsencrypt/live/procurement.kmuholding.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/procurement.kmuholding.com/privkey.pem;
       
       # Frontend
       location / {
           root /var/www/procurement-frontend/build;
           try_files $uri /index.html;
       }
       
       # Backend API
       location /api/ {
           proxy_pass http://localhost:3000/api/;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

5. **SSL Certificate (Let's Encrypt)**
   ```bash
   sudo apt-get install -y certbot python3-certbot-nginx
   sudo certbot certonly --standalone -d procurement.kmuholding.com
   sudo systemctl restart nginx
   ```

### Monitoring & Maintenance

```bash
# Check application status
pm2 status
pm2 logs procurement-api

# Database backups (daily)
# Add to crontab:
0 2 * * * pg_dump procurement > /backups/procurement-$(date +\%Y\%m\%d).sql

# Monitor system
sudo htop  # CPU, memory usage
df -h      # Disk space
nethogs    # Network traffic
```

---

## TROUBLESHOOTING & FAQ

### Common Issues

**Q: AI extraction failing for handwritten quotes**
A: Handwritten documents may have lower confidence scores. Upload high-resolution scans (300+ DPI). If still failing, flag for human review and process manually.

**Q: Payment approval stuck in workflow**
A: Check if all required documents (invoice, BAPB) are uploaded. Verify user permissions (Finance role). Check audit logs for rejection reason.

**Q: Vendor unable to login**
A: Verify vendor status is "approved" (not "pending"). Check email/password. Try password reset. Check if user account is linked to vendor company.

**Q: Database connection timeout**
A: Increase connection pool size in .env (`DB_POOL_MAX=10`). Check network/firewall. Verify database server is running.

---

## ROLLOUT PLAN

### Week 1: Internal Testing
- Internal team only (procurement, finance)
- Focus on tender creation & quote evaluation
- Identify bugs & UX issues

### Week 2: Vendor Testing  
- 5-10 trusted vendors test bidding
- Validate document upload & extraction
- Test end-to-end workflow

### Week 3: Beta Launch
- Open to all registered vendors
- Real tenders at small scale
- 24/7 support team on standby

### Week 4: Full Production
- All systems go live
- Complete migration from manual process
- Ongoing monitoring & optimization

---

## GLOSSARY

| Term | Definition |
|------|-----------|
| **IMT** | Informasi Kebutuhan Material / IMT/PP (Permintaan Pembelian) |
| **PO** | Purchase Order |
| **BAPB** | Berita Acara Penerimaan Barang |
| **DP** | Down Payment |
| **Pelunasan** | Final Payment |
| **Rekanan** | Registered supplier/vendor |
| **Alkes** | Alat Kesehatan (Medical equipment) |
| **SLA** | Service Level Agreement |
| **3-Way Match** | PO ↔ BAPB ↔ Invoice verification |
| **QC** | Quality Control |

---

## NEXT STEPS

1. **Review this blueprint** with IT team & procurement stakeholders
2. **Clarify any technical requirements** not covered
3. **Begin development** following phase breakdown (4 weeks)
4. **Weekly sync-ups** to track progress
5. **UAT in Week 3-4** with real users

**Questions?** Contact Procurement leadership for clarifications.

---

**Document Owner:** Departemen Pengadaan Umum dan Jasa  
**Last Updated:** June 2025  
**Status:** READY FOR IMPLEMENTATION


---

# ADDENDUM: CRITICAL INTEGRATIONS
## Unit Luar, Keuangan, BOD, Payment Alerts, SPI

**This section details critical external system integrations that were referenced but not fully detailed in the main blueprint.**

---

## INTEGRATION #1: UNIT LUAR (Branch Units / Clinical Departments)

### Use Case
Users in clinical/operational units (Radiology, Surgery, ICU, Pharmacy, etc.) can:
- Submit material/equipment needs directly from their unit dashboard
- Track delivery status in real-time
- Confirm receipt and quality (pembuatan BAPB)
- Request equipment validation/testing

### System Architecture

```
┌─────────────────────────────────┐
│ UNIT LUAR (Branch Departments)  │
├─────────────────────────────────┤
│ - Radiology Department          │
│ - Surgery Department            │
│ - Pharmacy                      │
│ - Warehouse/Logistics           │
│ - Equipment Management          │
└────────────────┬────────────────┘
                 │
         (API Integration)
                 │
    ┌────────────▼──────────────┐
    │ PROCUREMENT PLATFORM      │
    ├──────────────────────────┤
    │ ├─ Requisition Module    │
    │ ├─ Delivery Tracking     │
    │ ├─ QC/Testing Module     │
    │ └─ Feedback System       │
    └────────────┬─────────────┘
                 │
         (Data Sync)
                 │
    ┌────────────▼──────────────┐
    │ FINANCE SYSTEM (GL)       │
    │ WAREHOUSE SYSTEM (Inv)    │
    └──────────────────────────┘
```

### API Integration Points

**1. Unit Submit Requisition**
```
POST /api/v1/requisitions
{
  "unit_id": "RAD-001",          // Radiology unit
  "unit_name": "Radiology Dept",
  "requested_by": "Dr. Budi",
  "approver_unit": "Dr. Hendra", // Unit head
  "item": "Ultrasound probe",
  "quantity": 2,
  "urgency": "normal",           // or "urgent"
  "clinical_justification": "Replacement for broken probe",
  "expected_delivery_date": "2025-07-15",
  "budget_code": "RAD-2025-Q3"
}

Response (201):
{
  "requisition_id": "REQ-2025-001",
  "status": "submitted",
  "created_at": "2025-06-20T10:00:00Z",
  "estimated_tender_posting": "2025-06-25",
  "estimated_delivery": "2025-08-15"
}
```

**2. Unit Track Delivery Status**
```
GET /api/v1/units/{unit_id}/deliveries
?status=pending&date_range=last_30_days

Response:
{
  "unit_id": "RAD-001",
  "pending_deliveries": [
    {
      "po_number": "PO-2025-0100",
      "item": "Ultrasound probe",
      "vendor": "PT Medik Jaya",
      "ordered_date": "2025-06-15",
      "expected_delivery": "2025-07-15",
      "current_status": "in_transit",
      "tracking_number": "TRK-12345",
      "estimated_arrival": "2025-07-12",
      "contact": "PT Medik - 021-123456"
    }
  ]
}
```

**3. Unit Confirm Receipt & Buat BAPB**
```
POST /api/v1/grn
{
  "po_id": 100,
  "unit_id": "RAD-001",
  "delivery_date": "2025-07-15",
  "received_by": "Nurse Siti",
  "condition": "good",           // or "damaged", "incomplete"
  "items_received": [
    {
      "item_name": "Ultrasound probe",
      "quantity_received": 2,
      "quantity_expected": 2,
      "condition": "excellent"
    }
  ],
  "damage_notes": null,
  "photos": ["url-to-photo1", "url-to-photo2"]
}

Response (201):
{
  "grn_number": "BAPB-2025-001",
  "po_id": 100,
  "status": "approved",
  "created_at": "2025-07-15T14:00:00Z",
  "payment_milestone_triggered": {
    "milestone": "delivery_40_percent",
    "amount": 200000000,
    "next_milestone": "testing"
  }
}
```

**4. Unit Submit QC/Testing Results**
```
POST /api/v1/qc-results
{
  "po_id": 100,
  "unit_id": "RAD-001",
  "testing_date": "2025-07-17",
  "tested_by": "Dr. Budi (Radiologist)",
  "test_procedure": "Functional test per vendor manual",
  "test_results": {
    "power_on": "passed",
    "image_quality": "excellent",
    "probe_functionality": "all_functions_working",
    "safety_checks": "passed",
    "overall_status": "passed"
  },
  "issues_found": null,
  "recommendations": "Equipment ready for clinical use",
  "sign_off": true
}

Response (201):
{
  "qc_id": "QC-2025-001",
  "status": "approved",
  "payment_milestone_triggered": {
    "milestone": "testing_20_percent",
    "amount": 100000000,
    "next_milestone": "training_commission"
  }
}
```

### Unit Dashboard View

```
UNIT LUAR DASHBOARD - Radiology Department

═══════════════════════════════════════════════════════════════════

PENDING DELIVERIES (3)
┌──────────────────────────────────────────────────────────────────┐
│ PO-2025-0100 | Ultrasound probe | PT Medik Jaya                │
│ Expected: 2025-07-15 | Status: In Transit                      │
│ Track: TRK-12345 | Est. Arrival: Jul 12                        │
│ [CONFIRM DELIVERY]                                              │
└──────────────────────────────────────────────────────────────────┘

RECENT DELIVERIES (Last 30 days)
┌──────────────────────────────────────────────────────────────────┐
│ ✅ PO-2025-0095 | X-Ray Machine | Received Jul 10               │
│    BAPB: BAPB-2025-001 | QC: LULUS | Siap digunakan              │
│    [LIHAT BAPB] [VIEW QC REPORT]                                  │
└──────────────────────────────────────────────────────────────────┘

ACTIVE REQUISITIONS (Waiting for Tender)
┌──────────────────────────────────────────────────────────────────┐
│ REQ-2025-001 | ECG Machine | Urgent                            │
│ Submitted: Jun 15 | Est. Tender: Jun 25 | Est. Delivery: Aug 15 │
│ Status: Approved by Unit Head | [VIEW DETAILS]                 │
└──────────────────────────────────────────────────────────────────┘
```

---

## INTEGRATION #2: KEUANGAN (Finance/Accounting System)

### Use Case
Finance team needs to:
- Approve high-value purchases (>threshold)
- Process payments at correct milestones
- Post to GL (General Ledger)
- Reconcile with invoice/receipt
- Track budget vs. actual

### System Architecture

```
┌─────────────────────────────────────┐
│ PROCUREMENT PLATFORM                │
├─────────────────────────────────────┤
│ - PO Generation                     │
│ - Payment Milestone Tracking        │
│ - Invoice Management                │
└────────────────┬────────────────────┘
                 │
         (Real-time API)
                 │
    ┌────────────▼──────────────────┐
    │ FINANCE SYSTEM                │
    ├──────────────────────────────┤
    │ - GL (General Ledger)        │
    │ - AP (Accounts Payable)      │
    │ - Budget Tracking            │
    │ - Payment Processing         │
    │ - Bank Reconciliation        │
    └────────────┬──────────────────┘
```

### Finance Approval Workflow

```
THRESHOLD-BASED APPROVAL:

PO Amount?
  │
  ├─ ≤ 100M IDR
  │  └─ Auto-approve (Finance system)
  │     └─ Skip to payment processing
  │
  ├─ 100M - 500M IDR
  │  └─ Kepala Bagian Keuangan approval (1-2 days)
  │     └─ If approved → payment processing
  │     └─ If rejected → back to procurement
  │
  └─ > 500M IDR
     └─ Director approval (required)
        ├─ With Finance recommendation
        └─ If approved → payment processing
```

### Finance API Integration

**1. PO Routed to Finance for Approval**
```
POST /api/v1/finance/approve-po
{
  "po_id": 100,
  "po_number": "PO-2025-0100",
  "po_amount": 500000000,
  "vendor_name": "PT Medik Jaya",
  "budget_code": "RAD-2025-Q3",
  "budget_available": 600000000,
  "budget_remaining_after": 100000000,
  "approval_required": true,
  "approval_threshold": 100000000,
  "approver_role": "finance_manager"
}

Response (if auto-approved):
{
  "status": "approved",
  "approval_type": "auto",
  "approved_at": "2025-06-15T10:00:00Z",
  "next_step": "send_to_vendor_signature"
}

Response (if manual approval needed):
{
  "status": "pending",
  "approval_type": "manual",
  "assigned_to": "Kepala Bagian Keuangan",
  "deadline": "2025-06-17",
  "message": "Awaiting finance approval"
}
```

**2. GL Posting on PO Issuance**
```
Internal Process (auto-triggered):

PO Issued → GL Entry:
  Debit:  RAD-Equipment Expense   500,000,000 IDR
  Credit: Accounts Payable        500,000,000 IDR

GL Document Reference: PO-2025-0100
Cost Center: RAD (Radiology)
Date: 2025-06-15
Status: Posted
```

**3. 3-Way Match & Invoice Verification**
```
POST /api/v1/finance/invoice-verification
{
  "po_id": 100,
  "invoice_number": "INV-2025-001",
  "invoice_amount": 200000000,
  "invoice_date": "2025-07-17",
  
  "grn_number": "BAPB-2025-001",
  "grn_amount": 200000000,
  "grn_date": "2025-07-15",
  
  "po_amount_this_milestone": 200000000
}

System Auto-Validates:
  ✅ Invoice amount = BAPB amount = PO milestone amount
  ✅ Quantities match
  ✅ Dates logical (Invoice setelah BAPB, BAPB setelah PO)
  ✅ All supporting docs present

Response (if match):
{
  "status": "verified",
  "three_way_match": true,
  "variance": 0,
  "approval_status": "ready_to_pay"
}

Response (if mismatch):
{
  "status": "discrepancy",
  "three_way_match": false,
  "variance": 5000000,
  "discrepancy_details": {
    "invoice_vs_grn": 5000000,
    "reason": "Invoice melebihi BAPB"
  },
  "action_required": "reconcile_with_vendor"
}
```

**4. Payment Processing & GL Posting**
```
Payment Approved → GL Entry:

When DP (30%) Paid:
  Debit:  Accounts Payable        150,000,000 IDR
  Credit: Bank Account            150,000,000 IDR
  
GL Entry Reference: PM-2025-001 (Payment ID)
Date: Payment cleared
Status: Posted

When Delivery (40%) Paid:
  Debit:  Accounts Payable        200,000,000 IDR
  Credit: Bank Account            200,000,000 IDR
```

**5. Finance Dashboard with Budget Tracking**
```
FINANCE DASHBOARD

═══════════════════════════════════════════════════════════════════

BUDGET STATUS (YTD 2025)
┌──────────────────────────────────────────────────────────────────┐
│ Equipment Budget:  2,500,000,000 IDR                            │
│ Spent:             1,850,000,000 IDR (74%)                      │
│ Committed (POs):   400,000,000 IDR  (16%)                       │
│ Available:         250,000,000 IDR  (10%)                       │
│ ████████████████░░░░░░░░░░░░░░░░                                │
└──────────────────────────────────────────────────────────────────┘

PENDING APPROVALS
┌──────────────────────────────────────────────────────────────────┐
│ HIGH PRIORITY 🔴                                                │
│ ├─ PO-2025-0105 | Ventilator | 750M | DUE: 2025-06-22         │
│ │  Budget impact: Only 250M available! ACTION REQUIRED          │
│ └─ [REVIEW] [REJECT] [REQUEST_DIRECTOR_OVERRIDE]              │
│                                                                  │
│ NORMAL 🟡                                                       │
│ ├─ PO-2025-0104 | Infusion Pump | 250M | DUE: 2025-06-25      │
│ └─ [APPROVE] [REJECT]                                          │
└──────────────────────────────────────────────────────────────────┘

PAYMENT SCHEDULE (Next 30 Days)
┌──────────────────────────────────────────────────────────────────┐
│ Jun 21: DP (30%) x 5 POs = 450,000,000 IDR                     │
│ Jun 28: DP (30%) x 3 POs = 270,000,000 IDR                     │
│ Jul 15: Delivery (40%) x 2 POs = 200,000,000 IDR               │
│                                                                  │
│ TOTAL CASH NEEDED (Jun-Jul): 920,000,000 IDR                   │
│ Current Cash Position: 1,200,000,000 IDR ✅                     │
└──────────────────────────────────────────────────────────────────┘
```

---

## INTEGRATION #3: BOD (Direksi PT KMU)

### Use Case
BOD members (President, GM Operasi, Direktur Keuangan, SDM dan Umum) need:
- High-level procurement summary
- Budget impact analysis
- Vendor performance trends
- Approval authority for high-value tenders (>threshold)
- Strategic spend analytics

### BOD Dashboard

```
BOD EXECUTIVE DASHBOARD

═══════════════════════════════════════════════════════════════════

KEY METRICS (YTD 2025)
┌──────────────────────────────────────────────────────────────────┐
│ Total Procurement:      5,200,000,000 IDR                       │
│ vs Budget:              +8.3% (within tolerance)                │
│ On-Time Delivery:       94.2% (↑2.1% from last month)         │
│ Average Vendor Rating:  4.3/5.0 (stable)                       │
│ Cost Savings (vs quote): 156,000,000 IDR (3.2%)               │
└──────────────────────────────────────────────────────────────────┘

PROCUREMENT BY CATEGORY (Pie Chart)
┌──────────────────────────────────────────────────────────────────┐
│ Medical Equipment:  45% (2,340M)                               │
│ Medicines:          30% (1,560M)                               │
│ Support Services:   20% (1,040M)                               │
│ Other:              5% (260M)                                  │
└──────────────────────────────────────────────────────────────────┘

TOP VENDORS (by spend)
┌──────────────────────────────────────────────────────────────────┐
│ 1. PT Medik Jaya          520M (10.0%) | Rating: 4.7/5         │
│ 2. PT Farma Indonesia     480M (9.2%)  | Rating: 4.5/5         │
│ 3. PT Supply Chain Corp   420M (8.1%)  | Rating: 4.1/5         │
│ 4. PT Healthcare Support  380M (7.3%)  | Rating: 4.4/5         │
│ 5. PT Equipment Global    350M (6.7%)  | Rating: 4.6/5         │
└──────────────────────────────────────────────────────────────────┘

HIGH-VALUE APPROVALS REQUIRED
┌──────────────────────────────────────────────────────────────────┐
│ 🔴 TND-2025-0018: CT Scanner | 2,500,000,000 IDR               │
│    Status: Evaluated | Top vendor: PT Medik Jaya (score: 420)  │
│    Budget impact: -2,500M from capital equipment fund           │
│    Recommendation: Approve (meets all criteria)                 │
│    [APPROVE] [NEED_INFO] [REJECT]                              │
│                                                                  │
│ 🟡 TND-2025-0019: Annual Maintenance | 1,200,000,000 IDR       │
│    Status: Evaluated | Top vendor: PT Healthcare Support       │
│    Budget impact: -1,200M from operating budget (within)        │
│    Recommendation: Approve                                      │
│    [APPROVE] [NEED_INFO] [REJECT]                              │
└──────────────────────────────────────────────────────────────────┘

VENDOR PERFORMANCE TRENDS
┌──────────────────────────────────────────────────────────────────┐
│ Top Performer: PT Medik Jaya                                    │
│   - Delivery: 98.5% on-time (↑3.2%)                            │
│   - Quality: 4.7/5.0 (stable)                                  │
│   - Cost: 520M YTD (10% of total)                              │
│                                                                  │
│ At Risk: PT Supply Chain Corp                                   │
│   - Delivery: 85.2% on-time (↓5.3%)                            │
│   - Quality: 4.1/5.0 (declining)                               │
│   - Recommendation: Increase monitoring, reduce allocation     │
└──────────────────────────────────────────────────────────────────┘
```

### BOD API Integration

**1. BOD Approve High-Value Tender**
```
POST /api/v1/bod/approve-tender
{
  "tender_id": 18,
  "tender_number": "TND-2025-0018",
  "title": "CT Scanner",
  "amount": 2500000000,
  "selected_vendor": "PT Medik Jaya",
  "approval_by": "Direktur Utama",
  "approval_authority": "bod",
  "strategic_rationale": "Replacement for aging CT machine. Critical for radiology expansion."
}

Response (201):
{
  "status": "approved",
  "approval_timestamp": "2025-06-20T15:00:00Z",
  "po_generation_triggered": true,
  "next_step": "Finance verification, then send to vendor"
}
```

**2. BOD Request Information**
```
POST /api/v1/bod/request-info
{
  "tender_id": 19,
  "information_needed": "Cost comparison with domestic vs. imported equipment. What's the warranty difference?",
  "requested_by": "Direktur Keuangan, SDM dan Umum",
  "deadline": "2025-06-22"
}

Response:
{
  "status": "information_requested",
  "assigned_to": "Manager Pengadaan",
  "response_deadline": "2025-06-22",
  "notification_sent": true
}
```

---

## INTEGRATION #4: PAYMENT ALERT SYSTEM

### Use Case
Critical payment events trigger alerts to:
- Finance team (invoices ready, payment overdue)
- Procurement team (vendor non-compliance)
- Vendors (payment status, waiting action)
- Directors (budget impact, high-value payment approvals)
- SPI (compliance flags)

### Alert Types & Escalation

```
PAYMENT EVENT → TRIGGERS ALERT → ESCALATION LOGIC

Payment Milestone Ready
  └─ [Finance] "Invoice received for PO-2025-0100 delivery"
     └─ No action? After 2 days → escalate
        └─ [Kepala Bagian Keuangan] "Approve payment for 200M (PO-100)"
           └─ No action? After 3 days → escalate
              └─ [Director] "Payment overdue by 3 days. Approve?"

Vendor Query/Issue
  └─ [Procurement] "Vendor requesting payment status"
     └─ No response? After 1 day → escalate
        └─ [Manager Pengadaan] "Respond to vendor query"

Budget Threshold Warning
  └─ [Finance] "Remaining budget 150M. Next payment requests 200M."
     └─ Manual approval required

Compliance Flag
  └─ [SPI/Audit] "3-way match discrepancy. Investigate."
     └─ Finance + Procurement action required
```

### Alert Configuration

```javascript
// alert-config.json

{
  "alerts": {
    "invoice_received": {
      "enabled": true,
      "notify_to": ["finance", "procurement"],
      "escalation": [
        { "days": 2, "notify_to": ["finance_manager"] },
        { "days": 5, "notify_to": ["director"] }
      ],
      "email_template": "ALERT_INVOICE_RECEIVED",
      "sms_for_urgent": true
    },
    "vendor_payment_late": {
      "enabled": true,
      "trigger_days": 3,
      "notify_to": ["vendor", "finance", "procurement"],
      "escalation": [
        { "days": 5, "notify_to": ["director"] }
      ],
      "penalty_flag": true
    },
    "budget_threshold_warning": {
      "enabled": true,
      "threshold_percentage": 90,
      "notify_to": ["finance_manager", "director"],
      "require_approval": true
    },
    "compliance_flag": {
      "enabled": true,
      "trigger_events": ["three_way_mismatch", "missing_doc", "overdue_vendor"],
      "notify_to": ["spi", "finance", "procurement"],
      "escalation": [
        { "hours": 24, "notify_to": ["director"] }
      ]
    }
  }
}
```

### Alert Channels

**Channel 1: Email Notifications**
```
From: noreply@procurement.kmuholding.com
To: finance@kmu.co.id

Subject: 🔔 Action Required: Invoice Ready for Approval (PO-2025-0100)

Dear Finance Team,

Invoice INV-2025-001 for PO-2025-0100 (PT Medik Jaya - Ultrasound) has been 
received and verified (3-way match passed).

Invoice Amount: 200,000,000 IDR
Milestone: Delivery (40% of PO)
Approval Deadline: 2025-07-20

➜ [APPROVE PAYMENT] [VIEW DETAILS]

If you have questions, contact Manager Pengadaan.

---
Procurement Portal | Auto-generated alert
```

**Channel 2: SMS Alerts (Urgent Only)**
```
🚨 KMU PROCUREMENT: PO-100 payment OVERDUE 3 days. 200M pending approval. 
Act now: https://kmu-procurement.com/payments/123
```

**Channel 3: In-App Notifications**
```
Dashboard Badge: 5 pending approvals
Alert: ⚠️ Budget threshold reached (90% spent)
Alert: 🔴 Vendor payment overdue by 3 days
```

**Channel 4: Dashboard Widget**
```
ALERTS & NOTIFICATIONS (Dashboard)

┌──────────────────────────────────────────────────┐
│ 🔴 CRITICAL (2)                                 │
│ ├─ Invoice verification failed (PO-99)          │
│ └─ Payment overdue to PT Farma (5 days)        │
│                                                  │
│ 🟡 WARNING (5)                                  │
│ ├─ Invoice pending approval (3 items)           │
│ ├─ Budget threshold warning (2 items)           │
│                                                  │
│ 🟢 INFO (12)                                    │
│ ├─ Quote submitted notifications                │
│ └─ Delivery confirmations                       │
└──────────────────────────────────────────────────┘
```

---

## INTEGRATION #5: SPI (SISTEM PENGENDALIAN INTERNAL / Internal Control System)

### Use Case
SPI/Audit team needs to:
- Track 100% of procurement activities for compliance
- Verify 4-eye principle (segregation of duties)
- Monitor threshold violations
- Audit trail review
- Compliance report generation

### Segregation of Duties Matrix

```
┌──────────────────┬─────────────┬──────────────┬────────────┐
│ Activity         │ Procurement │ Finance      │ Director   │
├──────────────────┼─────────────┼──────────────┼────────────┤
│ Create Tender    │ ✅          │              │            │
│ Approve Tender   │             │ ✅ (<100M)   │ ✅ (>500M) │
│ Score Quotes     │ ✅          │              │            │
│ Select Vendor    │ ✅          │              │            │
│ Generate PO      │ ✅          │              │            │
│ Approve PO       │             │ ✅ (<100M)   │ ✅ (>500M) │
│ Receive Goods    │ Unit        │              │            │
│ Match Invoices   │ ✅          │              │            │
│ Approve Payment  │             │ ✅ (<500M)   │ ✅ (>500M) │
│ Process Payment  │             │ ✅ (Finance) │            │
│ Post GL          │             │ ✅           │            │
│ Review Audit Log │             │              │ SPI ✅     │
└──────────────────┴─────────────┴──────────────┴────────────┘
```

### SPI Dashboard

```
SPI / INTERNAL AUDIT DASHBOARD

═══════════════════════════════════════════════════════════════════

COMPLIANCE METRICS (2025 YTD)
┌──────────────────────────────────────────────────────────────────┐
│ Total Transactions:     847                                     │
│ Compliant:              824 (97.3%)  ✅                         │
│ With Exceptions:        23 (2.7%)   ⚠️                          │
│ Failed Controls:        0 (0.0%)    ✅                          │
└──────────────────────────────────────────────────────────────────┘

CONTROL EXCEPTIONS (Details)
┌──────────────────────────────────────────────────────────────────┐
│ 1. THRESHOLD VIOLATION                                          │
│    ├─ PO-2025-0045: 450M (auto-approved at <100M threshold)  │
│    ├─ Amount actually: 450M should need director approval    │
│    ├─ Reason: Error in system calculation                    │
│    ├─ Status: Retroactively approved (Jun 18)                │
│    └─ Action: [REVIEW_FULL_DETAILS] [CLOSE_EXCEPTION]       │
│                                                                  │
│ 2. MISSING DOCUMENTATION                                       │
│    ├─ Tender TND-2025-0012: Missing vendor registration doc   │
│    ├─ Vendor: PT Healthcare Support                           │
│    ├─ Status: Pending                                         │
│    └─ Action: [REQUEST_FROM_VENDOR] [WAIVE] [ESCALATE]      │
│                                                                  │
│ 3. SEGREGATION OF DUTIES VIOLATION                             │
│    ├─ PO-2025-0082: Same person created & approved PO        │
│    ├─ User: Manager Pengadaan (authorization error)         │
│    ├─ Amount: 85M (should not require approval anyway)        │
│    ├─ Status: Resolved                                        │
│    └─ Action: [ACCEPT] [CLOSE_EXCEPTION]                     │
└──────────────────────────────────────────────────────────────────┘

VENDOR COMPLIANCE HISTORY
┌──────────────────────────────────────────────────────────────────┐
│ PT Medik Jaya: 45 transactions, 44 compliant (97.8%)            │
│ PT Farma Indonesia: 38 transactions, 35 compliant (92.1%) ⚠️    │
│ PT Healthcare Support: 28 transactions, 28 compliant (100%) ✅  │
│ PT Supply Chain Corp: 32 transactions, 28 compliant (87.5%) ❌  │
│                                                                  │
│ Action Needed: PT Supply Chain Corp - Below 90% compliance    │
│ Recommendation: Reduce bid participation, increase monitoring  │
└──────────────────────────────────────────────────────────────────┘

AUDIT TRAIL REVIEW
┌──────────────────────────────────────────────────────────────────┐
│ Filter by: User | Date Range | Entity | Action                 │
│                                                                  │
│ Recent Audit Entries:                                          │
│ • 2025-06-20 10:30 | Manager Pengadaan | Created PO-2025-0106
│ • 2025-06-20 10:45 | Kepala Bagian Keuangan | Approved PO-2025-0106  │
│ • 2025-06-20 11:00 | System | Sent PO to vendor for signature │
│ • 2025-06-20 14:30 | Vendor (PT Medik) | Signed PO-2025-0106  │
│ • 2025-06-21 09:00 | Unit (Warehouse) | Barang diterima BAPB-001 │
│                                                                  │
│ Full audit trail immutable & timestamped                       │
│ [EXPORT_AUDIT_LOG] [PRINT_REPORT] [COMPLIANCE_CERT]           │
└──────────────────────────────────────────────────────────────────┘
```

### SPI API Endpoints

**1. Get Compliance Report**
```
GET /api/v1/spi/compliance-report
?date_range=2025-01-01:2025-06-30&entity_type=purchase_order

Response:
{
  "report_id": "SPI-2025-H1",
  "period": "2025-01-01 to 2025-06-30",
  "total_transactions": 847,
  "compliant": 824,
  "compliance_percentage": 97.3,
  "exceptions": [
    {
      "exception_id": "EXC-2025-001",
      "exception_type": "threshold_violation",
      "entity_id": "PO-2025-0045",
      "severity": "medium",
      "status": "resolved",
      "resolved_at": "2025-06-18",
      "resolution": "Retroactive approval by Director"
    }
  ],
  "controls_tested": {
    "segregation_of_duties": "100% coverage",
    "threshold_compliance": "99.8%",
    "documentation_completeness": "99.0%",
    "audit_trail_integrity": "100%"
  },
  "recommendations": [
    "Monitor PT Supply Chain Corp - compliance trending down",
    "Review threshold logic - one false positive in system config",
    "No major control gaps identified"
  ]
}
```

**2. Generate Compliance Certificate**
```
GET /api/v1/spi/compliance-certificate
?period=2025-H1&issued_by=SPI_Director&signature=digital

Response (PDF):
═══════════════════════════════════════════════════════════════════

COMPLIANCE CERTIFICATE
KMU Holding Procurement System

Period: January 1 - June 30, 2025

This is to certify that the Platform Digitalisasi Pengadaan KMU has been reviewed
and tested for internal control compliance. The system demonstrates:

✅ 97.3% compliance rate
✅ Proper segregation of duties (SAoD)
✅ Complete audit trail documentation
✅ Threshold-based approval logic working correctly
✅ Vendor performance monitoring in place

Minor exceptions (2.7%) identified and resolved.

Issued: June 30, 2025
Signed: [Digital Signature]
SPI Director: Ibu Rina Suryanto

═══════════════════════════════════════════════════════════════════
```

### SPI Monitoring Rules

```javascript
// spi-monitoring-rules.js

const SPI_RULES = {
  
  // Rule 1: Threshold Compliance
  threshold_compliance: {
    rule: "PO amount must match approval threshold",
    check: (po) => {
      if (po.amount <= 100M && po.approved_by !== 'finance_auto') return false;
      if (po.amount > 100M && po.amount <= 500M && !po.finance_approved) return false;
      if (po.amount > 500M && !po.director_approved) return false;
      return true;
    },
    severity: "high",
    auto_flag: true
  },
  
  // Rule 2: Segregation of Duties
  segregation_of_duties: {
    rule: "Cannot have same person in create + approve roles",
    check: (po) => {
      return po.created_by !== po.approved_by;
    },
    severity: "critical",
    auto_flag: true
  },
  
  // Rule 3: Documentation Completeness
  documentation_completeness: {
    rule: "All required docs must be attached",
    required_docs: ["invoice", "grn", "qc_report"],
    check: (po) => {
      return required_docs.every(doc => po.documents.includes(doc));
    },
    severity: "medium",
    auto_flag: true
  },
  
  // Rule 4: Audit Trail Integrity
  audit_trail_integrity: {
    rule: "All state changes must be logged with timestamp & user",
    check: (po) => {
      return po.audit_logs.length > 0 && 
             po.audit_logs.every(log => log.timestamp && log.user_id);
    },
    severity: "high",
    auto_flag: true
  },
  
  // Rule 5: Vendor Compliance Check
  vendor_compliance_check: {
    rule: "Only approved vendors can be selected",
    check: (po) => {
      return po.vendor.status === 'approved';
    },
    severity: "critical",
    auto_flag: true
  },
  
  // Rule 6: Budget Compliance
  budget_compliance: {
    rule: "PO cannot exceed available budget",
    check: (po, budget) => {
      return po.amount <= budget.available;
    },
    severity: "high",
    auto_flag: true
  },
  
  // Rule 7: Approval Timeliness
  approval_timeliness: {
    rule: "Approvals must happen within SLA",
    sla_days: 2,
    check: (po) => {
      const elapsed = (po.approved_at - po.created_at) / (1000 * 60 * 60 * 24);
      return elapsed <= this.sla_days;
    },
    severity: "medium",
    auto_flag: true
  }
};

// Run compliance check on every PO
async function runComplianceChecks(po) {
  const violations = [];
  
  for (const [ruleName, rule] of Object.entries(SPI_RULES)) {
    if (!rule.check(po)) {
      violations.push({
        rule: ruleName,
        severity: rule.severity,
        message: rule.rule
      });
      
      if (rule.auto_flag) {
        // Auto-flag in system
        await flagExceptionForSPI(po.id, ruleName, rule.severity);
      }
    }
  }
  
  return violations;
}
```

---

## COMPLETE INTEGRATION FLOW

### Example: End-to-End with All Integrations

```
1. UNIT SUBMITS REQUISITION
   Unit (Radiology) → POST /api/v1/requisitions
   └─ Escalation: Unit Head approval required
   
2. PROCUREMENT CREATES TENDER
   Procurement → Tender created in system
   └─ Alert: SPI logs action for audit trail
   
3. TENDER PUBLISHED
   Procurement → Tender visible on vendor portal
   └─ Finance: Budget reserved against requisition
   
4. VENDORS SUBMIT QUOTES
   Vendors → Document uploads (any format)
   └─ Alert: Procurement team "3 new quotes received"
   └─ Alert: SPI "Bid submission audit logged"
   
5. AI EXTRACTS DATA
   Gemini → Auto-tabulation & scoring
   └─ Alert: Procurement "Scoring complete, ready for review"
   
6. PROCUREMENT SELECTS VENDOR
   Procurement → Select PO-2025-0100 (PT Medik Jaya)
   └─ Alert: SPI "Vendor compliance check: APPROVED"
   └─ Alert: Finance "PO routed for approval (450M)"
   
7. FINANCE APPROVES
   Finance Mgr → PO approved (>100M < 500M threshold)
   └─ GL Entry: Debit Equipment, Credit AP
   └─ Alert: Procurement "Approved, send to vendor"
   └─ Alert: SPI "Approval logged by Finance"
   
8. PO SENT TO VENDOR
   System → Digital signature link sent to vendor
   └─ Alert: Vendor "Sign PO-2025-0100 by Jun 22"
   
9. VENDOR SIGNS
   Vendor → E-signature received
   └─ Alert: Unit (Radiology) "Equipment on order, ETA Jul 15"
   └─ Alert: Finance "DP payment due: 150M (30%)"
   
10. DP PAYMENT PROCESSED
    Finance → Payment approved & processed
    └─ GL Entry: Debit AP, Credit Bank
    └─ Alert: Vendor "DP received, proceeding with shipment"
    └─ Alert: Unit "Expected delivery: Jul 15"
    
11. GOODS RECEIVED
    Unit → BAPB created: "Ultrasound received in good condition"
    └─ Alert: Procurement "BAPB diterima"
    └─ Alert: Finance "40% Delivery payment: 200M due"
    └─ Alert: Unit (Clinical) "Equipment ready for testing"
    
12. TESTING COMPLETED
    Unit → QC report: "All tests PASSED"
    └─ Alert: Finance "20% Testing payment: 100M due"
    └─ Alert: Vendor "Proceed with training"
    
13. INVOICE VERIFICATION
    Finance → 3-way match (PO-BAPB-Invoice): ✅ MATCHED
    └─ Alert: Finance "Ready to approve payment"
    
14. PAYMENT APPROVED
    Finance → All 3 invoices approved & processed
    └─ GL Entry: Debit AP, Credit Bank (3 times)
    └─ Alert: Vendor "Payment confirmation sent"
    
15. TRAINING & COMMISSIONING
    Unit + Vendor → Completed
    └─ Alert: Finance "Final 10% payment: 50M due"
    
16. FINAL CLOSURE
    Procurement → PO marked complete
    └─ Vendor metrics updated
    └─ Alert: SPI "All compliance checks PASSED"
    └─ Alert: Finance "GL finalized, invoice complete"

FINAL STATE:
✅ Full audit trail logged
✅ Budget posted correctly (GL)
✅ All payments tracked
✅ Compliance certificate ready
✅ Vendor performance recorded
```

---

## IMPLEMENTATION SUMMARY

### New Integrations Added to Blueprint

| Integration | API Calls | Alerts | GL Posts | Audit | 
|-------------|-----------|--------|----------|-------|
| Unit Luar | 4 (PP/SPPJ, tracking, BAPB, QC) | 5 types | Yes | Full trail |
| Finance | 5 (approval, GL, 3-way, payment) | 6 types | Every transaction | All changes |
| BOD | 2 (approve, info request) | High-value only | N/A | Executive actions |
| Payment Alerts | Triggered events | 4 channels | N/A | All alerts |
| SPI | Compliance reports | Exceptions only | N/A | 100% coverage |

### Updated Database Schema

Add to existing tables:
```sql
-- Audit requirements
ALTER TABLE tenders ADD COLUMN budget_reserved_finance DECIMAL(15,2);
ALTER TABLE purchase_orders ADD COLUMN gl_post_reference VARCHAR(50);
ALTER TABLE payments ADD COLUMN gl_entry_date TIMESTAMP;

-- Alert tracking
CREATE TABLE alerts (
  id SERIAL PRIMARY KEY,
  alert_type VARCHAR(100),
  triggered_by INT REFERENCES users(id),
  entity_type VARCHAR(50),
  entity_id INT,
  recipients TEXT[], -- array of user IDs
  channels TEXT[], -- 'email', 'sms', 'in_app'
  status VARCHAR(50), -- 'sent', 'acknowledged', 'resolved'
  escalation_level INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Updated Deployment Checklist

Add to Phase 3 (Week 3):

- [ ] Unit Portal
  - [ ] Requisition form
  - [ ] Delivery tracking
  - [ ] BAPB submission
  - [ ] QC form

- [ ] Finance Integration
  - [ ] GL API connection
  - [ ] Budget reservation logic
  - [ ] 3-way match automation
  - [ ] Payment approval workflow

- [ ] BOD Dashboard
  - [ ] Executive summary views
  - [ ] High-value approval routing
  - [ ] Vendor performance analytics

- [ ] Alert System
  - [ ] Email service integration
  - [ ] SMS gateway (Twilio/AWS SNS)
  - [ ] Alert configuration UI
  - [ ] Escalation logic

- [ ] SPI Module
  - [ ] Compliance checks
  - [ ] Audit logging (immutable)
  - [ ] Exception flagging
  - [ ] Compliance reporting

---

## NEXT STEPS

1. **Review** this addendum with IT team
2. **Update tech stack** if new dependencies needed (email, SMS, GL integration)
3. **Extend database schema** with alert & SPI tables
4. **Implement integrations** in Phase 3
5. **UAT with Unit, Finance, BOD, SPI teams** in Week 3-4

---

**These critical integrations are now part of the complete blueprint.** IT team has all details needed to implement the full system with all stakeholder needs covered.


-- PROCUREMENT PLATFORM DATABASE SCHEMA
-- PostgreSQL 13+
-- Run: psql -U postgres -d procurement < 001-init.sql

-- ============================================================================
-- EXTENSIONS & SETUP
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================================
-- ENUM TYPES
-- ============================================================================

CREATE TYPE user_role AS ENUM (
  'vendor',
  'procurement',
  'finance',
  'director',
  'audit',
  'admin'
);

CREATE TYPE user_type AS ENUM ('internal', 'external');
CREATE TYPE user_status AS ENUM ('active', 'inactive', 'suspended');

CREATE TYPE tender_status AS ENUM (
  'draft',
  'published',
  'closed',
  'awarded',
  'completed'
);

CREATE TYPE vendor_status AS ENUM (
  'approved',
  'pending',
  'rejected',
  'inactive'
);

CREATE TYPE quote_negotiation_status AS ENUM (
  'initial',
  'revised',
  'final'
);

CREATE TYPE po_status AS ENUM (
  'draft',
  'issued',
  'acknowledged',
  'in_progress',
  'delivered',
  'completed',
  'cancelled'
);

CREATE TYPE payment_milestone_type AS ENUM (
  'dp',
  'delivery',
  'testing',
  'training_commission'
);

CREATE TYPE payment_status AS ENUM (
  'pending',
  'approved',
  'processing',
  'paid',
  'cancelled'
);

CREATE TYPE recommendation_type AS ENUM (
  'utama',
  'alternatif',
  'pertimbangan',
  'tidak'
);

-- ============================================================================
-- TABLES
-- ============================================================================

-- BRANCHES TABLE
CREATE TABLE branches (
  id SERIAL PRIMARY KEY,
  branch_name VARCHAR(255) NOT NULL,
  branch_code VARCHAR(50) UNIQUE NOT NULL,
  location VARCHAR(255),
  region VARCHAR(100),
  contact_person VARCHAR(255),
  contact_phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_branches_code ON branches(branch_code);
CREATE INDEX idx_branches_region ON branches(region);

-- VENDORS TABLE
CREATE TABLE vendors (
  id SERIAL PRIMARY KEY,
  company_name VARCHAR(255) NOT NULL,
  tax_id VARCHAR(50) UNIQUE,
  email VARCHAR(255),
  phone VARCHAR(20),
  
  street_address VARCHAR(255),
  city VARCHAR(100),
  province VARCHAR(100),
  postal_code VARCHAR(10),
  country VARCHAR(100) DEFAULT 'Indonesia',
  
  business_type VARCHAR(100),
  specialization TEXT,
  
  has_local_office BOOLEAN DEFAULT false,
  local_office_location VARCHAR(255),
  local_office_population_served INT,
  
  sparepart_availability VARCHAR(100),
  sparepart_price_level VARCHAR(50),
  support_rating DECIMAL(2,1),
  
  registration_date DATE,
  status vendor_status DEFAULT 'pending',
  certification_documents TEXT,
  verification_notes TEXT,
  verified_by INT REFERENCES users(id),
  verified_at TIMESTAMP,
  
  total_bids INT DEFAULT 0,
  total_wins INT DEFAULT 0,
  avg_delivery_days DECIMAL(5,2),
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_vendors_company ON vendors(company_name);
CREATE INDEX idx_vendors_status ON vendors(status);
CREATE INDEX idx_vendors_local_office ON vendors(has_local_office);
CREATE INDEX idx_vendors_email ON vendors(email);

-- USERS TABLE
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  full_name VARCHAR(255) NOT NULL,
  role user_role NOT NULL,
  user_type user_type NOT NULL,
  status user_status DEFAULT 'active',
  
  vendor_id INT REFERENCES vendors(id) ON DELETE SET NULL,
  department VARCHAR(100),
  branch_id INT REFERENCES branches(id) ON DELETE SET NULL,
  
  two_factor_enabled BOOLEAN DEFAULT false,
  last_login TIMESTAMP,
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_vendor_id ON users(vendor_id);
CREATE INDEX idx_users_status ON users(status);

-- TENDERS TABLE
CREATE TABLE tenders (
  id SERIAL PRIMARY KEY,
  tender_number VARCHAR(50) UNIQUE NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  
  category VARCHAR(100),
  sub_category VARCHAR(100),
  
  specifications JSONB,
  required_certifications TEXT,
  
  posting_date DATE,
  bid_closing_date TIMESTAMP NOT NULL,
  evaluation_period_days INT DEFAULT 7,
  expected_delivery_date DATE,
  
  budget_min DECIMAL(15,2),
  budget_max DECIMAL(15,2),
  approval_threshold DECIMAL(15,2),
  
  status tender_status DEFAULT 'draft',
  evaluation_criteria JSONB,
  
  medical_factor_override BOOLEAN DEFAULT false,
  medical_notes TEXT,
  
  created_by INT REFERENCES users(id),
  approved_by INT REFERENCES users(id),
  assigned_to INT REFERENCES users(id),
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_tenders_status ON tenders(status);
CREATE INDEX idx_tenders_closing_date ON tenders(bid_closing_date);
CREATE INDEX idx_tenders_category ON tenders(category);
CREATE INDEX idx_tenders_number ON tenders(tender_number);

-- QUOTES TABLE
CREATE TABLE sjph (
  id SERIAL PRIMARY KEY,
  tender_id INT NOT NULL REFERENCES tenders(id) ON DELETE CASCADE,
  vendor_id INT NOT NULL REFERENCES vendors(id) ON DELETE CASCADE,
  
  document_url VARCHAR(255),
  document_type VARCHAR(50),
  upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  extracted_data JSONB,
  
  requires_human_review BOOLEAN DEFAULT false,
  human_review_notes TEXT,
  reviewed_by INT REFERENCES users(id),
  reviewed_at TIMESTAMP,
  
  revision_number INT DEFAULT 1,
  negotiation_status quote_negotiation_status DEFAULT 'initial',
  negotiation_notes TEXT,
  
  calculated_score DECIMAL(5,2),
  score_breakdown JSONB,
  recommendation recommendation_type,
  
  selected BOOLEAN DEFAULT false,
  selected_reason TEXT,
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  UNIQUE(tender_id, vendor_id, revision_number)
);

CREATE INDEX idx_quotes_tender_id ON sjph(tender_id);
CREATE INDEX idx_quotes_vendor_id ON sjph(vendor_id);
CREATE INDEX idx_quotes_calculated_score ON sjph(calculated_score);
CREATE INDEX idx_quotes_selected ON sjph(selected);

-- PURCHASE ORDERS TABLE
CREATE TABLE purchase_orders (
  id SERIAL PRIMARY KEY,
  po_number VARCHAR(50) UNIQUE NOT NULL,
  tender_id INT NOT NULL REFERENCES tenders(id),
  vendor_id INT NOT NULL REFERENCES vendors(id),
  
  po_date DATE NOT NULL,
  po_amount DECIMAL(15,2) NOT NULL,
  currency VARCHAR(10) DEFAULT 'IDR',
  
  delivery_date DATE,
  payment_terms TEXT,
  
  payment_milestones JSONB,
  
  testing_required BOOLEAN DEFAULT true,
  testing_procedure TEXT,
  training_required BOOLEAN DEFAULT true,
  training_scope TEXT,
  commissioning_required BOOLEAN DEFAULT true,
  
  status po_status DEFAULT 'draft',
  
  approved_by INT REFERENCES users(id),
  approved_date TIMESTAMP,
  
  vendor_signature_url VARCHAR(255),
  vendor_signed_at TIMESTAMP,
  po_signature_url VARCHAR(255),
  po_signed_at TIMESTAMP,
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_po_vendor_id ON purchase_orders(vendor_id);
CREATE INDEX idx_po_tender_id ON purchase_orders(tender_id);
CREATE INDEX idx_po_status ON purchase_orders(status);
CREATE INDEX idx_po_number ON purchase_orders(po_number);

-- PAYMENTS TABLE
CREATE TABLE payments (
  id SERIAL PRIMARY KEY,
  po_id INT NOT NULL REFERENCES purchase_orders(id) ON DELETE CASCADE,
  vendor_id INT NOT NULL REFERENCES vendors(id),
  
  invoice_number VARCHAR(50),
  invoice_date DATE,
  invoice_amount DECIMAL(15,2),
  invoice_document_url VARCHAR(255),
  
  milestone_type payment_milestone_type NOT NULL,
  milestone_percentage DECIMAL(5,2),
  payment_amount DECIMAL(15,2),
  
  po_matched BOOLEAN DEFAULT false,
  grn_matched BOOLEAN DEFAULT false,
  invoice_matched BOOLEAN DEFAULT false,
  three_way_match_complete BOOLEAN DEFAULT false,
  match_date TIMESTAMP,
  
  status payment_status DEFAULT 'pending',
  approval_by INT REFERENCES users(id),
  approved_at TIMESTAMP,
  
  payment_date TIMESTAMP,
  payment_reference VARCHAR(100),
  
  payment_notes TEXT,
  rejection_reason TEXT,
  
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_payments_po_id ON payments(po_id);
CREATE INDEX idx_payments_vendor_id ON payments(vendor_id);
CREATE INDEX idx_payments_status ON payments(status);
CREATE INDEX idx_payments_milestone_type ON payments(milestone_type);

-- AUDIT LOGS TABLE
CREATE TABLE audit_logs (
  id SERIAL PRIMARY KEY,
  user_id INT REFERENCES users(id) ON DELETE SET NULL,
  action VARCHAR(100),
  entity_type VARCHAR(50),
  entity_id INT,
  
  old_value TEXT,
  new_value TEXT,
  
  ip_address VARCHAR(45),
  user_agent TEXT,
  
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  
  previous_hash VARCHAR(255),
  current_hash VARCHAR(255)
);

CREATE INDEX idx_audit_logs_user_id ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_entity_type ON audit_logs(entity_type);
CREATE INDEX idx_audit_logs_timestamp ON audit_logs(timestamp DESC);

-- ============================================================================
-- VIEWS FOR COMMON QUERIES
-- ============================================================================

-- View: Active Tenders with SJPH Counts
CREATE VIEW tenders_with_quotes AS
SELECT 
  t.id,
  t.tender_number,
  t.title,
  t.status,
  t.bid_closing_date,
  COUNT(q.id) as total_quotes,
  SUM(CASE WHEN q.selected THEN 1 ELSE 0 END) as selected_quotes,
  EXTRACT(DAY FROM (t.bid_closing_date - NOW())) as days_remaining
FROM tenders t
LEFT JOIN sjph q ON t.id = q.tender_id
GROUP BY t.id, t.tender_number, t.title, t.status, t.bid_closing_date;

-- View: Vendor Performance Metrics
CREATE VIEW vendor_metrics AS
SELECT 
  v.id,
  v.company_name,
  v.status,
  v.total_bids,
  v.total_wins,
  CASE WHEN v.total_bids > 0 
    THEN ROUND((v.total_wins::numeric / v.total_bids) * 100, 2)
    ELSE 0
  END as win_rate_percentage,
  v.avg_delivery_days,
  v.support_rating,
  COUNT(DISTINCT po.id) as active_pos
FROM vendors v
LEFT JOIN purchase_orders po ON v.id = po.vendor_id AND po.status NOT IN ('completed', 'cancelled')
GROUP BY v.id, v.company_name, v.status, v.total_bids, v.total_wins, v.avg_delivery_days, v.support_rating;

-- View: Payment Status by PO
CREATE VIEW payment_status_by_po AS
SELECT 
  po.id as po_id,
  po.po_number,
  po.po_amount,
  SUM(CASE WHEN p.status = 'paid' THEN p.payment_amount ELSE 0 END) as total_paid,
  SUM(CASE WHEN p.status IN ('approved', 'processing') THEN p.payment_amount ELSE 0 END) as total_approved,
  SUM(CASE WHEN p.status = 'pending' THEN p.payment_amount ELSE 0 END) as total_pending,
  (po.po_amount - SUM(CASE WHEN p.status = 'paid' THEN p.payment_amount ELSE 0 END)) as outstanding_amount
FROM purchase_orders po
LEFT JOIN payments p ON po.id = p.po_id
GROUP BY po.id, po.po_number, po.po_amount;

-- ============================================================================
-- INITIAL DATA
-- ============================================================================

-- Insert sample branches
INSERT INTO branches (branch_name, branch_code, location, region) VALUES
  ('RS Pusat', 'RSP', 'Jakarta', 'Jawa'),
  ('RS Cabang Surabaya', 'RSS', 'Surabaya', 'Jawa'),
  ('RS Cabang Bandung', 'RSB', 'Bandung', 'Jawa'),
  ('RS Cabang Samarinda', 'RSSM', 'Samarinda', 'Kalimantan Timur');

-- Insert admin user (change password immediately!)
INSERT INTO users (email, password_hash, full_name, role, user_type, status, department) VALUES
  ('admin@kmu.co.id', 
   '$2b$10$placeholder_hash_change_this', 
   'Administrator', 
   'admin'::user_role, 
   'internal'::user_type, 
   'active'::user_status, 
   'IT');

-- ============================================================================
-- GRANTS & SECURITY
-- ============================================================================

-- Create read-only role for audit team
CREATE ROLE audit_reader;
GRANT CONNECT ON DATABASE procurement TO audit_reader;
GRANT USAGE ON SCHEMA public TO audit_reader;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO audit_reader;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO audit_reader;

-- Ensure audit logs are append-only (no updates/deletes)
REVOKE DELETE, UPDATE ON audit_logs FROM PUBLIC;

-- ============================================================================
-- DONE
-- ============================================================================

COMMIT;

\echo 'Database initialization complete!'
\echo 'Important: Update the admin password hash in the users table'
\echo 'Current placeholder: $2b$10$placeholder_hash_change_this'

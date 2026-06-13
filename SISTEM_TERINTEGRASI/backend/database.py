import sqlite3
import os
import json
from datetime import datetime

# Path to database file
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, "kmu_procurement.db")

def init_db():
    """Initialize SQLite database with required tables"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create Vendors Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_id TEXT UNIQUE,
        company_name TEXT NOT NULL,
        company_name_short TEXT,
        vendor_type TEXT,
        vendor_category TEXT,
        phone TEXT,
        email TEXT,
        website TEXT,
        address_street TEXT,
        address_city TEXT,
        address_province TEXT,
        address_postal_code TEXT,
        address_country TEXT DEFAULT 'Indonesia',
        npwp TEXT,
        sio TEXT,
        bank_name TEXT,
        bank_account_number TEXT,
        bank_account_holder TEXT,
        contact_person_name TEXT,
        contact_person_title TEXT,
        contact_person_phone TEXT,
        contact_person_email TEXT,
        vendor_status TEXT DEFAULT 'submitted',
        registration_date DATETIME,
        notes TEXT,
        metadata TEXT
    )
    ''')

    # Create Activity Log Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS activity_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_type TEXT,
        entity_type TEXT,
        entity_id INTEGER,
        entity_reference TEXT,
        action_date DATETIME,
        description TEXT,
        vendor_id INTEGER,
        metadata TEXT
    )
    ''')

    # Create Users Table (for Admin/Vendor login later)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL,
        vendor_id INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Requisitions Table (Permintaan Pembelian)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS requisitions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        req_number TEXT UNIQUE,
        req_type TEXT NOT NULL,
        sbu_name TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        budget_code TEXT,
        total_amount REAL,
        status TEXT DEFAULT 'pending_kasie',
        created_by TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Purchase Orders Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS purchase_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        po_number TEXT UNIQUE,
        req_id INTEGER,
        vendor_id TEXT,
        total_amount REAL,
        status TEXT DEFAULT 'draft',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (req_id) REFERENCES requisitions (id),
        FOREIGN KEY (vendor_id) REFERENCES vendors (vendor_id)
    )
    ''')

    # Drop the old table if exists for dev purposes (so we can recreate with new schema)
    cursor.execute('DROP TABLE IF EXISTS kso_evaluations')

    # Create KSO Vendor Evaluations Table (7-Dimensi per Blueprint Fase 8)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kso_evaluations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_id TEXT,
        po_number TEXT,
        period_month TEXT,

        vendor_score_delivery INTEGER,
        vendor_score_quality INTEGER,
        vendor_score_response INTEGER,
        vendor_remarks TEXT,

        qc_evaluator_name TEXT,
        qc_score_delivery INTEGER,
        qc_score_quality INTEGER,
        qc_score_response INTEGER,
        qc_remarks TEXT,

        score_pricing INTEGER,
        score_compliance INTEGER,
        score_financial_health INTEGER,
        score_relationship INTEGER,
        dim4_notes TEXT,

        final_score REAL,
        deviation_flag BOOLEAN DEFAULT 0,
        status TEXT DEFAULT 'pending_vendor',
        evaluation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (vendor_id) REFERENCES vendors (vendor_id),
        FOREIGN KEY (po_number) REFERENCES purchase_orders (po_number)
    )
    ''')

    # Create KSO Financial Metrics Table (Phase 5)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kso_metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_id TEXT UNIQUE,
        total_revenue REAL,
        total_volume INTEGER,
        poli_volume INTEGER,
        mcu_volume INTEGER,
        last_sync_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (vendor_id) REFERENCES vendors (vendor_id)
    )
    ''')

    # Create KSO Tariffs Catalog Table (Phase 5)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kso_tariffs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_id TEXT,
        test_name TEXT,
        price REAL,
        FOREIGN KEY (vendor_id) REFERENCES vendors (vendor_id)
    )
    ''')

    # Create Tenders Table (Fase 4 - Manajemen Tender)
    cursor.execute('DROP TABLE IF EXISTS tenders')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tenders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tender_number TEXT UNIQUE,
        title TEXT NOT NULL,
        category TEXT,
        description TEXT,
        specifications TEXT,
        budget_max REAL,
        bid_closing_date TEXT,
        expected_delivery_date TEXT,
        status TEXT DEFAULT 'draft',
        created_by TEXT,
        awarded_vendor_id TEXT,
        notes TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Investment Spending Plans Table (Procurement Realization Plan)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS investment_spending_plans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        month_target TEXT NOT NULL,
        project_title TEXT NOT NULL,
        category TEXT,
        sbu_name TEXT,
        negotiated_price REAL,
        installation_fee REAL,
        testing_fee REAL,
        tax_pct REAL DEFAULT 11.0,
        tax_amount REAL,
        shipping_cost REAL,
        total_amount REAL,
        dp_pct REAL,
        dp_amount REAL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Payment Schedules Table (Finance Tracking)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS payment_schedules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        po_number TEXT UNIQUE,
        project_title TEXT NOT NULL,
        vendor_name TEXT,
        negotiated_amount REAL,
        dp_percentage REAL,
        dp_status TEXT DEFAULT 'Belum Dibayar',
        dp_planned_date TEXT,
        dp_realized_date TEXT,
        remaining_status TEXT DEFAULT 'Belum Dibayar',
        remaining_planned_date TEXT,
        remaining_realized_date TEXT,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == "__main__":
    init_db()

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

    # Create KSO Contracts Table (Fase 5)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS kso_contracts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contract_number TEXT UNIQUE,
        vendor_id TEXT,
        vendor_name TEXT,
        object_name TEXT,
        start_date TEXT,
        end_date TEXT,
        billing_type TEXT,
        status TEXT DEFAULT 'BERJALAN',
        FOREIGN KEY (vendor_id) REFERENCES vendors (vendor_id)
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

    # Create Internal Catalogs (E-Katalog)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS internal_catalogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_name TEXT,
        item_name TEXT NOT NULL,
        unit TEXT,
        sbu_name TEXT,
        price REAL,
        brand TEXT,
        availability_status TEXT,
        year INTEGER,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Quotation Requests (Minta Penawaran)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotation_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        req_number TEXT UNIQUE,
        item_name TEXT NOT NULL,
        target_realization_date TEXT,
        status TEXT DEFAULT 'open',
        awarded_vendor TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Quotation Bids (Nilai Scoring Vendor)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS quotation_bids (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quotation_id INTEGER,
        vendor_name TEXT,
        bid_price REAL,
        score_price INTEGER DEFAULT 0,
        score_quality INTEGER DEFAULT 0,
        score_service INTEGER DEFAULT 0,
        score_needs INTEGER DEFAULT 0,
        score_brand INTEGER DEFAULT 0,
        total_score INTEGER DEFAULT 0,
        is_winner BOOLEAN DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (quotation_id) REFERENCES quotation_requests (id)
    )
    ''')

    # Create MLM Price Comparisons
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mlm_price_comparisons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        po_number TEXT,
        item_name TEXT,
        qty_satuan TEXT,
        harga_mandiri REAL,
        vendor_mandiri TEXT,
        harga_mlm REAL,
        selisih REAL,
        merk TEXT,
        keterangan TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
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

    # Proker Bulanan (Rencana Realisasi RKAP — dibuat Bagian Umum, disetujui GM+Keuangan)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS proker_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_code TEXT UNIQUE,
        item_title TEXT NOT NULL,
        kategori TEXT NOT NULL,
        bidang_pekerjaan TEXT NOT NULL,
        rkap_ref TEXT,
        estimasi_nilai REAL,
        target_bulan TEXT NOT NULL,
        target_vendor TEXT,
        keterangan TEXT,
        submitted_by TEXT,
        status TEXT DEFAULT 'draft',
        approved_gm_by TEXT,
        approved_gm_at DATETIME,
        cleared_keuangan_by TEXT,
        cleared_keuangan_at DATETIME,
        catatan_keuangan TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Vendor Notifications (dipicu saat proker cleared → vendor bidang terkait dapat alert)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendor_notifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_category TEXT NOT NULL,
        title TEXT NOT NULL,
        message TEXT NOT NULL,
        priority TEXT DEFAULT 'normal',
        related_proker_id INTEGER,
        is_read INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (related_proker_id) REFERENCES proker_items (id)
    )
    ''')

    # BAPB — Berita Acara Penerimaan Barang
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bapb (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bapb_number TEXT UNIQUE,
        po_number TEXT NOT NULL,
        vendor_id TEXT,
        received_date TEXT,
        received_by TEXT,
        items_json TEXT,
        condition TEXT DEFAULT 'good',
        notes TEXT,
        status TEXT DEFAULT 'draft',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (po_number) REFERENCES purchase_orders (po_number)
    )
    ''')

    # Gudang Arsip Digital (Dokumen Upload)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT NOT NULL,
        file_path TEXT NOT NULL,
        category TEXT DEFAULT 'Uncategorized',
        uploaded_by TEXT DEFAULT 'System',
        uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        metadata_json TEXT
    )
    ''')

    # Invoices (Fase 7 - 3-Way Match)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        inv_number TEXT UNIQUE NOT NULL,
        po_number TEXT NOT NULL,
        bapb_number TEXT,
        vendor_id TEXT,
        inv_date TEXT,
        inv_due_date TEXT,
        amount REAL NOT NULL,
        notes TEXT,
        status TEXT DEFAULT 'pending',
        match_po BOOLEAN DEFAULT 0,
        match_bapb BOOLEAN DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (po_number) REFERENCES purchase_orders (po_number)
    )
    ''')

    # RKAP SBU Allocations
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rkap_sbu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sbu_name TEXT NOT NULL,
        sbu_code TEXT UNIQUE NOT NULL,
        budget_allocated REAL,
        budget_realized REAL DEFAULT 0,
        year INTEGER DEFAULT 2026
    )
    ''')

    # RKAP Category Allocations
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rkap_categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT NOT NULL,
        category_type TEXT NOT NULL,
        budget_allocated REAL,
        budget_realized REAL DEFAULT 0,
        year INTEGER DEFAULT 2026
    )
    ''')

    # Rencana Pembayaran Vendor — dari laporan Finance (Barang + Jasa + KSO + Rental)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rencana_pembayaran (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        periode TEXT NOT NULL,
        kategori TEXT NOT NULL,
        no_referensi TEXT,
        tanggal_ke_keuangan TEXT,
        vendor TEXT,
        no_po_spk TEXT,
        keterangan TEXT,
        jumlah REAL,
        unit_sbu TEXT,
        status TEXT DEFAULT 'rencana',
        metabisnis TEXT,
        term_of_payment TEXT,
        rencana_bayar TEXT,
        tanggal_transfer TEXT,
        link_legal INTEGER DEFAULT 0,
        link_ksu INTEGER DEFAULT 0,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # RUP Items — dari DataRUP (247 item investasi RKAP 2026)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rup_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        no_item INTEGER,
        kode TEXT,
        trimester INTEGER,
        bulan_target TEXT,
        metabisnis TEXT,
        item_name TEXT NOT NULL,
        kategori TEXT,
        qty REAL,
        satuan TEXT,
        harga_satuan REAL,
        nilai_total REAL,
        unit_dept TEXT,
        switching_flag INTEGER DEFAULT 0,
        status_realisasi TEXT DEFAULT 'belum',
        year INTEGER DEFAULT 2026,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
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

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

    conn.commit()
    conn.close()
    print(f"Database initialized at {DB_PATH}")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == "__main__":
    init_db()

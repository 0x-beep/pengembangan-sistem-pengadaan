#!/usr/bin/env python3
"""
PT KMU VENDOR REGISTRATION FORM - IMPORT TO DATABASE SCRIPT
============================================================

Purpose: Import vendor registration forms (Excel/CSV) into PostgreSQL database
Version: 1.0
Author: PT KMU IT Team
Date: 2025-06-04

Usage:
  python3 vendor_form_import_script.py --file vendor_form.xlsx --action import
  python3 vendor_form_import_script.py --file vendor_form.csv --action validate
  python3 vendor_form_import_script.py --file vendor_form.xlsx --action preview

Requirements:
  - pandas
  - openpyxl (for Excel files)
  - psycopg2 (for PostgreSQL)
  - python-dotenv (for environment variables)

Installation:
  pip install pandas openpyxl psycopg2-binary python-dotenv

Configuration:
  Create .env file with:
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=kmu_procurement
    DB_USER=postgres
    DB_PASSWORD=your_password

"""

import sys
import os
import json
import argparse
from datetime import datetime
import csv
import logging

try:
    import pandas as pd
    import psycopg2
    from psycopg2.extras import RealDictCursor
    from dotenv import load_dotenv
except ImportError as e:
    print(f"❌ Missing dependency: {e}")
    print("Install with: pip install pandas openpyxl psycopg2-binary python-dotenv")
    sys.exit(1)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class VendorFormImporter:
    """Import vendor registration forms into database"""
    
    def __init__(self):
        """Initialize database connection"""
        self.conn = None
        self.cursor = None
        self.form_data = {}
        self.validation_errors = []
        self.import_logs = []
        
    def connect_db(self):
        """Connect to PostgreSQL database"""
        try:
            self.conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', '5432'),
                database=os.getenv('DB_NAME', 'kmu_procurement'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASSWORD', '')
            )
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            logger.info("✅ Connected to database successfully")
            return True
        except psycopg2.Error as e:
            logger.error(f"❌ Database connection failed: {e}")
            return False
    
    def disconnect_db(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")
    
    def load_form_from_excel(self, filepath):
        """Load vendor registration form from Excel file"""
        try:
            df = pd.read_excel(filepath, sheet_name='Registrasi Vendor KMU')
            # Convert DataFrame to dictionary
            self.form_data = df.set_index('Field Name')['Field Value'].to_dict()
            logger.info(f"✅ Loaded form from Excel: {filepath}")
            logger.info(f"   Found {len(self.form_data)} fields")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to load Excel file: {e}")
            return False
    
    def load_form_from_csv(self, filepath):
        """Load vendor registration form from CSV file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    field_name = row.get('Field Name', '').strip()
                    field_value = row.get('Field Value', '').strip()
                    if field_name and field_name not in ['', 'Field Name']:
                        self.form_data[field_name] = field_value
            logger.info(f"✅ Loaded form from CSV: {filepath}")
            logger.info(f"   Found {len(self.form_data)} fields")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to load CSV file: {e}")
            return False
    
    def load_form_from_json(self, filepath):
        """Load vendor registration form from JSON file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                self.form_data = json.load(f)
            logger.info(f"✅ Loaded form from JSON: {filepath}")
            logger.info(f"   Found {len(self.form_data)} fields")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to load JSON file: {e}")
            return False
    
    def validate_form(self):
        """Validate form data"""
        logger.info("\n🔍 VALIDATING FORM DATA...")
        
        # Required fields
        required_fields = [
            'company_name',
            'business_license_number',
            'tax_id_npwp',
            'phone_main',
            'email_company',
            'office_address_street',
            'office_address_city',
            'contact_person_name',
            'contact_person_phone',
            'contact_person_email',
            'bank_name',
            'bank_account_number',
            'bank_account_holder',
            'can_serve_balikpapan',
            'has_delivery_vehicles',
            'working_capital_idr',
            'has_liability_insurance',
            'liability_insurance_amount',
            'customer_reference_1',
            'customer_reference_2',
            'customer_reference_3'
        ]
        
        # Check required fields
        for field in required_fields:
            if field not in self.form_data or not self.form_data[field]:
                error = f"❌ Missing required field: {field}"
                self.validation_errors.append(error)
                logger.warning(f"   {error}")
        
        # Validate email format
        if 'email_company' in self.form_data:
            email = self.form_data['email_company']
            if '@' not in email:
                error = f"❌ Invalid email format: {email}"
                self.validation_errors.append(error)
                logger.warning(f"   {error}")
        
        # Validate Balikpapan service capability (MANDATORY)
        if self.form_data.get('can_serve_balikpapan') != 'YES' and \
           self.form_data.get('can_serve_balikpapan') != 'TRUE' and \
           self.form_data.get('can_serve_balikpapan') != '✓':
            error = "❌ MANDATORY: Must be able to serve Balikpapan"
            self.validation_errors.append(error)
            logger.warning(f"   {error}")
        
        # Validate financial information
        try:
            if 'working_capital_idr' in self.form_data:
                float(self.form_data['working_capital_idr'])
        except ValueError:
            error = f"❌ Invalid working capital amount: {self.form_data.get('working_capital_idr')}"
            self.validation_errors.append(error)
            logger.warning(f"   {error}")
        
        if self.validation_errors:
            logger.info(f"\n⚠️  Validation found {len(self.validation_errors)} error(s)")
            return False
        else:
            logger.info("✅ All validations passed!")
            return True
    
    def generate_vendor_id(self):
        """Generate unique vendor ID"""
        try:
            self.cursor.execute("SELECT COUNT(*) as count FROM vendors")
            count = self.cursor.fetchone()['count']
            vendor_id = f"VND-{str(count + 1).zfill(3)}"
            logger.info(f"Generated Vendor ID: {vendor_id}")
            return vendor_id
        except Exception as e:
            logger.error(f"❌ Failed to generate vendor ID: {e}")
            return None
    
    def generate_application_ref(self):
        """Generate application reference number"""
        today = datetime.now()
        try:
            self.cursor.execute(
                "SELECT COUNT(*) as count FROM vendors WHERE DATE(registration_date) = %s",
                (today.date(),)
            )
            count = self.cursor.fetchone()['count']
            app_ref = f"APP-{today.strftime('%Y-%m-%d')}-{str(count + 1).zfill(3)}"
            logger.info(f"Generated Application Reference: {app_ref}")
            return app_ref
        except Exception as e:
            logger.error(f"❌ Failed to generate application ref: {e}")
            return None
    
    def import_to_database(self):
        """Import validated form data into database"""
        logger.info("\n📤 IMPORTING TO DATABASE...")
        
        if not self.validate_form():
            logger.error("Cannot import - validation failed")
            return False
        
        if not self.connect_db():
            return False
        
        try:
            # Generate IDs
            vendor_id = self.generate_vendor_id()
            app_ref = self.generate_application_ref()
            
            if not vendor_id or not app_ref:
                raise Exception("Failed to generate required IDs")
            
            # Prepare vendor data
            vendor_data = {
                'vendor_id': vendor_id,
                'company_name': self.form_data.get('company_name'),
                'company_name_short': self.form_data.get('company_name_short', ''),
                'vendor_type': self.form_data.get('vendor_type'),
                'vendor_category': self.form_data.get('vendor_category'),
                'phone': self.form_data.get('phone_main'),
                'email': self.form_data.get('email_company'),
                'website': self.form_data.get('website', ''),
                'address_street': self.form_data.get('office_address_street'),
                'address_city': self.form_data.get('office_address_city'),
                'address_province': self.form_data.get('office_address_province'),
                'address_postal_code': self.form_data.get('office_address_postal_code'),
                'address_country': 'Indonesia',
                'npwp': self.form_data.get('tax_id_npwp'),
                'sio': self.form_data.get('business_license_number'),
                'bank_name': self.form_data.get('bank_name'),
                'bank_account_number': self.form_data.get('bank_account_number'),
                'bank_account_holder': self.form_data.get('bank_account_holder'),
                'contact_person_name': self.form_data.get('contact_person_name'),
                'contact_person_title': self.form_data.get('contact_person_title'),
                'contact_person_phone': self.form_data.get('contact_person_phone'),
                'contact_person_email': self.form_data.get('contact_person_email'),
                'vendor_status': 'submitted',
                'registration_date': datetime.now(),
                'notes': f"Application Ref: {app_ref}"
            }
            
            # Build INSERT query
            columns = ', '.join(vendor_data.keys())
            placeholders = ', '.join(['%s'] * len(vendor_data))
            query = f"INSERT INTO vendors ({columns}) VALUES ({placeholders}) RETURNING id"
            
            # Execute insert
            self.cursor.execute(query, list(vendor_data.values()))
            vendor_pk_id = self.cursor.fetchone()['id']
            self.conn.commit()
            
            logger.info(f"✅ Vendor record created in database")
            logger.info(f"   Database ID: {vendor_pk_id}")
            logger.info(f"   Vendor ID: {vendor_id}")
            logger.info(f"   Application Reference: {app_ref}")
            
            # Log import activity
            activity_log = {
                'activity_type': 'vendor_registration_submitted',
                'entity_type': 'vendor',
                'entity_id': vendor_pk_id,
                'entity_reference': vendor_id,
                'action_date': datetime.now(),
                'description': f'Vendor registration form submitted: {vendor_data["company_name"]}',
                'vendor_id': vendor_pk_id,
                'metadata': json.dumps({'application_ref': app_ref})
            }
            
            columns = ', '.join(activity_log.keys())
            placeholders = ', '.join(['%s'] * len(activity_log))
            activity_query = f"INSERT INTO activity_log ({columns}) VALUES ({placeholders})"
            
            self.cursor.execute(activity_query, list(activity_log.values()))
            self.conn.commit()
            
            logger.info("✅ Activity logged successfully")
            
            self.import_logs.append({
                'status': 'SUCCESS',
                'company_name': vendor_data['company_name'],
                'vendor_id': vendor_id,
                'application_ref': app_ref,
                'timestamp': datetime.now().isoformat()
            })
            
            return True
            
        except Exception as e:
            self.conn.rollback()
            logger.error(f"❌ Import failed: {e}")
            self.import_logs.append({
                'status': 'FAILED',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            })
            return False
        finally:
            self.disconnect_db()
    
    def preview_form(self):
        """Show preview of form data"""
        logger.info("\n👁️ FORM DATA PREVIEW")
        logger.info("=" * 60)
        
        for field, value in sorted(self.form_data.items()):
            logger.info(f"  {field:.<40} {value}")
        
        logger.info("=" * 60)
        logger.info(f"\nTotal fields: {len(self.form_data)}")
    
    def generate_import_report(self, output_file=None):
        """Generate import report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_records': len(self.import_logs),
            'successful': sum(1 for log in self.import_logs if log['status'] == 'SUCCESS'),
            'failed': sum(1 for log in self.import_logs if log['status'] == 'FAILED'),
            'validation_errors': self.validation_errors,
            'import_logs': self.import_logs
        }
        
        if output_file:
            with open(output_file, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"\n✅ Report saved to: {output_file}")
        
        return report

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description='PT KMU Registrasi Vendor KMU Form Importer'
    )
    parser.add_argument(
        '--file',
        required=True,
        help='Path to vendor registration form file (Excel, CSV, or JSON)'
    )
    parser.add_argument(
        '--action',
        choices=['validate', 'preview', 'import'],
        default='validate',
        help='Action to perform: validate, preview, or import'
    )
    parser.add_argument(
        '--report',
        help='Output file for import report (JSON)'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        logger.error(f"❌ File not found: {args.file}")
        sys.exit(1)
    
    # Determine file type
    file_ext = os.path.splitext(args.file)[1].lower()
    
    # Initialize importer
    importer = VendorFormImporter()
    
    # Load form based on file type
    if file_ext in ['.xlsx', '.xls']:
        success = importer.load_form_from_excel(args.file)
    elif file_ext == '.csv':
        success = importer.load_form_from_csv(args.file)
    elif file_ext == '.json':
        success = importer.load_form_from_json(args.file)
    else:
        logger.error(f"❌ Unsupported file format: {file_ext}")
        sys.exit(1)
    
    if not success:
        sys.exit(1)
    
    # Perform requested action
    if args.action == 'preview':
        importer.preview_form()
    elif args.action == 'validate':
        importer.validate_form()
        if importer.validation_errors:
            logger.info(f"\n❌ {len(importer.validation_errors)} validation error(s) found")
        else:
            logger.info("\n✅ Form validation successful - ready for import")
    elif args.action == 'import':
        success = importer.import_to_database()
        if args.report:
            importer.generate_import_report(args.report)
        sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()

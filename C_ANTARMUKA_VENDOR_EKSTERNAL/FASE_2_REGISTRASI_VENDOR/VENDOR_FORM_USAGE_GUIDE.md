# VENDOR REGISTRATION FORM - USAGE GUIDE FOR VENDORS & IT

**PT KMU Registrasi Vendor KMU System**  
Version 1.0  
Date: June 2025

---

## 📋 WHAT YOU HAVE: 3 FORM FORMATS

### Format 1: Excel Fillable Form
**File:** `VENDOR_REGISTRATION_FORM_TEMPLATE.xlsx` (Create with IT)
**For:** Vendors who prefer Excel
**How to use:**
1. Download Excel file from PT KMU website
2. Fill in all fields marked with * (required)
3. Save as: `VENDOR_REGISTRATION_[YourCompanyName].xlsx`
4. Email to: vendor-registration@kmu.co.id
5. Attach supporting documents as PDF files

**Excel structure:**
- Sheet 1: "Registrasi Vendor KMU" (main form)
- Sheet 2: "Instructions" (how to fill out)
- Sheet 3: "Dropdown Options" (valid values for dropdowns)

---

### Format 2: JSON Structure
**File:** `VENDOR_REGISTRATION_FORM_STRUCTURE.json`
**For:** System integration & IT processing
**Contains:**
- All field definitions
- Data types for each field
- Required/optional indicators
- Database column mappings
- Dropdown options
- Validation rules

**Usage for developers:**
```bash
# Validate vendor form against schema
python3 -m jsonschema vendor_form.json VENDOR_REGISTRATION_FORM_STRUCTURE.json

# Use as API request body
curl -X POST https://api.kmu.co.id/vendor/register \
  -H "Content-Type: application/json" \
  -d @vendor_form.json
```

---

### Format 3: CSV Import Template
**File:** `VENDOR_REGISTRATION_FORM_TEMPLATE_STRUCTURE.csv`
**For:** Bulk imports & IT system integration
**Structure:**
- Column 1: Field Name (internal system name)
- Column 2: Field Label (display name)
- Column 3: Field Type (TEXT, NUMBER, DATE, DROPDOWN, CHECKBOX)
- Column 4: Required (YES/NO)
- Column 5: Field Value (filled by vendor)
- Column 6: Database Column (where data goes)

**IT Usage:**
```bash
# Import CSV directly to PostgreSQL
python3 vendor_form_import_script.py --file vendor_form.csv --action import

# Validate before importing
python3 vendor_form_import_script.py --file vendor_form.csv --action validate

# Preview data
python3 vendor_form_import_script.py --file vendor_form.csv --action preview
```

---

## 🤖 IT INTEGRATION: AUTOMATED IMPORT PROCESS

### Step 1: Vendor Submits Form
```
Vendor (via email):
├─ Excel file: VENDOR_REGISTRATION_PT_Medik_Jaya.xlsx
├─ Supporting docs: 
│  ├─ business_license.pdf
│  ├─ tax_id.pdf
│  ├─ financial_statements.pdf
│  └─ insurance_cert.pdf
└─ Email to: vendor-registration@kmu.co.il
```

### Step 2: IT Validates Form
```bash
# Command 1: Validate form
python3 vendor_form_import_script.py \
  --file "VENDOR_REGISTRATION_PT_Medik_Jaya.xlsx" \
  --action validate

# Output:
# ✅ All validations passed!
# OR
# ❌ 3 validation error(s) found
#   - Missing required field: company_name
#   - Invalid email format: invalid@
#   - MANDATORY: Must be able to serve Balikpapan
```

### Step 3: Preview Form Data (Optional)
```bash
# Command 2: Preview what will be imported
python3 vendor_form_import_script.py \
  --file "VENDOR_REGISTRATION_PT_Medik_Jaya.xlsx" \
  --action preview

# Output shows all fields to be imported
```

### Step 4: Import to Database
```bash
# Command 3: Import to database
python3 vendor_form_import_script.py \
  --file "VENDOR_REGISTRATION_PT_Medik_Jaya.xlsx" \
  --action import \
  --report import_report_20250604.json

# Output:
# ✅ Connected to database successfully
# Generated Vendor ID: VND-045
# Generated Application Reference: APP-2025-06-04-001
# ✅ Vendor record created in database
#    Database ID: 127
#    Vendor ID: VND-045
#    Application Reference: APP-2025-06-04-001
# ✅ Activity logged successfully
```

### Step 5: Report Generated
```json
{
  "timestamp": "2025-06-04T14:30:00",
  "total_records": 1,
  "successful": 1,
  "failed": 0,
  "validation_errors": [],
  "import_logs": [
    {
      "status": "SUCCESS",
      "company_name": "PT Medik Jaya Indonesia",
      "vendor_id": "VND-045",
      "application_ref": "APP-2025-06-04-001",
      "timestamp": "2025-06-04T14:30:00"
    }
  ]
}
```

---

## 🔧 FOR IT: SETUP INSTRUCTIONS

### Prerequisites
```bash
# Install required packages
pip install pandas openpyxl psycopg2-binary python-dotenv

# Create .env file
cat > .env << EOF
DB_HOST=localhost
DB_PORT=5432
DB_NAME=kmu_procurement
DB_USER=postgres
DB_PASSWORD=your_password
EOF
```

### Create Excel Template
```python
# Use this Python code to generate Excel template
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill
import json

# Load JSON structure
with open('VENDOR_REGISTRATION_FORM_STRUCTURE.json') as f:
    form_structure = json.load(f)

# Create Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Registrasi Vendor KMU"

# Write headers
ws['A1'] = "FIELD NAME"
ws['B1'] = "FIELD LABEL"
ws['C1'] = "FIELD VALUE"
ws['D1'] = "REQUIRED"

# Style headers
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_font = Font(bold=True, color="FFFFFF")
for cell in ['A1', 'B1', 'C1', 'D1']:
    ws[cell].fill = header_fill
    ws[cell].font = header_font

# Add form fields from JSON structure
row = 2
for section_name, section_data in form_structure.items():
    if section_name.startswith('section_'):
        for field_key, field_info in section_data.items():
            ws[f'A{row}'] = field_key
            ws[f'B{row}'] = field_info.get('label', '')
            ws[f'C{row}'] = ''  # Empty for vendor to fill
            ws[f'D{row}'] = "YES" if field_info.get('required') else "NO"
            row += 1

# Set column widths
ws.column_dimensions['A'].width = 30
ws.column_dimensions['B'].width = 40
ws.column_dimensions['C'].width = 40
ws.column_dimensions['D'].width = 10

# Save
wb.save('VENDOR_REGISTRATION_FORM_TEMPLATE.xlsx')
print("✅ Excel template created: VENDOR_REGISTRATION_FORM_TEMPLATE.xlsx")
```

### Set Up Database Tables
```sql
-- Run database initialization script
psql -U postgres -d kmu_procurement -f 001-database-init.sql

-- Verify tables created
SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public' AND table_name IN ('vendors', 'activity_log');

-- Output should show:
-- vendors table ✅
-- activity_log table ✅
```

### Create Import Workflow
```bash
#!/bin/bash
# save as: vendor_import_workflow.sh

FORM_FOLDER="/incoming_vendor_forms"
LOG_FILE="/logs/vendor_import.log"
REPORT_FOLDER="/reports"

# Monitor for new form files
for file in $FORM_FOLDER/*.xlsx; do
    if [ -f "$file" ]; then
        echo "$(date): Processing $file" >> $LOG_FILE
        
        # Validate
        python3 vendor_form_import_script.py --file "$file" --action validate
        
        if [ $? -eq 0 ]; then
            # Import
            python3 vendor_form_import_script.py \
              --file "$file" \
              --action import \
              --report "$REPORT_FOLDER/report_$(date +%Y%m%d_%H%M%S).json"
            
            # Move to processed folder
            mv "$file" "$FORM_FOLDER/processed/"
            echo "✅ $file imported successfully" >> $LOG_FILE
        else
            # Move to error folder for review
            mv "$file" "$FORM_FOLDER/errors/"
            echo "❌ $file validation failed" >> $LOG_FILE
        fi
    fi
done
```

### API Integration (Optional)
```python
# If using API instead of direct import
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/api/vendor/register', methods=['POST'])
def register_vendor():
    """Receive vendor form via API"""
    try:
        form_data = request.json
        importer = VendorFormImporter()
        importer.form_data = form_data
        
        if importer.import_to_database():
            return jsonify({
                'status': 'success',
                'vendor_id': importer.form_data.get('vendor_id'),
                'message': 'Vendor registered successfully'
            }), 201
        else:
            return jsonify({
                'status': 'error',
                'errors': importer.validation_errors,
                'message': 'Vendor registration failed'
            }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=False, port=5000)
```

---

## 📊 DATA FLOW DIAGRAM

```
VENDOR SUBMITS FORM
        ↓
┌──────────────────────────────────────┐
│  Form File (Excel/CSV/JSON)          │
│  + Supporting Documents (PDF)         │
└──────────────────────────────────────┘
        ↓
IT RECEIVES & VALIDATES
        ↓
python vendor_form_import_script.py
  --file vendor_form.xlsx
  --action validate
        ↓
  ✅ All validations pass? → YES → proceed
  ❌ Validation errors? → NO → send back to vendor
        ↓
python vendor_form_import_script.py
  --file vendor_form.xlsx
  --action import
  --report report.json
        ↓
DATA INSERTED INTO DATABASE
        ├─ vendors table (company info)
        ├─ vendor_portal_users table (login created)
        └─ activity_log table (timestamp recorded)
        ↓
VENDOR_ID GENERATED (VND-XXX)
APPLICATION_REF GENERATED (APP-2025-06-04-XXX)
        ↓
REPORT GENERATED (JSON)
        ↓
VENDOR NOTIFIED
```

---

## ✅ CHECKLIST FOR VENDORS

Before submitting form:

```
☐ Downloaded vendor registration form (Excel)
☐ Read instructions carefully
☐ Filled ALL fields marked with * (required)
☐ Company location: Balikpapan service (MANDATORY)
☐ Valid email format (contains @)
☐ Phone numbers in correct format
☐ Annual revenue in numbers only (no symbols)
☐ Dates in correct format (DD/MM/YYYY or YYYY-MM-DD)
☐ Selected correct dropdown options
☐ Checked all applicable checkboxes
☐ Provided 3 customer references
☐ Declared truthfulness (checked declaration box)
☐ Attached all required documents:
   ☐ Business License (SIU)
   ☐ Tax ID (NPWP)
   ☐ Company Registration
   ☐ Bank Reference Letter
   ☐ Financial Statements (2 years)
   ☐ Insurance Certificates
☐ Signed form (or director signature)
☐ Saved form with correct name: VENDOR_REGISTRATION_[CompanyName].xlsx
☐ All documents are PDF format
☐ Total file size under 50MB
☐ Ready to submit to: vendor-registration@kmu.co.id
```

---

## ❓ TROUBLESHOOTING

### Problem: "Missing required field: company_name"
**Solution:** Make sure the company name field is filled in the Excel form

### Problem: "Invalid email format"
**Solution:** Email must contain @ symbol and valid domain (e.g., sales@company.co.id)

### Problem: "Database connection failed"
**Solution:** Check .env file has correct database credentials

### Problem: "Vendor ID generation failed"
**Solution:** Ensure database connection is working, check vendors table exists

### Problem: "MANDATORY: Must be able to serve Balikpapan"
**Solution:** Check the "Can Serve Balikpapan?" checkbox in operational capability section

### Problem: Form validation passes but import fails
**Solution:** Check database connection, ensure all tables exist, check database permissions

---

## 📞 SUPPORT

**For Vendors:**
- Email: vendor-registration@kmu.co.id
- Phone: [Contact number]
- Hours: Monday-Friday, 8 AM - 4 PM Kaltim time

**For IT:**
- Technical: Claude Code / Python documentation
- Database: PostgreSQL admin
- Email: it-support@kmu.co.id

---

## 📝 VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-06-04 | Initial release - 3 form formats + import script |

---

**Everything ready to go!** 🚀

Vendors can fill forms easily, IT can import automatically. Zero manual data entry needed!


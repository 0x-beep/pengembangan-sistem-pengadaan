# SOP UPLOAD & MANAGEMENT GUIDE
## Quick Reference for KMU Procurement Team

---

## 🚀 QUICK START: Uploading Your Procedures

### Step 1: Gather All Documents
```
Collect ALL company procedures:

✓ SOP-Pengadaan.pdf (Main procurement procedure)
✓ Prosedur-Approval.docx (Approval workflows)
✓ Checklist-3WayMatch.xlsx (Payment verification)
✓ Guidelines-Vendor.pdf (Vendor management)
✓ Prosedur-RiskManagement.pdf (Risk assessment)
✓ Instruksi-BidEvaluation.docx (Quote evaluation)
✓ Pedoman-BudgetControl.pdf (Budget management)
✓ ... (all other procedures)

Format accepted:
- PDF (scanned or digital)
- Word (.docx, .doc)
- Excel (.xlsx)
- PowerPoint (.pptx)
- Text files
- Images (JPG, PNG)
```

### Step 2: Organize & Name Documents

```
Good naming convention:
├─ SOP-001-Tender-Creation.pdf
├─ SOP-002-Quote-Evaluation.pdf
├─ SOP-003-PO-Approval.pdf
├─ SOP-004-Payment-Processing.pdf
├─ Guidelines-Vendor-Management.pdf
├─ Checklist-3WayMatch.xlsx
└─ Training-Guide-Procurement.pdf

Why organized naming?
- AI can quickly identify document type
- Version control easier (SOP-003-v2.0.pdf)
- System can auto-categorize
```

### Step 3: Upload to System

```
UPLOAD PORTAL URL: https://procurement.kmu.co.id/sop-guardian/upload

Steps:
1. Click [UPLOAD DOCUMENTS] button
2. Select files (multi-select OK)
3. Fill metadata:
   ├─ Document Name: SOP-003 PO Approval Process
   ├─ Category: Procurement
   ├─ Version: 2.0
   ├─ Effective Date: 2025-01-01
   └─ Owner: Manager Pengadaan
4. Click [UPLOAD]
5. System processes documents (5-30 min depending on size)

For large batches (20+ docs):
- Use bulk upload: Select folder
- System processes in background
- You get email when done
```

### Step 4: Verify Extraction Quality

```
EXTRACTION QUALITY CHECK

After upload, system shows:

┌─────────────────────────────────────┐
│ SOP-003-PO-Approval.pdf             │
├─────────────────────────────────────┤
│ Extraction Status: ✅ COMPLETED     │
│ Confidence: 98.5%                   │
│                                     │
│ Extracted Procedures:               │
│ ✅ Tender Creation                  │
│ ✅ Quote Evaluation                 │
│ ✅ PO Approval                      │
│ ✅ Payment Processing               │
│                                     │
│ Steps Identified: 47                │
│ Rules Extracted: 23                 │
│                                     │
│ [REVIEW] [APPROVE] [NEEDS_WORK]    │
└─────────────────────────────────────┘

If confidence < 90%:
- System flags for manual review
- You can manually add missing procedures
- AI learns from corrections
```

---

## 📋 PROCEDURE STRUCTURE (What AI Looks For)

When AI reads your procedures, it extracts:

```
PROCEDURE ANATOMY:

1. IDENTIFICATION
   - Name: "PO Approval Process"
   - SOP ID: SOP-003
   - Version: 2.0
   - Effective Date: 2025-01-01

2. AUDIENCE
   - Applicable to: Kepala Bagian Keuangan, Director
   - When to use: When PO amount > 100M

3. SEQUENTIAL STEPS
   Step 1: Create PO
   └─ Responsible: Admin Pengadaan Barang
   └─ Condition: Tender must be closed
   └─ Expected outcome: PO generated
   
   Step 2: Submit for Finance Review
   └─ Responsible: Admin Pengadaan Barang
   └─ Condition: PO created with all details
   └─ Expected outcome: Kepala Bagian Keuangan notified
   
   Step 3: Finance reviews budget
   └─ Responsible: Kepala Bagian Keuangan
   └─ Condition: PO received
   └─ Expected outcome: Approval or rejection

4. APPROVAL RULES
   - Amount <= 100M: Auto-approve
   - 100M-500M: Kepala Bagian Keuangan approval
   - > 500M: Director approval

5. REQUIRED DOCUMENTS
   - Invoice
   - BAPB (BAPB (Berita Acara Penerimaan Barang))
   - Vendor agreement

6. TIMELINE
   - SLA: 2 days from creation
   - Escalation: If not approved in 2 days, notify Director

7. EXCEPTIONS
   - Emergency procurement: Can expedite by CxO approval
   - Framework agreement: Different process applies
```

---

## 🎯 REAL-WORLD EXAMPLES: How AI Uses Your SOPs

### Example 1: User Tries to Approve PO Without Finance Review

```
USER ACTION:
Admin Pengadaan Barang tries to approve 350M PO

AI CHECKS:
├─ SOP-003 Step 2: "Finance review required for > 100M"
├─ Finds: Finance review NOT completed yet
└─ Decision: 🔴 BLOCK

ALERT SHOWS:
┌─────────────────────────────────────┐
│ ❌ CANNOT APPROVE YET                │
├─────────────────────────────────────┤
│                                     │
│ SOP-003 Step 2 says:                │
│ "Finance review required for PO     │
│  amounts > 100M"                    │
│                                     │
│ Your PO: 350M (needs Finance OK)   │
│                                     │
│ WHAT TO DO:                         │
│ 1. Submit to Kepala Bagian Keuangan        │
│ 2. Wait for approval (SLA: 2 days)  │
│ 3. Then you can route to signature  │
│                                     │
│ [SUBMIT TO FINANCE] [LEARN SOP]    │
└─────────────────────────────────────┘
```

### Example 2: User Asks "Can I Approve This?"

```
USER QUESTION (via Chatbot):
"Saya Admin Pengadaan Barang, bisa approve PO 300 juta?"

AI CHECKS:
├─ SOP-003 Approval Matrix: Who can approve what?
├─ Finds: "Admin Pengadaan Barang - CANNOT approve"
├─ Only: "Kepala Bagian Keuangan (100M-500M) or Director (>500M)"
└─ Prepares answer

CHATBOT RESPONDS:
┌─────────────────────────────────────┐
│ 🤖 No, you cannot approve.          │
├─────────────────────────────────────┤
│                                     │
│ Per SOP-003 "PO Approval Process":  │
│                                     │
│ Admin Pengadaan Barang role:           │
│ ✓ Create PO ✓ Submit to Finance    │
│ ✗ Cannot approve                    │
│                                     │
│ Who CAN approve 300M PO?            │
│ → Kepala Bagian Keuangan (SOP-003 Step 3) │
│                                     │
│ YOUR NEXT STEP:                     │
│ Submit this PO to Kepala Bagian Keuangan   │
│ Expected review time: 1-2 days      │
│                                     │
│ [SUBMIT NOW] [VIEW FULL SOP]       │
└─────────────────────────────────────┘
```

### Example 3: SLA Breach Detection & Escalation

```
SYSTEM MONITORING (Daily at 10:00 AM):

Check all pending POs:
├─ PO-100: Created Jun 20 (2 days ago) - ALERT!
│  Status: Pending Finance approval
│  SOP-003 says: Max 2 days
│  Decision: SLA BREACHED
│
└─ Actions triggered:
   ├─ Flag on Finance dashboard: 🔴 OVERDUE
   ├─ Send email to Kepala Bagian Keuangan
   ├─ Notify via Slack
   ├─ If still pending > 3 days → Escalate to Director
   └─ Log for compliance report

EMAIL SENT TO FINANCE MANAGER:
┌─────────────────────────────────────┐
│ ⚠️ SLA BREACH - URGENT ACTION       │
├─────────────────────────────────────┤
│ PO-100 approval SLA expires today   │
│                                     │
│ Created: Jun 20                     │
│ Deadline: Jun 22 (TODAY)            │
│ Days pending: 2 (at limit)          │
│                                     │
│ [APPROVE NOW] [REQUEST EXTENSION]   │
│ [VIEW DETAILS]                      │
└─────────────────────────────────────┘
```

---

## 🔄 PROCEDURE UPDATE WORKFLOW

### When Procedures Change

```
SCENARIO: Finance changes approval limits

OLD SOP-003:
- Kepala Bagian Keuangan: 100M-500M
- Director: > 500M

NEW SOP-003:
- Kepala Bagian Keuangan: 100M-300M (CHANGED)
- Direktur Keuangan, SDM dan Umum: 300M-500M (NEW)
- Director: > 500M

STEPS TO UPDATE:

1. Document the change
   ├─ New version: 2.1
   ├─ Change date: 2025-07-01
   ├─ Reason: "Efficiency improvement"
   └─ Changed by: Direktur Keuangan, SDM dan Umum

2. Upload new SOP document
   File: SOP-003-v2.1-PO-Approval.pdf
   
3. AI processes new version
   └─ Extracts new approval matrix
   
4. System validates
   ├─ Compares to old version
   ├─ Identifies changes
   ├─ Updates validation rules
   └─ Ready for enforcement

5. Notify affected users
   Email: "SOP-003 updated. New approval limits effective 2025-07-01"

6. Future validations use new rules
   └─ Direktur Keuangan, SDM dan Umum now can approve 300M-500M
```

---

## 📊 COMPLIANCE METRICS YOU'LL GET

After AI Guardian is running, you can see:

```
MONTHLY COMPLIANCE REPORT

═══════════════════════════════════════════════════

COMPLIANCE SCORE: 94.3% (Target: 90%)

Breakdown:
├─ Approval Authority Compliance: 98.5% ✅
├─ SLA Compliance: 93.2% ⚠️ (improving)
├─ Documentation Completeness: 92.1% ⚠️
├─ Sequence Compliance: 96.8% ✅
└─ Threshold Compliance: 100% ✅

VIOLATIONS THIS MONTH: 12 total
├─ Critical: 0 (prevented by AI)
├─ High: 2 (user acknowledged)
├─ Medium: 5 (minor deviations)
└─ Low: 5 (logged for review)

PER-USER COMPLIANCE RANKING:
┌──────────────────────┬───────┬─────────────┐
│ User/Department      │ Score │ Violations  │
├──────────────────────┼───────┼─────────────┤
│ Procurement Team Avg │ 96.2% │ 2 (low)    │
│ Finance Team Avg     │ 93.5% │ 5 (mixed)  │
│ Kepala Unit yang Memintas Avg    │ 91.3% │ 4 (low)    │
│ Director             │ 98.1% │ 1 (high)   │
└──────────────────────┴───────┴─────────────┘

PROCEDURE EFFECTIVENESS:
├─ SOP-001: 98% adherence ✅
├─ SOP-002: 95% adherence ✅
├─ SOP-003: 89% adherence ⚠️ (needs attention)
├─ SOP-004: 96% adherence ✅
└─ SOP-005: 82% adherence 🔴 (CRITICAL)

ACTION ITEMS:
1. Review SOP-003 & SOP-005 with teams
2. Provide targeted training for low-performing areas
3. Consider process optimization
```

---

## ❓ FREQUENTLY ASKED QUESTIONS

**Q: What if a document is old or outdated?**
A: Upload the correct version with "v2.0" in the name or date. AI will detect the newer version and use that. Old versions kept in archive.

**Q: Can AI understand handwritten procedures?**
A: Yes! Take a clear photo of handwritten documents (JPG/PNG). AI can read handwriting. Just make sure image is clear.

**Q: What if a procedure has exceptions?**
A: Include exceptions clearly in the document. AI looks for:
   - "Exception:" or "Exception to the above rule..."
   - "In case of emergency..."
   - "Alternative procedure..."
   AI will extract and enforce exceptions correctly.

**Q: Can users override an AI block?**
A: Only if severity is "high" or below. "Critical" blocks require manager approval. This ensures compliance.

**Q: How fast is the validation?**
A: Sub-second (< 500ms). User doesn't wait.

**Q: What about procedures in Indonesian/local languages?**
A: AI is multilingual. Works with Indonesian, English, mixed. Just upload naturally.

**Q: Can AI learn from mistakes?**
A: Yes. If AI incorrectly flags something:
   - You can provide feedback: "This is actually allowed"
   - System logs the correction
   - AI improves over time (supervised learning)

**Q: What if someone deliberately violates procedures?**
A: All violations logged with user ID and timestamp. Full audit trail. Perfect for SPI review and disciplinary action if needed.

---

## 📞 SUPPORT & CONTACTS

**Technical Issues:**
- IT Support: it-support@kmu.co.id
- Chatbot Training: ai-training@kmu.co.id

**Procedure Questions:**
- Manager Pengadaan: procurement@kmu.co.id
- Kepala Bagian Keuangan: finance@kmu.co.id
- Compliance/SPI: compliance@kmu.co.id

**AI Guardian System:**
- Project Lead: [System Owner Name]
- Email: procurement-innovation@kmu.co.id

---

## 🎓 TRAINING SCHEDULE

```
Week 1: System Introduction
- What is AI Procedure Guardian?
- How it helps your work
- Live demo

Week 2: Hands-On Training
- Upload your SOPs
- Run sample validations
- Ask chatbot questions

Week 3: Advanced Usage
- Interpreting compliance reports
- Updating procedures
- Providing feedback to AI

Week 4: Go-Live Support
- Live monitoring
- Issue resolution
- Feedback collection
```

---

## ✅ IMPLEMENTATION CHECKLIST FOR KMU TEAM

```
BEFORE IT DEPLOYMENT:

[ ] Gather all current SOPs/procedures
[ ] Organize documents with clear naming
[ ] Identify SOP owners (who is responsible?)
[ ] Review document quality (legible, complete?)
[ ] Identify any procedures missing from collection
[ ] Notify all teams about upcoming system
[ ] Schedule training sessions
[ ] Identify super-users for peer support

DOCUMENTS NEEDED:

[ ] Tender creation procedures
[ ] Quote evaluation guidelines
[ ] PO approval workflow
[ ] Payment processing procedures
[ ] Vendor management guidelines
[ ] Budget control instructions
[ ] Risk assessment procedures
[ ] Dispute resolution guidelines
[ ] Contract management process
[ ] Training & documentation requirements
[ ] ... (all other KMU-specific procedures)

FIRST WEEK AFTER GO-LIVE:

[ ] Daily check: Any critical errors?
[ ] Monitor compliance metrics
[ ] Collect user feedback
[ ] Address questions via chatbot
[ ] Schedule refinement sessions if needed
[ ] Weekly status report to leadership
```

---

## 🚀 SUCCESS METRICS

After 1 month of using AI Guardian:

```
TARGET OUTCOMES:

Compliance: 90% → 95%+ ✅
SLA Achievement: 85% → 98%+ ✅
Errors Prevented: Start from 0, aim for 90% of issues caught ✅
User Training Time: 2-3 weeks → 3-5 days ✅
Audit Findings: 45-50 per Q → <5 per Q ✅
User Satisfaction: Measure via feedback ✅

HOW WE'LL MEASURE:

Weekly:
- Compliance score trend
- Violation count (should decrease)
- User questions handled

Monthly:
- Compliance report generation
- SOP adherence analysis
- Per-user performance review
- System reliability metrics
```

---

## 📚 ADDITIONAL RESOURCES

**Documentation:**
- Full System Guide: [Link to complete guide]
- API Documentation: [Link to API docs]
- Troubleshooting Guide: [Link]

**Contact & Support:**
- Slack Channel: #procurement-guardian
- Email: procure-guardian-support@kmu.co.id
- Phone: Extension 5555

---

**Ready to upload your SOPs and activate AI Guardian?** 🚀

Next Step: Gather your documents and start uploading!

Questions? Ask in Slack #procurement-guardian or email support team.


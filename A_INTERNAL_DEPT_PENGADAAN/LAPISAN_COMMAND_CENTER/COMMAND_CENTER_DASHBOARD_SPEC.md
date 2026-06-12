# PROCUREMENT COMMAND CENTER
## Real-Time Management Dashboard Specification

**Purpose:** Single pane of glass for management to monitor ALL procurement activities in real-time  
**Target Users:** BOD, GM Operasi, Direktur Keuangan, SDM dan Umum, Manager Pengadaan  
**Update Frequency:** Real-time (WebSocket, sub-second latency)  
**Display:** Large format (43"+ monitors, wall-mounted or control room)

---

## DASHBOARD LAYOUT (Command Center View)

```
╔════════════════════════════════════════════════════════════════════════════════╗
║                    PROCUREMENT COMMAND CENTER                                  ║
║                  Real-Time Monitoring Dashboard v1.0                            ║
║  Time: 2025-06-20 14:32:15 | Mode: LIVE | Status: ALL SYSTEMS OPERATIONAL     ║
╚════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────┬─────────────────────────────┬──────────────────────┐
│                             │                             │                      │
│  [1] REAL-TIME KPI BOARD    │  [2] ACTIVE TENDER STATUS   │  [3] ALERT CENTER    │
│  ═══════════════════════════│  ═══════════════════════════│  ══════════════════  │
│                             │                             │                      │
│  Total Procurement YTD:     │  ├─ TND-2025-0018: CT       │  🔴 CRITICAL (2)    │
│  5,200,000,000 IDR ✓        │  │  Budget: 2,500M          │  ├─ Payment overdue │
│  Budget: 5,000M (104%)      │  │  SLA: 10 days remaining  │  │  PO-099 (5 days) │
│  Spent: 4,200M              │  │  Quotes: 5 received      │  ├─ Invoice mismatch│
│  Outstanding: 1,000M        │  │  Status: 🟢 OPEN        │  │  PO-101          │
│                             │  │                           │                      │
│  On-Time Delivery: 94.2% ✓  │  ├─ TND-2025-0019: Lab     │  🟡 WARNING (5)     │
│  Avg Approval Time: 8 days  │  │  Budget: 1,200M          │  ├─ 3 invoices      │
│  Cost Variance: -2.3% ✓     │  │  SLA: 5 days remaining   │  │  pending approval│
│  Vendor Quality: 4.3/5.0    │  │  Quotes: 3 received      │  ├─ Budget threshold│
│                             │  │  Status: 🟡 EVAL        │  │  at 90%          │
│  Key Metrics Status:        │  │                           │  ├─ Vendor response │
│  ✓ Compliance: 97.3%        │  ├─ TND-2025-0020: Drug    │  │  overdue         │
│  ✓ SLA Achievement: 93.8%   │  │  Budget: 450M            │  └─ Compliance flag │
│  ✓ Budget Control: Within   │  │  SLA: 2 days URGENT ⏰  │                      │
│  ✓ Vendor Performance: OK   │  │  Quotes: 2 received      │  [ACK] [CLOSE]      │
│                             │  │  Status: 🔴 URGENT ⏰    │  [ESCALATE]         │
│                             │                             │                      │
│                             │  ├─ TND-2025-0021: Sutures│                      │
│                             │  │  Budget: 250M            │                      │
│                             │  │  SLA: 8 days remaining   │                      │
│                             │  │  Quotes: 1 received      │                      │
│                             │  │  Status: 🟢 OPEN        │                      │
│                             │                             │                      │
└─────────────────────────────┴─────────────────────────────┴──────────────────────┘

┌─────────────────────────────┬─────────────────────────────┬──────────────────────┐
│                             │                             │                      │
│  [4] PAYMENT PIPELINE       │  [5] VENDOR PERFORMANCE     │  [6] BUDGET TRACKER  │
│  ═════════════════════════  │  ═══════════════════════════│  ══════════════════  │
│                             │                             │                      │
│  Awaiting Approval: 3       │  Top Performers:            │  Total Budget:       │
│  ├─ INV-2025-001: 200M     │  ┌──────────────────────┐   │  5,000,000,000 IDR   │
│  │  Status: ⏳ PENDING     │  │ PT Medik Jaya    4.7★ │   │                      │
│  │  Due: 2025-06-22         │  │ 10% of spend         │   │  ████████░░░░░░░░░░  │
│  │  Amount: 200M            │  │ On-time: 98.5%       │   │  4,200M spent        │
│  │  [APPROVE]               │  └──────────────────────┘   │  800M remaining      │
│  │                          │                             │  16% available       │
│  ├─ INV-2025-002: 150M     │  ┌──────────────────────┐   │                      │
│  │  Status: ⏳ PENDING     │  │ PT Farma Indones 4.5★ │  │  Category Breakdown: │
│  │  Due: 2025-06-25         │  │ 9% of spend          │   │  Equipment: 45%      │
│  │  Amount: 150M            │  │ On-time: 92.1%       │   │  Medicine: 30%       │
│  │  [APPROVE]               │  └──────────────────────┘   │  Services: 20%       │
│  │                          │                             │  Other: 5%           │
│  ├─ INV-2025-003: 100M     │  At Risk:                   │                      │
│  │  Status: ⏳ PENDING     │  ┌──────────────────────┐   │  Projected YE:       │
│  │  Due: 2025-06-28         │  │ PT Supply Chain  4.1★ │  │  5,400,000,000 IDR   │
│  │  Amount: 100M            │  │ 7% of spend          │   │  (8% over budget)    │
│  │  [APPROVE]               │  │ On-time: 85.2% ⚠️    │   │  [MONITOR]           │
│  │                          │  │ Status: DECLINING ↓  │   │                      │
│  │  Subtotal: 450M          │  └──────────────────────┘   │                      │
│  │                          │                             │                      │
│  Processing: 2 (800M)       │  Recent Issues Resolved:    │  Threshold Alerts:   │
│  Paid: 12 (3,950M)          │  ✓ Vendor A - On track     │  ✓ Equipment: 65%    │
│  Total Pipeline: 5,200M     │  ✓ Vendor B - Improved     │  ⚠️ Medicine: 88%    │
│                             │  ⚠️ Vendor C - Monitoring  │  🔴 Services: 92%   │
│  Cash Flow Impact (30 days):│                             │                      │
│  Expected Outflow: 920M     │                             │                      │
│  Current Cash: 1,200M ✓     │                             │                      │
│                             │                             │                      │
└─────────────────────────────┴─────────────────────────────┴──────────────────────┘

┌─────────────────────────────┬─────────────────────────────┬──────────────────────┐
│                             │                             │                      │
│  [7] SLA COUNTDOWN TIMERS    │  [8] LIVE TRANSACTION LOG   │  [9] SYSTEM STATUS   │
│  ═════════════════════════  │  ═════════════════════════  │  ══════════════════  │
│                             │                             │                      │
│  🔴 URGENT (< 2 days)       │  14:32:01 Invoice verified  │  Procurement System: │
│  ├─ TND-2025-0020 (1 day)   │  14:31:45 PO sent to vendor │  ✅ OPERATIONAL      │
│  │  ⏰⏰⏰⏰⏰⏰░░░░░░░░  │  14:30:22 Quote extracted   │                      │
│  │                          │  14:29:18 BAPB approved      │  Database:           │
│  🟡 ATTENTION (2-5 days)    │  14:28:55 Payment approved  │  ✅ RESPONSIVE       │
│  ├─ TND-2025-0019 (5 days)  │  14:27:30 Vendor signed PO  │  Latency: 45ms       │
│  │  ⏰⏰⏰░░░░░░░░░░░░░ │  14:26:10 Tender closed     │                      │
│  ├─ TND-2025-0018 (10 days) │  14:25:40 Payment process   │  WebSocket:          │
│  │  ⏰⏰░░░░░░░░░░░░░░░ │  14:24:15 Invoice received  │  ✅ CONNECTED        │
│  │                          │  14:23:50 BAPB created       │  Subscribers: 23     │
│  🟢 NORMAL (> 5 days)       │  14:22:30 Goods delivered   │                      │
│  ├─ TND-2025-0021 (8 days)  │  14:21:15 Quote evaluated   │  Email Service:      │
│  │  ░░░░░░░░░░░░░░░░░░░ │  14:20:45 Vendor notified  │  ✅ SENDING          │
│                             │  14:19:30 Tender published  │  Last alert: 14:30   │
│  Total Active Tenders: 4    │                             │                      │
│  SLA Compliance: 93.8% ✓    │  [FILTER] [EXPORT LOG]      │  Payment Gateway:    │
│                             │  [SEARCH] [DETAILED VIEW]   │  ✅ CONNECTED        │
│                             │                             │  Last transaction:   │
│                             │                             │  14:25 - DP 150M     │
│                             │                             │                      │
│                             │                             │  GL Integration:     │
│                             │                             │  ✅ SYNCED          │
│                             │                             │  Last post: 14:28    │
│                             │                             │                      │
└─────────────────────────────┴─────────────────────────────┴──────────────────────┘

╔════════════════════════════════════════════════════════════════════════════════╗
║ QUICK CONTROLS: [FULL SCREEN] [DRILL DOWN] [CONFIGURE] [PRINT REPORT] [HELP]  ║
║ Auto-Refresh: 1 second | Mode: LIVE | Last Update: 14:32:15                   ║
╚════════════════════════════════════════════════════════════════════════════════╝
```

---

## COMMAND CENTER SECTIONS DETAILED

### Section 1: Real-Time KPI Board

**Displays:**
- Total procurement value (YTD)
- Budget variance (spent vs allocated)
- Outstanding commitments (POs issued but not paid)
- On-time delivery percentage (trending)
- Average approval cycle time
- Cost variance analysis
- Vendor quality rating (weighted average)
- Compliance score (SPI)
- SLA achievement rate

**Color Coding:**
```
✓ GREEN: On track (>90% target achievement)
⚠️ YELLOW: Attention needed (70-90%)
🔴 RED: Action required (<70%)
```

**Data Update:** Every 5 seconds from database

---

### Section 2: Active Tender Status

**Display Format:**
```
Tender Number | Item | Budget | SLA Days | Quotes | Status
──────────────────────────────────────────────────────────
TND-2025-0018 | CT   | 2.5B   | 10 days  | 5      | 🟢 OPEN
TND-2025-0019 | Lab  | 1.2B   | 5 days   | 3      | 🟡 EVAL
TND-2025-0020 | Drug | 450M   | 2 days   | 2      | 🔴 URGENT ⏰
TND-2025-0021 | Meds | 250M   | 8 days   | 1      | 🟢 OPEN
```

**Color Status Indicators:**
- 🟢 **OPEN:** Accepting bids, more than 5 days remaining
- 🟡 **EVALUATING:** Bids closed, scoring in progress
- 🔴 **URGENT:** Less than 2 days to closing deadline
- ⚫ **CLOSED:** Bidding ended, vendor selected
- ✅ **AWARDED:** PO issued

**Click to Drill Down:**
- View all quotes received
- See AI extracted data
- View scoring breakdown
- Approve/reject vendor

---

### Section 3: Alert Center (The Command Wall)

**Alert Hierarchy:**

```
SEVERITY | COLOR | EXAMPLE | ACTION | AUTO-ESCALATE
─────────────────────────────────────────────────────
CRITICAL| 🔴   | Payment overdue 5+ days | IMMEDIATE | Every 6 hours
HIGH    | 🟠   | SLA breach 1+ day      | Within 2h | Every 8 hours
MEDIUM  | 🟡   | Invoice discrepancy    | Within 4h | Next business day
LOW     | 🟢   | Info notification      | FYI       | Manual only
```

**Alert Management:**
```
Each Alert Has:
├─ Timestamp (when triggered)
├─ Entity (PO-100, TND-15, INV-001)
├─ Description (specific issue)
├─ Responsible person (auto-assigned)
├─ [ACK] Button (acknowledge received)
├─ [CLOSE] Button (resolved)
└─ [ESCALATE] Button (urgent action needed)

Auto-Actions:
├─ Critical → SMS to Director in 5 min
├─ High → Email to manager within 1 hour
├─ Medium → Dashboard notification
└─ Low → Logged for historical review
```

**Alert Examples:**
```
🔴 CRITICAL - 14:30 - Payment Overdue
   PO-2025-099 | PT Farma Indonesia
   Invoice due: 5 days ago | Amount: 250M
   Action: Contact vendor + Kepala Bagian Keuangan
   [ACK] [CLOSE] [ESCALATE]

🟠 HIGH - 14:15 - SLA Breach Warning
   TND-2025-0020 | Drug Procurement
   Closing in 1 day, only 2 quotes received
   Expected 4-5 quotes. Vendor reach-out in progress.
   [ACK] [CLOSE]

🟡 MEDIUM - 14:05 - Invoice Mismatch
   INV-2025-001 | PO-2025-101
   BAPB: 100 unit | Invoice: 105 unit (selisih 5 unit)
   3-way match FAILED. Contact vendor for clarification.
   [ACK] [INVESTIGATE] [APPROVE_VARIANCE]

🟢 INFO - 13:45 - Quote Extracted
   TND-2025-0019 | AI extracted quote from PT Medik Jaya
   Confidence: 95% | Recommend: Review & Score
   [VIEW_QUOTE] [MANUAL_REVIEW]
```

---

### Section 4: Payment Pipeline Status

**Pipeline Stages:**
```
INVOICE RECEIVED → VERIFIED → APPROVED → PROCESSING → PAID
     (3)              (2)         (5)          (2)       (12)
   Awaiting          Matched    Awaiting     In bank    Completed
  Submission     (3-way done)  Director    processing    YTD

Timeline View:
June 21:  DP (30%) x 5 = 450M  ⏰ Awaiting approval
June 28:  Delivery (40%) x 3 = 270M
July 15:  Testing (20%) x 2 = 200M
July 22:  Final (10%) = 100M
```

**Payment Status Colors:**
- 🟢 **PAID:** Cleared, GL posted
- 🟡 **PROCESSING:** Submitted to bank, clearing
- 🔵 **APPROVED:** Finance approved, awaiting processing
- ⏳ **PENDING:** Awaiting approval or matching
- 🔴 **OVERDUE:** Past due date, action needed
- ⚫ **CANCELLED:** Rejected or reversed

**Cash Flow Forecast:**
```
Current Cash Position: 1,200,000,000 IDR
Projected Outflow (30 days): 920,000,000 IDR
Projected Balance: 280,000,000 IDR ✓ (Healthy)

Daily Forecast:
Jun 21:  -450M (DP payments)
Jun 22-27: -50M/day (routine)
Jun 28:  -270M (more DPs)
Jul 1-14: -30M/day (routine)
Jul 15:  -200M (Delivery milestones)
```

---

### Section 5: Vendor Performance Dashboard

**Vendor Scorecard:**
```
VENDOR NAME          | SPEND | WIN% | ON-TIME | QUALITY | STATUS
──────────────────────────────────────────────────────────────
PT Medik Jaya        | 10%   | 45%  | 98.5%   | 4.7★    | 🟢 EXCELLENT
PT Farma Indonesia   | 9%    | 35%  | 92.1%   | 4.5★    | 🟢 GOOD
PT Healthcare Supp   | 8%    | 40%  | 100%    | 4.4★    | 🟢 GOOD
PT Equipment Global  | 7%    | 30%  | 95.2%   | 4.6★    | 🟢 EXCELLENT
PT Supply Chain Corp | 7%    | 20%  | 85.2%   | 4.1★    | 🟡 MONITOR
```

**Trending Analysis:**
```
Improving ↑
├─ PT Farma Indonesia (+5% on-time vs last month)
├─ PT Supply Chain Corp (+2% quality score improvement)

Stable →
├─ PT Medik Jaya (consistent excellence)
├─ PT Equipment Global

Declining ↓
├─ PT Supply Chain Corp (-5% on-time vs last month)
   Action: Increase monitoring, reduce allocation
```

---

### Section 6: Budget Tracking & Analysis

**Budget Allocation View:**
```
CATEGORY            | ALLOCATED | SPENT | PENDING | AVAILABLE | % USED
──────────────────────────────────────────────────────────────────────
Medical Equipment   | 2,250M    | 1,485M | 400M    | 365M      | 83.8%
Medicines          | 1,500M    | 1,200M | 200M    | 100M      | 93.3% ⚠️
Support Services   | 1,000M    | 650M   | 250M    | 100M      | 90.0% ⚠️
Other              | 250M      | 130M   | 50M     | 70M       | 72.0%
──────────────────────────────────────────────────────────────────────
TOTAL              | 5,000M    | 3,465M | 900M    | 635M      | 87.3%
```

**Budget Variance Analysis:**
```
Total Budget: 5,000M IDR
Spent: 3,465M (69.3%)
Committed (POs): 900M (18%)
Available: 635M (12.7%)

YE Projection: 5,400M (8% over budget)
Status: 🟡 ATTENTION - May require supplemental budget

Options:
1. Reduce non-essential categories
2. Request supplemental budget (300M)
3. Negotiate volume discounts with vendors
```

---

### Section 7: SLA Countdown Timers

**Visual Timer Bars (Decay Indicator):**

```
🔴 URGENT (Closing in < 2 days)
├─ TND-2025-0020: 1 day remaining
│  ⏰⏰⏰⏰⏰⏰░░░░░░░░ (14% remaining)
│  Closes: Jun 22, 23:59
│  [EXTEND] [EXPEDITE_EVAL]

🟡 ATTENTION (2-5 days)
├─ TND-2025-0019: 5 days remaining
│  ⏰⏰⏰░░░░░░░░░░░░░░ (40% remaining)
│  Closes: Jun 25, 23:59
│
├─ TND-2025-0018: 10 days remaining
│  ⏰⏰░░░░░░░░░░░░░░░░░ (80% remaining)
│  Closes: Jun 30, 23:59

🟢 NORMAL (> 5 days)
├─ TND-2025-0021: 8 days remaining
│  ░░░░░░░░░░░░░░░░░░░░░ (67% remaining)
│  Closes: Jul 3, 23:59
```

**Blink Animation:**
- Tenders with < 24 hours: **BLINK RAPIDLY** (Red)
- Tenders with 2-3 days: **SOLID RED** (Attention needed)
- Others: **Steady** (Normal)

---

### Section 8: Live Transaction Log

**Real-Time Activity Stream:**

```
Timestamp  | Type       | Entity      | Action                | Status
───────────────────────────────────────────────────────────────────
14:32:01   | PAYMENT    | INV-2025-001| Invoice verified      | ✅
14:31:45   | QUOTE      | TND-2025-0019| Quote extracted (AI)  | ✅
14:30:22   | TENDER     | TND-2025-0020| Evaluation completed  | ✅
14:29:18   | DELIVERY   | BAPB-2025-001| Goods received (QC)   | ✅
14:28:55   | PAYMENT    | PM-2025-003 | Payment approved      | ✅
14:27:30   | PO         | PO-2025-100 | Vendor signed         | ✅
14:26:10   | TENDER     | TND-2025-0018| Bidding closed        | ✅
14:25:40   | PAYMENT    | PM-2025-002 | Payment processed     | ✅
14:24:15   | INVOICE    | INV-2025-003| Invoice received      | ⏳
14:23:50   | DELIVERY   | BAPB-2025-002| BAPB created           | ✅
```

**Filtering Options:**
- By Entity Type (Tender, Quote, PO, Payment, Delivery)
- By Status (Success, Pending, Failed)
- By Time Range (Last hour, Last 24h, Last week)
- By User/Vendor
- By System (Procurement, Finance, Unit)

**Export Options:**
- CSV export
- PDF report
- Email to stakeholders
- Archive to compliance

---

### Section 9: System Health Status

**Component Status Indicators:**

```
COMPONENT           | STATUS | LATENCY | LAST CHECK | ACTION
────────────────────────────────────────────────────────
Procurement System  | ✅     | 45ms    | 14:32:15   | ✓
Database            | ✅     | 12ms    | 14:32:14   | ✓
WebSocket Server    | ✅     | <1ms    | 14:32:15   | ✓
Email Service       | ✅     | 230ms   | 14:30:45   | ✓
SMS Gateway         | ✅     | 340ms   | 14:31:00   | ✓
Payment Gateway     | ✅     | 850ms   | 14:25:32   | ✓
GL Integration      | ✅     | 1200ms  | 14:28:00   | ⚠️ (Monitor)
Gemini AI Service   | ✅     | 2500ms  | 14:30:15   | ✓
Document Storage    | ✅     | 150ms   | 14:31:30   | ✓
```

**Health Alerts:**
```
If Component DOWN:
├─ Automated failover (if available)
├─ Alert to System Admin
├─ Log incident
├─ Retry connection every 10 seconds
└─ Escalate if down > 5 minutes

If Performance DEGRADED:
├─ Monitor closely
├─ Log performance metrics
├─ Alert if latency > SLA
└─ Investigate root cause
```

---

## TECHNICAL IMPLEMENTATION

### Real-Time Data Architecture

```
┌──────────────────────────────────────────┐
│ Database                                 │
│ (PostgreSQL + Redis Cache)               │
└─────────────┬──────────────────────────┘
              │
              │ (Query every 5 seconds)
              │
    ┌─────────▼──────────┐
    │ Data Aggregation   │
    │ Service (Node.js)  │
    │                    │
    │ ├─ KPI Calculator  │
    │ ├─ Status Mapper   │
    │ ├─ Alert Engine    │
    │ └─ Log Aggregator  │
    └─────────┬──────────┘
              │
              │ (WebSocket push)
              │
    ┌─────────▼──────────────────┐
    │ WebSocket Server            │
    │ (Socket.io / ws)            │
    │                             │
    │ ├─ Dashboard (real-time)    │
    │ ├─ Mobile alerts            │
    │ ├─ Email notifications      │
    │ └─ SMS escalation           │
    └────────────────────────────┘
```

### WebSocket Events

```javascript
// Real-time events pushed to dashboard

socket.on('kpi_update', {
  timestamp: "2025-06-20T14:32:15Z",
  kpi: {
    total_procurement: 5200000000,
    budget_variance: 4.0,  // %
    on_time_delivery: 94.2,
    approval_cycle_days: 8,
    compliance_score: 97.3
  }
});

socket.on('tender_status_change', {
  tender_id: 18,
  tender_number: "TND-2025-0018",
  status: "evaluating",
  quotes_received: 5,
  sla_days_remaining: 10
});

socket.on('alert_triggered', {
  alert_id: "ALR-2025-001",
  severity: "critical",
  type: "payment_overdue",
  entity: "PO-2025-099",
  message: "Payment overdue 5 days",
  timestamp: "2025-06-20T14:30:00Z"
});

socket.on('transaction_logged', {
  timestamp: "2025-06-20T14:32:01Z",
  type: "invoice_verified",
  entity: "INV-2025-001",
  status: "success"
});
```

### Database Queries for Command Center

```sql
-- KPI Dashboard (5-second refresh)
SELECT 
  (SELECT SUM(po_amount) FROM purchase_orders WHERE EXTRACT(YEAR FROM po_date) = 2025) as total_procurement,
  (SELECT AVG(CAST(status AS INT)) FROM tenders WHERE status IN ('open', 'closed')) as avg_tender_status,
  (SELECT COUNT(*) FROM purchase_orders WHERE status NOT IN ('completed', 'cancelled')) as active_pos,
  (SELECT AVG(support_rating) FROM vendors WHERE status = 'approved') as avg_vendor_rating,
  (SELECT COUNT(*) FROM alerts WHERE status = 'pending') as pending_alerts
FROM (SELECT 1) dummy;

-- Active Tender Status (5-second refresh)
SELECT 
  tender_number,
  title,
  budget_max,
  EXTRACT(DAY FROM bid_closing_date - NOW()) as days_remaining,
  (SELECT COUNT(*) FROM quotes WHERE tender_id = tenders.id) as quote_count,
  status,
  CASE 
    WHEN EXTRACT(DAY FROM bid_closing_date - NOW()) < 2 THEN 'urgent'
    WHEN EXTRACT(DAY FROM bid_closing_date - NOW()) < 5 THEN 'attention'
    ELSE 'normal'
  END as urgency
FROM tenders
WHERE status IN ('published', 'closed')
ORDER BY bid_closing_date ASC;

-- Alert Summary (Real-time)
SELECT 
  severity,
  COUNT(*) as count,
  STRING_AGG(entity_type || ':' || entity_id, ', ') as entities
FROM alerts
WHERE status = 'pending'
GROUP BY severity
ORDER BY CASE severity WHEN 'critical' THEN 1 WHEN 'high' THEN 2 WHEN 'medium' THEN 3 ELSE 4 END;
```

---

## USER INTERACTIONS

### Dashboard Controls

**Header Controls:**
```
[FULL SCREEN] 
[DRILL DOWN] 
[CONFIGURE] 
[PRINT REPORT] 
[EXPORT DATA]
[AUTO REFRESH: ON/OFF]
[REFRESH INTERVAL: 1s / 5s / 10s]
[MODE: LIVE / PAUSE / HISTORICAL]
```

**Interactive Drill-Down:**
1. Click on Tender → See all quotes + scores
2. Click on Alert → See details + options
3. Click on Payment → See invoice + matching status
4. Click on Vendor → See performance history + recent activities

**Keyboard Shortcuts:**
```
F1: Help
F5: Full refresh
P: Pause updates
R: Resume updates
E: Export current view
Q: Quick filters
C: Configure dashboard
```

---

## DISPLAY HARDWARE RECOMMENDATIONS

**For Command Center:**
- **Main Display:** 55"+ 4K (3840x2160) landscape
- **Refresh Rate:** 60Hz minimum (supports sub-second updates)
- **Response Time:** <5ms
- **HDR Support:** For better color differentiation
- **Resolution Scaling:** 150% for readability from distance

**For Individual Workstations:**
- **Display:** 27"+ QHD (2560x1440) or 4K
- **Dual Monitor Setup:** Main + detail view

**Wall Mount:**
- Accessible from distance (8-10 feet)
- Anti-glare coating
- 24/7 operation capability

---

## AUTO-REFRESH & LATENCY

**Update Frequencies:**

| Component | Refresh | Latency | Notes |
|-----------|---------|---------|-------|
| KPI Board | 5s | <1s | Database query + calculation |
| Tender Status | 5s | <1s | Aggregated from multiple tables |
| Alerts | Real-time | <100ms | WebSocket push |
| Payment Pipeline | 10s | <1s | Combined query |
| Transaction Log | Real-time | <100ms | Event-driven |
| Vendor Performance | 30s | <2s | Aggregated metrics |
| Budget Tracker | 10s | <1s | Running calculation |
| System Status | 30s | <2s | Health check API |

**Network Requirements:**
- Dedicated high-speed connection (100Mbps+)
- Latency <50ms to data center
- Redundant internet connection (failover capability)
- Local WebSocket proxy for reliability

---

## COLOR SCHEME & VISUAL HIERARCHY

```css
/* Command Center Color Palette */

/* Status Colors */
--success: #00ff00    /* Green - All good */
--warning: #ffaa00    /* Orange/Amber - Attention */
--critical: #ff0000   /* Red - Action required */
--info: #0088ff       /* Blue - Information */
--neutral: #cccccc    /* Gray - Background */

/* Urgency Indicators */
--urgent-blink: #ff0000 blink 0.5s  /* < 24 hours */
--attention: #ffaa00 solid           /* 2-5 days */
--normal: #00ff00 solid              /* > 5 days */

/* Text Colors */
--text-primary: #ffffff             /* White on dark background */
--text-secondary: #cccccc           /* Light gray for secondary info */
--text-error: #ff6666               /* Light red for errors */

/* Backgrounds */
--bg-primary: #0a0e27              /* Dark blue-black */
--bg-secondary: #1a1f3a            /* Slightly lighter */
--bg-hover: #2a2f4a                /* Hover state */
--bg-alert: #1a0a0a                /* Dark red tint for alert area */
```

---

## PERFORMANCE OPTIMIZATION

**Caching Strategy:**
```
Redis Cache Layers:
├─ L1: KPI aggregates (5s TTL)
├─ L2: Tender summaries (10s TTL)
├─ L3: Vendor metrics (30s TTL)
└─ L4: Budget snapshots (30s TTL)

Database Connection Pool:
├─ Min connections: 10
├─ Max connections: 50
├─ Query timeout: 5 seconds
└─ Connection reuse: Enabled
```

**Frontend Optimization:**
```
Canvas/SVG Rendering:
├─ Use canvas for charts (faster rendering)
├─ Debounce updates (max 1/second)
├─ Progressive rendering (load-as-you-go)
└─ Lazy loading for detail panels
```

---

## EXAMPLE DASHBOARD LAYOUTS

### Layout 1: Executive Overview (Default)
- KPI Board (top-left)
- Alert Center (top-right)
- Tender Status (middle-left)
- Payment Pipeline (middle-center)
- Budget Tracker (middle-right)
- Vendor Performance (bottom)

### Layout 2: Operations Focus
- Tender Status (dominant, top-half)
- SLA Timers (top-right)
- Transaction Log (bottom)
- Alert Center (right sidebar)

### Layout 3: Finance Focus
- Budget Tracker (dominant)
- Payment Pipeline (large)
- KPI Board (top)
- Alert Center (right)

### Layout 4: Compliance/SPI
- Audit Log (dominant)
- Alerts/Exceptions (large)
- Vendor Compliance (right)
- System Status (footer)

---

## PRINTABLE REPORTS FROM DASHBOARD

**One-Click Report Generation:**
```
[PRINT] → Select Template:
├─ Executive Summary (1 page)
├─ Detailed Report (5 pages)
├─ SLA Compliance (2 pages)
├─ Budget Analysis (3 pages)
├─ Vendor Performance (2 pages)
└─ Custom (user-defined)

Output Format:
├─ PDF (formatted)
├─ Excel (data + charts)
├─ Email (automatic distribution)
└─ Archive (compliance storage)
```

---

## ACCESSIBILITY & INTERNATIONALIZATION

**Accessibility:**
- High contrast mode (white on black for critical alerts)
- Text size adjustment (12px - 24px)
- Keyboard navigation support
- Screen reader compatible
- Color-blind friendly indicators (not just color)

**Multi-Language Support:**
- English (default)
- Indonesian (Bahasa)
- Expandable to other languages

---

## NEXT STEPS FOR IT IMPLEMENTATION

1. **Frontend Framework:** React + D3.js/Chart.js for visualizations
2. **Real-Time Library:** Socket.io or ws (WebSocket)
3. **Backend Aggregation:** Node.js microservice
4. **Data Visualization:** Canvas/SVG for high-performance charts
5. **Testing:** Load test with 100+ concurrent viewers
6. **Hardware:** Procure display hardware + installation

---

**This Command Center gives Management complete visibility into ALL procurement activities in real-time. One dashboard, one source of truth.**


<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="Financial Flow - Pengadaan KMU">
    <edge COLOR="#000000" WIDTH="2"/>
    <font NAME="Arial" SIZE="18" BOLD="true"/>

    <!-- PLANNING PHASE -->
    <node ID="planning" TEXT="PLANNING PHASE (Fase 1)" POSITION="right">
      <edge COLOR="#3498DB" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#3498DB"/>

      <node TEXT="Budget Inputs">
        <node TEXT="RKAP (Rencana Kerja Anggaran Perusahaan)"/>
        <node TEXT="RAB (Rencana Anggaran Biaya)"/>
        <node TEXT="SBU Request"/>
      </node>

      <node TEXT="Budget Processing">
        <node TEXT="Total Available Budget"/>
        <node TEXT="Department Allocation"/>
        <node TEXT="Project Budgeting"/>
      </node>

      <node TEXT="Financial Output">
        <node TEXT="Budget Ceiling per SBU"/>
        <node TEXT="Spending Authority Levels"/>
        <node TEXT="Timeline"/>
      </node>

      <node TEXT="System: Finance/ERP"/>
      <node TEXT="Approval: Komite Anggaran, Direksi"/>
    </node>

    <!-- REQUISITION PHASE -->
    <node ID="requisition" TEXT="REQUISITION PHASE (Fase 3)" POSITION="right">
      <edge COLOR="#27AE60" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#27AE60"/>

      <node TEXT="SBU Creates Request">
        <node TEXT="PP (Permintaan Pembelian)"/>
        <node TEXT="IMT (Inventory Request)"/>
        <node TEXT="SPPJ (Surat Permintaan Pekerjaan Jasa)"/>
      </node>

      <node TEXT="Financial Info">
        <node TEXT="Requested Amount"/>
        <node TEXT="Budget Account"/>
        <node TEXT="Cost Center"/>
        <node TEXT="Approval Limit"/>
      </node>

      <node TEXT="AI Validation">
        <node TEXT="Budget availability check"/>
        <node TEXT="Approval authority check"/>
        <node TEXT="Compliance check"/>
      </node>

      <node TEXT="Output: Approved PP"/>
    </node>

    <!-- PROCUREMENT PHASE -->
    <node ID="procurement" TEXT="PROCUREMENT PHASE (Fase 4)" POSITION="right">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="Tender/Quotation">
        <node TEXT="SPPH (Surat Permintaan Penawaran)"/>
        <node TEXT="Quotes received from vendors"/>
        <node TEXT="HPS (Harga Perkiraan Sementara)"/>
      </node>

      <node TEXT="Bid Evaluation">
        <node TEXT="Price comparison"/>
        <node TEXT="Scoring (Price 25%)"/>
        <node TEXT="Total Cost of Ownership"/>
      </node>

      <node TEXT="Vendor Selection">
        <node TEXT="Winner announcement"/>
        <node TEXT="Final negotiated price"/>
        <node TEXT="PO amount finalized"/>
      </node>

      <node TEXT="Financial Record">
        <node TEXT="Commitment Register (Komitmen)"/>
        <node TEXT="Purchase Order (PO) amount"/>
      </node>
    </node>

    <!-- CONTRACT PHASE -->
    <node ID="contract" TEXT="CONTRACT PHASE (Fase 5)" POSITION="right">
      <edge COLOR="#9B59B6" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#9B59B6"/>

      <node TEXT="Contract Documents">
        <node TEXT="PO (Purchase Order) - Daan Umum"/>
        <node TEXT="SPK (Surat Perintah Kerja) - Daan Jasa"/>
        <node TEXT="PKS (Perjanjian Kerja Sama)"/>
      </node>

      <node TEXT="Payment Terms">
        <node TEXT="DP (Down Payment) %"/>
        <node TEXT="Milestone Payments"/>
        <node TEXT="Final Payment %"/>
        <node TEXT="Payment Method"/>
        <node TEXT="Due Date"/>
      </node>

      <node TEXT="Financial Recording">
        <node TEXT="GL Account assigned"/>
        <node TEXT="Cost center allocation"/>
        <node TEXT="Budget earmark"/>
      </node>
    </node>

    <!-- DELIVERY &amp; RECEIPT PHASE -->
    <node ID="delivery" TEXT="DELIVERY &amp; RECEIPT (Fase 6)" POSITION="right">
      <edge COLOR="#F39C12" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#F39C12"/>

      <node TEXT="Goods/Services Arrival">
        <node TEXT="Physical receipt at warehouse"/>
        <node TEXT="Service completion"/>
      </node>

      <node TEXT="BAPB (Berita Acara)">
        <node TEXT="Quantity verification"/>
        <node TEXT="Quality inspection"/>
        <node TEXT="Condition check"/>
        <node TEXT="Signed BAPB"/>
      </node>

      <node TEXT="Financial Status">
        <node TEXT="Ready for Invoice"/>
        <node TEXT="Actual amount confirmed"/>
      </node>
    </node>

    <!-- INVOICE &amp; PAYMENT PHASE -->
    <node ID="payment" TEXT="INVOICE &amp; PAYMENT (Fase 7)" POSITION="right">
      <edge COLOR="#16A085" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#16A085"/>

      <node TEXT="Vendor Submits Invoice">
        <node TEXT="Invoice document"/>
        <node TEXT="Invoice amount"/>
        <node TEXT="Invoice date"/>
        <node TEXT="Due date"/>
      </node>

      <node TEXT="3-Way Match">
        <node TEXT="PO vs Invoice (amount match)"/>
        <node TEXT="BAPB vs Invoice (quantity match)"/>
        <node TEXT="Invoice vs GL (account match)"/>
      </node>

      <node TEXT="Payment Processing">
        <node TEXT="DP Payment (if applicable)"/>
        <node TEXT="Hold period (if any)"/>
        <node TEXT="Final payment authorization"/>
        <node TEXT="Check/Bank transfer"/>
        <node TEXT="Payment recording (GL post)"/>
      </node>

      <node TEXT="Approval">
        <node TEXT="Finance Manager review"/>
        <node TEXT="CFO approval (if &gt; limit)"/>
      </node>

      <node TEXT="SLA: 30 hari"/>
    </node>

    <!-- CASH FLOW MANAGEMENT -->
    <node ID="cashflow" TEXT="💵 CASH FLOW MANAGEMENT" POSITION="right">
      <edge COLOR="#34495E" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#34495E"/>

      <node TEXT="Working Capital">
        <node TEXT="Days Payable Outstanding (DPO)"/>
        <node TEXT="Current target: 45 days"/>
        <node TEXT="Optimized: 30 days (with AI)"/>
        <node TEXT="Cash freed up: Rp 1.67B"/>
      </node>

      <node TEXT="Payment Cycles">
        <node TEXT="DP payment (if 10% upfront)"/>
        <node TEXT="Milestone payments"/>
        <node TEXT="Final payment (after BAPB)"/>
      </node>

      <node TEXT="Early Payment Discounts">
        <node TEXT="Vendors offer 2% for payment in 10 days"/>
        <node TEXT="Finance evaluates cost-benefit"/>
        <node TEXT="Savings opportunity: Rp 200M/year"/>
      </node>

      <node TEXT="Cash Forecasting">
        <node TEXT="Pending invoices"/>
        <node TEXT="Payment schedule"/>
        <node TEXT="Vendor payment status"/>
      </node>
    </node>

    <!-- BUDGET TRACKING &amp; CONTROL -->
    <node ID="budgetctl" TEXT="📊 BUDGET TRACKING &amp; CONTROL" POSITION="left">
      <edge COLOR="#1ABC9C" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#1ABC9C"/>

      <node TEXT="Budget Status">
        <node TEXT="Allocated: Rp X (from RKAP)"/>
        <node TEXT="Committed: Rp Y (from POs)"/>
        <node TEXT="Spent: Rp Z (from Invoices paid)"/>
        <node TEXT="Available: Rp (X - Y - Z)"/>
      </node>

      <node TEXT="Monthly Reconciliation">
        <node TEXT="Compare budget vs actual"/>
        <node TEXT="Variance analysis"/>
        <node TEXT="Forecast vs actual"/>
        <node TEXT="Reallocation if needed"/>
      </node>

      <node TEXT="Reports">
        <node TEXT="Budget execution report"/>
        <node TEXT="Spend analysis by vendor"/>
        <node TEXT="Spend analysis by category"/>
        <node TEXT="Deviations &amp; variances"/>
      </node>

      <node TEXT="Tools: Finance Dashboard, Analytics"/>
    </node>

    <!-- COST OPTIMIZATION -->
    <node ID="optimization" TEXT="💡 COST OPTIMIZATION" POSITION="left">
      <edge COLOR="#C0392B" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#C0392B"/>

      <node TEXT="Vendor Negotiation">
        <node TEXT="Price comparison"/>
        <node TEXT="Volume discounts"/>
        <node TEXT="Payment term optimization"/>
        <node TEXT="Estimated savings: Rp 2.5B/year"/>
      </node>

      <node TEXT="Procurement Strategy">
        <node TEXT="Direct appointment for small items"/>
        <node TEXT="Tender for high-value items"/>
        <node TEXT="Consolidated purchasing (multi-SBU)"/>
      </node>

      <node TEXT="Vendor Performance">
        <node TEXT="Quality improvements = less rework cost"/>
        <node TEXT="On-time delivery = less expedite cost"/>
        <node TEXT="Compliance = fewer penalty costs"/>
      </node>

      <node TEXT="Financial Impact">
        <node TEXT="Error prevention: Rp 7.3B/year"/>
        <node TEXT="Vendor improvement: Rp 4.2B/year"/>
        <node TEXT="Cash flow optimization: Rp 242M/year"/>
      </node>
    </node>

    <!-- FINANCIAL SUMMARY -->
    <node ID="summary" TEXT="FINANCIAL SUMMARY" POSITION="left">
      <edge COLOR="#000000" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true"/>

      <node TEXT="Annual Procurement Volume">
        <node TEXT="Daan Umum (Goods): ~Rp X per year"/>
        <node TEXT="Daan Jasa (Services): ~Rp Y per year"/>
        <node TEXT="Total: ~Rp Z per year"/>
      </node>

      <node TEXT="Key Financial Metrics">
        <node TEXT="Vendor count: 200+ active"/>
        <node TEXT="Monthly transactions: ~100"/>
        <node TEXT="Avg transaction: Rp 50-500M"/>
      </node>

      <node TEXT="Year 1 AI Impact">
        <node TEXT="Error prevention: Rp 7.3B"/>
        <node TEXT="Process efficiency: Rp 2.4B"/>
        <node TEXT="Vendor optimization: Rp 4.2B"/>
        <node TEXT="Cash flow: Rp 242M"/>
        <node TEXT="TOTAL: Rp 14.57B benefit"/>
      </node>

      <node TEXT="System Benefit">
        <node TEXT="Real-time visibility to Direksi"/>
        <node TEXT="Faster payment cycles"/>
        <node TEXT="Better vendor management"/>
        <node TEXT="Lower financial risk"/>
      </node>
    </node>
  </node>
</map>
<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="Stakeholder Ecosystem - Pengadaan KMU">
    <edge COLOR="#000000" WIDTH="2"/>
    <font NAME="Arial" SIZE="18" BOLD="true"/>

    <!-- DIREKSI LEVEL -->
    <node ID="direksi" TEXT="🎯 DIREKSI (Strategic Leadership)" POSITION="right">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="Direktur Utama">
        <node TEXT="Role: Final Approval &gt;100M"/>
        <node TEXT="Interest: Strategic Value, ROI"/>
        <node TEXT="Input: Command Center Dashboard"/>
        <node TEXT="Output: Major Decisions"/>
      </node>

      <node TEXT="Direktur Operasi &amp; Pengembangan">
        <node TEXT="Role: Approval 25-100M"/>
        <node TEXT="Interest: Operational Efficiency"/>
        <node TEXT="Input: Status Reports, Alerts"/>
        <node TEXT="Output: Approvals, Directives"/>
      </node>

      <node TEXT="Direktur Keuangan">
        <node TEXT="Role: Finance Oversight"/>
        <node TEXT="Interest: Budget, Cash Flow"/>
        <node TEXT="Input: Financial Reports"/>
        <node TEXT="Output: Payment Approval, Budget Control"/>
      </node>
    </node>

    <!-- DEPARTEMEN PENGADAAN (Internal) -->
    <node ID="dept_pengadaan" TEXT="📋 DEPT. PENGADAAN (Core)" POSITION="right">
      <edge COLOR="#3498DB" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#3498DB"/>

      <node TEXT="Kasie Pengadaan Barang">
        <node TEXT="Role: Manage Goods Procurement"/>
        <node TEXT="Approval: ≤25M (with Manager)"/>
        <node TEXT="Activities: Tender, PO, Vendor Selection"/>
        <node TEXT="Tools: E-Procurement, AI Guardian"/>
      </node>

      <node TEXT="Kasie Pengadaan Jasa">
        <node TEXT="Role: Manage Services"/>
        <node TEXT="Approval: ≤25M (with Manager)"/>
        <node TEXT="Activities: Konsultan, Konstruksi, Pemborongan, Swakelola"/>
        <node TEXT="Tools: E-Procurement, Contract Management"/>
      </node>

      <node TEXT="Manager Pengadaan">
        <node TEXT="Role: Supervisor, Approval 10-25M"/>
        <node TEXT="Activities: Review, Validation, Escalation"/>
        <node TEXT="Tools: Dashboard, Approval Workflow"/>
      </node>

      <node TEXT="Staff Pengadaan">
        <node TEXT="Role: Operational Execution"/>
        <node TEXT="Activities: Tender Prep, Bid Evaluation, PO Generation"/>
        <node TEXT="Tools: E-Procurement, AI Guidance"/>
      </node>
    </node>

    <!-- SBU &amp; UNIT KERJA (Internal) -->
    <node ID="sbu" TEXT="🏥 SBU &amp; UNIT KERJA (Requestors)" POSITION="right">
      <edge COLOR="#27AE60" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#27AE60"/>

      <node TEXT="RSUD/Bedah/ICU/etc">
        <node TEXT="Role: Request goods/services"/>
        <node TEXT="Activities: Create PP, Specify needs"/>
        <node TEXT="Input: Budget allocation"/>
        <node TEXT="Output: PP, Receive goods"/>
      </node>

      <node TEXT="Lab/Farmasi/BMHP">
        <node TEXT="Role: Request + KSO Management"/>
        <node TEXT="Activities: PP creation, KSO setup, Self-reporting"/>
        <node TEXT="Special: Consumables tracking via Vendor Portal"/>
      </node>

      <node TEXT="Warehouse/Logistics">
        <node TEXT="Role: Receive &amp; Store"/>
        <node TEXT="Activities: BAPB, Quality Check, Inventory Update"/>
      </node>

      <node TEXT="Quality Control">
        <node TEXT="Role: Inspection &amp; Verification"/>
        <node TEXT="Activities: QC, BAPB sign-off"/>
      </node>
    </node>

    <!-- GOVERNANCE &amp; CONTROL -->
    <node ID="governance" TEXT="⚖️ GOVERNANCE &amp; CONTROL" POSITION="right">
      <edge COLOR="#9B59B6" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#9B59B6"/>

      <node TEXT="Komite Anggaran">
        <node TEXT="Role: Budget Review &amp; Approval"/>
        <node TEXT="Activities: Budget ceiling, Special approvals"/>
        <node TEXT="Input: Budget reports"/>
      </node>

      <node TEXT="SPI (Satuan Pengawasan Internal)">
        <node TEXT="Role: Internal Audit &amp; Compliance"/>
        <node TEXT="Activities: Audit, Compliance checking, Risk assessment"/>
        <node TEXT="Input: Audit trail, Compliance reports"/>
        <node TEXT="Tool: AI Guardian Audit Trail"/>
      </node>

      <node TEXT="Legal &amp; Compliance">
        <node TEXT="Role: Contract review, Legal check"/>
        <node TEXT="Activities: PKS review, Risk assessment"/>
      </node>
    </node>

    <!-- FINANCE &amp; SUPPORT -->
    <node ID="finance" TEXT="💰 FINANCE &amp; SUPPORT" POSITION="right">
      <edge COLOR="#F39C12" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#F39C12"/>

      <node TEXT="Finance Department">
        <node TEXT="Role: Payment processing"/>
        <node TEXT="Activities: Invoice verification, GL posting, Payment execution"/>
        <node TEXT="Tool: 3-Way Match system"/>
      </node>

      <node TEXT="Accounting">
        <node TEXT="Role: Record keeping"/>
        <node TEXT="Activities: AR/AP, Budget tracking"/>
      </node>

      <node TEXT="HR/Admin">
        <node TEXT="Role: Support functions"/>
        <node TEXT="Activities: Vendor onboarding, Training"/>
      </node>

      <node TEXT="IT Department">
        <node TEXT="Role: System maintenance"/>
        <node TEXT="Activities: Platform management, Support"/>
      </node>
    </node>

    <!-- EXTERNAL STAKEHOLDERS -->
    <node ID="external" TEXT="🌐 EXTERNAL STAKEHOLDERS" POSITION="left">
      <edge COLOR="#E67E22" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#E67E22"/>

      <node TEXT="VENDORS (Suppliers)">
        <node TEXT="Categories: Barang, Jasa, Konstruksi, Konsultan"/>
        <node TEXT="Role: Supply goods/services"/>
        <node TEXT="Activities: Register, Quote, Deliver, Invoice, KSO Reporting"/>
        <node TEXT="Portal: Vendor Portal (Self-Service)"/>
        <node TEXT="KSO: Lab, Farmasi, BMHP contracts"/>
      </node>

      <node TEXT="REGULATORY BODIES">
        <node TEXT="BPK (Badan Pemeriksa Keuangan)"/>
        <node TEXT="Kemenkeu (Ministry of Finance)"/>
        <node TEXT="Permenkes (Health Ministry)"/>
        <node TEXT="LKPP (Procurement Policy)"/>
      </node>

      <node TEXT="PARTNERS &amp; INTEGRATIONS">
        <node TEXT="Bank (Payment processing)"/>
        <node TEXT="Insurance (Vendor coverage)"/>
        <node TEXT="Consultants (Support)"/>
      </node>
    </node>

    <!-- SYSTEM INTEGRATIONS -->
    <node ID="systems" TEXT="🔗 SYSTEM INTEGRATIONS" POSITION="left">
      <edge COLOR="#16A085" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#16A085"/>

      <node TEXT="Finance Systems">
        <node TEXT="ERP / Finance System"/>
        <node TEXT="GL Accounting"/>
        <node TEXT="Budget Module"/>
      </node>

      <node TEXT="Operational Systems">
        <node TEXT="SIMRS (Hospital System)"/>
        <node TEXT="Warehouse / Inventory"/>
        <node TEXT="HR / Payroll"/>
      </node>

      <node TEXT="Communication">
        <node TEXT="Email Notifications"/>
        <node TEXT="SMS Alerts"/>
        <node TEXT="Dashboard Updates"/>
      </node>

      <node TEXT="Reporting">
        <node TEXT="BI Tools"/>
        <node TEXT="Export Functions"/>
        <node TEXT="API Integrations"/>
      </node>
    </node>

    <!-- SUMMARY -->
    <node ID="summary" TEXT="STAKEHOLDER SUMMARY" POSITION="left">
      <edge COLOR="#000000" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true"/>

      <node TEXT="Internal: 14+ stakeholders">
        <node TEXT="Direksi (3)"/>
        <node TEXT="Dept. Pengadaan (4)"/>
        <node TEXT="SBU/Units (5+)"/>
        <node TEXT="Governance (3)"/>
        <node TEXT="Finance/Support (4+)"/>
      </node>

      <node TEXT="External: Vendors + Regulators"/>

      <node TEXT="Key Principle: Role-Based Access">
        <node TEXT="Different views for different users"/>
        <node TEXT="Approval workflow based on amount"/>
        <node TEXT="Transparency for all stakeholders"/>
      </node>

      <node TEXT="Communication">
        <node TEXT="Real-time notifications"/>
        <node TEXT="Status visibility"/>
        <node TEXT="Escalation alerts"/>
      </node>
    </node>
  </node>
</map>
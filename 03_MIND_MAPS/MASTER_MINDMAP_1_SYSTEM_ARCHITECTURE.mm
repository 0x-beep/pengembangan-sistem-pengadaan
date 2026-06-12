<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="Platform Digitalisasi Pengadaan PT. KMU">
    <edge COLOR="#000000" WIDTH="2"/>
    <font NAME="Arial" SIZE="18" BOLD="true"/>

    <!-- LAYER 1: Manajemen & Tata Kelola -->
    <node ID="layer1" TEXT="LAPISAN 1: Manajemen &amp; Tata Kelola" POSITION="right">
      <edge COLOR="#FF6B6B" WIDTH="2"/>
      <font NAME="Arial" SIZE="14" BOLD="true" COLOR="#FF6B6B"/>

      <node ID="l1_eproc" TEXT="E-Procurement Platform">
        <edge COLOR="#FF8C8C"/>
        <node TEXT="Tender Management"/>
        <node TEXT="Quote Processing"/>
        <node TEXT="PO Generation"/>
        <node TEXT="Vendor Scoring"/>
      </node>

      <node ID="l1_workflow" TEXT="Workflow &amp; Approval">
        <edge COLOR="#FF8C8C"/>
        <node TEXT="Authorization Matrix"/>
        <node TEXT="Approval Routing"/>
        <node TEXT="SLA Tracking"/>
        <node TEXT="Escalation Rules"/>
      </node>

      <node ID="l1_compliance" TEXT="Compliance Engine">
        <edge COLOR="#FF8C8C"/>
        <node TEXT="SPO Validation"/>
        <node TEXT="Rule Engine"/>
        <node TEXT="Audit Trail"/>
        <node TEXT="Reporting"/>
      </node>
    </node>

    <!-- LAYER 2: Operasional -->
    <node ID="layer2" TEXT="LAPISAN 2: Operasional Pengadaan" POSITION="right">
      <edge COLOR="#4ECDC4" WIDTH="2"/>
      <font NAME="Arial" SIZE="14" BOLD="true" COLOR="#4ECDC4"/>

      <node ID="l2_vendor" TEXT="Vendor Management">
        <edge COLOR="#7FE5E0"/>
        <node TEXT="Registration"/>
        <node TEXT="Qualification"/>
        <node TEXT="Master Database"/>
        <node TEXT="Performance Tracking"/>
      </node>

      <node ID="l2_catalog" TEXT="Catalog &amp; Inventory">
        <edge COLOR="#7FE5E0"/>
        <node TEXT="Product Database"/>
        <node TEXT="Stock Levels"/>
        <node TEXT="SKU Management"/>
        <node TEXT="Pricing"/>
      </node>

      <node ID="l2_contract" TEXT="Contract Lifecycle">
        <edge COLOR="#7FE5E0"/>
        <node TEXT="PKS (Contracts)"/>
        <node TEXT="SPK (Work Orders)"/>
        <node TEXT="KSO Management"/>
        <node TEXT="Renewal Tracking"/>
      </node>
    </node>

    <!-- LAYER 3: Integrasi -->
    <node ID="layer3" TEXT="LAPISAN 3: Integrasi Sistem" POSITION="right">
      <edge COLOR="#FFE66D" WIDTH="2"/>
      <font NAME="Arial" SIZE="14" BOLD="true" COLOR="#FFE66D"/>

      <node ID="l3_simrs" TEXT="SIMRS Integration">
        <edge COLOR="#FFF0A3"/>
        <node TEXT="Bidding Data"/>
        <node TEXT="Inventory Updates"/>
        <node TEXT="Stock Confirmation"/>
      </node>

      <node ID="l3_finance" TEXT="Finance/ERP">
        <edge COLOR="#FFF0A3"/>
        <node TEXT="GL Posting"/>
        <node TEXT="Invoice Processing"/>
        <node TEXT="Payment Execution"/>
        <node TEXT="Budget Tracking"/>
      </node>

      <node ID="l3_other" TEXT="Other Systems">
        <edge COLOR="#FFF0A3"/>
        <node TEXT="Warehouse"/>
        <node TEXT="HR/Payroll"/>
        <node TEXT="Komite Anggaran"/>
      </node>
    </node>

    <!-- LAYER 4: Analitik &amp; Transparansi -->
    <node ID="layer4" TEXT="LAPISAN 4: Analitik &amp; Transparansi" POSITION="right">
      <edge COLOR="#95E1D3" WIDTH="2"/>
      <font NAME="Arial" SIZE="14" BOLD="true" COLOR="#95E1D3"/>

      <node ID="l4_dashboard" TEXT="Command Center Dashboard">
        <edge COLOR="#B8F3ED"/>
        <node TEXT="Real-time KPIs"/>
        <node TEXT="Vendor Status"/>
        <node TEXT="Financial Metrics"/>
        <node TEXT="Alerts &amp; Escalations"/>
      </node>

      <node ID="l4_analytics" TEXT="Analytics &amp; Insights">
        <edge COLOR="#B8F3ED"/>
        <node TEXT="Spend Analysis"/>
        <node TEXT="Vendor Benchmarking"/>
        <node TEXT="Trend Analysis"/>
        <node TEXT="Forecasting"/>
      </node>

      <node ID="l4_audit" TEXT="Audit Trail &amp; SPI">
        <edge COLOR="#B8F3ED"/>
        <node TEXT="Complete Traceability"/>
        <node TEXT="Compliance Reports"/>
        <node TEXT="Exception Logs"/>
        <node TEXT="SPI Integration"/>
      </node>
    </node>

    <!-- LAYER 5: Infrastruktur &amp; Keamanan -->
    <node ID="layer5" TEXT="LAPISAN 5: Infrastruktur &amp; Keamanan" POSITION="right">
      <edge COLOR="#C7CEEA" WIDTH="2"/>
      <font NAME="Arial" SIZE="14" BOLD="true" COLOR="#C7CEEA"/>

      <node ID="l5_cloud" TEXT="Cloud Infrastructure">
        <edge COLOR="#DDD6F3"/>
        <node TEXT="Servers (GCP/AWS)"/>
        <node TEXT="Database"/>
        <node TEXT="Storage"/>
        <node TEXT="Backup &amp; DR"/>
      </node>

      <node ID="l5_security" TEXT="Security &amp; Access">
        <edge COLOR="#DDD6F3"/>
        <node TEXT="SSO / LDAP"/>
        <node TEXT="Role-Based Access"/>
        <node TEXT="Encryption"/>
        <node TEXT="Audit Logging"/>
      </node>

      <node ID="l5_integration" TEXT="API &amp; Integration">
        <edge COLOR="#DDD6F3"/>
        <node TEXT="REST APIs"/>
        <node TEXT="Webhooks"/>
        <node TEXT="Data Sync"/>
        <node TEXT="Mobile Apps"/>
      </node>
    </node>

    <!-- AI GUARDIAN OVERLAY -->
    <node ID="ai_guardian" TEXT="🤖 AI PENJAGA SPO (Cross-Layer)" POSITION="left">
      <edge COLOR="#FF006E" WIDTH="2"/>
      <font NAME="Arial" SIZE="14" BOLD="true" COLOR="#FF006E"/>

      <node TEXT="Real-time SPO Validation">
        <node TEXT="Document Processing"/>
        <node TEXT="Rule Engine"/>
        <node TEXT="Compliance Checking"/>
      </node>

      <node TEXT="Guidance &amp; Alerts">
        <node TEXT="Chatbot Q&amp;A"/>
        <node TEXT="Violation Detection"/>
        <node TEXT="Auto-alerts"/>
      </node>

      <node TEXT="Analytics">
        <node TEXT="Compliance Metrics"/>
        <node TEXT="Risk Scoring"/>
        <node TEXT="Insights"/>
      </node>
    </node>
  </node>
</map>
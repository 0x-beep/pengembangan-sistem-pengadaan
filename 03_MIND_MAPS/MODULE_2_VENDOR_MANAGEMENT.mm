<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="MODULE 2: Vendor Management (Registration, KSO, Database)">
    <edge COLOR="#000000" WIDTH="2"/>
    <font NAME="Arial" SIZE="16" BOLD="true"/>

    <!-- VENDOR REGISTRATION -->
    <node ID="registration" TEXT="VENDOR REGISTRATION" POSITION="right">
      <edge COLOR="#3498DB" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#3498DB"/>

      <node TEXT="Self-Service Portal">
        <node TEXT="Vendor creates account"/>
        <node TEXT="Login credentials"/>
        <node TEXT="Profile setup"/>
      </node>

      <node TEXT="Information Capture">
        <node TEXT="Company name &amp; address"/>
        <node TEXT="Contact person &amp; phone"/>
        <node TEXT="Tax ID (NPWP)"/>
        <node TEXT="Business license (SIUP)"/>
        <node TEXT="Bank account info"/>
      </node>

      <node TEXT="Document Upload">
        <node TEXT="Company registration"/>
        <node TEXT="Tax certificate"/>
        <node TEXT="Business license"/>
        <node TEXT="Financial statements (3 years)"/>
        <node TEXT="References/Previous contracts"/>
      </node>

      <node TEXT="Initial Review">
        <node TEXT="Document completeness check"/>
        <node TEXT="Format verification"/>
        <node TEXT="Validity check"/>
        <node TEXT="Request for clarification if needed"/>
      </node>
    </node>

    <!-- QUALIFICATION PROCESS -->
    <node ID="qualification" TEXT="VENDOR QUALIFICATION &amp; APPROVAL" POSITION="right">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="Legal Checklist">
        <node TEXT="✓ Tax ID valid"/>
        <node TEXT="✓ Business license current"/>
        <node TEXT="✓ No blacklist status"/>
        <node TEXT="✓ Financial health acceptable"/>
        <node TEXT="✓ References verified"/>
      </node>

      <node TEXT="Technical Qualification">
        <node TEXT="Product/Service expertise"/>
        <node TEXT="Equipment &amp; facilities"/>
        <node TEXT="Quality certifications"/>
        <node TEXT="Compliance with standards"/>
      </node>

      <node TEXT="Financial Qualification">
        <node TEXT="Financial stability assessment"/>
        <node TEXT="Bank references"/>
        <node TEXT="Payment history"/>
        <node TEXT="Capacity to deliver"/>
      </node>

      <node TEXT="Approval Decision">
        <node TEXT="Qualified: Activate in master DB"/>
        <node TEXT="Conditional: Request more info"/>
        <node TEXT="Not qualified: Reject with reason"/>
      </node>

      <node TEXT="Notification">
        <node TEXT="Email to vendor (approved/rejected)"/>
        <node TEXT="Portal status update"/>
      </node>
    </node>

    <!-- VENDOR MASTER DATABASE -->
    <node ID="masterdb" TEXT="VENDOR MASTER DATABASE" POSITION="right">
      <edge COLOR="#27AE60" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#27AE60"/>

      <node TEXT="Data Fields">
        <node TEXT="Vendor ID (auto)"/>
        <node TEXT="Company name"/>
        <node TEXT="Category (Barang/Jasa/Konstruksi/Konsultan)"/>
        <node TEXT="Contact details"/>
        <node TEXT="Bank account"/>
        <node TEXT="Tax ID"/>
        <node TEXT="Status (Active/Inactive/Blacklist)"/>
      </node>

      <node TEXT="Categories">
        <node TEXT="Daan Umum: Goods suppliers"/>
        <node TEXT="Daan Jasa Konstruksi: Construction"/>
        <node TEXT="Daan Jasa Konsultan: Consultants"/>
        <node TEXT="Daan Jasa Pemborongan: Services"/>
        <node TEXT="KSO Suppliers: Lab/Farmasi/BMHP"/>
      </node>

      <node TEXT="Data Management">
        <node TEXT="Auto-update from portal"/>
        <node TEXT="Manual updates by Kasie"/>
        <node TEXT="Regular review &amp; cleanup"/>
        <node TEXT="Audit trail of changes"/>
      </node>

      <node TEXT="Visibility">
        <node TEXT="Procurement: All active vendors"/>
        <node TEXT="Tender: Filter by category"/>
        <node TEXT="Finance: Payment tracking"/>
        <node TEXT="SBU: View for direct request"/>
      </node>
    </node>

    <!-- CATEGORY MANAGEMENT -->
    <node ID="category" TEXT="CATEGORY MANAGEMENT" POSITION="right">
      <edge COLOR="#F39C12" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#F39C12"/>

      <node TEXT="Daan Umum (Goods)">
        <node TEXT="Medical supplies"/>
        <node TEXT="Office equipment"/>
        <node TEXT="Utilities &amp; maintenance"/>
        <node TEXT="Food &amp; beverages"/>
        <node TEXT="Consumables"/>
      </node>

      <node TEXT="Daan Jasa Konstruksi">
        <node TEXT="Building construction"/>
        <node TEXT="Renovation"/>
        <node TEXT="Civil works"/>
      </node>

      <node TEXT="Daan Jasa Konsultan">
        <node TEXT="Management consulting"/>
        <node TEXT="Technical consultation"/>
        <node TEXT="Training services"/>
      </node>

      <node TEXT="Daan Jasa Swakelola">
        <node TEXT="In-house service execution"/>
        <node TEXT="Equipment rental"/>
      </node>

      <node TEXT="KSO Suppliers (Special)">
        <node TEXT="Lab consumables"/>
        <node TEXT="Pharmacy supplies"/>
        <node TEXT="Medical devices (BMHP)"/>
      </node>
    </node>

    <!-- KSO SETUP &amp; MANAGEMENT -->
    <node ID="kso" TEXT="KSO (KONTRAK SUPLAI OBAT/ALKES) SETUP" POSITION="right">
      <edge COLOR="#9B59B6" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#9B59B6"/>

      <node TEXT="KSO Types">
        <node TEXT="Lab: Consumables &amp; reagents"/>
        <node TEXT="Farmasi: Medicines &amp; drugs"/>
        <node TEXT="BMHP: Medical devices (alkes)"/>
      </node>

      <node TEXT="Contract Setup">
        <node TEXT="Vendor selection (tender/direct)"/>
        <node TEXT="Contract negotiation"/>
        <node TEXT="Price list agreed"/>
        <node TEXT="Delivery schedule"/>
        <node TEXT="Payment terms (usually 30 days)"/>
      </node>

      <node TEXT="KSO Terms">
        <node TEXT="Quantity commitment (minimum)"/>
        <node TEXT="Price lock period"/>
        <node TEXT="Delivery SLA"/>
        <node TEXT="Quality guarantees"/>
        <node TEXT="Damage/defect policy"/>
      </node>

      <node TEXT="Vendor Portal Feature">
        <node TEXT="Self-reporting of deliveries"/>
        <node TEXT="Consumption tracking"/>
        <node TEXT="Obligation fulfillment"/>
        <node TEXT="Invoice submission"/>
      </node>

      <node TEXT="Multi-KSO Strategy">
        <node TEXT="Lab: 2-3 vendors per category"/>
        <node TEXT="Pharmacy: Main + backup"/>
        <node TEXT="BMHP: Specialized vendors"/>
        <node TEXT="Load balancing based on consumption"/>
      </node>
    </node>

    <!-- VENDOR PERFORMANCE TRACKING -->
    <node ID="performance" TEXT="VENDOR PERFORMANCE TRACKING" POSITION="right">
      <edge COLOR="#16A085" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#16A085"/>

      <node TEXT="7-Dimension Scoring">
        <node TEXT="1. Harga (Price competitiveness)"/>
        <node TEXT="2. Kualitas (Product quality)"/>
        <node TEXT="3. Pengiriman (On-time delivery)"/>
        <node TEXT="4. Compliance (SPO adherence)"/>
        <node TEXT="5. Keuangan (Financial reliability)"/>
        <node TEXT="6. Respons (Response time)"/>
        <node TEXT="7. Partnership (Collaboration)"/>
      </node>

      <node TEXT="Data Collection">
        <node TEXT="Invoice data"/>
        <node TEXT="Delivery tracking"/>
        <node TEXT="Quality reports"/>
        <node TEXT="Complaints log"/>
        <node TEXT="KSO reporting (self)"/>
      </node>

      <node TEXT="Monthly Scoring">
        <node TEXT="Collect performance data"/>
        <node TEXT="Score each dimension (1-5)"/>
        <node TEXT="Calculate weighted score"/>
        <node TEXT="Generate scorecard"/>
      </node>

      <node TEXT="Quarterly Review">
        <node TEXT="Trend analysis"/>
        <node TEXT="Improvement identification"/>
        <node TEXT="Discussion with vendor"/>
        <node TEXT="Corrective action plan if needed"/>
      </node>
    </node>

    <!-- VENDOR DECISIONS &amp; ACTIONS -->
    <node ID="decisions" TEXT="VENDOR DECISIONS &amp; ACTIONS" POSITION="right">
      <edge COLOR="#C0392B" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#C0392B"/>

      <node TEXT="Renewal Decision">
        <node TEXT="Score &gt;80%: Auto-renewal"/>
        <node TEXT="Score 60-80%: Improvement plan"/>
        <node TEXT="Score &lt;60%: Replacement consideration"/>
      </node>

      <node TEXT="Contract Actions">
        <node TEXT="Extend contract (12+ months)"/>
        <node TEXT="Renegotiate price"/>
        <node TEXT="Adjust volumes"/>
        <node TEXT="Add new categories"/>
      </node>

      <node TEXT="Corrective Actions">
        <node TEXT="Performance improvement plan"/>
        <node TEXT="Cost reduction negotiation"/>
        <node TEXT="Quality certification requirement"/>
      </node>

      <node TEXT="Termination/Blacklist">
        <node TEXT="Non-performance (repeated)"/>
        <node TEXT="Quality failures"/>
        <node TEXT="Compliance violations"/>
        <node TEXT="Financial instability"/>
        <node TEXT="Proper notice &amp; documentation"/>
      </node>
    </node>

    <!-- INTEGRATION &amp; COMMUNICATION -->
    <node ID="integration" TEXT="INTEGRATION &amp; COMMUNICATION" POSITION="left">
      <edge COLOR="#1ABC9C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#1ABC9C"/>

      <node TEXT="Systems Connected">
        <node TEXT="Vendor portal (self-service)"/>
        <node TEXT="Procurement platform"/>
        <node TEXT="Finance (payment tracking)"/>
        <node TEXT="Warehouse (stock tracking)"/>
      </node>

      <node TEXT="Data Flow">
        <node TEXT="Registration → Master DB"/>
        <node TEXT="Performance data → Scoring"/>
        <node TEXT="KSO data → Portal"/>
        <node TEXT="Reports → Stakeholders"/>
      </node>

      <node TEXT="Vendor Communication">
        <node TEXT="Email notifications"/>
        <node TEXT="Portal announcements"/>
        <node TEXT="Performance scorecards"/>
        <node TEXT="Contract updates"/>
      </node>

      <node TEXT="Reporting">
        <node TEXT="Vendor roster report"/>
        <node TEXT="Performance rankings"/>
        <node TEXT="Category analysis"/>
        <node TEXT="Compliance status"/>
      </node>
    </node>

    <!-- SUCCESS METRICS -->
    <node ID="metrics" TEXT="SUCCESS METRICS" POSITION="left">
      <edge COLOR="#2980B9" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#2980B9"/>

      <node TEXT="Vendor Count">
        <node TEXT="Active vendors: 200+"/>
        <node TEXT="By category: Distributed"/>
        <node TEXT="New vendors: Regular intake"/>
      </node>

      <node TEXT="Performance">
        <node TEXT="Avg quality score: &gt;85%"/>
        <node TEXT="On-time delivery: &gt;95%"/>
        <node TEXT="Compliance: 100%"/>
      </node>

      <node TEXT="Cost Impact">
        <node TEXT="Better vendor selection"/>
        <node TEXT="Fewer quality issues"/>
        <node TEXT="Reduced disputes"/>
        <node TEXT="Annual savings: Rp 4.2B"/>
      </node>

      <node TEXT="System Benefit">
        <node TEXT="Transparent vendor database"/>
        <node TEXT="Consistent scoring"/>
        <node TEXT="Data-driven decisions"/>
      </node>
    </node>
  </node>
</map>
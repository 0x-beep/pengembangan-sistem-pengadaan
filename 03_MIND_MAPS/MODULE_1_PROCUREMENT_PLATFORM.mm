<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="MODULE 1: Procurement Platform (Tender → Quote → PO → Payment)">
    <edge COLOR="#000000" WIDTH="2"/>
    <font NAME="Arial" SIZE="16" BOLD="true"/>

    <!-- REQUISITION FLOW -->
    <node ID="requisition" TEXT="REQUISITION FLOW" POSITION="right">
      <edge COLOR="#3498DB" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#3498DB"/>

      <node TEXT="SBU Creates Request">
        <node TEXT="Daan Umum: PP (Permintaan Pembelian)"/>
        <node TEXT="Daan Barang Investasi: IMT (Inventory Material Request)"/>
        <node TEXT="Daan Jasa: SPPJ (Surat Permintaan Pekerjaan Jasa)"/>
      </node>

      <node TEXT="Information Capture">
        <node TEXT="Item/Service description"/>
        <node TEXT="Quantity &amp; Specification"/>
        <node TEXT="Required delivery date"/>
        <node TEXT="Budget code &amp; amount"/>
        <node TEXT="Cost center"/>
      </node>

      <node TEXT="AI Validation">
        <node TEXT="Budget availability check"/>
        <node TEXT="Approval authority validation"/>
        <node TEXT="Specification compliance"/>
        <node TEXT="Historical price check"/>
      </node>

      <node TEXT="Approval Workflow">
        <node TEXT="SBU Head approval"/>
        <node TEXT="Budget manager review"/>
        <node TEXT="Finance pre-check"/>
        <node TEXT="Ready for tender"/>
      </node>
    </node>

    <!-- APPROVAL WORKFLOW -->
    <node ID="approval" TEXT="APPROVAL WORKFLOW" POSITION="right">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="Authority Matrix (Daan Umum)">
        <node TEXT="≤10M: Kasie + Manager"/>
        <node TEXT="&gt;10-25M: + GM"/>
        <node TEXT="&gt;25-50M: + Direktur Ops"/>
        <node TEXT="&gt;50-100M: + Direktur Utama"/>
      </node>

      <node TEXT="Authority Matrix (Daan Jasa)">
        <node TEXT="1-25M: Kasie + Manager"/>
        <node TEXT="&gt;25-100M: + GM"/>
        <node TEXT="&gt;100M-1B: + Direktur Ops"/>
        <node TEXT="&gt;1B: + Direktur Utama (+ 5% bank guarantee)"/>
      </node>

      <node TEXT="Approval Rules">
        <node TEXT="Sequential approval required"/>
        <node TEXT="No skipping authority levels"/>
        <node TEXT="Time-based escalation"/>
        <node TEXT="Override approval trail"/>
      </node>

      <node TEXT="System Enforcement">
        <node TEXT="AI validates approval authority"/>
        <node TEXT="System blocks if insufficient authority"/>
        <node TEXT="Audit trail of all approvals"/>
      </node>
    </node>

    <!-- TENDER PROCESS -->
    <node ID="tender" TEXT="TENDER PROCESS" POSITION="right">
      <edge COLOR="#27AE60" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#27AE60"/>

      <node TEXT="Tender Preparation">
        <node TEXT="SPPH (Surat Permintaan Penawaran) creation"/>
        <node TEXT="HPS (Harga Perkiraan Sementara) calculation"/>
        <node TEXT="Specification finalization"/>
        <node TEXT="Timeline setting"/>
      </node>

      <node TEXT="Vendor Invitation">
        <node TEXT="Select vendors from master database"/>
        <node TEXT="Send SPPH via system"/>
        <node TEXT="Email notification to vendors"/>
        <node TEXT="Portal access for quote submission"/>
      </node>

      <node TEXT="Quote Collection">
        <node TEXT="SJPH (Surat Jawaban Penawaran) submission"/>
        <node TEXT="Quote deadline management"/>
        <node TEXT="Document verification"/>
        <node TEXT="Completeness check"/>
      </node>

      <node TEXT="Bid Tabulation">
        <node TEXT="Quote compilation"/>
        <node TEXT="Price comparison"/>
        <node TEXT="Format validation"/>
        <node TEXT="AI-assisted evaluation"/>
      </node>

      <node TEXT="SLA: 14 hari (typical)"/>
    </node>

    <!-- DIRECT APPOINTMENT (ALTERNATIVE) -->
    <node ID="direct" TEXT="DIRECT APPOINTMENT (Alternative)" POSITION="right">
      <edge COLOR="#F39C12" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#F39C12"/>

      <node TEXT="Criteria for Direct">
        <node TEXT="Emergency situations"/>
        <node TEXT="Single source availability"/>
        <node TEXT="Specialized services"/>
        <node TEXT="Prev vendor continuation"/>
      </node>

      <node TEXT="Process">
        <node TEXT="Vendor selection"/>
        <node TEXT="Quotation request"/>
        <node TEXT="Price negotiation"/>
        <node TEXT="Final approval"/>
      </node>

      <node TEXT="Documentation">
        <node TEXT="Justification memo"/>
        <node TEXT="Approval from authority"/>
        <node TEXT="Final quote"/>
      </node>

      <node TEXT="SLA: 5 hari (faster)"/>
    </node>

    <!-- VENDOR SCORING &amp; SELECTION -->
    <node ID="scoring" TEXT="VENDOR SCORING &amp; SELECTION" POSITION="right">
      <edge COLOR="#9B59B6" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#9B59B6"/>

      <node TEXT="Scoring Criteria">
        <node TEXT="Harga (Price): 25%"/>
        <node TEXT="Kualitas (Quality): 20%"/>
        <node TEXT="Delivery/Maintenance: 20%"/>
        <node TEXT="User Need Fulfillment: 20%"/>
        <node TEXT="Brand/Certification: 15%"/>
      </node>

      <node TEXT="Scoring Process">
        <node TEXT="Create evaluation form"/>
        <node TEXT="Assign scoring panel"/>
        <node TEXT="Individual scoring"/>
        <node TEXT="Consensus discussion"/>
        <node TEXT="Final scoring"/>
      </node>

      <node TEXT="Scoring System">
        <node TEXT="1-5 point scale"/>
        <node TEXT="Weighted calculation"/>
        <node TEXT="Total score ranking"/>
      </node>

      <node TEXT="Winner Selection">
        <node TEXT="Highest score vendor selected"/>
        <node TEXT="Price acceptability check (vs HPS)"/>
        <node TEXT="Final approval"/>
      </node>

      <node TEXT="Output: Winning vendor + final price"/>
    </node>

    <!-- PO GENERATION -->
    <node ID="po" TEXT="PO GENERATION &amp; ISSUANCE" POSITION="right">
      <edge COLOR="#16A085" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#16A085"/>

      <node TEXT="PO Preparation">
        <node TEXT="Vendor details (from master DB)"/>
        <node TEXT="Item specifications"/>
        <node TEXT="Quantity &amp; unit price"/>
        <node TEXT="Total amount"/>
        <node TEXT="Delivery requirements"/>
        <node TEXT="Payment terms"/>
      </node>

      <node TEXT="PO Content">
        <node TEXT="PO number (auto-generated)"/>
        <node TEXT="Vendor name &amp; address"/>
        <node TEXT="Delivery address (SBU location)"/>
        <node TEXT="Item line items"/>
        <node TEXT="Terms &amp; conditions"/>
        <node TEXT="Payment schedule"/>
      </node>

      <node TEXT="Approvals">
        <node TEXT="Kasie review"/>
        <node TEXT="Manager approval"/>
        <node TEXT="Finance final check"/>
        <node TEXT="System sign-off"/>
      </node>

      <node TEXT="Issuance">
        <node TEXT="PO PDF generation"/>
        <node TEXT="Vendor notification"/>
        <node TEXT="Vendor portal update"/>
        <node TEXT="Finance recording (commitment)"/>
      </node>

      <node TEXT="Output: Signed PO + vendor acknowledgment"/>
    </node>

    <!-- SLA TRACKING -->
    <node ID="sla" TEXT="SLA TRACKING" POSITION="left">
      <edge COLOR="#34495E" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#34495E"/>

      <node TEXT="Cycle SLAs">
        <node TEXT="PP approval: 2 hours"/>
        <node TEXT="Tender: 14 days"/>
        <node TEXT="Direct: 5 days"/>
        <node TEXT="PO generation: 1 day"/>
      </node>

      <node TEXT="Monitoring">
        <node TEXT="Real-time timer in system"/>
        <node TEXT="Escalation alerts at 80% time used"/>
        <node TEXT="Dashboard visibility"/>
      </node>

      <node TEXT="Reporting">
        <node TEXT="SLA compliance rate"/>
        <node TEXT="Bottleneck analysis"/>
        <node TEXT="Performance trends"/>
      </node>
    </node>

    <!-- INTEGRATION POINTS -->
    <node ID="integration" TEXT="INTEGRATION POINTS" POSITION="left">
      <edge COLOR="#1ABC9C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#1ABC9C"/>

      <node TEXT="Systems Connected">
        <node TEXT="Finance (budget check)"/>
        <node TEXT="Vendor Master DB"/>
        <node TEXT="Warehouse (delivery address)"/>
        <node TEXT="SIMRS (integration)"/>
      </node>

      <node TEXT="Data Flow">
        <node TEXT="Budget data in"/>
        <node TEXT="Vendor data in"/>
        <node TEXT="PO data out to Finance"/>
        <node TEXT="Delivery tracking"/>
      </node>

      <node TEXT="Notifications">
        <node TEXT="Email to SBU on approval"/>
        <node TEXT="Email to vendor on PO issuance"/>
        <node TEXT="Portal update for all parties"/>
      </node>
    </node>

    <!-- KEY SUCCESS FACTORS -->
    <node ID="success" TEXT="KEY SUCCESS FACTORS" POSITION="left">
      <edge COLOR="#C0392B" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#C0392B"/>

      <node TEXT="Data Quality">
        <node TEXT="Complete vendor master DB"/>
        <node TEXT="Accurate specifications"/>
        <node TEXT="Correct budget codes"/>
      </node>

      <node TEXT="Process Discipline">
        <node TEXT="Follow approval matrix"/>
        <node TEXT="Complete documentation"/>
        <node TEXT="Timely actions"/>
      </node>

      <node TEXT="AI Guardian Role">
        <node TEXT="Validate specifications"/>
        <node TEXT="Check authority"/>
        <node TEXT="Suggest improvements"/>
        <node TEXT="Alert on issues"/>
      </node>

      <node TEXT="Stakeholder Engagement">
        <node TEXT="SBU cooperation"/>
        <node TEXT="Vendor responsiveness"/>
        <node TEXT="Finance coordination"/>
      </node>
    </node>
  </node>
</map>
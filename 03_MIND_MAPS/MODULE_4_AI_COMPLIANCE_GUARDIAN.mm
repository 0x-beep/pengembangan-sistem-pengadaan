<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="MODULE 4: AI Penjaga Kepatuhan SPO">
    <edge COLOR="#000000" WIDTH="2"/>
    <font NAME="Arial" SIZE="16" BOLD="true"/>

    <!-- SYSTEM OVERVIEW -->
    <node ID="overview" TEXT="SYSTEM OVERVIEW" POSITION="right">
      <edge COLOR="#FF006E" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#FF006E"/>

      <node TEXT="Purpose">
        <node TEXT="Real-time SPO enforcement"/>
        <node TEXT="Compliance validation at every step"/>
        <node TEXT="Guidance system for users"/>
        <node TEXT="Audit trail for SPI"/>
      </node>

      <node TEXT="Scope">
        <node TEXT="All 9 phases of procurement"/>
        <node TEXT="All document types (PP, SPPH, PO, etc)"/>
        <node TEXT="All procurement pathways"/>
        <node TEXT="Both Daan Umum &amp; Daan Jasa"/>
      </node>

      <node TEXT="AI Provider">
        <node TEXT="Deepseek API (recommended)"/>
        <node TEXT="Document processing"/>
        <node TEXT="Rule validation"/>
        <node TEXT="Guidance generation"/>
      </node>

      <node TEXT="Performance Target">
        <node TEXT="Response time: &lt;500ms"/>
        <node TEXT="Accuracy: &gt;95%"/>
        <node TEXT="Compliance rate: 100%"/>
        <node TEXT="Uptime: 99.5%"/>
      </node>
    </node>

    <!-- SPO KNOWLEDGE BASE -->
    <node ID="knowledge" TEXT="SPO KNOWLEDGE BASE" POSITION="right">
      <edge COLOR="#3498DB" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#3498DB"/>

      <node TEXT="SPO Sources">
        <node TEXT="Pedoman Pengadaan KMU (official)"/>
        <node TEXT="GLOSARIUM_ISTILAH_KMU"/>
        <node TEXT="Historical decisions &amp; precedents"/>
        <node TEXT="Permenkes requirements"/>
        <node TEXT="LKPP guidelines"/>
      </node>

      <node TEXT="SPO Digitization">
        <node TEXT="Extract key rules from documents"/>
        <node TEXT="Structure rules in database"/>
        <node TEXT="Create rule engine format"/>
        <node TEXT="Regular updates &amp; maintenance"/>
      </node>

      <node TEXT="Vector Database">
        <node TEXT="Embed SPO rules as vectors"/>
        <node TEXT="Semantic search capability"/>
        <node TEXT="Fast retrieval (similarity)"/>
        <node TEXT="Link to source documents"/>
      </node>

      <node TEXT="Rule Categories">
        <node TEXT="Authorization rules"/>
        <node TEXT="Sequence rules"/>
        <node TEXT="Document rules"/>
        <node TEXT="Vendor rules"/>
        <node TEXT="Financial rules"/>
      </node>
    </node>

    <!-- DOCUMENT PROCESSING -->
    <node ID="document" TEXT="DOCUMENT PROCESSING" POSITION="right">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="Input Documents">
        <node TEXT="PP (Permintaan Pembelian)"/>
        <node TEXT="SPPH (Surat Permintaan Penawaran)"/>
        <node TEXT="SJPH (Surat Jawaban Penawaran)"/>
        <node TEXT="PO (Purchase Order)"/>
        <node TEXT="SPK/PKS (Contracts)"/>
        <node TEXT="BAPB (Receipt)"/>
        <node TEXT="Invoice"/>
      </node>

      <node TEXT="Processing Steps">
        <node TEXT="1. Upload document"/>
        <node TEXT="2. OCR/extract text"/>
        <node TEXT="3. Parse structure"/>
        <node TEXT="4. Extract key fields"/>
        <node TEXT="5. Validate format"/>
        <node TEXT="6. Compare with SPO"/>
      </node>

      <node TEXT="Data Extraction">
        <node TEXT="Amount"/>
        <node TEXT="Vendor"/>
        <node TEXT="Specification"/>
        <node TEXT="Timeline"/>
        <node TEXT="Approvers"/>
        <node TEXT="Cost center"/>
      </node>

      <node TEXT="Output">
        <node TEXT="Extracted data (JSON)"/>
        <node TEXT="Confidence score"/>
        <node TEXT="Issues found (if any)"/>
        <node TEXT="Recommendations"/>
      </node>
    </node>

    <!-- PROCEDURE VALIDATION ENGINE -->
    <node ID="validation" TEXT="PROCEDURE VALIDATION ENGINE" POSITION="right">
      <edge COLOR="#27AE60" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#27AE60"/>

      <node TEXT="6-Step Validation">
        <node TEXT="Step 1: Document completeness"/>
        <node TEXT="Step 2: Required approvals"/>
        <node TEXT="Step 3: Authorization matrix"/>
        <node TEXT="Step 4: Amount thresholds"/>
        <node TEXT="Step 5: Vendor status"/>
        <node TEXT="Step 6: Timeline/SLA"/>
      </node>

      <node TEXT="Step 1: Completeness">
        <node TEXT="All required fields present"/>
        <node TEXT="Supporting docs attached"/>
        <node TEXT="Data format correct"/>
        <node TEXT="Legible &amp; signed (if needed)"/>
      </node>

      <node TEXT="Step 2: Approvals">
        <node TEXT="Check approval sequence"/>
        <node TEXT="Verify all levels present"/>
        <node TEXT="Signature validation"/>
        <node TEXT="Approval authority confirmation"/>
      </node>

      <node TEXT="Step 3: Authorization Matrix">
        <node TEXT="Check amount vs authority"/>
        <node TEXT="Daan Umum rules applied"/>
        <node TEXT="Daan Jasa rules applied"/>
        <node TEXT="Special category rules (KSO)"/>
      </node>

      <node TEXT="Step 4: Thresholds">
        <node TEXT="Amount within approval limit"/>
        <node TEXT="Amount within budget"/>
        <node TEXT="No over-spending"/>
        <node TEXT="Cost center valid"/>
      </node>

      <node TEXT="Step 5: Vendor Status">
        <node TEXT="Vendor in master database"/>
        <node TEXT="Vendor not blacklisted"/>
        <node TEXT="Vendor qualified for category"/>
        <node TEXT="Vendor SPA (if needed)"/>
      </node>

      <node TEXT="Step 6: Timeline/SLA">
        <node TEXT="Action within SLA"/>
        <node TEXT="Milestone dates achievable"/>
        <node TEXT="No past dates"/>
        <node TEXT="Reasonable timeline"/>
      </node>
    </node>

    <!-- RULE IMPLEMENTATION -->
    <node ID="rules" TEXT="RULE IMPLEMENTATION DETAILS" POSITION="right">
      <edge COLOR="#9B59B6" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#9B59B6"/>

      <node TEXT="Authorization Rules">
        <node TEXT="IF amount ≤ 10M THEN Kasie + Manager"/>
        <node TEXT="IF 10M &lt; amount ≤ 25M THEN + GM"/>
        <node TEXT="IF 25M &lt; amount ≤ 50M THEN + Dir Ops"/>
        <node TEXT="IF amount &gt; 50M THEN + Dir Utama"/>
        <node TEXT="Special: Daan Jasa different thresholds"/>
      </node>

      <node TEXT="Sequence Rules">
        <node TEXT="Must have PP before SPPH"/>
        <node TEXT="Must have SPPH before quotes"/>
        <node TEXT="Must have quotes before PO"/>
        <node TEXT="Must have BAPB before payment"/>
      </node>

      <node TEXT="Document Rules">
        <node TEXT="PO must reference SPPH number"/>
        <node TEXT="BAPB must match PO"/>
        <node TEXT="Invoice must match BAPB"/>
        <node TEXT="All signatures present"/>
      </node>

      <node TEXT="Vendor Rules">
        <node TEXT="Only approved vendors"/>
        <node TEXT="Vendor matches category"/>
        <node TEXT="No repeated violations"/>
        <node TEXT="SPA/Insurance current"/>
      </node>

      <node TEXT="Financial Rules">
        <node TEXT="Budget available"/>
        <node TEXT="Amount matches quotes"/>
        <node TEXT="No unauthorized changes"/>
        <node TEXT="Price within HPS range"/>
      </node>
    </node>

    <!-- CHATBOT GUIDANCE SYSTEM -->
    <node ID="chatbot" TEXT="CHATBOT GUIDANCE SYSTEM" POSITION="right">
      <edge COLOR="#F39C12" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#F39C12"/>

      <node TEXT="User Interface">
        <node TEXT="Chat widget on platform"/>
        <node TEXT="Natural language input"/>
        <node TEXT="Mobile accessible"/>
        <node TEXT="Available 24/7"/>
      </node>

      <node TEXT="Question Types">
        <node TEXT="SPO procedure: How do I...?"/>
        <node TEXT="Approval process: Who approves...?"/>
        <node TEXT="Document types: What is BAPB?"/>
        <node TEXT="Vendor rules: Can I use...?"/>
        <node TEXT="Timeline: How long for...?"/>
      </node>

      <node TEXT="Guidance Examples">
        <node TEXT="Q: Bagaimana cara membuat PO?"/>
        <node TEXT="A: Pertama buat PP, tunggu approval, lalu buat SPPH, terima quotes, pilih vendor, buat PO, kirim ke vendor..."/>
        <node TEXT=""/>
        <node TEXT="Q: Siapa yang harus approve PO 50 Juta?"/>
        <node TEXT="A: Kasie + Manager + GM + Direktur Ops. Semua harus approve sesuai urutan."/>
      </node>

      <node TEXT="RAG System">
        <node TEXT="Question → Vector search"/>
        <node TEXT="Find relevant SPO rules"/>
        <node TEXT="Context retrieval"/>
        <node TEXT="Generate answer"/>
        <node TEXT="Cite sources"/>
      </node>

      <node TEXT="Learning">
        <node TEXT="Track FAQ"/>
        <node TEXT="Improve responses"/>
        <node TEXT="Add new questions"/>
      </node>
    </node>

    <!-- REAL-TIME ALERTS &amp; COMPLIANCE -->
    <node ID="alerts" TEXT="REAL-TIME ALERTS &amp; COMPLIANCE" POSITION="right">
      <edge COLOR="#16A085" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#16A085"/>

      <node TEXT="Alert Types">
        <node TEXT="ERROR: Compliance violation"/>
        <node TEXT="WARNING: Potential issue"/>
        <node TEXT="INFO: Guidance suggestion"/>
        <node TEXT="SUCCESS: Valid action"/>
      </node>

      <node TEXT="Alert Triggers">
        <node TEXT="Missing required info"/>
        <node TEXT="Insufficient authority"/>
        <node TEXT="Budget exceeded"/>
        <node TEXT="Vendor blacklisted"/>
        <node TEXT="SLA exceeded"/>
        <node TEXT="Document incomplete"/>
      </node>

      <node TEXT="Alert Actions">
        <node TEXT="Display in UI (red/yellow)"/>
        <node TEXT="Block submission (errors)"/>
        <node TEXT="Allow with warning (warnings)"/>
        <node TEXT="Auto-suggest fixes"/>
        <node TEXT="Escalate to supervisor"/>
      </node>

      <node TEXT="Compliance Tracking">
        <node TEXT="Count violations"/>
        <node TEXT="Track patterns"/>
        <node TEXT="User training triggers"/>
        <node TEXT="Performance scoring"/>
      </node>
    </node>

    <!-- AUDIT TRAIL &amp; REPORTING -->
    <node ID="audit" TEXT="AUDIT TRAIL &amp; REPORTING" POSITION="right">
      <edge COLOR="#C0392B" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#C0392B"/>

      <node TEXT="Audit Logging">
        <node TEXT="Every validation action logged"/>
        <node TEXT="User identification"/>
        <node TEXT="Timestamp"/>
        <node TEXT="Document version"/>
        <node TEXT="Rules applied"/>
        <node TEXT="Result (pass/fail)"/>
      </node>

      <node TEXT="Compliance Reports">
        <node TEXT="Monthly compliance rate"/>
        <node TEXT="Violation types breakdown"/>
        <node TEXT="User performance"/>
        <node TEXT="Department comparison"/>
        <node TEXT="Trend analysis"/>
      </node>

      <node TEXT="SPI Integration">
        <node TEXT="Audit trail export to SPI"/>
        <node TEXT="Compliance dashboard"/>
        <node TEXT="Exception reporting"/>
        <node TEXT="Risk scoring"/>
      </node>

      <node TEXT="Evidence Preservation">
        <node TEXT="All decisions documented"/>
        <node TEXT="Validation logic traceable"/>
        <node TEXT="Source rule referenced"/>
        <node TEXT="Ready for auditor review"/>
      </node>
    </node>

    <!-- ANALYTICS &amp; INSIGHTS -->
    <node ID="analytics" TEXT="ANALYTICS &amp; INSIGHTS" POSITION="left">
      <edge COLOR="#1ABC9C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#1ABC9C"/>

      <node TEXT="Compliance Metrics">
        <node TEXT="Overall compliance: 95%+"/>
        <node TEXT="By department"/>
        <node TEXT="By procurement type"/>
        <node TEXT="Trend (improvement/decline)"/>
      </node>

      <node TEXT="Common Issues">
        <node TEXT="Most frequent violations"/>
        <node TEXT="Root cause analysis"/>
        <node TEXT="Training needs identification"/>
        <node TEXT="Process improvement ideas"/>
      </node>

      <node TEXT="Risk Scoring">
        <node TEXT="User risk profile"/>
        <node TEXT="Department risk"/>
        <node TEXT="Transaction risk"/>
        <node TEXT="Alert priority"/>
      </node>

      <node TEXT="Dashboard">
        <node TEXT="Real-time compliance metrics"/>
        <node TEXT="Alert heatmap"/>
        <node TEXT="Performance trends"/>
        <node TEXT="Comparative analysis"/>
      </node>
    </node>

    <!-- INTEGRATION &amp; WORKFLOW -->
    <node ID="integration" TEXT="INTEGRATION WITH PLATFORM" POSITION="left">
      <edge COLOR="#2980B9" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#2980B9"/>

      <node TEXT="Validation Points">
        <node TEXT="On document submission"/>
        <node TEXT="Before approval"/>
        <node TEXT="At workflow step"/>
        <node TEXT="Real-time as user types"/>
      </node>

      <node TEXT="Data Flow">
        <node TEXT="Document → AI processing"/>
        <node TEXT="Rules check → Validation"/>
        <node TEXT="Alert → User notification"/>
        <node TEXT="Compliance → Audit log"/>
      </node>

      <node TEXT="Workflow Integration">
        <node TEXT="Block invalid actions"/>
        <node TEXT="Suggest corrections"/>
        <node TEXT="Highlight issues"/>
        <node TEXT="Allow overrides (with audit)"/>
      </node>

      <node TEXT="Performance">
        <node TEXT="Sub-500ms response"/>
        <node TEXT="Parallel processing"/>
        <node TEXT="Caching for speed"/>
        <node TEXT="Failover protection"/>
      </node>
    </node>

    <!-- SUCCESS METRICS -->
    <node ID="metrics" TEXT="SUCCESS METRICS" POSITION="left">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="Compliance Achievement">
        <node TEXT="SPO adherence: 100% (target)"/>
        <node TEXT="Violation rate: &lt;1%"/>
        <node TEXT="User compliance training: Done"/>
      </node>

      <node TEXT="Efficiency">
        <node TEXT="Faster approval cycle"/>
        <node TEXT="Fewer rework/corrections"/>
        <node TEXT="Less audit findings"/>
        <node TEXT="Reduced processing time"/>
      </node>

      <node TEXT="Financial Impact">
        <node TEXT="Error prevention: Rp 7.3B/year"/>
        <node TEXT="Audit efficiency: 80% faster"/>
        <node TEXT="Risk reduction: 95%"/>
      </node>

      <node TEXT="User Satisfaction">
        <node TEXT="Clear guidance available"/>
        <node TEXT="System easy to use"/>
        <node TEXT="Support responsive"/>
        <node TEXT="Training effective"/>
      </node>
    </node>
  </node>
</map>
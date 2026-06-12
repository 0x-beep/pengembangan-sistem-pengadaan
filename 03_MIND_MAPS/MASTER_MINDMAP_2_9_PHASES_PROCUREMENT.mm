<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="9 Fase Siklus Pengadaan PT. KMU">
    <edge COLOR="#000000" WIDTH="2"/>
    <font NAME="Arial" SIZE="18" BOLD="true"/>

    <!-- FASE 1 -->
    <node ID="fase1" TEXT="FASE 1: Perencanaan &amp; Anggaran" POSITION="right">
      <edge COLOR="#1A3A52" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#1A3A52"/>

      <node TEXT="Inputs">
        <node TEXT="SBU Kebutuhan"/>
        <node TEXT="RAB (Rencana Anggaran Biaya)"/>
        <node TEXT="RKAP (Rencana Kerja)"/>
      </node>

      <node TEXT="Activities">
        <node TEXT="Validasi Kebutuhan"/>
        <node TEXT="Budget Review"/>
        <node TEXT="Approval Direksi"/>
      </node>

      <node TEXT="Outputs">
        <node TEXT="Budget Ceiling"/>
        <node TEXT="Approved Plan"/>
      </node>

      <node TEXT="Sistem">
        <node TEXT="Finance System"/>
        <node TEXT="Planning Tool"/>
      </node>

      <node TEXT="SLA: 7 hari"/>
    </node>

    <!-- FASE 2 -->
    <node ID="fase2" TEXT="FASE 2: Registrasi &amp; Database Vendor" POSITION="right">
      <edge COLOR="#2E8B9E" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#2E8B9E"/>

      <node TEXT="Inputs">
        <node TEXT="Vendor Registration Form"/>
        <node TEXT="Legal Documents"/>
        <node TEXT="Financial Statements"/>
      </node>

      <node TEXT="Activities">
        <node TEXT="Vendor Register"/>
        <node TEXT="Legal Checklist"/>
        <node TEXT="Database Upload"/>
        <node TEXT="Qualification Review"/>
      </node>

      <node TEXT="Outputs">
        <node TEXT="Vendor Master DB"/>
        <node TEXT="Active Vendor List"/>
      </node>

      <node TEXT="Sistem">
        <node TEXT="Vendor Portal"/>
        <node TEXT="Master Database"/>
      </node>

      <node TEXT="SLA: 14 hari"/>
    </node>

    <!-- FASE 3 -->
    <node ID="fase3" TEXT="FASE 3: Permintaan Pengadaan (PP)" POSITION="right">
      <edge COLOR="#FF9F1C" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#FF9F1C"/>

      <node TEXT="Inputs">
        <node TEXT="PP (Permintaan Pembelian)"/>
        <node TEXT="IMT (Inventory Request)"/>
        <node TEXT="SPPJ (Surat Permintaan Jasa)"/>
      </node>

      <node TEXT="Activities">
        <node TEXT="Create PP/IMT/SPPJ"/>
        <node TEXT="Validation by AI"/>
        <node TEXT="Approval Workflow"/>
      </node>

      <node TEXT="Outputs">
        <node TEXT="Approved PP"/>
        <node TEXT="Ready for Tender"/>
      </node>

      <node TEXT="Sistem">
        <node TEXT="E-Procurement"/>
        <node TEXT="AI Guardian"/>
      </node>

      <node TEXT="SLA: 2 hari"/>
    </node>

    <!-- FASE 4 -->
    <node ID="fase4" TEXT="FASE 4: Pelaksanaan Pengadaan" POSITION="right">
      <edge COLOR="#26A65B" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#26A65B"/>

      <node TEXT="Path A: Tender">
        <node TEXT="SPPH (Surat Permintaan Penawaran)"/>
        <node TEXT="SJPH (Surat Jawaban Penawaran)"/>
        <node TEXT="Bid Evaluation"/>
        <node TEXT="Winner Selection"/>
      </node>

      <node TEXT="Path B: Direct Appointment">
        <node TEXT="Vendor Selection"/>
        <node TEXT="Price Negotiation"/>
        <node TEXT="Final Approval"/>
      </node>

      <node TEXT="Outputs">
        <node TEXT="Selected Vendor"/>
        <node TEXT="Final Price"/>
        <node TEXT="Ready for PO/SPK"/>
      </node>

      <node TEXT="Sistem">
        <node TEXT="E-Procurement"/>
        <node TEXT="Vendor Scoring"/>
      </node>

      <node TEXT="SLA: 14 hari (Tender)"/>
      <node TEXT="SLA: 5 hari (Direct)"/>
    </node>

    <!-- FASE 5 -->
    <node ID="fase5" TEXT="FASE 5: Kontrak &amp; Portal KSO" POSITION="right">
      <edge COLOR="#8E44AD" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#8E44AD"/>

      <node TEXT="Daan Umum">
        <node TEXT="PO (Purchase Order)"/>
        <node TEXT="Contract Terms"/>
      </node>

      <node TEXT="Daan Jasa">
        <node TEXT="SPK (Surat Perintah Kerja)"/>
        <node TEXT="PKS (Perjanjian Kerja Sama)"/>
      </node>

      <node TEXT="KSO Setup">
        <node TEXT="Lab Contract"/>
        <node TEXT="Farmasi Contract"/>
        <node TEXT="BMHP Setup"/>
      </node>

      <node TEXT="Vendor Portal">
        <node TEXT="Self-reporting"/>
        <node TEXT="KSO Obligations"/>
        <node TEXT="Document Upload"/>
      </node>

      <node TEXT="SLA: 7 hari"/>
    </node>

    <!-- FASE 6 -->
    <node ID="fase6" TEXT="FASE 6: Penerimaan &amp; Verifikasi" POSITION="right">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="Activities">
        <node TEXT="Goods Arrival"/>
        <node TEXT="BAPB (Berita Acara)"/>
        <node TEXT="QC &amp; Inspection"/>
        <node TEXT="3-Way Match"/>
      </node>

      <node TEXT="Verifikasi">
        <node TEXT="PO vs BAPB"/>
        <node TEXT="Invoice Match"/>
        <node TEXT="Quantity Check"/>
        <node TEXT="Quality Check"/>
      </node>

      <node TEXT="Outputs">
        <node TEXT="BAPB Signed"/>
        <node TEXT="Approved for Payment"/>
      </node>

      <node TEXT="SLA: 7 hari"/>
    </node>

    <!-- FASE 7 -->
    <node ID="fase7" TEXT="FASE 7: Pembayaran &amp; Invoice" POSITION="right">
      <edge COLOR="#34495E" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#34495E"/>

      <node TEXT="Invoice Processing">
        <node TEXT="Invoice Receipt"/>
        <node TEXT="3-Way Match Final"/>
        <node TEXT="GL Posting"/>
      </node>

      <node TEXT="Payment">
        <node TEXT="DP (Down Payment)"/>
        <node TEXT="Final Payment"/>
        <node TEXT="Check/Transfer"/>
      </node>

      <node TEXT="Recording">
        <node TEXT="Finance Record"/>
        <node TEXT="Vendor Receipt"/>
      </node>

      <node TEXT="SLA: 30 hari"/>
    </node>

    <!-- FASE 8 -->
    <node ID="fase8" TEXT="FASE 8: Evaluasi Vendor" POSITION="right">
      <edge COLOR="#16A085" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#16A085"/>

      <node TEXT="Scoring (7 Dimensi)">
        <node TEXT="Harga (Price)"/>
        <node TEXT="Kualitas (Quality)"/>
        <node TEXT="Delivery"/>
        <node TEXT="Compliance"/>
        <node TEXT="Financial Health"/>
        <node TEXT="Response Time"/>
        <node TEXT="Partnership"/>
      </node>

      <node TEXT="Decision">
        <node TEXT="Renewal"/>
        <node TEXT="Improvement"/>
        <node TEXT="Blacklist"/>
      </node>

      <node TEXT="Outputs">
        <node TEXT="Vendor Scorecard"/>
        <node TEXT="Ranking"/>
      </node>

      <node TEXT="Frequency: Monthly"/>
    </node>

    <!-- FASE 9 -->
    <node ID="fase9" TEXT="FASE 9: Pelaporan &amp; Analitik" POSITION="right">
      <edge COLOR="#F39C12" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true" COLOR="#F39C12"/>

      <node TEXT="Monthly Reports">
        <node TEXT="Procurement Volume"/>
        <node TEXT="Vendor Performance"/>
        <node TEXT="Budget Execution"/>
      </node>

      <node TEXT="Quarterly Analysis">
        <node TEXT="Trend Analysis"/>
        <node TEXT="Spend Analysis"/>
        <node TEXT="Risk Assessment"/>
      </node>

      <node TEXT="Annual Reports">
        <node TEXT="KPI Summary"/>
        <node TEXT="Vendor Ranking"/>
        <node TEXT="Strategic Insights"/>
      </node>

      <node TEXT="Outputs">
        <node TEXT="Dashboard (Command Center)"/>
        <node TEXT="Executive Reports"/>
        <node TEXT="SPI Compliance Reports"/>
      </node>

      <node TEXT="Continuous"/>
    </node>

    <!-- SUMMARY -->
    <node ID="summary" TEXT="CYCLE SUMMARY" POSITION="left">
      <edge COLOR="#000000" WIDTH="2"/>
      <font NAME="Arial" SIZE="13" BOLD="true"/>

      <node TEXT="Total Cycle: 60-90 hari (Tender)"/>
      <node TEXT="Direct Appointment: 30-45 hari"/>

      <node TEXT="Key Documents">
        <node TEXT="PP, IMT, SPPJ, SPPH, SJPH"/>
        <node TEXT="PO, SPK, PKS, BAPB"/>
        <node TEXT="Invoice, Payment"/>
      </node>

      <node TEXT="Key Stakeholders">
        <node TEXT="SBU (requestor)"/>
        <node TEXT="Dept. Pengadaan (processor)"/>
        <node TEXT="Finance (payment)"/>
        <node TEXT="Vendor (supplier)"/>
        <node TEXT="SPI (auditor)"/>
      </node>

      <node TEXT="AI Guardian Coverage">
        <node TEXT="All 9 phases"/>
        <node TEXT="Real-time validation"/>
        <node TEXT="Compliance checking"/>
      </node>
    </node>
  </node>
</map>
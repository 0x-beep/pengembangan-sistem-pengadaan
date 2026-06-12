<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <node ID="root" TEXT="MODULE 3: Vendor Portal (Self-reporting, Obligations)">
    <edge COLOR="#000000" WIDTH="2"/>
    <font NAME="Arial" SIZE="16" BOLD="true"/>

    <!-- PORTAL ACCESS &amp; AUTHENTICATION -->
    <node ID="access" TEXT="PORTAL ACCESS &amp; AUTHENTICATION" POSITION="right">
      <edge COLOR="#3498DB" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#3498DB"/>

      <node TEXT="Login Mechanism">
        <node TEXT="Username (email)"/>
        <node TEXT="Password + 2FA"/>
        <node TEXT="Session management"/>
        <node TEXT="Timeout protection"/>
      </node>

      <node TEXT="Vendor Dashboard">
        <node TEXT="Home: Quick stats"/>
        <node TEXT="Profile: Company info"/>
        <node TEXT="Contracts: Active KSOs"/>
        <node TEXT="Obligations: To-do items"/>
        <node TEXT="Reports: History &amp; analytics"/>
      </node>

      <node TEXT="User Management">
        <node TEXT="Multiple users per vendor"/>
        <node TEXT="Role-based access (Admin/User)"/>
        <node TEXT="Permission control"/>
        <node TEXT="Activity logging"/>
      </node>

      <node TEXT="Security">
        <node TEXT="SSL encryption"/>
        <node TEXT="Data privacy"/>
        <node TEXT="Audit trail"/>
        <node TEXT="Compliance with standards"/>
      </node>
    </node>

    <!-- SELF-REPORTING INTERFACE -->
    <node ID="reporting" TEXT="SELF-REPORTING INTERFACE" POSITION="right">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="KSO Delivery Reporting">
        <node TEXT="Date of delivery"/>
        <node TEXT="Products delivered"/>
        <node TEXT="Quantity per item"/>
        <node TEXT="Quality status (OK/Issue)"/>
        <node TEXT="Recipient confirmation"/>
      </node>

      <node TEXT="Consumables Tracking">
        <node TEXT="Lab: Reagents used"/>
        <node TEXT="Pharmacy: Medicines dispensed"/>
        <node TEXT="BMHP: Devices allocated"/>
        <node TEXT="Stock level after"/>
      </node>

      <node TEXT="Performance Data">
        <node TEXT="On-time delivery: Y/N"/>
        <node TEXT="Quality issues: Y/N (details)"/>
        <node TEXT="Quantity discrepancies"/>
        <node TEXT="Special circumstances"/>
      </node>

      <node TEXT="Document Upload">
        <node TEXT="Delivery proof (photo/scan)"/>
        <node TEXT="Receipt confirmation"/>
        <node TEXT="Quality certificate"/>
        <node TEXT="Test reports (if applicable)"/>
      </node>

      <node TEXT="Form Validation">
        <node TEXT="AI checks completeness"/>
        <node TEXT="Flag inconsistencies"/>
        <node TEXT="Request clarification"/>
        <node TEXT="Accept &amp; record"/>
      </node>
    </node>

    <!-- OBLIGATION MANAGEMENT -->
    <node ID="obligations" TEXT="OBLIGATION MANAGEMENT &amp; TRACKING" POSITION="right">
      <edge COLOR="#27AE60" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#27AE60"/>

      <node TEXT="Contract Obligations">
        <node TEXT="Minimum delivery frequency"/>
        <node TEXT="Quality standards"/>
        <node TEXT="Price lock terms"/>
        <node TEXT="Documentation requirements"/>
        <node TEXT="SLA compliance"/>
      </node>

      <node TEXT="System-Generated Tasks">
        <node TEXT="Monthly reporting due"/>
        <node TEXT="Quality certificate renewal"/>
        <node TEXT="Financial statement update"/>
        <node TEXT="Insurance verification"/>
        <node TEXT="Compliance checklist"/>
      </node>

      <node TEXT="Dashboard View">
        <node TEXT="Open obligations (to-do)"/>
        <node TEXT="Due dates &amp; countdown"/>
        <node TEXT="Completion status"/>
        <node TEXT="Late items (red flag)"/>
        <node TEXT="Historical record"/>
      </node>

      <node TEXT="Notifications">
        <node TEXT="Email reminder (7 days before)"/>
        <node TEXT="Urgent alert (1 day before)"/>
        <node TEXT="Overdue notification"/>
        <node TEXT="Completion confirmation"/>
      </node>

      <node TEXT="Tracking &amp; Enforcement">
        <node TEXT="System tracks completion"/>
        <node TEXT="AI flags overdue items"/>
        <node TEXT="Escalation to Kasie"/>
        <node TEXT="Impact on performance score"/>
      </node>
    </node>

    <!-- INVOICE SUBMISSION -->
    <node ID="invoice" TEXT="INVOICE SUBMISSION &amp; TRACKING" POSITION="right">
      <edge COLOR="#9B59B6" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#9B59B6"/>

      <node TEXT="Invoice Creation">
        <node TEXT="Template available on portal"/>
        <node TEXT="Auto-fill vendor details"/>
        <node TEXT="Manual entry: Items &amp; amounts"/>
        <node TEXT="Invoice date &amp; PO reference"/>
      </node>

      <node TEXT="Invoice Data">
        <node TEXT="Invoice number (vendor)"/>
        <node TEXT="Items delivered"/>
        <node TEXT="Quantities &amp; unit prices"/>
        <node TEXT="Total amount"/>
        <node TEXT="Payment terms"/>
        <node TEXT="Tax information"/>
      </node>

      <node TEXT="Supporting Documents">
        <node TEXT="Delivery receipt (BAPB)"/>
        <node TEXT="Packing slip"/>
        <node TEXT="Quality certificate"/>
        <node TEXT="Bank account details"/>
      </node>

      <node TEXT="Submission &amp; Tracking">
        <node TEXT="Submit via portal"/>
        <node TEXT="System confirmation email"/>
        <node TEXT="Finance receives notification"/>
        <node TEXT="Status tracking in vendor portal"/>
      </node>

      <node TEXT="Payment Status">
        <node TEXT="Pending review"/>
        <node TEXT="Under 3-way match"/>
        <node TEXT="Approved for payment"/>
        <node TEXT="Payment processed"/>
        <node TEXT="Paid confirmation"/>
      </node>
    </node>

    <!-- COMMUNICATION &amp; SUPPORT -->
    <node ID="communication" TEXT="COMMUNICATION &amp; SUPPORT" POSITION="right">
      <edge COLOR="#F39C12" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#F39C12"/>

      <node TEXT="Announcements">
        <node TEXT="System maintenance notice"/>
        <node TEXT="Policy changes"/>
        <node TEXT="New requirements"/>
        <node TEXT="Best practices"/>
      </node>

      <node TEXT="Q&amp;A Support">
        <node TEXT="FAQ section"/>
        <node TEXT="Video tutorials"/>
        <node TEXT="User guides"/>
        <node TEXT="Contact info (Kasie, Finance)"/>
      </node>

      <node TEXT="Messaging">
        <node TEXT="Vendor → Kasie messages"/>
        <node TEXT="Issue reporting"/>
        <node TEXT="Clarification requests"/>
        <node TEXT="Status inquiries"/>
      </node>

      <node TEXT="Escalation">
        <node TEXT="Unresolved issues"/>
        <node TEXT="Urgent requests"/>
        <node TEXT="Escalate to Manager"/>
        <node TEXT="Documentation &amp; follow-up"/>
      </node>
    </node>

    <!-- VENDOR DASHBOARD ANALYTICS -->
    <node ID="analytics" TEXT="VENDOR DASHBOARD &amp; ANALYTICS" POSITION="right">
      <edge COLOR="#16A085" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#16A085"/>

      <node TEXT="Performance Scorecard">
        <node TEXT="Current score (by dimension)"/>
        <node TEXT="Trend (monthly)"/>
        <node TEXT="Benchmark (vs category avg)"/>
        <node TEXT="Ranking (position among peers)"/>
      </node>

      <node TEXT="Order History">
        <node TEXT="Active POs/Contracts"/>
        <node TEXT="Historical deliveries"/>
        <node TEXT="Invoice status"/>
        <node TEXT="Payment history"/>
      </node>

      <node TEXT="Reports">
        <node TEXT="Monthly delivery summary"/>
        <node TEXT="Revenue report"/>
        <node TEXT="Performance trends"/>
        <node TEXT="Compliance status"/>
      </node>

      <node TEXT="Insights">
        <node TEXT="Improvement opportunities"/>
        <node TEXT="Peer benchmarking"/>
        <node TEXT="Recommendations from system"/>
      </node>
    </node>

    <!-- DOCUMENT MANAGEMENT -->
    <node ID="documents" TEXT="DOCUMENT MANAGEMENT" POSITION="right">
      <edge COLOR="#C0392B" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#C0392B"/>

      <node TEXT="Document Types">
        <node TEXT="Contracts (KSO, PO, SPK)"/>
        <node TEXT="Certificates (ISO, Quality)"/>
        <node TEXT="Insurance documentation"/>
        <node TEXT="Financial statements"/>
        <node TEXT="Compliance certificates"/>
      </node>

      <node TEXT="Upload &amp; Storage">
        <node TEXT="Secure file upload"/>
        <node TEXT="File type validation"/>
        <node TEXT="Version control"/>
        <node TEXT="Expiry tracking"/>
      </node>

      <node TEXT="Notifications">
        <node TEXT="Certificate expiry alert (30 days)"/>
        <node TEXT="Required renewal reminders"/>
        <node TEXT="Overdue document warning"/>
      </node>

      <node TEXT="Visibility">
        <node TEXT="Vendor can access own docs"/>
        <node TEXT="Kasie/Finance can view"/>
        <node TEXT="Audit trail of access"/>
      </node>
    </node>

    <!-- MOBILE ACCESS -->
    <node ID="mobile" TEXT="MOBILE ACCESS" POSITION="left">
      <edge COLOR="#1ABC9C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#1ABC9C"/>

      <node TEXT="Mobile App">
        <node TEXT="iOS &amp; Android"/>
        <node TEXT="Same functionality as web"/>
        <node TEXT="Offline capability (limited)"/>
        <node TEXT="Push notifications"/>
      </node>

      <node TEXT="Use Cases">
        <node TEXT="Quick status check"/>
        <node TEXT="Obligation tracking"/>
        <node TEXT="Document uploads (photo)"/>
        <node TEXT="Receive alerts"/>
      </node>

      <node TEXT="Benefits">
        <node TEXT="Convenient access in field"/>
        <node TEXT="Real-time notifications"/>
        <node TEXT="Faster reporting"/>
      </node>
    </node>

    <!-- INTEGRATION WITH PROCUREMENT -->
    <node ID="integration" TEXT="INTEGRATION WITH PROCUREMENT" POSITION="left">
      <edge COLOR="#2980B9" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#2980B9"/>

      <node TEXT="Data Exchange">
        <node TEXT="PO data sent to vendor"/>
        <node TEXT="Delivery reported back"/>
        <node TEXT="Performance data collected"/>
        <node TEXT="Invoice linked to PO"/>
      </node>

      <node TEXT="Workflow">
        <node TEXT="PO issuance → Vendor notification"/>
        <node TEXT="Delivery report → Finance alert"/>
        <node TEXT="Invoice → 3-way match"/>
        <node TEXT="Payment confirmation → Vendor notification"/>
      </node>

      <node TEXT="Real-time Sync">
        <node TEXT="KSO stock levels"/>
        <node TEXT="Consumption data"/>
        <node TEXT="Pending deliveries"/>
        <node TEXT="Outstanding invoices"/>
      </node>
    </node>

    <!-- COMPLIANCE &amp; SECURITY -->
    <node ID="compliance" TEXT="COMPLIANCE &amp; SECURITY" POSITION="left">
      <edge COLOR="#E74C3C" WIDTH="2"/>
      <font NAME="Arial" SIZE="12" BOLD="true" COLOR="#E74C3C"/>

      <node TEXT="Data Security">
        <node TEXT="Encryption in transit"/>
        <node TEXT="Encryption at rest"/>
        <node TEXT="Access control"/>
        <node TEXT="Regular backups"/>
      </node>

      <node TEXT="Audit Trail">
        <node TEXT="All actions logged"/>
        <node TEXT="User identification"/>
        <node TEXT="Timestamp recorded"/>
        <node TEXT="Changes tracked"/>
      </node>

      <node TEXT="Compliance Rules">
        <node TEXT="Mandatory fields"/>
        <node TEXT="Required documents"/>
        <node TEXT="Approval workflows"/>
        <node TEXT="SLA enforcement"/>
      </node>

      <node TEXT="Privacy">
        <node TEXT="Vendor data protected"/>
        <node TEXT="Confidential info secured"/>
        <node TEXT="Restricted access"/>
        <node TEXT="GDPR/Local compliance"/>
      </node>
    </node>
  </node>
</map>
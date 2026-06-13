<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <!-- Dikonversi otomatis dari MINDMAP_FASE7_PEMBAYARAN_INVOICE.mermaid -->
  <!-- Konverter: mermaid_to_freemind.py | ID Penulis Skrip: claude-sonnet-4-6 (agen Cowork) -->
  <node TEXT="FASE 7 PEMBAYARAN &amp; INVOICE" COLOR="#34a853" FOLDED="false">
    <node TEXT="INPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="3-Way Match yang sudah clear dari Fase 6" COLOR="#ea4335"/>
      <node TEXT="Invoice resmi dari vendor" COLOR="#ea4335"/>
      <node TEXT="Syarat pembayaran sesuai PKS atau PO DP dan pelunasan" COLOR="#ea4335"/>
    </node>
    <node TEXT="PENGELOLA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Bagian Keuangan sebagai pelaksana pembayaran" COLOR="#ea4335"/>
      <node TEXT="Manager Pengadaan sebagai approval" COLOR="#ea4335"/>
      <node TEXT="Otorisasi Direksi untuk nilai tertentu" COLOR="#ea4335"/>
    </node>
    <node TEXT="PROSES PEMBAYARAN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Invoice masuk ke sistem dari vendor" COLOR="#ea4335"/>
      <node TEXT="Auto-validasi 3-Way Match PO BAPB Invoice" COLOR="#ea4335"/>
      <node TEXT="Jika matched masuk antrian approval pembayaran" COLOR="#ea4335"/>
      <node TEXT="Approval bertingkat sesuai nilai sama dengan otorisasi PO" COLOR="#ea4335"/>
      <node TEXT="Pembayaran DP dahulu jika kontrak mensyaratkan" COLOR="#ea4335"/>
      <node TEXT="Pelunasan setelah semua milestone terpenuhi" COLOR="#ea4335"/>
      <node TEXT="GL Posting otomatis ke sistem keuangan KMU" COLOR="#ea4335"/>
      <node TEXT="Konfirmasi pembayaran di Portal Vendor KMU" COLOR="#ea4335"/>
    </node>
    <node TEXT="SKEMA PEMBAYARAN MILESTONE" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="DP 30 persen setelah kontrak aktif dan jaminan diterima" COLOR="#ea4335"/>
      <node TEXT="Pengiriman 40 persen setelah barang diterima dan BAPB clear" COLOR="#ea4335"/>
      <node TEXT="Testing 20 persen setelah uji coba alat selesai" COLOR="#ea4335"/>
      <node TEXT="Training dan Komisioning 10 persen setelah serah terima final" COLOR="#ea4335"/>
    </node>
    <node TEXT="OTORISASI BERTINGKAT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Nilai sampai 50 juta Manager Pengadaan" COLOR="#ea4335"/>
      <node TEXT="Nilai 50 sampai 500 juta GM Operasi" COLOR="#ea4335"/>
      <node TEXT="Nilai 500 juta sampai 1 miliar Direktur Keuangan" COLOR="#ea4335"/>
      <node TEXT="Nilai lebih dari 1 miliar Direktur Utama atau BOD" COLOR="#ea4335"/>
    </node>
    <node TEXT="BANK GUARANTEE" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Wajib untuk nilai kontrak lebih dari 1 miliar" COLOR="#ea4335"/>
      <node TEXT="BG senilai 5 persen dari nilai kontrak" COLOR="#ea4335"/>
      <node TEXT="Berlaku selama masa retensi" COLOR="#ea4335"/>
      <node TEXT="Pencairan BG setelah masa retensi selesai dan tanpa klaim" COLOR="#ea4335"/>
    </node>
    <node TEXT="OUTPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Rekaman pembayaran lengkap ke Fase 9 Pelaporan" COLOR="#ea4335"/>
      <node TEXT="Status pembayaran vendor sebagai data Fase 8 Evaluasi" COLOR="#ea4335"/>
      <node TEXT="GL Posting integrasi dengan sistem keuangan ERP KMU" COLOR="#ea4335"/>
      <node TEXT="Konfirmasi LUNAS ke Portal Vendor sebagai trigger Fase 8" COLOR="#ea4335"/>
    </node>
    <node TEXT="DOKUMEN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Invoice vendor" COLOR="#ea4335"/>
      <node TEXT="BAPB Berita Acara Penerimaan Barang" COLOR="#ea4335"/>
      <node TEXT="Rekap 3-Way Match PO BAPB Invoice" COLOR="#ea4335"/>
      <node TEXT="Bukti transfer pembayaran" COLOR="#ea4335"/>
      <node TEXT="Bank Guarantee untuk kontrak besar" COLOR="#ea4335"/>
    </node>
    <node TEXT="AI PENJAGA KEPATUHAN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Blokir pembayaran jika 3-Way Match belum clear" COLOR="#ea4335"/>
      <node TEXT="Alert jika nilai invoice melebihi nilai kontrak" COLOR="#ea4335"/>
      <node TEXT="Validasi masa retensi Bank Guarantee sebelum pencairan" COLOR="#ea4335"/>
      <node TEXT="Flag duplikasi invoice dari vendor yang sama" COLOR="#ea4335"/>
      <node TEXT="Alert keterlambatan pembayaran yang mendekati jatuh tempo" COLOR="#ea4335"/>
    </node>
    <node TEXT="INTEGRASI SISTEM" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Finance ERP sinkronisasi GL posting otomatis" COLOR="#ea4335"/>
      <node TEXT="Portal Vendor KMU update status pembayaran real-time" COLOR="#ea4335"/>
      <node TEXT="Command Center Dashboard tampilkan payment pipeline" COLOR="#ea4335"/>
    </node>
    <node TEXT="KONEKSI KE FASE LAIN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Input 3-Way Match dari Fase 6 sebagai syarat wajib" COLOR="#ea4335"/>
      <node TEXT="Output rekaman pembayaran ke Fase 9 Pelaporan" COLOR="#ea4335"/>
      <node TEXT="Output status vendor ke Fase 8 Evaluasi Vendor" COLOR="#ea4335"/>
    </node>
    <node TEXT="SLA TARGET" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Submission invoice vendor maksimal 3 hari setelah BAPB" COLOR="#ea4335"/>
      <node TEXT="Validasi 3-Way Match maksimal 5 hari kerja" COLOR="#ea4335"/>
      <node TEXT="Pembayaran ke vendor maksimal 30 hari dari tanggal invoice" COLOR="#ea4335"/>
    </node>
  </node>
</map>

<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <!-- Dikonversi otomatis dari MINDMAP_FASE3_PERMINTAAN_PENGADAAN.mermaid -->
  <!-- Konverter: mermaid_to_freemind.py | ID Penulis Skrip: claude-sonnet-4-6 (agen Cowork) -->
  <node TEXT="FASE 3 PERMINTAAN PENGADAAN" COLOR="#34a853" FOLDED="false">
    <node TEXT="INPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Anggaran RKAP yang sudah disahkan dari Fase 1" COLOR="#ea4335"/>
      <node TEXT="Kebutuhan operasional SBU yang muncul sepanjang tahun" COLOR="#ea4335"/>
      <node TEXT="IMT dari unit peminta" COLOR="#ea4335"/>
    </node>
    <node TEXT="PENGELOLA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="SBU atau Unit yang Meminta sebagai pemrakarsa" COLOR="#ea4335"/>
      <node TEXT="Departemen Umum sebagai pengolah dokumen" COLOR="#ea4335"/>
      <node TEXT="Admin Pengadaan Barang dan Jasa" COLOR="#ea4335"/>
    </node>
    <node TEXT="JALUR BARANG UMUM" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="IMT masuk dari unit peminta" COLOR="#ea4335"/>
      <node TEXT="Departemen Umum proses IMT menjadi PP" COLOR="#ea4335"/>
      <node TEXT="PP dilengkapi spesifikasi teknis dan RAB" COLOR="#ea4335"/>
      <node TEXT="Komite Anggaran validasi ketersediaan budget" COLOR="#ea4335"/>
      <node TEXT="PP disetujui trigger Fase 4 jalur barang" COLOR="#ea4335"/>
    </node>
    <node TEXT="JALUR BARANG INVESTASI" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="IMT masuk dengan nilai lebih dari 100 juta" COLOR="#ea4335"/>
      <node TEXT="Studi Kelayakan FS wajib dilampirkan" COLOR="#ea4335"/>
      <node TEXT="Departemen Umum proses IMT menjadi PP Investasi" COLOR="#ea4335"/>
      <node TEXT="Review tambahan Komite Anggaran dan Direksi" COLOR="#ea4335"/>
      <node TEXT="PP Investasi disetujui trigger Fase 4" COLOR="#ea4335"/>
    </node>
    <node TEXT="JALUR JASA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="JOR Jurnal Operasional dari unit peminta" COLOR="#ea4335"/>
      <node TEXT="Departemen Umum susun SPPJ lengkap" COLOR="#ea4335"/>
      <node TEXT="SPPJ dilengkapi RAB dan BOQ" COLOR="#ea4335"/>
      <node TEXT="Untuk jasa konstruksi wajib ada DED" COLOR="#ea4335"/>
      <node TEXT="SPPJ disetujui trigger Fase 4 jalur jasa" COLOR="#ea4335"/>
    </node>
    <node TEXT="DOKUMEN YANG DIHASILKAN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="IMT Instruksi Memo Teknis" COLOR="#ea4335"/>
      <node TEXT="PP Permintaan Pembelian barang umum dan investasi" COLOR="#ea4335"/>
      <node TEXT="SPPJ Surat Permintaan Pekerjaan Jasa" COLOR="#ea4335"/>
      <node TEXT="RAB Rencana Anggaran Biaya" COLOR="#ea4335"/>
      <node TEXT="BOQ Bill of Quantity untuk konstruksi" COLOR="#ea4335"/>
      <node TEXT="DED Detail Engineering Design untuk konstruksi" COLOR="#ea4335"/>
      <node TEXT="JOR Jurnal Operasional untuk jasa" COLOR="#ea4335"/>
    </node>
    <node TEXT="AI PENJAGA KEPATUHAN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Validasi PP apakah ada di RKAP sebelum diproses" COLOR="#ea4335"/>
      <node TEXT="Validasi investasi lebih dari 100 juta wajib ada FS" COLOR="#ea4335"/>
      <node TEXT="Cek kelengkapan SPPJ haruus ada BOQ dan DED" COLOR="#ea4335"/>
      <node TEXT="Blokir jika unit tidak punya otorisasi budget" COLOR="#ea4335"/>
    </node>
    <node TEXT="KONEKSI KE FASE LAIN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Input dari Fase 1 validasi ketersediaan RKAP" COLOR="#ea4335"/>
      <node TEXT="Output PP dan SPPJ menjadi trigger Fase 4" COLOR="#ea4335"/>
      <node TEXT="Departemen Umum terlibat di Fase 3 Fase 4 dan Fase 6" COLOR="#ea4335"/>
    </node>
    <node TEXT="SLA TARGET" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Pengajuan IMT ke proses PP maksimal 1 hari kerja" COLOR="#ea4335"/>
      <node TEXT="Review dan penentuan metode pengadaan maksimal 2 hari kerja" COLOR="#ea4335"/>
    </node>
  </node>
</map>

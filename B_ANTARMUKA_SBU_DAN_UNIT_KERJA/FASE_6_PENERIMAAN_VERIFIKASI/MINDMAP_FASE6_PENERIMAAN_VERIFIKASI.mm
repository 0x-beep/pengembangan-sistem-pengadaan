<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <!-- Dikonversi otomatis dari MINDMAP_FASE6_PENERIMAAN_VERIFIKASI.mermaid -->
  <!-- Konverter: mermaid_to_freemind.py | ID Penulis Skrip: claude-sonnet-4-6 (agen Cowork) -->
  <node TEXT="FASE 6 PENERIMAAN &amp; VERIFIKASI" COLOR="#34a853" FOLDED="false">
    <node TEXT="INPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Barang datang ke gudang setelah vendor kirim dari Fase 4" COLOR="#ea4335"/>
      <node TEXT="BAPP Berita Acara Penyelesaian Pekerjaan dari vendor jasa Fase 5" COLOR="#ea4335"/>
      <node TEXT="Invoice dari vendor" COLOR="#ea4335"/>
    </node>
    <node TEXT="PENGELOLA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Staf Pemeriksa Barang di gudang" COLOR="#ea4335"/>
      <node TEXT="Unit yang Meminta sebagai validator kesesuaian" COLOR="#ea4335"/>
      <node TEXT="Admin Pengadaan sebagai koordinator dokumen" COLOR="#ea4335"/>
    </node>
    <node TEXT="PROSES PENERIMAAN BARANG" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Pengecekan fisik kuantitas sesuai PO" COLOR="#ea4335"/>
      <node TEXT="Pengecekan kualitas dan spesifikasi teknis" COLOR="#ea4335"/>
      <node TEXT="Pengecekan kesesuaian merek dan tipe dengan PO" COLOR="#ea4335"/>
      <node TEXT="Jika sesuai BAPB ditandatangani" COLOR="#ea4335"/>
      <node TEXT="Jika tidak sesuai notifikasi ke vendor untuk revisi atau penggantian" COLOR="#ea4335"/>
    </node>
    <node TEXT="PROSES VERIFIKASI JASA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Menerima BAPP dari vendor setelah pekerjaan selesai" COLOR="#ea4335"/>
      <node TEXT="Tim teknis KMU periksa hasil pekerjaan jasa" COLOR="#ea4335"/>
      <node TEXT="Departemen Umum terlibat serah terima lokasi dan pekerjaan" COLOR="#ea4335"/>
      <node TEXT="Konfirmasi ke unit peminta bahwa pekerjaan sesuai scope" COLOR="#ea4335"/>
    </node>
    <node TEXT="THREE WAY MATCH" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Komponen 1 PO Purchase Order dari Fase 4" COLOR="#ea4335"/>
      <node TEXT="Komponen 2 BAPB Berita Acara Penerimaan Barang" COLOR="#ea4335"/>
      <node TEXT="Komponen 3 Invoice dari vendor" COLOR="#ea4335"/>
      <node TEXT="Jika semua cocok Invoice disetujui lanjut ke Fase 7" COLOR="#ea4335"/>
      <node TEXT="Jika tidak cocok Invoice ditolak vendor diberitahu" COLOR="#ea4335"/>
    </node>
    <node TEXT="OUTPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="BAPB yang ditandatangani sebagai bukti penerimaan resmi" COLOR="#ea4335"/>
      <node TEXT="Hasil 3-Way Match sebagai clearance pembayaran ke Fase 7" COLOR="#ea4335"/>
      <node TEXT="Data kualitas barang dan jasa untuk evaluasi vendor di Fase 8" COLOR="#ea4335"/>
      <node TEXT="Konfirmasi ke unit peminta bahwa barang siap digunakan" COLOR="#ea4335"/>
    </node>
    <node TEXT="DOKUMEN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="BAPB Berita Acara Penerimaan Barang" COLOR="#ea4335"/>
      <node TEXT="BAPP Berita Acara Penyelesaian Pekerjaan" COLOR="#ea4335"/>
      <node TEXT="Checklist QC Pemeriksaan Barang" COLOR="#ea4335"/>
      <node TEXT="Formulir Penolakan Barang jika tidak sesuai" COLOR="#ea4335"/>
    </node>
    <node TEXT="AI PENJAGA KEPATUHAN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Blokir proses Invoice jika BAPB belum ditandatangani" COLOR="#ea4335"/>
      <node TEXT="Alert jika nilai Invoice melebihi nilai BAPB" COLOR="#ea4335"/>
      <node TEXT="Validasi 3-Way Match wajib clear sebelum lanjut ke Fase 7" COLOR="#ea4335"/>
      <node TEXT="Notifikasi otomatis ke vendor jika barang ditolak" COLOR="#ea4335"/>
    </node>
    <node TEXT="KONEKSI KE FASE LAIN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Input dari Fase 4 via pengiriman barang oleh vendor" COLOR="#ea4335"/>
      <node TEXT="Input dari Fase 5 via BAPP untuk jasa" COLOR="#ea4335"/>
      <node TEXT="Output 3-Way Match ke Fase 7 sebagai syarat pembayaran" COLOR="#ea4335"/>
      <node TEXT="Output data kualitas ke Fase 8 untuk evaluasi vendor" COLOR="#ea4335"/>
    </node>
    <node TEXT="SLA TARGET" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="QC dan pembuatan BAPB maksimal 2 hari kerja setelah barang datang" COLOR="#ea4335"/>
      <node TEXT="Validasi 3-Way Match maksimal 5 hari kerja" COLOR="#ea4335"/>
    </node>
  </node>
</map>

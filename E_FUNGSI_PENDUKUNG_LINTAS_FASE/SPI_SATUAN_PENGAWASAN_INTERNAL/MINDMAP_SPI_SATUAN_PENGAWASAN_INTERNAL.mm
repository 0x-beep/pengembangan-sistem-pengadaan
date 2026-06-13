<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <!-- Dikonversi otomatis dari MINDMAP_SPI_SATUAN_PENGAWASAN_INTERNAL.mermaid -->
  <!-- Konverter: mermaid_to_freemind.py | ID Penulis Skrip: claude-sonnet-4-6 (agen Cowork) -->
  <node TEXT="SPI SATUAN PENGAWASAN INTERNAL" COLOR="#34a853" FOLDED="false">
    <node TEXT="PERAN STRATEGIS" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Lapisan pengawasan independen di luar alur operasional pengadaan" COLOR="#ea4335"/>
      <node TEXT="Melapor langsung ke Direksi tanpa melalui Dept Pengadaan" COLOR="#ea4335"/>
      <node TEXT="Memantau semua fase dari luar proses kapan saja" COLOR="#ea4335"/>
      <node TEXT="Watchdog independen untuk kepatuhan dan integritas" COLOR="#ea4335"/>
    </node>
    <node TEXT="CARA KERJA CROSS-CUTTING" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Akses penuh ke Audit Trail semua aksi dokumen nilai timestamp user" COLOR="#ea4335"/>
      <node TEXT="Sampling review di fase mana saja tanpa izin dari Pengadaan" COLOR="#ea4335"/>
      <node TEXT="Memantau kepatuhan SPO secara independen" COLOR="#ea4335"/>
      <node TEXT="Flag anomali nilai tidak wajar proses yang dilompati vendor bermasalah" COLOR="#ea4335"/>
    </node>
    <node TEXT="KETERLIBATAN FASE 9 LAPORAN DAN AUDIT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Menerima laporan compliance otomatis dari sistem" COLOR="#ea4335"/>
      <node TEXT="Generate laporan audit khusus per vendor per periode per nilai transaksi" COLOR="#ea4335"/>
      <node TEXT="Bukti digital tidak bisa dimanipulasi tersimpan di sistem" COLOR="#ea4335"/>
      <node TEXT="Input laporan SPI masuk ke Fase 9 sebagai bagian laporan tahunan" COLOR="#ea4335"/>
    </node>
    <node TEXT="CHECKLIST PENGAWASAN SPI" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Apakah otorisasi sesuai nilai PO dan SPK sudah terpenuhi" COLOR="#ea4335"/>
      <node TEXT="Apakah Aanwijzing dan Bidding Tabulasi dilakukan sebelum PO keluar" COLOR="#ea4335"/>
      <node TEXT="Apakah 3-Way Match PO BAPB Invoice sudah clear sebelum pembayaran" COLOR="#ea4335"/>
      <node TEXT="Apakah vendor yang menang ada di Daftar Vendor Terverifikasi KMU" COLOR="#ea4335"/>
      <node TEXT="Apakah ada vendor di Daftar Vendor Bermasalah yang masuk proses tender" COLOR="#ea4335"/>
    </node>
    <node TEXT="KEWENANGAN SPI" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Eskalasi langsung ke Direksi jika ditemukan pelanggaran material" COLOR="#ea4335"/>
      <node TEXT="Meminta freeze transaksi tertentu untuk investigasi lebih lanjut" COLOR="#ea4335"/>
      <node TEXT="Mengakses semua dokumen tanpa perlu izin departemen terkait" COLOR="#ea4335"/>
      <node TEXT="Output laporan audit masuk ke Fase 9 Pelaporan Tahunan" COLOR="#ea4335"/>
    </node>
    <node TEXT="TIPE ANOMALI YANG DIPANTAU" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Nilai PO tidak wajar jauh di bawah atau di atas HPS" COLOR="#ea4335"/>
      <node TEXT="Proses yang dilompati SPPH langsung ke PO tanpa tender" COLOR="#ea4335"/>
      <node TEXT="Vendor bermasalah yang lolos masuk ke proses tender" COLOR="#ea4335"/>
      <node TEXT="Otorisasi tidak sesuai nilai transaksi" COLOR="#ea4335"/>
      <node TEXT="3-Way Match tidak terpenuhi namun pembayaran tetap diproses" COLOR="#ea4335"/>
    </node>
    <node TEXT="LAPORAN AUDIT SPI" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Laporan sampling rutin bulanan atau triwulan" COLOR="#ea4335"/>
      <node TEXT="Laporan investigasi khusus jika ada temuan" COLOR="#ea4335"/>
      <node TEXT="Laporan tahunan sebagai bagian Fase 9" COLOR="#ea4335"/>
      <node TEXT="Laporan ke Direksi untuk temuan material" COLOR="#ea4335"/>
    </node>
    <node TEXT="AKSES SISTEM" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Role SPI di sistem dengan akses read-only ke semua modul" COLOR="#ea4335"/>
      <node TEXT="Dashboard khusus SPI di Command Center" COLOR="#ea4335"/>
      <node TEXT="Export audit trail dalam format standar untuk kebutuhan audit eksternal" COLOR="#ea4335"/>
      <node TEXT="Tidak bisa memodifikasi data hanya bisa baca dan export" COLOR="#ea4335"/>
    </node>
    <node TEXT="KEPATUHAN REGULASI" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Mendukung audit BPK jika KMU diaudit eksternal" COLOR="#ea4335"/>
      <node TEXT="Memastikan kepatuhan LKPP dan Permenkes" COLOR="#ea4335"/>
      <node TEXT="Bukti digital audit trail siap kapan saja diminta auditor" COLOR="#ea4335"/>
    </node>
  </node>
</map>

<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <!-- Dikonversi otomatis dari MINDMAP_FASE5_KONTRAK_PORTAL_KSO.mermaid -->
  <!-- Konverter: mermaid_to_freemind.py | ID Penulis Skrip: claude-sonnet-4-6 (agen Cowork) -->
  <node TEXT="FASE 5 PELAKSANAAN KONTRAK &amp; PORTAL VENDOR KSO" COLOR="#34a853" FOLDED="false">
    <node TEXT="INPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="PKS dan SPK yang sudah ditandatangani kedua pihak dari Fase 4" COLOR="#ea4335"/>
      <node TEXT="KSO obligations dari kontrak vendor di Database Fase 2" COLOR="#ea4335"/>
    </node>
    <node TEXT="PENGELOLA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Kasie Pengadaan Jasa sebagai koordinator" COLOR="#ea4335"/>
      <node TEXT="Tim Teknis KMU sebagai pengawas lapangan" COLOR="#ea4335"/>
      <node TEXT="Vendor melalui Portal Vendor KMU" COLOR="#ea4335"/>
    </node>
    <node TEXT="PORTAL VENDOR KMU" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Vendor login menggunakan akun terverifikasi" COLOR="#ea4335"/>
      <node TEXT="Dashboard kewajiban KSO vendor" COLOR="#ea4335"/>
      <node TEXT="Upload laporan kegiatan harian bulanan tahunan" COLOR="#ea4335"/>
      <node TEXT="Status verifikasi laporan oleh KMU" COLOR="#ea4335"/>
      <node TEXT="Notifikasi dan reminder kewajiban mendatang" COLOR="#ea4335"/>
      <node TEXT="Riwayat kepatuhan dan skor kinerja" COLOR="#ea4335"/>
    </node>
    <node TEXT="KEWAJIBAN KSO MAINTENANCE" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Harian" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Laporan inspeksi visual alat" COLOR="#9334e6"/>
        <node TEXT="Power on test dan verifikasi fungsi dasar" COLOR="#9334e6"/>
        <node TEXT="Dokumentasi foto kondisi alat" COLOR="#9334e6"/>
      </node>
      <node TEXT="Bulanan" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Kalibrasi alat sesuai standar" COLOR="#9334e6"/>
        <node TEXT="Penggantian suku cadang terjadwal" COLOR="#9334e6"/>
        <node TEXT="Laporan preventive maintenance" COLOR="#9334e6"/>
      </node>
      <node TEXT="Tahunan" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Overhaul menyeluruh alat" COLOR="#9334e6"/>
        <node TEXT="Sertifikasi ulang alat medis" COLOR="#9334e6"/>
        <node TEXT="Laporan kondisi alat jangka panjang" COLOR="#9334e6"/>
      </node>
    </node>
    <node TEXT="KEWAJIBAN KSO KONSUMABEL" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="BHP Bahan Habis Pakai" COLOR="#ea4335" FOLDED="false">
        <node TEXT="ATK dan alat tulis kantor jadwal bulanan" COLOR="#9334e6"/>
        <node TEXT="Cleaning supply jadwal bulanan" COLOR="#9334e6"/>
      </node>
      <node TEXT="BMHP Bahan Medis Habis Pakai" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Jarum suntik jadwal mingguan" COLOR="#9334e6"/>
        <node TEXT="Sarung tangan dan masker jadwal mingguan" COLOR="#9334e6"/>
        <node TEXT="Plester dan perban jadwal mingguan" COLOR="#9334e6"/>
      </node>
      <node TEXT="Reagen" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Reagen lab dan diagnostik jadwal sesuai kontrak" COLOR="#9334e6"/>
        <node TEXT="Stok minimal buffer sesuai KPI kontrak" COLOR="#9334e6"/>
      </node>
    </node>
    <node TEXT="PROSES MONITORING" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Vendor upload laporan ke Portal" COLOR="#ea4335"/>
      <node TEXT="KMU verifikasi laporan secara digital bukan manual" COLOR="#ea4335"/>
      <node TEXT="Jika sesuai status hijau kewajiban terpenuhi" COLOR="#ea4335"/>
      <node TEXT="Jika tidak sesuai eskalasi otomatis ke Kasie dan Manager" COLOR="#ea4335"/>
      <node TEXT="Tim Teknis pantau progress pekerjaan konstruksi di lapangan" COLOR="#ea4335"/>
      <node TEXT="Pekerjaan selesai vendor buat BAPP" COLOR="#ea4335"/>
    </node>
    <node TEXT="OUTPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Data kinerja vendor real-time ke Fase 8 Evaluasi Vendor" COLOR="#ea4335"/>
      <node TEXT="BAPP Berita Acara Penyelesaian Pekerjaan sebagai trigger Fase 6" COLOR="#ea4335"/>
      <node TEXT="Log kewajiban KSO ke Fase 9 Pelaporan" COLOR="#ea4335"/>
    </node>
    <node TEXT="ESKALASI OTOMATIS" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Laporan terlambat 1 hari notifikasi ke vendor" COLOR="#ea4335"/>
      <node TEXT="Laporan terlambat 3 hari alert ke Kasie Pengadaan" COLOR="#ea4335"/>
      <node TEXT="Laporan terlambat 7 hari eskalasi ke Manager Pengadaan" COLOR="#ea4335"/>
      <node TEXT="Kewajiban kritis tidak terpenuhi eskalasi ke Direksi" COLOR="#ea4335"/>
    </node>
    <node TEXT="AI PENJAGA KEPATUHAN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Alert jika maintenance terlambat dari jadwal kontrak" COLOR="#ea4335"/>
      <node TEXT="Flag jika vendor tidak upload laporan sesuai tenggat" COLOR="#ea4335"/>
      <node TEXT="Eskalasi otomatis jika kewajiban melebihi toleransi" COLOR="#ea4335"/>
      <node TEXT="Skor kepatuhan real-time masuk ke profil vendor" COLOR="#ea4335"/>
    </node>
    <node TEXT="KONEKSI KE FASE LAIN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Input dari Fase 4 PKS dan SPK sebagai dasar kewajiban" COLOR="#ea4335"/>
      <node TEXT="Input dari Fase 2 KSO obligations dari database vendor" COLOR="#ea4335"/>
      <node TEXT="Output BAPP ke Fase 6 sebagai trigger penerimaan jasa" COLOR="#ea4335"/>
      <node TEXT="Output kinerja ke Fase 8 sebagai bahan evaluasi vendor" COLOR="#ea4335"/>
    </node>
  </node>
</map>

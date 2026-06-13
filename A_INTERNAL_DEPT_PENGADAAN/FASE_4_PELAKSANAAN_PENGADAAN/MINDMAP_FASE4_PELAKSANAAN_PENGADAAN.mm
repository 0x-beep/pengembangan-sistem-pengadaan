<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <!-- Dikonversi otomatis dari MINDMAP_FASE4_PELAKSANAAN_PENGADAAN.mermaid -->
  <!-- Konverter: mermaid_to_freemind.py | ID Penulis Skrip: claude-sonnet-4-6 (agen Cowork) -->
  <node TEXT="FASE 4 PELAKSANAAN PENGADAAN PROSES TENDER" COLOR="#34a853" FOLDED="false">
    <node TEXT="INPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="PP Permintaan Pembelian yang sudah disetujui dari Fase 3" COLOR="#ea4335"/>
      <node TEXT="SPPJ Surat Permintaan Pekerjaan Jasa dari Fase 3" COLOR="#ea4335"/>
      <node TEXT="Pool vendor terverifikasi dari Fase 2" COLOR="#ea4335"/>
      <node TEXT="Budget ceiling RKAP dari Fase 1" COLOR="#ea4335"/>
    </node>
    <node TEXT="PENGELOLA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Kasie Pengadaan Barang untuk jalur barang" COLOR="#ea4335"/>
      <node TEXT="Kasie Pengadaan Jasa untuk jalur jasa" COLOR="#ea4335"/>
      <node TEXT="Panitia Pengadaan SKD untuk nilai besar" COLOR="#ea4335"/>
    </node>
    <node TEXT="JALUR BARANG" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="PP diterima dan diverifikasi" COLOR="#ea4335"/>
      <node TEXT="SPPH dikirim ke minimal 2 vendor estimasi jawab 2 hari" COLOR="#ea4335"/>
      <node TEXT="SJPH diterima dari vendor peserta" COLOR="#ea4335"/>
      <node TEXT="Bidding Tabulasi dibuat dalam 1 hari" COLOR="#ea4335"/>
      <node TEXT="Scoring vendor 5 kriteria Harga 25 Kualitas 20 Maintenance 20 Kebutuhan User 20 Brand 15" COLOR="#ea4335"/>
      <node TEXT="Negosiasi harga waktu garansi after-sales" COLOR="#ea4335"/>
      <node TEXT="Pemenang ditetapkan" COLOR="#ea4335"/>
      <node TEXT="PO dibuat dalam 1 hari dan diotorisasi sesuai nilai" COLOR="#ea4335"/>
      <node TEXT="PO dikirim ke vendor trigger pengiriman barang" COLOR="#ea4335"/>
    </node>
    <node TEXT="JALUR JASA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="SPPJ dan BOQ serta DED diterima" COLOR="#ea4335"/>
      <node TEXT="Aanwijzing Internal 1 hari unit peminta pengadaan keuangan" COLOR="#ea4335"/>
      <node TEXT="SPPH dikirim ke minimal 2 kontraktor atau konsultan" COLOR="#ea4335"/>
      <node TEXT="Aanwijzing Eksternal briefing semua peserta" COLOR="#ea4335"/>
      <node TEXT="SJPH diterima kecil 1 minggu sedang 10 hari besar 1 bulan" COLOR="#ea4335"/>
      <node TEXT="Bidding Tabulasi dibuat dalam 1 hari" COLOR="#ea4335"/>
      <node TEXT="Negosiasi dan penetapan pemenang" COLOR="#ea4335"/>
      <node TEXT="PKS dan SPK dibuat dan diotorisasi sesuai nilai" COLOR="#ea4335"/>
      <node TEXT="BASTL Berita Acara Serah Terima Lokasi pekerjaan dimulai" COLOR="#ea4335"/>
    </node>
    <node TEXT="JALUR KHUSUS" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Penunjukan Langsung" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Tanpa proses tender kompetitif" COLOR="#9334e6"/>
        <node TEXT="Syarat ketat kondisi darurat atau vendor tunggal" COLOR="#9334e6"/>
        <node TEXT="SLA maksimal 3 hari kerja" COLOR="#9334e6"/>
      </node>
      <node TEXT="Swakelola" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Dikerjakan oleh tim internal KMU" COLOR="#9334e6"/>
        <node TEXT="Tidak ada proses vendor" COLOR="#9334e6"/>
        <node TEXT="Anggaran tetap dari RKAP" COLOR="#9334e6"/>
      </node>
    </node>
    <node TEXT="OTORISASI NILAI PO DAN SPK" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Sampai 50 juta Kasie Pengadaan" COLOR="#ea4335"/>
      <node TEXT="50 sampai 500 juta Manager Pengadaan" COLOR="#ea4335"/>
      <node TEXT="500 juta sampai 1 miliar GM Operasi" COLOR="#ea4335"/>
      <node TEXT="Lebih dari 1 miliar Direktur atau BOD" COLOR="#ea4335"/>
    </node>
    <node TEXT="SKORING BIDDING TABULASI" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Harga Penawaran bobot 25 persen mendekati HPS" COLOR="#ea4335"/>
      <node TEXT="Kualitas Barang bobot 20 persen spesifikasi dan sertifikasi" COLOR="#ea4335"/>
      <node TEXT="Maintenance dan Sparepart bobot 20 persen respons dan ketersediaan" COLOR="#ea4335"/>
      <node TEXT="Kesesuaian Kebutuhan User bobot 20 persen fit to clinical requirements" COLOR="#ea4335"/>
      <node TEXT="Orientasi Merek Track Record bobot 15 persen reputasi dan populasi" COLOR="#ea4335"/>
      <node TEXT="Skor lebih dari 400 Rekomendasi Utama" COLOR="#ea4335"/>
      <node TEXT="Skor 350 sampai 399 Rekomendasi Alternatif" COLOR="#ea4335"/>
      <node TEXT="Skor 300 sampai 349 Pertimbangan Bersyarat" COLOR="#ea4335"/>
      <node TEXT="Skor kurang dari 300 Tidak Direkomendasikan" COLOR="#ea4335"/>
    </node>
    <node TEXT="OUTPUT" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="PO yang ditandatangani sebagai trigger pengiriman barang ke Fase 6" COLOR="#ea4335"/>
      <node TEXT="PKS dan SPK yang ditandatangani sebagai trigger pelaksanaan jasa ke Fase 5" COLOR="#ea4335"/>
      <node TEXT="Data tender tersimpan di sistem masuk ke Pelaporan Fase 9" COLOR="#ea4335"/>
    </node>
    <node TEXT="AI PENJAGA KEPATUHAN" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Validasi minimal 2 vendor di SPPH" COLOR="#ea4335"/>
      <node TEXT="Cek Aanwijzing sudah dilakukan sebelum SJPH diterima" COLOR="#ea4335"/>
      <node TEXT="Blokir PO jika nilai melebihi budget RKAP tanpa persetujuan tambahan" COLOR="#ea4335"/>
      <node TEXT="Validasi otorisasi sesuai kewenangan nilai PO dan SPK" COLOR="#ea4335"/>
    </node>
    <node TEXT="SLA TARGET" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="PP ke SPPH maksimal 1 hari kerja" COLOR="#ea4335"/>
      <node TEXT="SPPH ke SJPH estimasi 2 hari kerja" COLOR="#ea4335"/>
      <node TEXT="Bidding Tabulasi maksimal 1 hari kerja" COLOR="#ea4335"/>
      <node TEXT="Total PP ke PO jalur tender maksimal 14 hari kerja" COLOR="#ea4335"/>
      <node TEXT="Total PP ke PO jalur penunjukan langsung maksimal 3 hari kerja" COLOR="#ea4335"/>
    </node>
  </node>
</map>

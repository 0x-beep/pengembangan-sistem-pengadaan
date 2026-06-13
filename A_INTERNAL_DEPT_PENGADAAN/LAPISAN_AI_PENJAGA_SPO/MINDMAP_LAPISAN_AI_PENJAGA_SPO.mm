<?xml version="1.0" encoding="UTF-8"?>
<map version="1.0.1">
  <!-- Dikonversi otomatis dari MINDMAP_LAPISAN_AI_PENJAGA_SPO.mermaid -->
  <!-- Konverter: mermaid_to_freemind.py | ID Penulis Skrip: claude-sonnet-4-6 (agen Cowork) -->
  <node TEXT="LAPISAN AI PENJAGA KEPATUHAN SPO" COLOR="#34a853" FOLDED="false">
    <node TEXT="FUNGSI UTAMA" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Memantau setiap aksi di seluruh modul sistem" COLOR="#ea4335"/>
      <node TEXT="Membandingkan aksi dengan SPO yang sudah diingesti" COLOR="#ea4335"/>
      <node TEXT="Alert real-time jika deviasi terdeteksi" COLOR="#ea4335"/>
      <node TEXT="Memberikan panduan langkah yang benar otomatis" COLOR="#ea4335"/>
      <node TEXT="Mencegah pelanggaran sebelum terjadi" COLOR="#ea4335"/>
    </node>
    <node TEXT="ARSITEKTUR SISTEM" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Document Repository" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Semua SPO dan prosedur KMU dalam format PDF" COLOR="#9334e6"/>
        <node TEXT="Guidelines dan checklist operasional" COLOR="#9334e6"/>
        <node TEXT="Regulasi LKPP dan Permenkes" COLOR="#9334e6"/>
      </node>
      <node TEXT="AI Document Processor" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Gemini Vision untuk ingesti dokumen" COLOR="#9334e6"/>
        <node TEXT="Ekstraksi aturan dan alur dari setiap SPO" COLOR="#9334e6"/>
        <node TEXT="Pembaruan otomatis jika SPO direvisi" COLOR="#9334e6"/>
      </node>
      <node TEXT="Procedure Validation Engine" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Rule database berisi semua aturan terekstrak" COLOR="#9334e6"/>
        <node TEXT="Real-time matching setiap aksi pengguna" COLOR="#9334e6"/>
        <node TEXT="Pattern recognition anomali" COLOR="#9334e6"/>
      </node>
      <node TEXT="Real-Time Guidance System" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Alert dan panduan saat aksi dilakukan" COLOR="#9334e6"/>
        <node TEXT="Step-by-step guidance langkah benar" COLOR="#9334e6"/>
        <node TEXT="Chatbot 24 jam untuk tanya jawab prosedur" COLOR="#9334e6"/>
      </node>
    </node>
    <node TEXT="TITIK VALIDASI PER FASE" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Fase 1 Perencanaan" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Apakah RKAP sudah disahkan Direksi sebelum proses dimulai" COLOR="#9334e6"/>
      </node>
      <node TEXT="Fase 3 Permintaan" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Apakah PP sudah ada di RKAP yang disetujui" COLOR="#9334e6"/>
        <node TEXT="Apakah investasi lebih dari 100 juta ada Feasibility Study" COLOR="#9334e6"/>
        <node TEXT="Apakah SPPJ sudah dilengkapi BOQ dan DED" COLOR="#9334e6"/>
      </node>
      <node TEXT="Fase 4 Tender" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Apakah jumlah vendor SPPH minimal 2" COLOR="#9334e6"/>
        <node TEXT="Apakah Aanwijzing sudah dilakukan sebelum SJPH diterima" COLOR="#9334e6"/>
        <node TEXT="Apakah nilai PO tidak melebihi budget RKAP" COLOR="#9334e6"/>
        <node TEXT="Apakah otorisasi PO sesuai kewenangan nilai" COLOR="#9334e6"/>
      </node>
      <node TEXT="Fase 6 Penerimaan" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Apakah BAPB sudah ada sebelum invoice diproses" COLOR="#9334e6"/>
        <node TEXT="Apakah 3-Way Match sudah clear" COLOR="#9334e6"/>
      </node>
      <node TEXT="Fase 7 Pembayaran" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Apakah 3-Way Match sudah verified sebelum bayar" COLOR="#9334e6"/>
        <node TEXT="Apakah nilai pembayaran tidak melebihi nilai kontrak" COLOR="#9334e6"/>
      </node>
      <node TEXT="Fase 5 Kontrak KSO" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Apakah laporan maintenance vendor terlambat dari jadwal" COLOR="#9334e6"/>
      </node>
    </node>
    <node TEXT="LEVEL RESPONS" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Pelanggaran Ringan" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Alert popup dengan penjelasan" COLOR="#9334e6"/>
        <node TEXT="Panduan langkah yang benar" COLOR="#9334e6"/>
        <node TEXT="User bisa lanjut setelah konfirmasi" COLOR="#9334e6"/>
      </node>
      <node TEXT="Pelanggaran Sedang" COLOR="#ea4335" FOLDED="false">
        <node TEXT="Warning dengan detail pelanggaran" COLOR="#9334e6"/>
        <node TEXT="Harus ada override approval dari atasan" COLOR="#9334e6"/>
        <node TEXT="Dicatat di audit trail sebagai exception" COLOR="#9334e6"/>
      </node>
      <node TEXT="Pelanggaran Berat" COLOR="#ea4335" FOLDED="false">
        <node TEXT="BLOKIR total aksi tidak bisa dilanjutkan" COLOR="#9334e6"/>
        <node TEXT="Eskalasi otomatis ke Manager atau Direksi" COLOR="#9334e6"/>
        <node TEXT="Investigasi wajib sebelum proses bisa dilanjutkan" COLOR="#9334e6"/>
      </node>
    </node>
    <node TEXT="CHATBOT 24 JAM" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Staff bisa tanya prosedur kapan saja" COLOR="#ea4335"/>
      <node TEXT="Jawaban berbasis SPO KMU yang sudah diingesti" COLOR="#ea4335"/>
      <node TEXT="Contoh pertanyaan Apa langkah selanjutnya untuk SPPJ konstruksi" COLOR="#ea4335"/>
      <node TEXT="Contoh pertanyaan Berapa minimal vendor untuk SPPH jasa" COLOR="#ea4335"/>
      <node TEXT="Contoh pertanyaan Dokumen apa yang dibutuhkan untuk PP investasi" COLOR="#ea4335"/>
    </node>
    <node TEXT="PEMBELAJARAN AI" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Semakin banyak data transaksi semakin akurat deteksi anomali" COLOR="#ea4335"/>
      <node TEXT="Pattern learning dari histori pelanggaran" COLOR="#ea4335"/>
      <node TEXT="Penyesuaian threshold berdasarkan data aktual KMU" COLOR="#ea4335"/>
    </node>
    <node TEXT="INTEGRASI" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Embedded di seluruh modul platform pengadaan KMU" COLOR="#ea4335"/>
      <node TEXT="Standalone sebagai SOP Assistant chatbot" COLOR="#ea4335"/>
      <node TEXT="Feed ke Command Center Dashboard untuk alert kritis" COLOR="#ea4335"/>
      <node TEXT="Feed ke Audit Trail semua kejadian pelanggaran tercatat" COLOR="#ea4335"/>
    </node>
    <node TEXT="MANFAAT TERUKUR" COLOR="#fbbc04" FOLDED="false">
      <node TEXT="Compliance rate dari 15 persen ke target 95 persen" COLOR="#ea4335"/>
      <node TEXT="Pelanggaran SPO terdeteksi real-time bukan saat audit" COLOR="#ea4335"/>
      <node TEXT="Waktu pencarian prosedur manual dieliminasi" COLOR="#ea4335"/>
      <node TEXT="Konsistensi penerapan SPO di seluruh user KMU" COLOR="#ea4335"/>
    </node>
  </node>
</map>

import os
import re

def update_dashboard():
    # 1. Read existing
    with open('manager_pengadaan_dashboard.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 2. Update Header & User Profile
    html = html.replace('Command Center Pengadaan', 'Portal Pengadaan Terintegrasi')
    html = html.replace('Command Center Proses Pengadaan', 'Portal Operasional Pengadaan')
    
    role_switcher_html = '''
    <div class="relative group">
        <button class="flex items-center gap-2 bg-slate-100 hover:bg-slate-200 px-4 py-2 rounded-lg text-sm font-bold text-slate-700 transition">
            <i class="fas fa-user-circle text-blue-600"></i> Role: Manager Pengadaan <i class="fas fa-chevron-down text-xs ml-1"></i>
        </button>
        <div class="absolute right-0 mt-2 w-48 bg-white border border-slate-200 rounded-lg shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all z-50">
            <a href="#" class="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50 border-b border-slate-100 font-bold"><i class="fas fa-user-tie text-blue-500 mr-2"></i> Manager Pengadaan</a>
            <a href="#" class="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50 border-b border-slate-100"><i class="fas fa-user text-emerald-500 mr-2"></i> Kasie Barang (Kasim)</a>
            <a href="#" class="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50 border-b border-slate-100"><i class="fas fa-user text-indigo-500 mr-2"></i> Kasie Jasa (Firman)</a>
            <a href="#" class="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50 text-rose-600"><i class="fas fa-sign-out-alt mr-2"></i> Logout</a>
        </div>
    </div>
    '''
    
    # Insert role switcher after the header title
    html = re.sub(r'(<h1 class="text-2xl font-bold text-slate-800">.*?</h1>\s*<p.*?>.*?</p>)', r'\1\n</div>\n' + role_switcher_html + '\n<div>', html)
    # Fix the div structure that was broken by the hacky replace above
    # Wait, better to just replace the header container
    # Let's find the header div: `<div class="mb-8">` after `<main class="p-6">`
    # Let's use a more precise replacement:
    
    # 3. Add Modal HTML at the end of body
    modal_html = '''
    <!-- Card Detail Modal -->
    <div id="cardModal" class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm hidden z-50 flex items-center justify-center">
        <div class="bg-white rounded-xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col transform scale-95 opacity-0 transition-all duration-200" id="cardModalContent">
            
            <!-- Modal Header -->
            <div class="px-6 py-4 border-b border-slate-100 flex justify-between items-center bg-slate-50">
                <div class="flex items-center gap-3">
                    <span class="px-3 py-1 bg-slate-200 text-slate-700 rounded-lg text-sm font-bold font-mono" id="modalNoPP">PP-000</span>
                    <span class="px-3 py-1 bg-amber-100 text-amber-700 rounded-lg text-xs font-bold" id="modalStatus"><i class="fas fa-clock mr-1"></i> Status</span>
                </div>
                <button onclick="closeModal()" class="text-slate-400 hover:text-slate-700 transition">
                    <i class="fas fa-times text-xl"></i>
                </button>
            </div>

            <!-- Modal Body -->
            <div class="p-6 overflow-y-auto flex-1">
                <h3 class="text-xl font-bold text-slate-800 mb-1" id="modalTitle">Judul Pengadaan</h3>
                <p class="text-sm text-slate-500 mb-6" id="modalSBU">SBU / Departemen</p>

                <div class="grid grid-cols-2 gap-4 mb-6">
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                        <p class="text-xs text-slate-500 font-medium mb-1">Estimasi Nilai (HPS)</p>
                        <p class="text-lg font-black text-blue-600" id="modalValue">Rp 0</p>
                    </div>
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-100">
                        <p class="text-xs text-slate-500 font-medium mb-1">Vendor Terpilih / Kandidat</p>
                        <p class="text-sm font-bold text-slate-700" id="modalVendor">TBA</p>
                    </div>
                </div>

                <!-- Kolom Komunikasi / Catatan -->
                <div class="border-t border-slate-100 pt-6">
                    <h4 class="text-sm font-bold text-slate-800 mb-4 flex items-center gap-2">
                        <i class="fas fa-comments text-blue-500"></i> Kolom Komunikasi & Catatan Internal
                    </h4>
                    
                    <div class="space-y-4 mb-4">
                        <div class="flex gap-3">
                            <div class="w-8 h-8 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold text-xs shrink-0">KG</div>
                            <div class="bg-blue-50 p-3 rounded-lg rounded-tl-none border border-blue-100 text-sm text-slate-700">
                                <p class="font-bold text-xs text-blue-800 mb-1">Kasim Ganteng (Kasie Barang) <span class="text-[10px] text-blue-400 font-normal ml-2">Hari ini, 09:12</span></p>
                                Dokumen teknis sudah lengkap. Tinggal menunggu TTD Direksi untuk pencairan DP.
                            </div>
                        </div>
                        <div class="flex gap-3">
                            <div class="w-8 h-8 rounded-full bg-amber-100 text-amber-600 flex items-center justify-center font-bold text-xs shrink-0">MP</div>
                            <div class="bg-amber-50 p-3 rounded-lg rounded-tl-none border border-amber-100 text-sm text-slate-700">
                                <p class="font-bold text-xs text-amber-800 mb-1">Manager Pengadaan <span class="text-[10px] text-amber-400 font-normal ml-2">Hari ini, 10:45</span></p>
                                Tolong di-follow up lagi ke Keuangan, jangan sampai melewati SLA 3 hari.
                            </div>
                        </div>
                    </div>

                    <!-- Input Komentar -->
                    <div class="flex gap-3 items-start mt-4 relative">
                        <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-xs shrink-0">MP</div>
                        <div class="flex-1">
                            <textarea class="w-full border border-slate-200 rounded-lg p-3 text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition resize-none outline-none" rows="2" placeholder="Tulis instruksi atau catatan opsional untuk tim..."></textarea>
                            <div class="flex justify-end mt-2">
                                <button class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-1.5 rounded-md text-xs font-bold transition shadow-sm">Kirim Pesan</button>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <script>
        function openCardModal(element) {
            // Get data from element
            const noPP = element.querySelector('.text-[10px].bg-slate-100')?.innerText || element.querySelector('.text-[10px].bg-emerald-100')?.innerText || 'PP-XXX';
            const title = element.querySelector('h5')?.innerText || 'Judul';
            const sbu = element.querySelector('p.text-slate-500')?.innerText || 'SBU';
            const value = element.querySelector('.font-black')?.innerText || 'Rp -';
            
            let vendor = 'TBA';
            if(element.querySelector('h5').innerText.startsWith('PT') || element.querySelector('h5').innerText.startsWith('CV')) {
                vendor = title;
                title = sbu;
                sbu = 'TBA';
            }

            document.getElementById('modalNoPP').innerText = noPP;
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalSBU').innerText = sbu;
            document.getElementById('modalValue').innerText = value;
            document.getElementById('modalVendor').innerText = vendor;

            const modal = document.getElementById('cardModal');
            const content = document.getElementById('cardModalContent');
            
            modal.classList.remove('hidden');
            // trigger reflow
            void modal.offsetWidth;
            content.classList.remove('scale-95', 'opacity-0');
            content.classList.add('scale-100', 'opacity-100');
        }

        function closeModal() {
            const modal = document.getElementById('cardModal');
            const content = document.getElementById('cardModalContent');
            
            content.classList.remove('scale-100', 'opacity-100');
            content.classList.add('scale-95', 'opacity-0');
            
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 200);
        }
    </script>
    '''
    
    html = html.replace('</body>', modal_html + '\n</body>')

    # 4. Inject onclick="openCardModal(this)" into all <div class="k-card ...">
    html = re.sub(r'(<div class="k-card[^>]*?)(">)', r'\1" onclick="openCardModal(this)">', html)

    # 5. Add massive bottlenecks to "Persetujuan Keuangan"
    # We will find the "Persetujuan Keuangan" column and append more cards
    bottleneck_cards = '''
                    <div class="k-card warning" onclick="openCardModal(this)">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-054</span>
                            <span class="text-[10px] font-bold text-amber-600"><i class="fas fa-clock"></i> 4 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Rajawali Nusindo</h5>
                        <p class="text-[11px] text-slate-500 mb-2">Reagen Lab Reguler</p>
                        <div class="text-[10px] text-amber-600 mt-1"><i class="fas fa-user-tie"></i> Menunggu TTD GM Keuangan</div>
                    </div>
                    <div class="k-card urgent" onclick="openCardModal(this)">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-050</span>
                            <span class="text-[10px] font-bold text-red-600 animate-pulse"><i class="fas fa-exclamation-triangle"></i> 6 Hari!</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Enseval Medika</h5>
                        <p class="text-[11px] text-slate-500 mb-2">BMHP Farmasi</p>
                        <div class="text-[10px] text-red-600 mt-1"><i class="fas fa-user-tie"></i> Macet di Direktur Keuangan</div>
                    </div>
                    <div class="k-card normal" onclick="openCardModal(this)">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-056</span>
                            <span class="text-[10px] font-bold text-emerald-600"><i class="fas fa-clock"></i> 1 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">CV Kaltim Berjaya</h5>
                        <p class="text-[11px] text-slate-500 mb-2">ATK & Cetakan</p>
                        <div class="text-[10px] text-amber-600 mt-1"><i class="fas fa-user-tie"></i> Review Anggaran</div>
                    </div>
                    <div class="k-card warning" onclick="openCardModal(this)">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-049</span>
                            <span class="text-[10px] font-bold text-amber-600"><i class="fas fa-clock"></i> 3 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Global Solusi</h5>
                        <p class="text-[11px] text-slate-500 mb-2">Lisensi Software HIS</p>
                        <div class="text-[10px] text-amber-600 mt-1"><i class="fas fa-user-tie"></i> Menunggu TTD GM Keuangan</div>
                    </div>
    '''
    
    # Insert bottleneck cards into Persetujuan Keuangan (Col 5 of Barang)
    # The header is `<span>5. Persetujuan Keuangan</span>`
    html = re.sub(
        r'(<span>5\. Persetujuan Keuangan</span>.*?</div\s*>\s*<div class="kanban-cards">)(.*?)(</div>\s*<!-- Col 6 -->)',
        lambda m: m.group(1) + m.group(2) + bottleneck_cards + m.group(3),
        html,
        flags=re.DOTALL
    )

    # 6. Save as pengadaan_dashboard.html
    with open('pengadaan_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Dashboard created successfully")

update_dashboard()

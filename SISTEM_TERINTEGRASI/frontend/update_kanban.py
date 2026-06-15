import re

def build_kanban_html(is_dark=False):
    # Theme colors
    bg_container = "bg-[#0f172a]/80" if is_dark else "bg-slate-50"
    bg_col = "bg-slate-800/50" if is_dark else "bg-slate-100"
    border_col = "border-slate-700" if is_dark else "border-slate-200"
    
    bg_card = "bg-slate-900 border-slate-700 hover:border-slate-600" if is_dark else "bg-white border-slate-200 hover:border-slate-300"
    text_primary = "text-slate-200" if is_dark else "text-slate-800"
    text_muted = "text-slate-400" if is_dark else "text-slate-500"
    
    html = f"""
                        <div class="p-4 w-full overflow-x-auto {bg_container} rounded-b-xl border-t {border_col}">
                            
                            <!-- Kanban Board Container -->
                            <div class="flex gap-4 min-w-[1000px] h-[500px]">
                                
                                <!-- Column 1: Gudang & Pengadaan (Ops) -->
                                <div class="flex-1 flex flex-col {bg_col} border {border_col} rounded-xl overflow-hidden shadow-sm">
                                    <div class="p-3 border-b {border_col} bg-blue-500/10">
                                        <h4 class="font-bold text-sm text-blue-600 flex items-center justify-between">
                                            <span><i class="fas fa-boxes mr-1"></i> Ops / Gudang</span>
                                            <span class="bg-blue-500 text-white text-[10px] px-2 py-0.5 rounded-full">2</span>
                                        </h4>
                                    </div>
                                    <div class="p-3 flex-1 overflow-y-auto flex flex-col gap-3 custom-scrollbar">
                                        
                                        <!-- Card 1 -->
                                        <div class="{bg_card} border rounded-lg p-3 shadow-sm transition cursor-pointer relative group">
                                            <div class="flex justify-between items-start mb-2">
                                                <span class="text-[10px] font-bold text-slate-500 bg-slate-200/50 dark:bg-slate-800 px-2 py-0.5 rounded">INV-0992</span>
                                                <span class="text-[10px] font-bold text-emerald-600 flex items-center gap-1"><i class="fas fa-clock"></i> 1 Hari</span>
                                            </div>
                                            <h5 class="font-bold text-xs {text_primary} mb-1">PT Borneo Etam Mandiri</h5>
                                            <p class="text-[11px] {text_muted} mb-2">Alkes Kebutuhan Tahunan</p>
                                            <div class="flex justify-between items-center mt-2 pt-2 border-t {border_col}">
                                                <span class="text-xs font-black text-blue-600">Rp 125.000.000</span>
                                                <span class="text-[10px] text-blue-500 font-medium"><i class="fas fa-user-cog"></i> Admin 3WM</span>
                                            </div>
                                        </div>

                                        <!-- Card 2 -->
                                        <div class="{bg_card} border rounded-lg p-3 shadow-sm transition cursor-pointer relative group">
                                            <div class="flex justify-between items-start mb-2">
                                                <span class="text-[10px] font-bold text-slate-500 bg-slate-200/50 dark:bg-slate-800 px-2 py-0.5 rounded">INV-0985</span>
                                                <span class="text-[10px] font-bold text-emerald-600 flex items-center gap-1"><i class="fas fa-clock"></i> 2 Hari</span>
                                            </div>
                                            <h5 class="font-bold text-xs {text_primary} mb-1">PT Global Medik Persada</h5>
                                            <p class="text-[11px] {text_muted} mb-2">Obat Farmasi Bulanan</p>
                                            <div class="flex justify-between items-center mt-2 pt-2 border-t {border_col}">
                                                <span class="text-xs font-black text-blue-600">Rp 85.500.000</span>
                                                <span class="text-[10px] text-blue-500 font-medium"><i class="fas fa-user-tie"></i> Manajer Pengadaan</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- Column 2: Approval Direksi (BOD) -->
                                <div class="flex-1 flex flex-col {bg_col} border {border_col} rounded-xl overflow-hidden shadow-sm">
                                    <div class="p-3 border-b {border_col} bg-amber-500/10">
                                        <h4 class="font-bold text-sm text-amber-600 flex items-center justify-between">
                                            <span><i class="fas fa-crown mr-1"></i> BOD Approval</span>
                                            <span class="bg-amber-500 text-white text-[10px] px-2 py-0.5 rounded-full">3</span>
                                        </h4>
                                    </div>
                                    <div class="p-3 flex-1 overflow-y-auto flex flex-col gap-3 custom-scrollbar">
                                        
                                        <!-- Card 3 -->
                                        <div class="{bg_card} border rounded-lg p-3 shadow-sm transition cursor-pointer relative group border-l-4 border-l-rose-500">
                                            <div class="flex justify-between items-start mb-2">
                                                <span class="text-[10px] font-bold text-slate-500 bg-slate-200/50 dark:bg-slate-800 px-2 py-0.5 rounded">INV-0850</span>
                                                <span class="text-[10px] font-bold text-rose-600 flex items-center gap-1 animate-pulse"><i class="fas fa-exclamation-triangle"></i> 14 Hari!</span>
                                            </div>
                                            <h5 class="font-bold text-xs {text_primary} mb-1">PT Transmedic Indonesia</h5>
                                            <p class="text-[11px] {text_muted} mb-2">Pengadaan MRI Scanner</p>
                                            <div class="flex justify-between items-center mt-2 pt-2 border-t {border_col}">
                                                <span class="text-xs font-black text-amber-600">Rp 2.500.000.000</span>
                                                <span class="text-[10px] text-amber-600 font-medium"><i class="fas fa-user-shield"></i> Tunggu Dirut</span>
                                            </div>
                                        </div>

                                        <!-- Card 4 -->
                                        <div class="{bg_card} border rounded-lg p-3 shadow-sm transition cursor-pointer relative group border-l-4 border-l-amber-500">
                                            <div class="flex justify-between items-start mb-2">
                                                <span class="text-[10px] font-bold text-slate-500 bg-slate-200/50 dark:bg-slate-800 px-2 py-0.5 rounded">INV-0910</span>
                                                <span class="text-[10px] font-bold text-amber-600 flex items-center gap-1"><i class="fas fa-clock"></i> 5 Hari</span>
                                            </div>
                                            <h5 class="font-bold text-xs {text_primary} mb-1">PT BTL Indonesia</h5>
                                            <p class="text-[11px] {text_muted} mb-2">Maintenance CT Scan</p>
                                            <div class="flex justify-between items-center mt-2 pt-2 border-t {border_col}">
                                                <span class="text-xs font-black text-amber-600">Rp 450.000.000</span>
                                                <span class="text-[10px] text-amber-600 font-medium"><i class="fas fa-user-shield"></i> Dir Operasi</span>
                                            </div>
                                        </div>
                                        
                                        <!-- Card 5 -->
                                        <div class="{bg_card} border rounded-lg p-3 shadow-sm transition cursor-pointer relative group">
                                            <div class="flex justify-between items-start mb-2">
                                                <span class="text-[10px] font-bold text-slate-500 bg-slate-200/50 dark:bg-slate-800 px-2 py-0.5 rounded">INV-0935</span>
                                                <span class="text-[10px] font-bold text-emerald-600 flex items-center gap-1"><i class="fas fa-clock"></i> 2 Hari</span>
                                            </div>
                                            <h5 class="font-bold text-xs {text_primary} mb-1">CV Akar Sakti</h5>
                                            <p class="text-[11px] {text_muted} mb-2">Renovasi Ruang Rawat Inap</p>
                                            <div class="flex justify-between items-center mt-2 pt-2 border-t {border_col}">
                                                <span class="text-xs font-black text-amber-600">Rp 150.000.000</span>
                                                <span class="text-[10px] text-amber-600 font-medium"><i class="fas fa-user-shield"></i> Dir Keuangan</span>
                                            </div>
                                        </div>

                                    </div>
                                </div>

                                <!-- Column 3: Verifikasi Finance -->
                                <div class="flex-1 flex flex-col {bg_col} border {border_col} rounded-xl overflow-hidden shadow-sm">
                                    <div class="p-3 border-b {border_col} bg-emerald-500/10">
                                        <h4 class="font-bold text-sm text-emerald-600 flex items-center justify-between">
                                            <span><i class="fas fa-search-dollar mr-1"></i> Verifikasi Finance</span>
                                            <span class="bg-emerald-500 text-white text-[10px] px-2 py-0.5 rounded-full">1</span>
                                        </h4>
                                    </div>
                                    <div class="p-3 flex-1 overflow-y-auto flex flex-col gap-3 custom-scrollbar">
                                        
                                        <!-- Card 6 -->
                                        <div class="{bg_card} border rounded-lg p-3 shadow-sm transition cursor-pointer relative group border-l-4 border-l-amber-500">
                                            <div class="flex justify-between items-start mb-2">
                                                <span class="text-[10px] font-bold text-slate-500 bg-slate-200/50 dark:bg-slate-800 px-2 py-0.5 rounded">INV-0901</span>
                                                <span class="text-[10px] font-bold text-amber-600 flex items-center gap-1"><i class="fas fa-clock"></i> 6 Hari</span>
                                            </div>
                                            <h5 class="font-bold text-xs {text_primary} mb-1">PT Enseval Putera Megatrading</h5>
                                            <p class="text-[11px] {text_muted} mb-2">Suplai Infus & APD</p>
                                            <div class="flex justify-between items-center mt-2 pt-2 border-t {border_col}">
                                                <span class="text-xs font-black text-emerald-600">Rp 75.200.000</span>
                                                <span class="text-[10px] text-emerald-500 font-medium"><i class="fas fa-file-invoice"></i> Verifikasi Pajak</span>
                                            </div>
                                        </div>

                                    </div>
                                </div>

                                <!-- Column 4: Menunggu Pencairan -->
                                <div class="flex-1 flex flex-col {bg_col} border {border_col} rounded-xl overflow-hidden shadow-sm">
                                    <div class="p-3 border-b {border_col} bg-teal-500/10">
                                        <h4 class="font-bold text-sm text-teal-600 flex items-center justify-between">
                                            <span><i class="fas fa-money-check-alt mr-1"></i> Siap Bayar / Komite</span>
                                            <span class="bg-teal-500 text-white text-[10px] px-2 py-0.5 rounded-full">2</span>
                                        </h4>
                                    </div>
                                    <div class="p-3 flex-1 overflow-y-auto flex flex-col gap-3 custom-scrollbar">
                                        
                                        <!-- Card 7 -->
                                        <div class="{bg_card} border rounded-lg p-3 shadow-sm transition cursor-pointer relative group border-l-4 border-l-rose-500">
                                            <div class="flex justify-between items-start mb-2">
                                                <span class="text-[10px] font-bold text-slate-500 bg-slate-200/50 dark:bg-slate-800 px-2 py-0.5 rounded">INV-0805</span>
                                                <span class="text-[10px] font-bold text-rose-600 flex items-center gap-1 animate-pulse"><i class="fas fa-exclamation-triangle"></i> 21 Hari!</span>
                                            </div>
                                            <h5 class="font-bold text-xs {text_primary} mb-1">PT Capricorn Mulia</h5>
                                            <p class="text-[11px] {text_muted} mb-2">Pengadaan Genset RS</p>
                                            <div class="flex justify-between items-center mt-2 pt-2 border-t {border_col}">
                                                <span class="text-xs font-black text-teal-600">Rp 1.200.000.000</span>
                                                <span class="text-[10px] text-rose-500 font-bold bg-rose-500/10 px-1.5 py-0.5 rounded">Dana Macet (BPJS)</span>
                                            </div>
                                        </div>

                                        <!-- Card 8 -->
                                        <div class="{bg_card} border rounded-lg p-3 shadow-sm transition cursor-pointer relative group">
                                            <div class="flex justify-between items-start mb-2">
                                                <span class="text-[10px] font-bold text-slate-500 bg-slate-200/50 dark:bg-slate-800 px-2 py-0.5 rounded">INV-0955</span>
                                                <span class="text-[10px] font-bold text-emerald-600 flex items-center gap-1"><i class="fas fa-clock"></i> 1 Hari</span>
                                            </div>
                                            <h5 class="font-bold text-xs {text_primary} mb-1">PT Sumber Rejeki Medika Jaya</h5>
                                            <p class="text-[11px] {text_muted} mb-2">Obat Sirup Anak</p>
                                            <div class="flex justify-between items-center mt-2 pt-2 border-t {border_col}">
                                                <span class="text-xs font-black text-teal-600">Rp 45.000.000</span>
                                                <span class="text-[10px] text-teal-500 font-medium"><i class="fas fa-check-circle"></i> Dijadwalkan Besok</span>
                                            </div>
                                        </div>

                                    </div>
                                </div>

                            </div>
                        </div>"""
    return html

def replace_in_file(filepath, is_dark=False):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return

    # Find the container using regex
    start_pattern = r'<div class="p-0 (overflow-x-auto relative|relative w-full overflow-hidden).*?">'
    end_pattern = r'(?P<end></div>\s*</div>\s*(?:</div>|<!-- SECTION 4|<!-- SECTION 3: LOG AUDIT|<div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden mb-8">))'
    
    match = re.search(f"{start_pattern}.*?{end_pattern}", content, re.DOTALL)
    if not match:
        print(f"Could not find replacement block in {filepath}")
        return
        
    new_html = build_kanban_html(is_dark)
    end_text = match.group('end')
    
    replaced_content = content[:match.start()] + new_html + "\n                  " + end_text[12:] 
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(replaced_content)
    print(f"Successfully updated {filepath}")

if __name__ == "__main__":
    files = [
        ("finance_dashboard.html", False),
        ("director_dashboard.html", True),
        ("spi_audit_dashboard.html", False)
    ]
    for f, dark in files:
        replace_in_file(f, dark)

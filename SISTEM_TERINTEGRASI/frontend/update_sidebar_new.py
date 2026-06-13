import os
import glob
import re

files = glob.glob('*.html')

logo_header = '''
        <!-- Logo -->
        <div class="p-4 border-b border-slate-800 shrink-0 bg-white">
            <h1 class="text-xl font-black text-slate-800 flex items-center gap-3">
                <img src="logo_kmu.png" alt="Logo KMU" class="h-10 object-contain drop-shadow-sm">
                <div class="flex flex-col">
                    <span class="text-lg leading-none tracking-tight text-emerald-700">KMU</span>
                    <span class="text-[9px] font-bold text-orange-500 uppercase tracking-wider">Kaltim Medika Utama</span>
                </div>
            </h1>
        </div>
'''

sidebar_content = '''
        <div class="flex-1 overflow-y-auto py-6 px-4 space-y-6">
            <!-- 1. INTERNAL PENGADAAN (Operasional Core) -->
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-boxes text-slate-600"></i> Internal Pengadaan
                </div>
                <div class="space-y-1">
                    <a href="fase1_rkap_anggaran.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-file-invoice-dollar w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 1: RKAP & Anggaran</span>
                    </a>
                    <a href="fase2_vendor_database.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-users w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 2: Registrasi Vendor</span>
                    </a>
                    <a href="fase3_imt_pp_sppj.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-clipboard-list w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 3: Permintaan (PP)</span>
                    </a>
                    <a href="fase4_tender.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-gavel w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 4: Tender & Bidding</span>
                    </a>
                    <a href="fase5_kso_portal.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-handshake w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 5: KSO & Kontrak</span>
                    </a>
                    <a href="fase6_bapb_penerimaan.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-box-open w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 6: BAPB & Penerimaan</span>
                    </a>
                    <a href="fase7_invoice_3waymatch.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-file-invoice w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 7: Invoice & Bayar</span>
                    </a>
                    <a href="fase8_raport_vendor.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-star text-amber-400 w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 8: Raport Vendor</span>
                    </a>
                    <a href="fase9_laporan_analitik.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-chart-pie w-5 text-center"></i>
                        <span class="text-sm font-medium">Fase 9: Laporan & Analitik</span>
                    </a>
                </div>
            </div>

            <!-- 2. LINTAS DEPARTEMEN (Beririsan) -->
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-building text-slate-600"></i> Lintas Departemen
                </div>
                <div class="space-y-1">
                    <a href="command_center.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-tv w-5 text-center"></i>
                        <span class="text-sm font-medium">Command Center</span>
                    </a>
                    <a href="finance_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-wallet w-5 text-center"></i>
                        <span class="text-sm font-medium">Finance Dashboard</span>
                    </a>
                    <a href="spi_audit_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-shield-check w-5 text-center"></i>
                        <span class="text-sm font-medium">SPI & Audit Trail</span>
                    </a>
                    <a href="director_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-user-tie w-5 text-center"></i>
                        <span class="text-sm font-medium">Dashboard Direksi</span>
                    </a>
                    <a href="legal_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-balance-scale w-5 text-center"></i>
                        <span class="text-sm font-medium">Legal & Kontrak</span>
                    </a>
                    <a href="ksu_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-handshake w-5 text-center"></i>
                        <span class="text-sm font-medium">KSU (Kerjasama Usaha)</span>
                    </a>
                </div>
            </div>

            <!-- 3. EKSTERNAL (UI Vendor) -->
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-globe text-slate-600"></i> Eksternal
                </div>
                <div class="space-y-1">
                    <a href="vendor_portal.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-store w-5 text-center"></i>
                        <span class="text-sm font-medium">Vendor Portal Umum</span>
                    </a>
                    <a href="vendor_kso_lab_portal.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-flask w-5 text-center"></i>
                        <span class="text-sm font-medium">Portal Vendor KSO</span>
                    </a>
                </div>
            </div>

            <!-- 4. LAPISAN AI (Guardian) -->
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-robot text-slate-600"></i> Lapisan AI
                </div>
                <div class="space-y-1">
                    <a href="ai_guardian_placeholder.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-shield-alt w-5 text-center"></i>
                        <span class="text-sm font-medium">AI Penjaga SOP</span>
                    </a>
                    <a href="admin_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-database w-5 text-center"></i>
                        <span class="text-sm font-medium">Admin & Vendor DB</span>
                    </a>
                </div>
            </div>
        </div>
'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(r'<(aside|div)[^>]*class="[^"]*\bw-64\b[^"]*"[^>]*>', content)
    if not match:
        print(f"Skipping {filepath} (no w-64 sidebar found)")
        return False
    
    sidebar_start_idx = match.start()
    tag_name = match.group(1) # aside or div
    
    idx = sidebar_start_idx
    depth = 0
    tag_pattern = re.compile(f'</?{tag_name}\\b[^>]*>', re.IGNORECASE)
    
    sidebar_end_idx = -1
    for tag_match in tag_pattern.finditer(content[sidebar_start_idx:]):
        tag_str = tag_match.group(0)
        if tag_str.startswith('</'):
            depth -= 1
        else:
            depth += 1
        
        if depth == 0:
            sidebar_end_idx = sidebar_start_idx + tag_match.end()
            break
            
    if sidebar_end_idx == -1:
        print(f"Could not find end tag for sidebar in {filepath}")
        return False
        
    sidebar_outer_html = content[sidebar_start_idx:sidebar_end_idx]
    
    # Identify user footer by looking for border-t
    user_div_start = sidebar_outer_html.rfind('border-t border-slate-800')
    user_footer = ""
    if user_div_start != -1:
        div_start = sidebar_outer_html.rfind('<div', 0, user_div_start)
        if div_start != -1:
            closing_tag_match = re.search(f'</{tag_name}>$', sidebar_outer_html, re.IGNORECASE)
            if closing_tag_match:
                user_footer = sidebar_outer_html[div_start:closing_tag_match.start()]
            else:
                user_footer = sidebar_outer_html[div_start:-len(f'</{tag_name}>')]
                
    if not user_footer.strip():
        user_footer = '''
        <!-- User Profile -->
        <div class="p-4 border-t border-slate-800 bg-[#0F172A]">
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center text-slate-400 border border-slate-700">
                    <i class="fas fa-user"></i>
                </div>
                <div>
                    <p class="text-sm font-bold text-white">Kasim Ganteng</p>
                    <p class="text-[10px] text-slate-500">Kasie Pengadaan Barang</p>
                </div>
            </div>
        </div>
        '''

    # Ensure user_footer ends nicely
    user_footer = user_footer.strip()

    standard_sidebar_start = '<aside class="w-64 bg-[#0F172A] border-r border-slate-800 flex flex-col z-20 shrink-0 h-full relative">'
    standard_sidebar_end = '</aside>'
    
    new_sidebar = standard_sidebar_start + '\n' + logo_header + '\n' + sidebar_content + '\n' + user_footer + '\n' + standard_sidebar_end
    
    # Replace active link class
    active_class = 'bg-emerald-600 text-white shadow-md shadow-emerald-900/20'
    inactive_class = 'text-slate-400 hover:text-white hover:bg-slate-800 transition-colors'
    filename = os.path.basename(filepath)
    
    target_link = f'href="{filename}" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {inactive_class}"'
    replacement_link = f'href="{filename}" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {active_class}"'
    new_sidebar = new_sidebar.replace(target_link, replacement_link)
    
    new_content = content[:sidebar_start_idx] + new_sidebar + content[sidebar_end_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filepath}")
    return True

# Exceptions for files that shouldn't have the main sidebar
skip_files = ['vendor_registration.html'] # vendor portal and lab portal MIGHT have it, but maybe different structure

success_count = 0
for filepath in files:
    if filepath in skip_files:
        continue
    if process_file(filepath):
        success_count += 1
        
print(f"Done! Successfully updated {success_count} files.")

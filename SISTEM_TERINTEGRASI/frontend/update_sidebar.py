import os
import glob
import re

files = glob.glob('*.html')

# Define the correct, unified sidebar content with Kasim Ganteng
sidebar_content = '''<div class="flex-1 overflow-y-auto py-6 px-4 space-y-6">
            <!-- FASE 1 & E-KATALOG -->
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-book text-slate-600"></i> Fase 1: Perencanaan
                </div>
                <div class="space-y-1">
                    <a href="catalogue_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-book-open w-5 text-center"></i>
                        <span class="text-sm font-medium">E-Katalog Investasi</span>
                    </a>
                </div>
            </div>

            <!-- FASE 4 -->
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-layer-group text-slate-600"></i> Fase 4: Pelaksanaan
                </div>
                <div class="space-y-1">
                    <a href="approval_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-check-double w-5 text-center"></i>
                        <span class="text-sm font-medium">Approval Matrix</span>
                    </a>
                    <a href="fase4_tender.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-file-contract w-5 text-center"></i>
                        <span class="text-sm font-medium">Manajemen Tender</span>
                    </a>
                    <a href="swakelola_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-tools w-5 text-center"></i>
                        <span class="text-sm font-medium">Proyek Swakelola</span>
                    </a>
                </div>
            </div>

            <!-- FASE 8 & KEUANGAN -->
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-star text-slate-600"></i> Fase 8: Evaluasi & Realisasi
                </div>
                <div class="space-y-1">
                    <a href="fase8_raport_vendor.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-chart-bar w-5 text-center"></i>
                        <span class="text-sm font-medium">Raport Vendor</span>
                    </a>
                    <a href="kso_evaluasi_wasit.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-balance-scale-right w-5 text-center"></i>
                        <span class="text-sm font-medium">Wasit Deviasi KSO</span>
                        <span class="ml-auto bg-red-500/20 text-red-500 text-[10px] font-bold px-2 py-0.5 rounded-full border border-red-500/30">!</span>
                    </a>
                    <a href="kso_management_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-microscope w-5 text-center"></i>
                        <span class="text-sm font-medium">Pengelolaan KSO (Ops)</span>
                    </a>
                </div>
            </div>

            <!-- LAPISAN AI -->
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-robot text-slate-600"></i> Lapisan AI
                </div>
                <div class="space-y-1">
                    <a href="ai_guardian_placeholder.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-shield-alt w-5 text-center"></i>
                        <span class="text-sm font-medium">SOP Guardian</span>
                    </a>
                </div>
            </div>

            <!-- COMMAND CENTER -->
            <div class="px-3">
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-2 px-3 flex items-center gap-2">
                    Command Center
                </div>
                <div class="space-y-1">
                    <a href="command_center.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="KPI Dashboard">
                        <i class="fas fa-tv w-6 text-center"></i>
                        <span class="text-sm font-medium">KPI Dashboard</span>
                    </a>
                </div>
            </div>

            <!-- LINTAS DEPARTEMEN -->
            <div class="px-3 mt-4">
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-2 px-3 flex items-center gap-2">
                    Lintas Departemen
                </div>
                <div class="space-y-1">
                    <a href="finance_dashboard.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="Keuangan (Finance)">
                        <i class="fas fa-wallet w-6 text-center"></i>
                        <span class="text-sm font-medium">Keuangan (Finance)</span>
                    </a>
                    <a href="spi_audit_dashboard.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="SPI & Audit">
                        <i class="fas fa-shield-alt w-6 text-center"></i>
                        <span class="text-sm font-medium">SPI & Audit</span>
                    </a>
                    <a href="legal_dashboard.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="Legal & Kontrak">
                        <i class="fas fa-balance-scale w-6 text-center"></i>
                        <span class="text-sm font-medium">Legal & Kontrak</span>
                    </a>
                    <a href="ksu_dashboard.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="KSU / Kerjasama Usaha">
                        <i class="fas fa-handshake w-6 text-center"></i>
                        <span class="text-sm font-medium">KSU (Kerjasama Usaha)</span>
                    </a>
                    <a href="director_dashboard.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="Direksi (BOD)">
                        <i class="fas fa-chart-line w-6 text-center"></i>
                        <span class="text-sm font-medium">Direksi (BOD)</span>
                    </a>
                    <a href="umum_dashboard.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="Bagian Umum (GA)">
                        <i class="fas fa-building w-6 text-center"></i>
                        <span class="text-sm font-medium">Bagian Umum (GA)</span>
                    </a>
                </div>
            </div>
            
            <!-- VENDOR (EXTERNAL) -->
            <div class="px-3 mt-4 mb-4">
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-2 px-3 flex items-center gap-2">
                    Eksternal
                </div>
                <div class="space-y-1">
                    <a href="vendor_portal.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="Vendor Portal">
                        <i class="fas fa-store w-6 text-center"></i>
                        <span class="text-sm font-medium">Vendor Portal Umum</span>
                    </a>
                    <a href="vendor_kso_lab_portal.html" class="flex items-center gap-3 px-3 py-2 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors" title="Portal KSO Lab">
                        <i class="fas fa-flask w-6 text-center text-teal-400"></i>
                        <span class="text-sm font-medium">Portal KSO Lab</span>
                    </a>
                </div>
            </div>
        </div>'''

sidebar_wrapper_start = '<aside class="w-64 bg-[#0F172A] border-r border-slate-800 flex flex-col z-20 shrink-0 h-full relative">'
sidebar_wrapper_end = '</aside>'

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

full_sidebar = sidebar_wrapper_start + logo_header + sidebar_content + user_footer + sidebar_wrapper_end

for fname in files:
    # Skip files that don't need a sidebar
    if fname in ['vendor_portal.html', 'vendor_kso_lab_portal.html', 'vendor_registration.html', 'requisition_form.html', 'admin_dashboard.html', 'kso_evaluation.html', 'command_center.html', 'arm_portal.html']:
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(
        r'<(aside|div) class="w-64 bg-\[#(0F172A|0B1120)\].*?(Budi Santoso|Kasim Ganteng).*?</\1>',
        re.DOTALL
    )

    if pattern.search(content):
        new_content = pattern.sub(full_sidebar, content)
    else:
        fallback_pattern = re.compile(
            r'<aside class="w-64 bg-\[#0F172A\].*?(Admin Pengadaan|Kasie Pengadaan Barang).*?</div>\s*</div>\s*</div>\s*(</aside||</div>)',
            re.DOTALL
        )
        if fallback_pattern.search(content):
            new_content = fallback_pattern.sub(full_sidebar, content)
        else:
            continue

    # Apply active state to specific files
    active_class = 'bg-emerald-600 text-white shadow-md shadow-emerald-900/20'
    inactive_class = 'text-slate-400 hover:text-white hover:bg-slate-800 transition-colors'
    
    target_link = f'href="{fname}" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {inactive_class}"'
    replacement_link = f'href="{fname}" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {active_class}"'
    target_link2 = f'href="{fname}" class="flex items-center gap-3 px-3 py-2 rounded-lg {inactive_class}"'
    replacement_link2 = f'href="{fname}" class="flex items-center gap-3 px-3 py-2 rounded-lg {active_class}'

    if fname == 'finance_dashboard.html':
        active_finance = 'bg-emerald-600 text-white shadow-md shadow-emerald-950/20'
        target_fin = f'href="finance_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {inactive_class}"'
        rep_fin = f'href="finance_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {active_finance}"'
        new_content = new_content.replace(target_fin, rep_fin)
    else:
        new_content = new_content.replace(target_link, replacement_link).replace(target_link2, replacement_link2)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("update_sidebar.py successfully replaced and unified sidebars.")

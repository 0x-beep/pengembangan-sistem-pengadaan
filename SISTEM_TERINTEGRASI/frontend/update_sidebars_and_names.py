import os
import glob
import re

files = glob.glob('*.html')

# 1. Define the correct, unified sidebar content with Kasim Ganteng
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
                    <a href="finance_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-wallet w-5 text-center"></i>
                        <span class="text-sm font-medium">Keuangan (Finance)</span>
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
                        <span class="text-sm font-medium">Vendor Portal</span>
                    </a>
                </div>
            </div>
        </div>'''

sidebar_wrapper_start = '<aside class="w-64 bg-[#0F172A] border-r border-slate-800 flex flex-col z-20 shrink-0 h-full relative">'
sidebar_wrapper_end = '</aside>'

logo_header = '''
        <!-- Logo -->
        <div class="p-6 border-b border-slate-800 shrink-0">
            <h1 class="text-xl font-black text-white flex items-center gap-2">
                <i class="fas fa-hospital text-blue-500"></i>
                <span class="bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400">KMU</span>
                <span class="text-xs font-medium bg-blue-600 text-white px-2 py-0.5 rounded ml-1">v2.0</span>
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
    if fname in ['vendor_portal.html', 'vendor_registration.html', 'requisition_form.html', 'admin_dashboard.html', 'kso_evaluation.html', 'command_center.html', 'arm_portal.html']:
        continue

    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 2. Cleanup double sidebars or mismatched sidebars
    # We will search from the start of <aside or <div class="w-64 bg-[#0B1120] text-slate-300 flex flex-col shrink-0 h-full border-r border-slate-800 z-10">
    # and match anything up to the end of Budi Santoso user footer or Kasim Ganteng user footer
    pattern = re.compile(
        r'<(aside|div) class="w-64 bg-\[#(0F172A|0B1120)\].*?(Budi Santoso|Kasim Ganteng).*?</\1>',
        re.DOTALL
    )

    if pattern.search(content):
        # We replace the entire matched block (which includes any duplicate sidebar segments trapped inside the matched tags)
        new_content = pattern.sub(full_sidebar, content)
    else:
        # If the regex doesn't match because it got cut off, let's find the start of the injected sidebar
        # and delete everything until the end of the dangling old sidebar.
        # Let's fallback to replacing from '<aside class="w-64 bg-[#0F172A]' to the end of 'Admin Pengadaan' or 'Kasie Pengadaan Barang' segment.
        fallback_pattern = re.compile(
            r'<aside class="w-64 bg-\[#0F172A\].*?(Admin Pengadaan|Kasie Pengadaan Barang).*?</div>\s*</div>\s*</div>\s*(</aside>|</div>)',
            re.DOTALL
        )
        if fallback_pattern.search(content):
            new_content = fallback_pattern.sub(full_sidebar, content)
        else:
            print(f"Could not automatically clean {fname}. Skipping.")
            continue

    # Apply active state to specific files
    active_class = 'bg-blue-600 text-white shadow-md shadow-blue-900/20'
    inactive_class = 'text-slate-400 hover:text-white hover:bg-slate-800 transition-colors'
    
    target_link = f'href="{fname}" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {inactive_class}"'
    replacement_link = f'href="{fname}" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {active_class}"'
    target_link2 = f'href="{fname}" class="flex items-center gap-3 px-3 py-2 rounded-lg {inactive_class}"'
    replacement_link2 = f'href="{fname}" class="flex items-center gap-3 px-3 py-2 rounded-lg {active_class}'

    # Custom handling for finance_dashboard which uses emerald highlight
    if fname == 'finance_dashboard.html':
        active_finance = 'bg-emerald-600 text-white shadow-md shadow-emerald-950/20'
        target_fin = f'href="finance_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {inactive_class}"'
        rep_fin = f'href="finance_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg {active_finance}"'
        new_content = new_content.replace(target_fin, rep_fin)
    else:
        new_content = new_content.replace(target_link, replacement_link).replace(target_link2, replacement_link2)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Repaired and updated sidebar in: {fname}")

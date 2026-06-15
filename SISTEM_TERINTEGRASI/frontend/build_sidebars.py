import os
import glob
import re

# ==========================================
# 1. SIDEBAR HTML TEMPLATES
# ==========================================

sidebar_internal = """
    <!-- Sidebar Internal Holding -->
    <aside class="w-64 bg-[#0F172A] border-r border-slate-800 flex flex-col z-20 shrink-0 h-full relative">
        <a href="portal_hub.html" class="p-4 border-b border-slate-800 shrink-0 bg-white flex items-center gap-3 hover:bg-slate-50 transition group">
            <img src="logo_kmu.png" alt="Logo KMU" class="h-10 object-contain drop-shadow-sm">
            <div class="flex flex-col">
                <span class="text-lg leading-none tracking-tight text-emerald-700 font-black">KMU</span>
                <span class="text-[9px] font-bold text-orange-500 uppercase tracking-wider">Holding Internal</span>
            </div>
            <i class="fas fa-home text-slate-300 group-hover:text-slate-500 text-xs ml-auto transition"></i>
        </a>
        <div class="flex-1 overflow-y-auto py-6 px-4 space-y-6">
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-building text-slate-600"></i> Portal Internal
                </div>
                <div class="space-y-1">
                    <a href="director_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-user-tie w-5 text-center"></i><span class="text-sm font-medium">Dashboard Direksi</span>
                    </a>
                    <a href="command_center.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-tv w-5 text-center"></i><span class="text-sm font-medium">Command Center</span>
                    </a>
                    <a href="finance_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-wallet w-5 text-center"></i><span class="text-sm font-medium">Finance & Pembayaran</span>
                    </a>
                    <a href="spi_audit_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-shield-halved w-5 text-center"></i><span class="text-sm font-medium">SPI & Audit</span>
                    </a>
                    <a href="legal_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-scale-balanced w-5 text-center"></i><span class="text-sm font-medium">Legal & Kontrak</span>
                    </a>
                    <a href="ksu_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-handshake w-5 text-center"></i><span class="text-sm font-medium">KSU (Kerjasama Usaha)</span>
                    </a>
                    <a href="umum_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-box w-5 text-center"></i><span class="text-sm font-medium">Bagian Umum (IMT -> PP)</span>
                    </a>
                </div>
            </div>
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-robot text-slate-600"></i> Lapisan AI
                </div>
                <div class="space-y-1">
                    <a href="ai_guardian.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-shield-alt w-5 text-center"></i><span class="text-sm font-medium">AI Penjaga SOP</span>
                    </a>
                </div>
            </div>
        </div>
    </aside>
"""

sidebar_pengadaan = """
    <!-- Sidebar Portal Pengadaan -->
    <aside class="w-64 bg-[#0F172A] border-r border-slate-800 flex flex-col z-20 shrink-0 h-full relative">
        <a href="portal_hub.html" class="p-4 border-b border-slate-800 shrink-0 bg-white flex items-center gap-3 hover:bg-slate-50 transition group">
            <img src="logo_kmu.png" alt="Logo KMU" class="h-10 object-contain drop-shadow-sm">
            <div class="flex flex-col">
                <span class="text-lg leading-none tracking-tight text-emerald-700 font-black">KMU</span>
                <span class="text-[9px] font-bold text-blue-500 uppercase tracking-wider">Portal Pengadaan</span>
            </div>
            <i class="fas fa-home text-slate-300 group-hover:text-slate-500 text-xs ml-auto transition"></i>
        </a>
        <div class="flex-1 overflow-y-auto py-6 px-4 space-y-6">
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-tasks text-slate-600"></i> Meja Kerja
                </div>
                <div class="space-y-1">
                    <a href="pengadaan_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-desktop w-5 text-center"></i><span class="text-sm font-medium">Papan Kanban</span>
                    </a>
                    <a href="approval_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-inbox w-5 text-center relative"><span class="absolute -top-1 -right-1 w-2 h-2 bg-red-500 rounded-full"></span></i><span class="text-sm font-medium">Inbox Approval</span>
                    </a>
                    <a href="catalogue_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-bookmark w-5 text-center"></i><span class="text-sm font-medium">E-Katalog Internal</span>
                    </a>
                    <a href="swakelola_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-tools w-5 text-center"></i><span class="text-sm font-medium">Swakelola & Jasa</span>
                    </a>
                </div>
            </div>
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-boxes text-slate-600"></i> Siklus Pengadaan
                </div>
                <div class="space-y-1">
                    <a href="fase1_rkap_anggaran.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-file-invoice-dollar w-5 text-center"></i><span class="text-sm font-medium">1. RKAP & Anggaran</span>
                    </a>
                    <a href="fase2_vendor_database.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-users w-5 text-center"></i><span class="text-sm font-medium">2. Registrasi Vendor</span>
                    </a>
                    <a href="fase3_imt_pp_sppj.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-clipboard-list w-5 text-center"></i><span class="text-sm font-medium">3. PP Final</span>
                    </a>
                    <a href="fase4_tender.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-gavel w-5 text-center"></i><span class="text-sm font-medium">4. Tender & Bidding</span>
                    </a>
                    <a href="fase5_kso_portal.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-handshake w-5 text-center"></i><span class="text-sm font-medium">5. KSO & Kontrak</span>
                    </a>
                    <a href="fase6_bapb_penerimaan.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-box-open w-5 text-center"></i><span class="text-sm font-medium">6. BAPB & Penerimaan</span>
                    </a>
                    <a href="fase7_invoice_3waymatch.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-file-invoice w-5 text-center"></i><span class="text-sm font-medium">7. Invoice & Bayar</span>
                    </a>
                    <a href="fase8_raport_vendor.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-star w-5 text-center"></i><span class="text-sm font-medium">8. Raport Vendor</span>
                    </a>
                    <a href="fase9_laporan_analitik.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-chart-pie w-5 text-center"></i><span class="text-sm font-medium">9. Laporan & Analitik</span>
                    </a>
                    <a href="vendor_blacklist.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-rose-400 hover:text-white hover:bg-rose-900 transition-colors">
                        <i class="fas fa-ban w-5 text-center"></i><span class="text-sm font-medium">Daftar Blacklist</span>
                    </a>
                </div>
            </div>
        </div>
    </aside>
"""

sidebar_sbu = """
    <!-- Sidebar Portal Unit Bisnis (SBU) -->
    <aside class="w-64 bg-[#0F172A] border-r border-slate-800 flex flex-col z-20 shrink-0 h-full relative">
        <a href="portal_hub.html" class="p-4 border-b border-slate-800 shrink-0 bg-white flex items-center gap-3 hover:bg-slate-50 transition group">
            <img src="logo_kmu.png" alt="Logo KMU" class="h-10 object-contain drop-shadow-sm">
            <div class="flex flex-col">
                <span class="text-lg leading-none tracking-tight text-emerald-700 font-black">KMU</span>
                <span class="text-[9px] font-bold text-emerald-500 uppercase tracking-wider">Unit Bisnis / SBU</span>
            </div>
            <i class="fas fa-home text-slate-300 group-hover:text-slate-500 text-xs ml-auto transition"></i>
        </a>
        <div class="flex-1 overflow-y-auto py-6 px-4 space-y-6">
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-clinic-medical text-slate-600"></i> Operasional Unit
                </div>
                <div class="space-y-1">
                    <a href="rs_klinik_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-desktop w-5 text-center"></i><span class="text-sm font-medium">Beranda SBU</span>
                    </a>
                    <a href="requisition_form.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-file-signature w-5 text-center"></i><span class="text-sm font-medium">Buat IMT Baru</span>
                    </a>
                    <a href="proker_bulanan.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-calendar-check w-5 text-center"></i><span class="text-sm font-medium">Proker & Realisasi</span>
                    </a>
                    <a href="catalogue_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-bookmark w-5 text-center"></i><span class="text-sm font-medium">Katalog Terpadu</span>
                    </a>
                    <a href="kso_management_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-microscope w-5 text-center"></i><span class="text-sm font-medium">Monitoring KSO</span>
                    </a>
                </div>
            </div>
        </div>
    </aside>
"""

sidebar_vendor = """
    <!-- Sidebar Portal Vendor -->
    <aside class="w-64 bg-[#0F172A] border-r border-slate-800 flex flex-col z-20 shrink-0 h-full relative">
        <a href="portal_hub.html" class="p-4 border-b border-slate-800 shrink-0 bg-white flex items-center gap-3 hover:bg-slate-50 transition group">
            <img src="logo_kmu.png" alt="Logo KMU" class="h-10 object-contain drop-shadow-sm">
            <div class="flex flex-col">
                <span class="text-lg leading-none tracking-tight text-emerald-700 font-black">KMU</span>
                <span class="text-[9px] font-bold text-amber-500 uppercase tracking-wider">Vendor B2B</span>
            </div>
            <i class="fas fa-sign-out-alt text-slate-300 group-hover:text-slate-500 text-xs ml-auto transition"></i>
        </a>
        <div class="flex-1 overflow-y-auto py-6 px-4 space-y-6">
            <div>
                <div class="text-[10px] font-bold text-slate-500 uppercase tracking-widest mb-3 px-2 flex items-center gap-2">
                    <i class="fas fa-store text-slate-600"></i> Workspace Vendor
                </div>
                <div class="space-y-1">
                    <a href="vendor_hub.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-door-open w-5 text-center"></i><span class="text-sm font-medium">Vendor Hub (Login)</span>
                    </a>
                    <a href="vendor_portal.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-store w-5 text-center"></i><span class="text-sm font-medium">Vendor Portal Umum</span>
                    </a>
                    <a href="vendor_kso_lab_portal.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-flask w-5 text-center"></i><span class="text-sm font-medium">Portal KSO Lab</span>
                    </a>
                    <a href="vendor_kso_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-handshake w-5 text-center"></i><span class="text-sm font-medium">Monitoring KSO</span>
                    </a>
                    <a href="vendor_registration.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
                        <i class="fas fa-id-card w-5 text-center"></i><span class="text-sm font-medium">Registrasi Mandiri</span>
                    </a>
                </div>
            </div>
        </div>
    </aside>
"""

# ==========================================
# 2. FILE MAPPING
# ==========================================

internal_files = [
    'director_dashboard.html',
    'command_center.html',
    'finance_dashboard.html',
    'finance_simulation.html',
    'spi_audit_dashboard.html',
    'legal_dashboard.html',
    'ksu_dashboard.html',
    'umum_dashboard.html'
]

pengadaan_files = [
    'pengadaan_dashboard.html',
    'fase1_rkap_anggaran.html',
    'fase2_vendor_database.html',
    'fase3_imt_pp_sppj.html',
    'fase4_tender.html',
    'fase5_kso_portal.html',
    'fase6_bapb_penerimaan.html',
    'fase7_invoice_3waymatch.html',
    'fase8_raport_vendor.html',
    'fase9_laporan_analitik.html',
    'catalogue_dashboard.html',
    'e_katalog_internal.html',
    'swakelola_dashboard.html',
    'approval_dashboard.html',
    'vendor_blacklist.html'
]

sbu_files = [
    'rs_klinik_dashboard.html',
    'proker_bulanan.html',
    'requisition_form.html',
    'kso_management_dashboard.html'
]

vendor_files = [
    'vendor_hub.html',
    'vendor_portal.html',
    'vendor_registration.html',
    'vendor_kso_lab_portal.html',
    'vendor_kso_dashboard.html'
]

# ==========================================
# 3. REPLACEMENT SCRIPT
# ==========================================

def get_sidebar_for_file(filename):
    if filename in internal_files: return sidebar_internal
    if filename in pengadaan_files: return sidebar_pengadaan
    if filename in sbu_files: return sidebar_sbu
    if filename in vendor_files: return sidebar_vendor
    return None

# Helper to find and highlight the active link in the sidebar
def highlight_active_link(sidebar_html, filename):
    # Regex to find the <a href="filename" ...> and add a special bg color depending on the portal
    # Portal Pengadaan: bg-blue-600 text-white
    # Portal Internal: bg-emerald-600 text-white
    # Portal SBU: bg-emerald-600 text-white
    # Portal Vendor: bg-amber-600 text-white
    
    # Let's just make it generic bg-slate-700 text-white border-l-4 border-blue-500
    pattern = r'(<a href="' + re.escape(filename) + r'" class=".*?)(text-slate-400 hover:text-white hover:bg-slate-800)(.*?>)'
    active_class = 'bg-slate-800 text-white border-l-4 border-blue-500'
    
    # For vendor, maybe amber
    if filename in vendor_files: active_class = 'bg-slate-800 text-white border-l-4 border-amber-500'
    if filename in internal_files: active_class = 'bg-slate-800 text-white border-l-4 border-emerald-500'
    if filename in sbu_files: active_class = 'bg-slate-800 text-white border-l-4 border-emerald-500'
    if filename in pengadaan_files: active_class = 'bg-slate-800 text-white border-l-4 border-blue-500'

    # If it matches, replace
    res = re.sub(pattern, r'\1' + active_class + r'\3', sidebar_html)
    return res

for filepath in glob.glob('*.html'):
    filename = os.path.basename(filepath)
    sidebar_template = get_sidebar_for_file(filename)
    
    if not sidebar_template:
        continue # Skip files like portal_hub.html
        
    sidebar_html = highlight_active_link(sidebar_template, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace the existing <aside ...> ... </aside>
    # Note: re.DOTALL is needed to match across newlines
    new_html = re.sub(r'<aside.*?</aside>', sidebar_html, html, flags=re.DOTALL)
    
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated sidebar for {filename}")
    else:
        print(f"No <aside> found or replacement failed for {filename}")

print("All sidebars updated successfully!")

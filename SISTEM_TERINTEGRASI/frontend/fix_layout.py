import os
import re

files_to_fix = [
    'approval_dashboard.html',
    'fase4_tender.html',
    'fase8_raport_vendor.html',
    'kso_evaluasi_wasit.html',
    'ai_guardian_placeholder.html'
]

for fname in files_to_fix:
    if not os.path.exists(fname):
        print(f"File not found: {fname}")
        continue
        
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
        
    pattern = re.compile(r'</aside>.*?<!-- Main Content -->', re.DOTALL)
    new_content = pattern.sub('</aside>\n\n    <!-- Main Content -->', content)
    
    if fname == 'approval_dashboard.html':
        new_header = '''<header class="bg-white border-b border-slate-200 px-8 py-5 shrink-0 shadow-sm flex items-center justify-between">
            <div>
                <h2 class="text-xl font-bold text-slate-800">Daftar Antrean Persetujuan (Approval Matrix)</h2>
                <p class="text-xs text-slate-500 mt-1">Fase 4: Pelaksanaan Pengadaan & Persetujuan Dokumen</p>
            </div>
            <div class="flex items-center gap-3">
                <label class="text-xs font-bold text-slate-500">Simulasi Role (Testing):</label>
                <select id="roleSelector" onchange="loadRequisitions()" class="border border-slate-300 rounded px-3 py-1.5 text-sm font-medium focus:border-blue-500 focus:outline-none">
                    <option value="kasie">Kasie Pengadaan</option>
                    <option value="manager" selected>Manager Pengadaan</option>
                    <option value="gm">General Manager (GM)</option>
                    <option value="dir_ops">Direktur Ops & Bang</option>
                    <option value="dir_utama">Direktur Utama</option>
                </select>
            </div>
        </header>'''
        new_content = re.sub(r'<header class="bg-white border-b border-slate-200 px-8 py-5 shrink-0 shadow-sm">\s*<h2 class="text-xl font-bold text-slate-800">Daftar Antrean Persetujuan \(Approval Matrix\)</h2>\s*<p class="text-xs text-slate-500 mt-1">Fase 4: Pelaksanaan Pengadaan & Persetujuan Dokumen</p>\s*</header>', new_header, new_content)
        
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Done cleaning files.")

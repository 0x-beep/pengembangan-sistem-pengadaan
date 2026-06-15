import re
with open('portal_hub.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_link = """
                <a href="manager_pengadaan_dashboard.html" class="block p-4 rounded-xl border border-slate-700 bg-slate-800/50 hover:bg-slate-700/80 transition group relative overflow-hidden">
                    <div class="absolute top-0 right-0 p-3 opacity-10 group-hover:opacity-20 transition">
                        <i class="fas fa-desktop text-4xl text-blue-400"></i>
                    </div>
                    <h3 class="text-blue-400 font-bold mb-1 flex items-center gap-2"><i class="fas fa-desktop"></i> Dashboard Manajer</h3>
                    <p class="text-xs text-slate-400">Kanban monitoring untuk Kasie Barang & Jasa</p>
                </a>
"""

if "manager_pengadaan_dashboard.html" not in html:
    html = html.replace('<!-- LINTAS DEPARTEMEN -->', '<!-- LINTAS DEPARTEMEN -->\\n' + new_link)
    with open('portal_hub.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Portal hub updated')

import re

def modify_html(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return

    # 1. Add new Tab Button
    tab_btn_pattern = r'(<button onclick="switchTab\(\'rencana\'\).*?>.*?</button>)'
    new_tab_btn = r"""\1
            <button onclick="switchTab('pemilihan')" id="tab-btn-pemilihan" class="tab-link border-b-2 border-transparent px-4 py-2 text-sm font-semibold text-slate-500 hover:text-slate-800 transition-colors">
                <i class="fas fa-check-double mr-1.5"></i> Proses Pemilihan Vendor
            </button>"""
    content = re.sub(tab_btn_pattern, new_tab_btn, content, count=1, flags=re.DOTALL)

    # 2. Add new Tab Content for "Proses Pemilihan"
    # We'll insert it right after the end of `<div id="view-keuangan"...</div>`
    tab_content_pattern = r'(<div id="view-keuangan" class="tab-content.*?</div>\s*</div>\s*</div>)'
    new_tab_content = r"""\1

            <!-- TAB 4: PROSES PEMILIHAN -->
            <div id="view-pemilihan" class="tab-content max-w-7xl mx-auto hidden h-full flex gap-6">
                <!-- Left: List of Kebutuhan -->
                <div class="w-1/3 bg-white border border-slate-200 rounded-xl flex flex-col shadow-sm max-h-[70vh]">
                    <div class="p-4 border-b border-slate-200 bg-slate-50 rounded-t-xl">
                        <h3 class="font-bold text-slate-800"><i class="fas fa-list text-blue-600 mr-2"></i>Daftar Kebutuhan (RKAP)</h3>
                    </div>
                    <div id="pemilihan-list" class="flex-1 overflow-y-auto p-2 space-y-2">
                        <!-- Loaded via JS -->
                    </div>
                </div>

                <!-- Right: Vendor Selection -->
                <div class="w-2/3 bg-white border border-slate-200 rounded-xl flex flex-col shadow-sm max-h-[70vh]">
                    <div class="p-4 border-b border-slate-200 bg-slate-50 rounded-t-xl flex justify-between items-center">
                        <h3 class="font-bold text-slate-800"><i class="fas fa-store text-emerald-600 mr-2"></i>Penawaran Vendor</h3>
                        <span id="selected-item-title" class="text-xs font-bold bg-blue-100 text-blue-800 px-3 py-1 rounded-full">Pilih item di kiri</span>
                    </div>
                    <div id="pemilihan-vendors" class="flex-1 overflow-y-auto p-6 bg-slate-50/50">
                        <div class="flex flex-col items-center justify-center h-full text-slate-400">
                            <i class="fas fa-mouse-pointer text-4xl mb-3"></i>
                            <p>Silakan klik salah satu item kebutuhan untuk melihat daftar vendor yang menawarkan.</p>
                        </div>
                    </div>
                </div>
            </div>"""
    content = re.sub(tab_content_pattern, new_tab_content, content, count=1, flags=re.DOTALL)

    # 3. Replace fetchRealCatalogs JS
    js_pattern = r'async function fetchRealCatalogs\(\) \{.*?(?=window\.addEventListener)'
    new_js = """let globalCatalogGroups = {};

        function renderPemilihanVendors(itemName) {
            const container = document.getElementById('pemilihan-vendors');
            document.getElementById('selected-item-title').textContent = itemName;
            
            const vendors = globalCatalogGroups[itemName] || [];
            if (vendors.length === 0) {
                container.innerHTML = '<p class="text-center text-slate-500 mt-10">Tidak ada vendor yang menawarkan item ini.</p>';
                return;
            }

            // Sort by price ascending
            vendors.sort((a, b) => a.price - b.price);

            container.innerHTML = `<div class="grid grid-cols-1 gap-4">
                ${vendors.map((v, idx) => `
                    <div class="bg-white border ${idx === 0 ? 'border-emerald-400 shadow-md ring-1 ring-emerald-400' : 'border-slate-200 shadow-sm'} rounded-xl p-4 flex justify-between items-center transition hover:border-blue-400">
                        <div class="flex gap-4 items-center">
                            <div class="w-12 h-12 rounded-full ${idx === 0 ? 'bg-emerald-100 text-emerald-600' : 'bg-slate-100 text-slate-500'} flex items-center justify-center text-xl shrink-0">
                                <i class="fas ${idx === 0 ? 'fa-trophy' : 'fa-store'}"></i>
                            </div>
                            <div>
                                <h4 class="font-bold text-slate-800 text-base">${v.vendor_name}</h4>
                                <p class="text-xs text-slate-500 mt-0.5"><i class="fas fa-tag mr-1"></i> Merk: ${v.brand || '-'}</p>
                            </div>
                        </div>
                        <div class="text-right flex flex-col items-end gap-2">
                            <span class="text-lg font-black text-slate-800">${fmtRp(v.price)}</span>
                            <button onclick="alert('Vendor ${v.vendor_name} terpilih untuk ${itemName}!')" class="text-xs font-bold px-4 py-1.5 rounded-lg ${idx === 0 ? 'bg-emerald-600 hover:bg-emerald-700 text-white' : 'bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-300'} transition shadow-sm">
                                <i class="fas fa-check mr-1"></i> Pilih Vendor
                            </button>
                        </div>
                    </div>
                `).join('')}
            </div>`;
        }

        async function fetchRealCatalogs() {
            try {
                const res = await fetch('http://127.0.0.1:8000/api/catalogs');
                const json = await res.json();
                const grid = document.getElementById('catalogGrid');
                const pemList = document.getElementById('pemilihan-list');
                
                if (!grid || !pemList) return;
                grid.innerHTML = '';
                pemList.innerHTML = '';
                globalCatalogGroups = {};
                
                if (json.data && json.data.length > 0) {
                    // Group by item_name
                    json.data.forEach(item => {
                        if(!globalCatalogGroups[item.item_name]) {
                            globalCatalogGroups[item.item_name] = [];
                        }
                        globalCatalogGroups[item.item_name].push(item);
                    });

                    // Render Tab 1 (Katalog Umum tanpa Harga/Vendor)
                    Object.keys(globalCatalogGroups).forEach(itemName => {
                        // Mock quantity requirement based on name hash just for UI
                        const reqQty = (itemName.length % 5) + 2; 
                        const vendorsCount = globalCatalogGroups[itemName].length;
                        
                        grid.innerHTML += `
                        <div class="glass-card rounded-2xl shadow-sm hover:shadow-md transition-shadow overflow-hidden flex flex-col group border border-slate-200">
                            <div class="h-1 bg-gradient-to-r from-blue-400 to-blue-600"></div>
                            <div class="p-5 flex-1 flex flex-col">
                                <div class="flex justify-between items-start mb-3">
                                    <span class="bg-blue-100 text-blue-700 text-[10px] font-bold px-2 py-1 rounded border border-blue-200 uppercase tracking-wide truncate max-w-[60%]"><i class="fas fa-clipboard-list mr-1"></i> Terdaftar di RKAP</span>
                                    <span class="bg-slate-100 text-slate-600 text-[10px] font-bold px-2 py-1 rounded-full border border-slate-200"><i class="fas fa-users mr-1"></i> ${vendorsCount} Penawar</span>
                                </div>
                                <h3 class="font-bold text-slate-800 text-lg leading-tight group-hover:text-blue-600 transition-colors mb-2">${itemName}</h3>
                                
                                <div class="mt-auto space-y-2 text-xs font-medium text-slate-600 bg-slate-50 p-3 rounded-lg border border-slate-100">
                                    <div class="flex justify-between items-center">
                                        <span class="text-slate-500">Jumlah Kebutuhan:</span> 
                                        <span class="font-bold text-lg text-emerald-600">${reqQty} <span class="text-xs text-emerald-600/70">Unit</span></span>
                                    </div>
                                </div>
                            </div>
                        </div>`;

                        // Render Tab Pemilihan (List Kiri)
                        pemList.innerHTML += `
                        <button onclick="renderPemilihanVendors('${itemName}')" class="w-full text-left p-3 rounded-lg border border-slate-200 bg-white hover:bg-blue-50 hover:border-blue-300 transition group flex flex-col gap-1 focus:bg-blue-50 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none">
                            <h4 class="font-bold text-slate-700 text-sm group-hover:text-blue-700 leading-tight">${itemName}</h4>
                            <div class="flex justify-between text-[10px]">
                                <span class="text-emerald-600 font-bold">${reqQty} Unit Needed</span>
                                <span class="text-slate-500">${vendorsCount} Vendor Input</span>
                            </div>
                        </button>`;
                    });
                } else {
                    grid.innerHTML = '<p class="col-span-3 text-center text-slate-500">Tidak ada data kebutuhan RKAP.</p>';
                    pemList.innerHTML = '<p class="text-center p-4 text-slate-500 text-xs">Belum ada data.</p>';
                }
            } catch (e) {
                console.error(e);
            }
        }

        """
    content = re.sub(js_pattern, new_js, content, count=1, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath} successfully")

modify_html('catalogue_dashboard.html')

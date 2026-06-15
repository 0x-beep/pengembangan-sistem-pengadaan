import re
import os

html_path = r"d:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend\fase1_rkap_anggaran.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add ID to KPI stats
content = content.replace('<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">', '<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8" id="kpi-container">')

# Add ID to SBU tbody and tfoot
content = re.sub(r'<tbody class="divide-y divide-gray-100 text-sm">.*?</tbody\>', '<tbody id="sbu-tbody" class="divide-y divide-gray-100 text-sm"></tbody>', content, flags=re.DOTALL)
content = re.sub(r'<tfoot class="bg-gray-50 font-bold border-t border-gray-200">.*?</tfoot\>', '<tfoot id="sbu-tfoot" class="bg-gray-50 font-bold border-t border-gray-200"></tfoot>', content, flags=re.DOTALL)

# Add ID to Categories grid
content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">\s*<!-- Card: Alat Medis -->.*?</div\>\s*</div\>\s*</div\>', '<div id="kategori-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4"></div>\n                </div>\n            </div>', content, flags=re.DOTALL)

# Inject JS
js_injection = """
        // Fetch data from backend
        async function loadDashboardData() {
            try {
                const response = await fetch('/api/rkap/dashboard');
                const result = await response.json();
                if(result.status === 'success') {
                    renderDashboard(result.data);
                }
            } catch (err) {
                console.error("Failed to load dashboard data", err);
            }
        }
        
        function formatRp(value) {
            return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', maximumFractionDigits: 0 }).format(value);
        }
        
        function renderDashboard(data) {
            // Calculate KPI
            let totalAnggaran = 0;
            let totalRealisasi = 0;
            let warningCount = 0;
            
            const tbody = document.getElementById('sbu-tbody');
            tbody.innerHTML = '';
            
            data.sbu.forEach(item => {
                totalAnggaran += item.budget_allocated;
                totalRealisasi += item.budget_realized;
                let sisa = item.budget_allocated - item.budget_realized;
                let serapan = (item.budget_realized / item.budget_allocated) * 100;
                
                let statusBadge = '';
                let bgClass = '';
                let warningCls = '';
                if(serapan > 90) {
                    warningCount++;
                    statusBadge = '<span class="badge bg-rose-100 text-rose-700">Warning</span>';
                    warningCls = 'text-rose-600 font-bold';
                    bgClass = 'bg-rose-500';
                } else {
                    statusBadge = '<span class="badge bg-emerald-100 text-emerald-700">Aman</span>';
                    warningCls = '';
                    bgClass = 'bg-sky-500';
                }
                
                tbody.innerHTML += `
                    <tr class="hover:bg-gray-50">
                        <td class="py-3 px-4 font-semibold text-gray-900">${item.sbu_name}</td>
                        <td class="py-3 px-4 font-mono text-xs text-gray-500">${item.sbu_code}</td>
                        <td class="py-3 px-4 text-right">${formatRp(item.budget_allocated)}</td>
                        <td class="py-3 px-4 text-right text-gray-600">${formatRp(item.budget_realized)}</td>
                        <td class="py-3 px-4 text-right font-semibold ${serapan > 90 ? 'text-rose-600' : 'text-emerald-600'}">${formatRp(sisa)}</td>
                        <td class="py-3 px-4">
                            <div class="flex items-center gap-2">
                                <div class="w-full bg-gray-200 rounded-full h-1.5"><div class="${bgClass} h-1.5 rounded-full" style="width: ${serapan.toFixed(1)}%"></div></div>
                                <span class="text-xs ${warningCls}">${serapan.toFixed(1)}%</span>
                            </div>
                        </td>
                        <td class="py-3 px-4">${statusBadge}</td>
                    </tr>
                `;
            });
            
            let totalSisa = totalAnggaran - totalRealisasi;
            let totalSerapan = (totalRealisasi / totalAnggaran) * 100;
            
            document.getElementById('sbu-tfoot').innerHTML = `
                <tr>
                    <td colspan="2" class="py-3 px-4">TOTAL</td>
                    <td class="py-3 px-4 text-right">${formatRp(totalAnggaran)}</td>
                    <td class="py-3 px-4 text-right">${formatRp(totalRealisasi)}</td>
                    <td class="py-3 px-4 text-right text-sky-700">${formatRp(totalSisa)}</td>
                    <td class="py-3 px-4">${totalSerapan.toFixed(1)}%</td>
                    <td></td>
                </tr>
            `;
            
            // KPI Update
            document.getElementById('kpi-container').innerHTML = `
                <div class="bg-white rounded-xl border border-gray-100 shadow-sm p-5">
                    <p class="text-xs text-gray-500 font-medium">Total Anggaran (RKAP 2026)</p>
                    <p class="text-3xl font-bold text-gray-900 mt-1">${formatRp(totalAnggaran)}</p>
                    <p class="text-xs text-gray-400 mt-1">Disetujui BOD</p>
                </div>
                <div class="bg-white rounded-xl border border-gray-100 shadow-sm p-5">
                    <p class="text-xs text-gray-500 font-medium">Realisasi (YTD)</p>
                    <p class="text-3xl font-bold text-sky-600 mt-1">${formatRp(totalRealisasi)}</p>
                    <p class="text-xs text-gray-400 mt-1">${totalSerapan.toFixed(1)}% dari Anggaran</p>
                </div>
                <div class="bg-white rounded-xl border border-gray-100 shadow-sm p-5">
                    <p class="text-xs text-gray-500 font-medium">Sisa Anggaran</p>
                    <p class="text-3xl font-bold text-emerald-500 mt-1">${formatRp(totalSisa)}</p>
                    <p class="text-xs text-gray-400 mt-1">Tersedia untuk Pengadaan</p>
                </div>
                <div class="bg-white rounded-xl border border-gray-100 shadow-sm p-5 bg-gradient-to-br from-rose-50 to-red-50 border-rose-100">
                    <p class="text-xs text-rose-700 font-medium">Overbudget Warning</p>
                    <p class="text-3xl font-bold text-rose-600 mt-1">${warningCount} SBU</p>
                    <p class="text-xs text-rose-500 mt-1">Mendekati limit >90%</p>
                </div>
            `;
            
            // Categories
            const catContainer = document.getElementById('kategori-container');
            catContainer.innerHTML = '';
            
            const icons = ["⚕️", "💊", "🧪", "🏢"];
            const colors = ["sky", "emerald", "violet", "amber"];
            
            data.categories.forEach((cat, idx) => {
                let c = colors[idx % colors.length];
                let i = icons[idx % icons.length];
                let sisa = cat.budget_allocated - cat.budget_realized;
                let pct = (cat.budget_realized / cat.budget_allocated) * 100;
                
                catContainer.innerHTML += `
                    <div class="border border-gray-200 rounded-xl p-5 hover:border-${c}-300 transition">
                        <div class="flex justify-between items-start mb-4">
                            <div class="w-10 h-10 rounded-lg bg-${c}-100 flex items-center justify-center text-${c}-600 text-xl">${i}</div>
                            <span class="badge bg-${c}-100 text-${c}-700">${cat.category_type}</span>
                        </div>
                        <h4 class="font-bold text-gray-900">${cat.category_name}</h4>
                        <div class="mt-4 space-y-2 text-sm">
                            <div class="flex justify-between"><span class="text-gray-500">Anggaran:</span> <span class="font-semibold">${formatRp(cat.budget_allocated)}</span></div>
                            <div class="flex justify-between"><span class="text-gray-500">Realisasi:</span> <span>${formatRp(cat.budget_realized)}</span></div>
                            <div class="flex justify-between border-t border-gray-100 pt-2"><span class="text-gray-500">Sisa:</span> <span class="font-bold text-${sisa < 0 ? 'rose' : 'emerald'}-600">${formatRp(sisa)}</span></div>
                        </div>
                        <div class="w-full bg-gray-200 rounded-full h-1.5 mt-4"><div class="bg-${c}-500 h-1.5 rounded-full" style="width: ${pct}%"></div></div>
                    </div>
                `;
            });
        }
"""

content = content.replace("// Initialize Chart", js_injection + "\n\n        // Initialize Chart\n        loadDashboardData();\n")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated fase1 HTML.")

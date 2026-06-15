import re

html_path = r"d:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend\fase4_tender.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Tab Kompetitif tbody
new_kompetitif_tbody = """<tbody class="divide-y divide-gray-100 text-sm" id="tbody-kompetitif">
                                <tr><td colspan="7" class="py-4 text-center text-gray-500">Memuat data...</td></tr>
                            </tbody>"""
content = re.sub(r'<tbody class="divide-y divide-gray-100 text-sm">.*?</tbody>', new_kompetitif_tbody, content, count=1, flags=re.DOTALL)

# Replace Tab Langsung tbody
new_langsung_tbody = """<tbody class="divide-y divide-gray-100 text-sm" id="tbody-langsung">
                                <tr><td colspan="5" class="py-4 text-center text-gray-500">Memuat data...</td></tr>
                            </tbody>"""
content = re.sub(r'<tbody class="divide-y divide-gray-100 text-sm">.*?</tbody>', new_langsung_tbody, content, count=1, flags=re.DOTALL)

# Add API call logic
js_injection = """
        const API_URL = '/api';
        
        async function loadTenders() {
            try {
                const res = await fetch(API_URL + '/tenders');
                const result = await res.json();
                if(result.status === 'success') {
                    const data = result.data;
                    
                    const kompetitif = data.filter(t => t.tender_number.startsWith('TND'));
                    const langsung = data.filter(t => t.tender_number.startsWith('PL'));
                    
                    renderKompetitif(kompetitif);
                    renderLangsung(langsung);
                }
            } catch(e) {
                document.getElementById('tbody-kompetitif').innerHTML = '<tr><td colspan="7" class="text-center text-red-500 py-4">Gagal memuat data</td></tr>';
                document.getElementById('tbody-langsung').innerHTML = '<tr><td colspan="5" class="text-center text-red-500 py-4">Gagal memuat data</td></tr>';
            }
        }
        
        function formatRp(value) {
            return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', maximumFractionDigits: 0 }).format(value);
        }
        
        function renderKompetitif(data) {
            const tbody = document.getElementById('tbody-kompetitif');
            if(data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="7" class="py-4 text-center text-gray-500">Tidak ada tender kompetitif aktif.</td></tr>';
                return;
            }
            
            tbody.innerHTML = data.map(t => {
                let statusBadge = '';
                if(t.status === 'bidding') statusBadge = '<span class="badge bg-blue-100 text-blue-700">Masa Bidding</span>';
                else if(t.status === 'closing_soon') statusBadge = '<span class="badge bg-amber-100 text-amber-700">Segera Berakhir</span>';
                else statusBadge = `<span class="badge bg-gray-100 text-gray-700">${t.status}</span>`;
                
                let dateClass = t.status === 'closing_soon' ? 'text-rose-500 font-medium' : 'text-gray-500';
                
                return `
                <tr class="hover:bg-gray-50">
                    <td class="py-3 px-4 font-mono text-xs text-gray-500">${t.tender_number}</td>
                    <td class="py-3 px-4 font-medium text-gray-900">${t.title}</td>
                    <td class="py-3 px-4">${formatRp(t.budget_max)}</td>
                    <td class="py-3 px-4 font-bold text-blue-600">N/A</td>
                    <td class="py-3 px-4 ${dateClass}">${t.bid_closing_date}</td>
                    <td class="py-3 px-4">${statusBadge}</td>
                    <td class="py-3 px-4 text-right">
                        <button class="text-xs bg-emerald-50 text-emerald-700 hover:bg-emerald-100 px-3 py-1.5 rounded-lg font-semibold">Tutup & Evaluasi</button>
                    </td>
                </tr>
                `;
            }).join('');
        }
        
        function renderLangsung(data) {
            const tbody = document.getElementById('tbody-langsung');
            if(data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="5" class="py-4 text-center text-gray-500">Tidak ada penunjukan langsung.</td></tr>';
                return;
            }
            
            tbody.innerHTML = data.map(t => {
                let statusBadge = '<span class="badge bg-emerald-100 text-emerald-700">Disetujui</span>';
                return `
                <tr class="hover:bg-gray-50">
                    <td class="py-3 px-4 font-mono text-xs text-gray-500">${t.tender_number}</td>
                    <td class="py-3 px-4 font-medium text-gray-900">${t.title}</td>
                    <td class="py-3 px-4 text-gray-600">${t.description || '-'}</td>
                    <td class="py-3 px-4">${formatRp(t.budget_max)}</td>
                    <td class="py-3 px-4">${statusBadge}</td>
                </tr>
                `;
            }).join('');
        }
        
        async function submitTender() {
            const t = {
                tender_number: "TND-2026-" + Math.floor(Math.random() * 10000).toString().padStart(4, '0'),
                title: document.getElementById('t_title').value,
                category: document.getElementById('t_category').value,
                budget_max: parseFloat(document.getElementById('t_budget').value) || 0,
                bid_closing_date: document.getElementById('t_close').value,
                expected_delivery_date: document.getElementById('t_delivery').value,
                description: document.getElementById('t_desc').value,
                status: "bidding"
            };
            
            try {
                const res = await fetch(API_URL + '/tenders', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(t)
                });
                const result = await res.json();
                if(result.status === 'success') {
                    closeModal('tenderModal');
                    alert('Tender berhasil dipublish dan dikirim ke portal vendor!');
                    loadTenders();
                } else {
                    alert('Gagal membuat tender');
                }
            } catch(e) {
                alert('Gagal membuat tender: ' + e);
            }
        }
        
        window.onload = loadTenders;
"""

content = re.sub(r'function submitTender\(\) \{.*?\n        }', '', content, flags=re.DOTALL)
content = re.sub(r'</script>', js_injection + "\n    </script>", content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated fase4 HTML.")

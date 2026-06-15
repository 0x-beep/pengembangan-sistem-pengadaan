import re

html_path = r"d:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend\fase5_kso_portal.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Tab 1 (KSO Contracts) tbody
new_kso_tbody = """<tbody class="divide-y divide-gray-100" id="tbody-kso">
                            <tr><td colspan="6" class="py-4 text-center text-gray-500">Memuat data...</td></tr>
                        </tbody>"""
content = re.sub(r'<tbody class="divide-y divide-gray-100">.*?</tbody>', new_kso_tbody, content, count=1, flags=re.DOTALL)

js_injection = """
        const API_URL = '/api';
        
        async function loadContracts() {
            try {
                const res = await fetch(API_URL + '/kso-contracts');
                const result = await res.json();
                if(result.status === 'success') {
                    renderContracts(result.data);
                }
            } catch(e) {
                document.getElementById('tbody-kso').innerHTML = '<tr><td colspan="6" class="text-center text-red-500 py-4">Gagal memuat data</td></tr>';
            }
        }
        
        function renderContracts(data) {
            const tbody = document.getElementById('tbody-kso');
            if(data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="6" class="py-4 text-center text-gray-500">Tidak ada kontrak KSO.</td></tr>';
                return;
            }
            
            tbody.innerHTML = data.map(c => {
                let statusBadge = '';
                if(c.status === 'BERJALAN') statusBadge = '<span class="badge bg-emerald-100 text-emerald-700 border border-emerald-200">BERJALAN</span>';
                else statusBadge = '<span class="badge bg-amber-100 text-amber-700 border border-amber-200">RENEWAL PERIOD</span>';
                
                return `
                <tr class="hover:bg-slate-50">
                    <td class="px-6 py-4">
                        <div class="font-mono text-xs text-gray-500">${c.contract_number}</div>
                        <div class="font-bold text-gray-900">${c.object_name}</div>
                    </td>
                    <td class="px-6 py-4 font-medium text-gray-700">${c.vendor_name}</td>
                    <td class="px-6 py-4">
                        <div class="text-gray-900 text-xs">${c.start_date} - ${c.end_date}</div>
                    </td>
                    <td class="px-6 py-4"><span class="badge bg-purple-50 text-purple-700 border border-purple-200">${c.billing_type}</span></td>
                    <td class="px-6 py-4 text-center">${statusBadge}</td>
                    <td class="px-6 py-4 text-right">
                        <button class="text-blue-600 hover:bg-blue-50 px-2 py-1 rounded transition text-xs font-medium border border-blue-200">Lihat Detail</button>
                    </td>
                </tr>
                `;
            }).join('');
        }
        
        window.onload = loadContracts;
"""

content = re.sub(r'</script>', js_injection + "\n    </script>", content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated fase5 HTML.")

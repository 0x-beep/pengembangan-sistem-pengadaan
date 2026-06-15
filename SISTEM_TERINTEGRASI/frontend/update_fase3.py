import re

html_path = r"d:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend\fase3_imt_pp_sppj.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the content of id="pp-list" with a loading indicator
content = re.sub(r'<div class="space-y-3" id="pp-list">.*?</div>\s*</main>', 
"""<div class="space-y-3" id="pp-list">
                <div class="text-center py-10 text-slate-500">
                    <i class="fas fa-spinner fa-spin text-2xl mb-3"></i>
                    <p>Memuat data PP...</p>
                </div>
            </div>
        </main>""", content, flags=re.DOTALL)

# Inject the load function in JS
js_injection = """
        const API_URL = '/api';
        let ppData = [];

        async function loadRequisitions() {
            try {
                const res = await fetch(API_URL + '/requisitions');
                const result = await res.json();
                if(result.status === 'success') {
                    ppData = result.data;
                    renderPP(ppData);
                    updateSummary();
                }
            } catch(e) {
                document.getElementById('pp-list').innerHTML = '<p class="text-rose-500 text-center py-4">Gagal memuat data.</p>';
            }
        }
        
        function formatRp(value) {
            return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', maximumFractionDigits: 0 }).format(value);
        }

        function renderPP(data) {
            const list = document.getElementById('pp-list');
            if(data.length === 0) {
                list.innerHTML = '<p class="text-center text-slate-500 py-4">Tidak ada data.</p>';
                return;
            }
            
            list.innerHTML = data.map(item => {
                let borderClass = item.status === 'baru' ? 'border-l-amber-400' : (item.status === 'proses' ? 'border-l-blue-500' : 'border-l-emerald-500 opacity-60');
                
                let badgeType = '';
                if(item.req_type === 'PP') badgeType = '<span class="badge bg-blue-50 text-blue-700 border border-blue-200">PP — Barang</span>';
                else if(item.req_type === 'IMT') badgeType = '<span class="badge bg-violet-50 text-violet-700 border border-violet-200">IMT — Alat Medis</span>';
                else badgeType = '<span class="badge bg-amber-50 text-amber-700 border border-amber-200">SPPJ — Jasa</span>';
                
                let statusBadge = '';
                if(item.status === 'baru') statusBadge = '<span class="badge bg-amber-50 text-amber-700 border border-amber-200">Baru Masuk</span>';
                else if(item.status === 'proses') statusBadge = '<span class="badge bg-blue-50 text-blue-700 border border-blue-200">Sedang Diproses</span>';
                else statusBadge = '<span class="badge bg-emerald-50 text-emerald-700 border border-emerald-200">Selesai</span>';
                
                let buttons = '';
                if(item.status === 'baru') {
                    if(item.req_type === 'PP') buttons = `<button onclick="tindakLanjut('${item.req_number}','tender')" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition"><i class="fas fa-gavel"></i> Tender & Bidding</button>`;
                    else if(item.req_type === 'IMT') buttons = `<button onclick="tindakLanjut('${item.req_number}','kso')" class="bg-violet-600 hover:bg-violet-700 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition"><i class="fas fa-handshake"></i> KSO & Kontrak</button>`;
                    else buttons = `<button onclick="tindakLanjut('${item.req_number}','swakelola')" class="bg-amber-600 hover:bg-amber-700 text-white text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition"><i class="fas fa-tools"></i> Swakelola & Jasa</button>`;
                    
                    buttons += `<button onclick="lihatDetail('${item.req_number}')" class="bg-slate-100 hover:bg-slate-200 text-slate-600 text-xs font-semibold px-3 py-2 rounded-lg flex items-center gap-1.5 transition mt-2"><i class="fas fa-eye"></i> Lihat Detail</button>`;
                } else if(item.status === 'proses') {
                    buttons = `<button onclick="lihatProgress('${item.req_number}')" class="bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 text-xs font-bold px-3 py-2 rounded-lg flex items-center gap-1.5 transition"><i class="fas fa-chart-line"></i> Lihat Progress</button>`;
                }
                
                return `
                <div class="bg-white rounded-xl border-l-4 ${borderClass} border border-slate-200 shadow-sm p-5 pp-item" data-tipe="${item.req_type}" data-status="${item.status}">
                    <div class="flex items-start justify-between gap-4">
                        <div class="flex-1 min-w-0">
                            <div class="flex items-center gap-2 flex-wrap mb-2">
                                <span class="font-mono text-xs text-slate-400">${item.req_number}</span>
                                ${badgeType}
                                ${statusBadge}
                                <span class="badge bg-emerald-50 text-emerald-700 border border-emerald-200"><i class="fas fa-check-circle mr-1 text-[10px]"></i>Cleared RKAP</span>
                                ${item.total_amount > 1000000000 ? '<span class="badge bg-red-50 text-red-600 border border-red-200"><i class="fas fa-exclamation-triangle mr-1 text-[10px]"></i>&gt; Rp 1M — perlu BOD</span>' : ''}
                            </div>
                            <p class="font-semibold text-slate-800">${item.title}</p>
                            <div class="flex gap-4 text-xs text-slate-500 mt-1 flex-wrap">
                                <span><i class="fas fa-building mr-1"></i>${item.sbu_name}</span>
                                <span><i class="fas fa-tag mr-1"></i>${formatRp(item.total_amount)}</span>
                                <span><i class="fas fa-calendar mr-1"></i>Masuk: ${item.created_at ? item.created_at.split(' ')[0] : '-'}</span>
                            </div>
                            ${item.description ? `<p class="text-xs text-slate-400 mt-1.5 italic">${item.description}</p>` : ''}
                        </div>
                        <div class="flex flex-col gap-2 shrink-0">
                            ${buttons}
                        </div>
                    </div>
                </div>
                `;
            }).join('');
        }

        function updateSummary() {
            document.getElementById('sum-total').textContent = ppData.length;
            document.getElementById('sum-baru').textContent = ppData.filter(x => x.status === 'baru').length;
            document.getElementById('sum-proses').textContent = ppData.filter(x => x.status === 'proses').length;
            document.getElementById('sum-selesai').textContent = ppData.filter(x => x.status === 'selesai').length;
        }

        function filterPP() {
            const tipe = document.getElementById('filter-tipe').value;
            const status = document.getElementById('filter-status').value;
            
            const filtered = ppData.filter(item => {
                const matchTipe = !tipe || item.req_type === tipe;
                const matchStatus = !status || item.status === status;
                return matchTipe && matchStatus;
            });
            renderPP(filtered);
        }

        function tindakLanjut(noPP, jalur) {
            const dest = { tender: 'fase4_tender.html', kso: 'fase5_kso_portal.html', swakelola: 'swakelola_dashboard.html' }[jalur];
            if (dest) window.location.href = dest + '?pp=' + noPP;
        }

        function lihatDetail(noPP) {
            alert('Detail PP: ' + noPP + '\\nAkan terhubung ke modul detail PP Bagian Umum.');
        }

        function lihatProgress(noPP) {
            window.location.href = 'fase4_tender.html?pp=' + noPP;
        }
        
        window.onload = loadRequisitions;
"""

content = re.sub(r'const API_URL = .*?</script>', js_injection + "\n    </script>", content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated fase3 HTML.")

import re

html_path = r"d:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend\fase6_bapb_penerimaan.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

js_injection = """
        const API = '/api';
        
        let bapbCounter = 1;

        function showToast(msg, isSuccess = true) {
            const t = document.getElementById('toast');
            document.getElementById('toast-msg').textContent = msg;
            document.getElementById('toast-icon').textContent = isSuccess ? '✓' : '⚠';
            t.classList.remove('hidden');
            setTimeout(() => t.classList.add('hidden'), 3000);
        }

        function switchTab(tab) {
            ['po','qc','bapb','retur'].forEach(t => {
                document.getElementById('tab-' + t).classList.add('hidden');
                document.getElementById('tab-btn-' + t).classList.remove('active');
            });
            document.getElementById('tab-' + tab).classList.remove('hidden');
            document.getElementById('tab-btn-' + tab).classList.add('active');
            if (tab === 'po') loadPOs();
            if (tab === 'bapb') loadBAPBs();
        }

        async function loadPOs() {
            try {
                const res = await fetch(`${API}/purchase-orders`);
                const result = await res.json();
                const tbody = document.getElementById('po-table-body');
                tbody.innerHTML = '';
                
                if(result.status === 'success') {
                    let pendingCount = 0;
                    result.data.forEach(po => {
                        pendingCount++;
                        const etaDate = new Date(); // Mocking ETA
                        etaDate.setDate(etaDate.getDate() + 3);
                        const overdue = false;
                        
                        tbody.innerHTML += `
                            <tr class="hover:bg-gray-50 transition">
                                <td class="py-3 pr-4 font-mono text-xs text-gray-600">${po.po_number}</td>
                                <td class="py-3 pr-4 font-medium text-gray-900">${po.vendor_name || po.vendor_id}</td>
                                <td class="py-3 pr-4 font-semibold">Rp ${(po.total_amount || 0).toLocaleString('id-ID')}</td>
                                <td class="py-3 pr-4 text-gray-500 text-xs">${po.created_at ? po.created_at.split(' ')[0] : '-'}</td>
                                <td class="py-3 pr-4 text-xs ${overdue ? 'text-rose-600 font-bold' : 'text-gray-500'}">ETA</td>
                                <td class="py-3 pr-4"><span class="badge-status bg-amber-100 text-amber-700">Menunggu Tiba</span></td>
                                <td class="py-3 text-right">
                                    <button onclick="startQC('${po.po_number}', '${po.vendor_id}')" class="text-xs bg-blue-600 text-white hover:bg-blue-700 px-3 py-1.5 rounded-lg font-semibold transition">Konfirmasi Terima</button>
                                </td>
                            </tr>`;
                    });
                    document.getElementById('stat_pending').textContent = pendingCount;
                }
            } catch (e) {
                console.error(e);
            }
        }
        
        async function loadBAPBs() {
            try {
                const res = await fetch(`${API}/bapb`);
                const result = await res.json();
                const tbody = document.getElementById('bapb-table-body');
                tbody.innerHTML = '';
                
                if(result.status === 'success') {
                    let doneCount = 0;
                    result.data.forEach(b => {
                        doneCount++;
                        tbody.innerHTML += `
                            <tr>
                                <td class="py-3 pr-4 font-mono text-xs text-gray-600">${b.bapb_number}</td>
                                <td class="py-3 pr-4 font-mono text-xs text-gray-600">${b.po_number}</td>
                                <td class="py-3 pr-4">${b.vendor_name || b.vendor_id}</td>
                                <td class="py-3 pr-4">Barang Sesuai PO</td>
                                <td class="py-3 pr-4 font-semibold">-</td>
                                <td class="py-3 pr-4 text-gray-500">${b.received_date || b.created_at.split(' ')[0]}</td>
                                <td class="py-3 pr-4"><span class="badge-status bg-emerald-100 text-emerald-700">✓ Lulus QC</span></td>
                                <td class="py-3 text-right">
                                    <button class="text-xs bg-blue-50 text-blue-700 hover:bg-blue-100 px-3 py-1.5 rounded-lg font-semibold transition">Cetak BAPB</button>
                                </td>
                            </tr>
                        `;
                    });
                    document.getElementById('stat_done').textContent = doneCount;
                    updatePassRate();
                }
            } catch (e) {
                console.error(e);
            }
        }

        function startQC(poNumber, vendor) {
            showToast(`Memulai proses QC untuk ${poNumber}...`);
            switchTab('qc');
        }

        function updatePassRate() {
            const done = parseInt(document.getElementById('stat_done').textContent) || 0;
            const rejected = parseInt(document.getElementById('stat_rejected').textContent) || 0;
            const total = done + rejected;
            if (total > 0) {
                document.getElementById('stat_passrate').textContent = Math.round((done / total) * 100) + '%';
            }
        }

        async function openBAPBModal() {
            document.getElementById('bapb-modal').classList.remove('hidden');
            document.getElementById('bapb-date').value = new Date().toISOString().split('T')[0];
            
            const sel = document.getElementById('bapb-po');
            sel.innerHTML = '<option value="">-- Pilih PO --</option>';
            try {
                const res = await fetch(`${API}/purchase-orders`);
                const result = await res.json();
                if(result.status === 'success') {
                    result.data.forEach(p => {
                        sel.innerHTML += `<option value="${p.po_number}">${p.po_number} (${p.vendor_name})</option>`;
                    });
                }
            } catch(e) {}
        }

        function closeBAPBModal() {
            document.getElementById('bapb-modal').classList.add('hidden');
        }

        async function submitBAPB() {
            const po = document.getElementById('bapb-po').value;
            const receiver = document.getElementById('bapb-receiver').value;
            const qcResult = document.getElementById('bapb-qc-result').value;
            if (!po || !receiver) {
                showToast('Nomor PO dan Penerima wajib diisi!', false);
                return;
            }
            
            if(qcResult === 'rejected') {
                showToast('Barang ditolak! Masuk daftar retur.', false);
                document.getElementById('stat_rejected').textContent = parseInt(document.getElementById('stat_rejected').textContent || 0) + 1;
                closeBAPBModal();
                updatePassRate();
                return;
            }
            
            const today = new Date().toISOString().split('T')[0];
            const bapbNo = `BAPB-2026-06-${String(Math.floor(Math.random()*1000)).padStart(3,'0')}`;
            
            const payload = {
                bapb_number: bapbNo,
                po_number: po,
                received_date: today,
                received_by: receiver,
                condition: qcResult === 'partial' ? 'partial' : 'good',
                notes: document.getElementById('bapb-notes').value,
                status: 'approved'
            };
            
            try {
                const res = await fetch(`${API}/bapb`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(payload)
                });
                const result = await res.json();
                if(result.status === 'success') {
                    showToast(`BAPB ${bapbNo} berhasil diterbitkan!`);
                    closeBAPBModal();
                    loadBAPBs();
                } else {
                    showToast('Gagal menerbitkan BAPB', false);
                }
            } catch(e) {
                showToast('Gagal terhubung ke server', false);
            }
        }

        window.addEventListener('DOMContentLoaded', () => {
            loadPOs();
            loadBAPBs();
            document.getElementById('stat_qc').textContent = 1;
        });
"""

content = re.sub(r'const API = .*?</script>', js_injection + "\n    </script>", content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated fase6 HTML.")

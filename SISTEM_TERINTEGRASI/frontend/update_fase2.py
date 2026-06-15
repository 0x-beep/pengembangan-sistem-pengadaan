import re

html_path = r"d:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend\fase2_vendor_database.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace loadVendors
new_load_vendors = """        async function loadVendors() {
            const tb = document.getElementById('vendorTable');
            tb.innerHTML = `<tr><td colspan="6" class="px-6 py-8 text-center text-slate-400 text-sm"><i class="fas fa-spinner fa-spin text-2xl mb-2"></i><br>Memuat...</td></tr>`;
            
            try {
                const response = await fetch('/api/vendors');
                const result = await response.json();
                if(result.status === 'success') {
                    // Map to existing structure
                    vendorData = result.data.map(v => ({
                        id: v.vendor_id,
                        name: v.company_name,
                        cat: v.vendor_category || 'Umum & Jasa',
                        nib: v.sio || '-',
                        npwp: v.npwp || '-',
                        contact: `${v.contact_person_name || 'Admin'} (${v.contact_person_phone || '-'})`,
                        status: (v.vendor_status === 'submitted' ? 'pending' : v.vendor_status) || 'pending'
                    }));
                    renderTable(vendorData);
                    updateStats();
                }
            } catch (err) {
                tb.innerHTML = `<tr><td colspan="6" class="px-6 py-8 text-center text-rose-500 font-bold">Gagal terhubung ke server backend.</td></tr>`;
            }
        }
        
        function updateStats() {
            const total = vendorData.length;
            const pending = vendorData.filter(v => v.status === 'pending' || v.status === 'submitted').length;
            const active = vendorData.filter(v => v.status === 'active').length;
            const blacklist = vendorData.filter(v => v.status === 'rejected' || v.status === 'blacklist').length;
            
            document.getElementById('stat-total').textContent = total;
            document.getElementById('stat-pending').textContent = pending;
            document.getElementById('stat-active').textContent = active;
            document.getElementById('stat-blacklist').textContent = blacklist;
        }
"""

content = re.sub(r'async function loadVendors\(\) \{.*?\n        }', new_load_vendors, content, flags=re.DOTALL)

# Replace approveVendor
new_approve_vendor = """        async function approveVendor() {
            if(currentVerifyId) {
                try {
                    const response = await fetch(`/api/vendors/${currentVerifyId}/approve`, {
                        method: 'PUT'
                    });
                    const res = await response.json();
                    if(res.status === 'success') {
                        const v = vendorData.find(x => x.id === currentVerifyId);
                        if(v) v.status = 'active';
                        filterTable();
                        updateStats();
                    }
                } catch (err) {
                    alert("Gagal menyetujui vendor.");
                }
            }
            closeModal();
        }"""

content = re.sub(r'function approveVendor\(\) \{.*?\n        }', new_approve_vendor, content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated fase2 HTML.")

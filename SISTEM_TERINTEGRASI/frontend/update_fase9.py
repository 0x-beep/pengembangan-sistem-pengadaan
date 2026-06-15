import re

html_path = r"d:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend\fase9_laporan_analitik.html"

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

js_injection = """
        const API_URL = 'http://127.0.0.1:8000/api';

        async function loadDashboard() {
            try {
                const res = await fetch(`${API_URL}/analytics/dashboard`);
                const result = await res.json();
                
                if(result.status === 'success') {
                    const data = result.data;
                    
                    // Update Metrics
                    const m = data.metrics;
                    
                    document.querySelector('.text-emerald-600').innerHTML = 
                        `Rp ${(m.total_efficiency/1000000000).toFixed(1)}M <span class="text-sm font-normal text-slate-400">YTD</span>`;
                        
                    document.querySelectorAll('.text-blue-600')[0].innerHTML = 
                        `${m.avg_lead_time} <span class="text-sm font-normal text-slate-400">Hari</span>`;
                        
                    document.querySelectorAll('.text-slate-800')[1].innerHTML = 
                        `${m.budget_realized_pct}% <span class="text-sm font-normal text-slate-400">Terserap</span>`;
                        
                    document.querySelector('.text-purple-600').innerHTML = 
                        `${m.total_po} <span class="text-sm font-normal text-slate-400">Dokumen</span>`;
                        
                    // Update Charts
                    renderAnggaranChart(data.chartAnggaran);
                    renderKategoriChart(data.chartKategori);
                }
            } catch(e) {
                console.error("Gagal memuat analitik", e);
                // Fallback to static render if API is down
                renderAnggaranChart({
                    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
                    anggaran: [500, 600, 550, 700, 650, 800],
                    realisasi: [450, 580, 500, 650, 600, 750]
                });
                renderKategoriChart({
                    labels: ['Alat Kesehatan / KSO', 'Obat & Farmasi', 'IT & Infrastruktur', 'Umum & Jasa'],
                    data: [45, 25, 15, 15]
                });
            }
        }
        
        function renderAnggaranChart(data) {
            const ctxAnggaran = document.getElementById('chartAnggaran').getContext('2d');
            new Chart(ctxAnggaran, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [
                        { label: 'Anggaran (RKAP)', data: data.anggaran, backgroundColor: '#e2e8f0', borderRadius: 4 },
                        { label: 'Realisasi', data: data.realisasi, backgroundColor: '#3b82f6', borderRadius: 4 }
                    ]
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top', labels: { boxWidth: 12, font: { size: 10 } } } }, scales: { y: { beginAtZero: true, grid: { borderDash: [4, 4] } } } }
            });
        }
        
        function renderKategoriChart(data) {
            const ctxKategori = document.getElementById('chartKategori').getContext('2d');
            new Chart(ctxKategori, {
                type: 'doughnut',
                data: {
                    labels: data.labels,
                    datasets: [{ data: data.data, backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#8b5cf6'], borderWidth: 0 }]
                },
                options: { responsive: true, maintainAspectRatio: false, cutout: '70%', plugins: { legend: { position: 'right', labels: { boxWidth: 12, font: { size: 10 } } } } }
            });
        }
        
        window.addEventListener('DOMContentLoaded', loadDashboard);
"""

# Replace the old static script block
content = re.sub(r'<script>.*?</script>', '<script>' + js_injection + '</script>', content, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated fase9 HTML.")

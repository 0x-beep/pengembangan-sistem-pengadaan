import re

def update_fase7():
    with open('fase7_invoice_3waymatch.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the start and end of the subway map
    start_marker = r'<!-- Pipeline Map Container \(Multi-Lane Bottleneck\) -->'
    end_marker = r'<!-- Mitigasi & Rekomendasi AI -->'

    match = re.search(f'({start_marker}.*?)({end_marker})', html, re.DOTALL)
    if not match:
        print("Could not find the map section in fase7")
        return

    kanban_css = '''
    <style>
        .kanban-board {
            display: grid;
            grid-template-columns: repeat(8, minmax(220px, 1fr));
            gap: 1rem;
            overflow-x: auto;
            padding-bottom: 1rem;
            align-items: start;
        }
        .kanban-col {
            background-color: #f8fafc;
            border-radius: 0.75rem;
            border: 1px solid #e2e8f0;
            display: flex;
            flex-direction: column;
            max-height: 60vh;
        }
        .kanban-header {
            padding: 0.75rem;
            border-bottom: 2px solid #e2e8f0;
            font-weight: 700;
            font-size: 0.75rem;
            color: #334155;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #f1f5f9;
            border-top-left-radius: 0.75rem;
            border-top-right-radius: 0.75rem;
        }
        .kanban-cards {
            padding: 0.75rem;
            overflow-y: auto;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }
        .k-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 0.5rem;
            padding: 0.75rem;
            box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05);
            transition: all 0.2s;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }
        .k-card:hover {
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }
        .k-card.urgent {
            border-left: 4px solid #ef4444;
            background-color: #fef2f2;
        }
        .k-card.warning {
            border-left: 4px solid #f59e0b;
            background-color: #fffbeb;
        }
        .k-card.normal {
            border-left: 4px solid #10b981;
        }
        .k-card.empty-placeholder {
            border: 2px dashed #cbd5e1;
            background: transparent;
            text-align: center;
            color: #94a3b8;
            font-size: 0.75rem;
            padding: 1rem;
            box-shadow: none;
            cursor: default;
        }
        .k-card.empty-placeholder:hover {
            transform: none;
        }
    </style>
    '''

    new_kanban_html = f'''
    <!-- Pipeline Map Container (Kanban Bottleneck) -->
    <div class="mb-6">
        {kanban_css}
        <div class="kanban-board">
            
            <!-- Col 1 -->
            <div class="kanban-col border-t-4 border-t-violet-500">
                <div class="kanban-header">
                    <span>1. Gudang / Admin<br>(3-Way Match)</span>
                    <span class="bg-violet-100 text-violet-700 text-xs px-2 py-0.5 rounded-full">Rp 480jt</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card normal">
                        <div class="flex justify-between mb-2">
                            <span class="text-[9px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">INV-012</span>
                            <span class="text-[9px] font-bold text-emerald-600"><i class="fas fa-check-circle"></i></span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Alkes Indo</h5>
                        <div class="text-[11px] font-black text-emerald-600">Rp 480.000.000</div>
                    </div>
                </div>
            </div>

            <!-- Col 2 -->
            <div class="kanban-col border-t-4 border-t-violet-400">
                <div class="kanban-header">
                    <span>2. Manajer<br>Pengadaan</span>
                    <span class="bg-slate-100 text-slate-500 text-xs px-2 py-0.5 rounded-full">Rp 0</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card empty-placeholder">Tidak ada antrean</div>
                </div>
            </div>

            <!-- Col 3 -->
            <div class="kanban-col border-t-4 border-t-violet-300">
                <div class="kanban-header">
                    <span>3. GM<br>Operasi</span>
                    <span class="bg-slate-100 text-slate-500 text-xs px-2 py-0.5 rounded-full">Rp 0</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card empty-placeholder">Tidak ada antrean</div>
                </div>
            </div>

            <!-- Col 4 -->
            <div class="kanban-col border-t-4 border-t-amber-400">
                <div class="kanban-header">
                    <span>4. Direktur<br>Operasi</span>
                    <span class="bg-slate-100 text-slate-500 text-xs px-2 py-0.5 rounded-full">Rp 0</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card empty-placeholder">Tidak ada antrean</div>
                </div>
            </div>

            <!-- Col 5 -->
            <div class="kanban-col border-t-4 border-t-amber-500">
                <div class="kanban-header">
                    <span>5. Direktur<br>Utama (BOD)</span>
                    <span class="bg-slate-100 text-slate-500 text-xs px-2 py-0.5 rounded-full">Rp 0</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card empty-placeholder">Tidak ada antrean</div>
                </div>
            </div>

            <!-- Col 6 -->
            <div class="kanban-col border-t-4 border-t-emerald-400">
                <div class="kanban-header">
                    <span>6. Verifikasi<br>Pajak/Finance</span>
                    <span class="bg-amber-100 text-amber-700 text-xs px-2 py-0.5 rounded-full">Rp 210jt</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card warning">
                        <div class="flex justify-between mb-2">
                            <span class="text-[9px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">INV-015</span>
                            <span class="text-[9px] font-bold text-amber-600"><i class="fas fa-exclamation-triangle"></i> Tersendat</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Reagen Maju</h5>
                        <div class="text-[11px] font-black text-amber-600 mb-1">Rp 210.000.000</div>
                        <p class="text-[9px] text-amber-700 leading-tight">Beda Nama Rekening</p>
                    </div>
                </div>
            </div>

            <!-- Col 7 -->
            <div class="kanban-col border-t-4 border-t-rose-500">
                <div class="kanban-header">
                    <span>7. Komite<br>Anggaran</span>
                    <span class="bg-rose-100 text-rose-700 text-xs px-2 py-0.5 rounded-full">Rp 1,2M</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card urgent">
                        <div class="flex justify-between mb-2">
                            <span class="text-[9px] font-bold text-rose-700 bg-rose-200 px-2 py-0.5 rounded">INV-2026-06-001</span>
                            <span class="text-[9px] font-bold text-rose-600 animate-pulse"><i class="fas fa-siren-on"></i> Macet 12hr!</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Medik Jaya</h5>
                        <div class="text-[11px] font-black text-rose-600 mb-1">Rp 1.200.000.000</div>
                        <p class="text-[9px] text-rose-700 leading-tight">Tunggu Pencairan BPJS</p>
                    </div>
                </div>
            </div>

            <!-- Col 8 -->
            <div class="kanban-col border-t-4 border-t-emerald-600">
                <div class="kanban-header">
                    <span>8. Kasir<br>(Eksekusi)</span>
                    <span class="bg-emerald-100 text-emerald-700 text-xs px-2 py-0.5 rounded-full">Rp 120jt</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card normal">
                        <div class="flex justify-between mb-2">
                            <span class="text-[9px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">INV-008</span>
                            <span class="text-[9px] font-bold text-emerald-600"><i class="fas fa-check-circle"></i></span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">CV ATK Kaltim</h5>
                        <div class="text-[11px] font-black text-emerald-600">Rp 120.000.000</div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    \n                    <!-- Mitigasi & Rekomendasi AI -->'''

    html = html[:match.start()] + new_kanban_html + html[match.end(2):]

    with open('fase7_invoice_3waymatch.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done fase7 update")

update_fase7()

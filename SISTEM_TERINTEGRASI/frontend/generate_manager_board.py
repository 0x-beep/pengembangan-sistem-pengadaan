import sys, re

def create():
    with open('finance_dashboard.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract everything up to the main content
    match_start = re.search(r'(<main class="p-6">|<div class="p-6">|<main.*?>)', html)
    if not match_start:
        print('Could not find main start')
        return

    head_and_sidebar = html[:match_start.end()]

    # Replace Title
    head_and_sidebar = head_and_sidebar.replace('<title>Finance & Payment Dashboard', '<title>Command Center Pengadaan')
    head_and_sidebar = head_and_sidebar.replace('text-emerald-600', 'text-blue-600').replace('text-emerald-700', 'text-blue-700')

    # Update Header Title
    head_and_sidebar = re.sub(r'<h1.*?</h1>', '<h1 class="text-2xl font-bold text-slate-800">Command Center Proses Pengadaan</h1>', head_and_sidebar)
    head_and_sidebar = re.sub(r'<p class="text-slate-500 mt-1">.*?</p>', '<p class="text-slate-500 mt-1">Pantau seluruh alur kerja tim pengadaan barang dan jasa secara real-time.</p>', head_and_sidebar)

    # User Profile in sidebar
    head_and_sidebar = re.sub(r'<p class="text-sm font-bold text-slate-800">.*?</p>', '<p class="text-sm font-bold text-slate-800">Manager Pengadaan</p>', head_and_sidebar)
    head_and_sidebar = re.sub(r'<p class="text-xs text-slate-500">.*?</p>', '<p class="text-xs text-slate-500">Kadep Pengadaan</p>', head_and_sidebar)

    # Update the Sidebar Link (Add Dashboard Manajer Pengadaan)
    # Let's insert a link under "INTERNAL PENGADAAN"
    new_link = '''
                    <a href="manager_pengadaan_dashboard.html" class="flex items-center gap-3 px-3 py-2.5 rounded-lg bg-blue-700 text-white shadow-md shadow-blue-900/20">
                        <i class="fas fa-desktop w-5 text-center"></i>
                        <span class="text-sm font-medium">Dashboard Manajer</span>
                    </a>
    '''
    head_and_sidebar = head_and_sidebar.replace('<div class="space-y-1">', '<div class="space-y-1">' + new_link, 1)

    kanban_css = '''
    <style>
        .kanban-board {
            display: grid;
            grid-template-columns: repeat(6, minmax(250px, 1fr));
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
            max-height: 70vh;
        }
        .kanban-header {
            padding: 0.75rem;
            border-bottom: 2px solid #e2e8f0;
            font-weight: 700;
            font-size: 0.875rem;
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
        }
        .k-card.warning {
            border-left: 4px solid #f59e0b;
        }
        .k-card.normal {
            border-left: 4px solid #3b82f6;
        }
    </style>
    '''

    board1_html = '''
    <!-- KASIE PENGADAAN BARANG -->
    <div class="mb-8 mt-4">
        <div class="flex items-center justify-between mb-4">
            <div>
                <h2 class="text-xl font-bold text-slate-800 flex items-center gap-2">
                    <i class="fas fa-boxes text-blue-600"></i> Pipeline: Pengadaan Barang
                </h2>
                <p class="text-sm text-slate-500 mt-1"><i class="fas fa-user-circle mr-1"></i> PIC: <strong>Kasim Ganteng</strong> (Kasie Pengadaan Barang)</p>
            </div>
            <div class="flex gap-2">
                <span class="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-xs font-bold">Total: 45 PP</span>
                <span class="px-3 py-1 bg-red-100 text-red-700 rounded-full text-xs font-bold">3 Urgent</span>
            </div>
        </div>

        <div class="kanban-board">
            <!-- Col 1 -->
            <div class="kanban-col border-t-4 border-t-slate-400">
                <div class="kanban-header">
                    <span>1. PP Masuk</span>
                    <span class="bg-slate-200 text-slate-600 text-xs px-2 py-0.5 rounded-full">12</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card normal">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-089</span>
                            <span class="text-[10px] font-bold text-emerald-600"><i class="fas fa-clock"></i> 1 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">Pengadaan Infus Pump</h5>
                        <p class="text-[11px] text-slate-500 mb-2">SBU Klinik Cito</p>
                        <div class="text-xs font-black text-blue-600">Rp 120.000.000</div>
                    </div>
                </div>
            </div>

            <!-- Col 2 -->
            <div class="kanban-col border-t-4 border-t-indigo-400">
                <div class="kanban-header">
                    <span>2. Bidding & Minta Penawaran</span>
                    <span class="bg-indigo-100 text-indigo-700 text-xs px-2 py-0.5 rounded-full">8</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card warning">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-081</span>
                            <span class="text-[10px] font-bold text-amber-600"><i class="fas fa-clock"></i> 4 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">Pengadaan Obat Farmasi</h5>
                        <p class="text-[11px] text-slate-500 mb-2">SBU Apotek Pusat</p>
                        <div class="text-[10px] text-amber-600 mt-1"><i class="fas fa-info-circle"></i> Menunggu 3 Penawaran</div>
                    </div>
                </div>
            </div>

            <!-- Col 3 -->
            <div class="kanban-col border-t-4 border-t-blue-500">
                <div class="kanban-header">
                    <span>3. Presentasi Vendor & Nego</span>
                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-0.5 rounded-full">5</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card normal">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-075</span>
                            <span class="text-[10px] font-bold text-emerald-600"><i class="fas fa-clock"></i> 3 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Transmedic Indonesia</h5>
                        <p class="text-[11px] text-slate-500 mb-2">USG 4D - SBU RS Utama</p>
                        <div class="text-[10px] text-blue-600 mt-1 font-bold"><i class="fas fa-handshake"></i> Jadwal Presentasi: Besok</div>
                    </div>
                </div>
            </div>

            <!-- Col 4 -->
            <div class="kanban-col border-t-4 border-t-purple-500">
                <div class="kanban-header">
                    <span>4. Draft PO</span>
                    <span class="bg-purple-100 text-purple-700 text-xs px-2 py-0.5 rounded-full">4</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card urgent">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-060</span>
                            <span class="text-[10px] font-bold text-red-600 animate-pulse"><i class="fas fa-exclamation-triangle"></i> 7 Hari!</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT BORNEO ETAM MANDIRI</h5>
                        <p class="text-[11px] text-slate-500 mb-2">Alat Bedah Minor</p>
                        <div class="text-[10px] text-red-600 mt-1"><i class="fas fa-file-contract"></i> Menyusun Klausul Draft PO</div>
                    </div>
                </div>
            </div>

            <!-- Col 5 -->
            <div class="kanban-col border-t-4 border-t-amber-500">
                <div class="kanban-header">
                    <span>5. Persetujuan Keuangan</span>
                    <span class="bg-amber-100 text-amber-700 text-xs px-2 py-0.5 rounded-full">6</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card normal">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PP-2026-055</span>
                            <span class="text-[10px] font-bold text-emerald-600"><i class="fas fa-clock"></i> 1 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT BTL Indonesia</h5>
                        <p class="text-[11px] text-slate-500 mb-2">Maintenance CT Scan</p>
                        <div class="text-[10px] text-amber-600 mt-1"><i class="fas fa-user-tie"></i> Menunggu TTD GM Keuangan</div>
                    </div>
                </div>
            </div>

            <!-- Col 6 -->
            <div class="kanban-col border-t-4 border-t-emerald-500">
                <div class="kanban-header">
                    <span>6. Selesai (PO Issued)</span>
                    <span class="bg-emerald-100 text-emerald-700 text-xs px-2 py-0.5 rounded-full">10</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card border-l-4 border-emerald-500 opacity-70">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">PO-2026-042</span>
                            <span class="text-[10px] font-bold text-slate-500"><i class="fas fa-check-circle text-emerald-500"></i></span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Capricorn Mulia</h5>
                        <p class="text-[11px] text-slate-500 mb-2">Sent to Vendor</p>
                    </div>
                </div>
            </div>

        </div>
    </div>
    '''

    board2_html = '''
    <!-- KASIE PENGADAAN JASA -->
    <div class="mb-8 mt-12 border-t border-slate-200 pt-8">
        <div class="flex items-center justify-between mb-4">
            <div>
                <h2 class="text-xl font-bold text-slate-800 flex items-center gap-2">
                    <i class="fas fa-tools text-indigo-600"></i> Pipeline: Pengadaan Jasa & Swakelola
                </h2>
                <p class="text-sm text-slate-500 mt-1"><i class="fas fa-user-circle mr-1"></i> PIC: <strong>Firman Utina</strong> (Kasie Pengadaan Jasa)</p>
            </div>
            <div class="flex gap-2">
                <span class="px-3 py-1 bg-indigo-100 text-indigo-700 rounded-full text-xs font-bold">Total: 18 PP</span>
                <span class="px-3 py-1 bg-red-100 text-red-700 rounded-full text-xs font-bold">1 Urgent</span>
            </div>
        </div>

        <div class="kanban-board">
            <!-- Col 1 -->
            <div class="kanban-col border-t-4 border-t-slate-400">
                <div class="kanban-header">
                    <span>1. PP & TOR Masuk</span>
                    <span class="bg-slate-200 text-slate-600 text-xs px-2 py-0.5 rounded-full">4</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card normal">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PPJ-2026-012</span>
                            <span class="text-[10px] font-bold text-emerald-600"><i class="fas fa-clock"></i> 2 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">Jasa Renovasi Toilet VIP</h5>
                        <p class="text-[11px] text-slate-500 mb-2">SBU RS Utama</p>
                    </div>
                </div>
            </div>

            <!-- Col 2 -->
            <div class="kanban-col border-t-4 border-t-indigo-400">
                <div class="kanban-header">
                    <span>2. Bidding Vendor Jasa</span>
                    <span class="bg-indigo-100 text-indigo-700 text-xs px-2 py-0.5 rounded-full">3</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card normal">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PPJ-2026-010</span>
                            <span class="text-[10px] font-bold text-emerald-600"><i class="fas fa-clock"></i> 3 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">Jasa Pembuatan SIstem Antrean</h5>
                        <p class="text-[11px] text-slate-500 mb-2">IT Department</p>
                    </div>
                </div>
            </div>

            <!-- Col 3 -->
            <div class="kanban-col border-t-4 border-t-blue-500">
                <div class="kanban-header">
                    <span>3. Aanwijzing & Presentasi</span>
                    <span class="bg-blue-100 text-blue-700 text-xs px-2 py-0.5 rounded-full">2</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card warning">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PPJ-2026-008</span>
                            <span class="text-[10px] font-bold text-amber-600"><i class="fas fa-clock"></i> 5 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">Cleaning Service Tahunan</h5>
                        <p class="text-[11px] text-slate-500 mb-2">SBU Klinik Cito</p>
                        <div class="text-[10px] text-blue-600 mt-1 font-bold"><i class="fas fa-users"></i> Presentasi 3 Vendor: Besok</div>
                    </div>
                </div>
            </div>

            <!-- Col 4 -->
            <div class="kanban-col border-t-4 border-t-purple-500">
                <div class="kanban-header">
                    <span>4. Negosiasi & Draft SPK</span>
                    <span class="bg-purple-100 text-purple-700 text-xs px-2 py-0.5 rounded-full">5</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card urgent">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PPJ-2026-004</span>
                            <span class="text-[10px] font-bold text-red-600 animate-pulse"><i class="fas fa-exclamation-triangle"></i> 8 Hari!</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">CV Akar Sakti</h5>
                        <p class="text-[11px] text-slate-500 mb-2">Sewa Tenda & Event Organizer HUT RS</p>
                        <div class="text-[10px] text-red-600 mt-1"><i class="fas fa-exclamation-circle"></i> Alot di Negosiasi Harga</div>
                    </div>
                </div>
            </div>

            <!-- Col 5 -->
            <div class="kanban-col border-t-4 border-t-amber-500">
                <div class="kanban-header">
                    <span>5. Persetujuan Keuangan</span>
                    <span class="bg-amber-100 text-amber-700 text-xs px-2 py-0.5 rounded-full">2</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card normal">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-slate-500 bg-slate-100 px-2 py-0.5 rounded">PPJ-2026-002</span>
                            <span class="text-[10px] font-bold text-emerald-600"><i class="fas fa-clock"></i> 1 Hari</span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Global Medik Persada</h5>
                        <p class="text-[11px] text-slate-500 mb-2">Jasa Kalibrasi Alkes</p>
                        <div class="text-[10px] text-amber-600 mt-1"><i class="fas fa-user-tie"></i> Menunggu TTD Dir. Keuangan</div>
                    </div>
                </div>
            </div>

            <!-- Col 6 -->
            <div class="kanban-col border-t-4 border-t-emerald-500">
                <div class="kanban-header">
                    <span>6. Selesai (SPK Issued)</span>
                    <span class="bg-emerald-100 text-emerald-700 text-xs px-2 py-0.5 rounded-full">2</span>
                </div>
                <div class="kanban-cards">
                    <div class="k-card border-l-4 border-emerald-500 opacity-70">
                        <div class="flex justify-between mb-2">
                            <span class="text-[10px] font-bold text-emerald-700 bg-emerald-100 px-2 py-0.5 rounded">SPK-2026-011</span>
                            <span class="text-[10px] font-bold text-slate-500"><i class="fas fa-check-circle text-emerald-500"></i></span>
                        </div>
                        <h5 class="font-bold text-xs text-slate-800 mb-1">PT Security Kaltim</h5>
                        <p class="text-[11px] text-slate-500 mb-2">Jasa Keamanan 2026</p>
                    </div>
                </div>
            </div>

        </div>
    </div>
    '''

    end_html = '</div>\n</body>\n</html>'

    final_html = head_and_sidebar + kanban_css + board1_html + board2_html + end_html

    with open('manager_pengadaan_dashboard.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Done")

create()

import re

def build_pipeline_html(is_dark=False):
    # Colors
    bg_color = "bg-[#0f172a]/50" if is_dark else "bg-white"
    bg_lane_label = "bg-slate-800/80" if is_dark else "bg-slate-50/80"
    border_lane = "border-slate-700/50" if is_dark else "border-slate-200"
    border_left_bg = "bg-slate-800 border-slate-700" if is_dark else "bg-slate-50 border-slate-200"
    text_muted = "text-slate-300" if is_dark else "text-slate-700"
    bg_node = "bg-slate-900" if is_dark else "bg-white"
    route_bg_inactive = "bg-slate-700" if is_dark else "bg-slate-200"
    
    # We will use w-full instead of min-w-[1400px] to prevent scrolling
    # X coordinates in percentage (0 to 100).
    # Since left menu is 36, we map the remaining width.
    x = [10, 30, 50, 70, 90]
    
    # Path logic:
    # SDM(x[0]) -> Gudang(x[0]) -> Manajer(x[1]) -> GMOps(x[2]) -> DirOps(x[3]) -> Dirut(x[2]) -> DirKeu(x[1]) -> GMKeu(x[1]) -> ManKeu(x[2]) -> Verif(x[3]) -> Komite(x[4])
    
    html = f"""
                        <div class="p-0 relative w-full overflow-hidden">
                            <div class="w-full flex flex-col relative {bg_color}">
                                
                                <!-- Background vertical lane borders -->
                                <div class="absolute left-0 top-0 bottom-0 w-28 {border_left_bg} border-r z-0"></div>

                                <!-- ZONA 1: DIREKSI (Top Lane) -->
                                <div class="flex relative z-10 border-b {border_lane} border-dashed h-28 items-stretch">
                                    <div class="w-28 flex-shrink-0 flex flex-col items-center justify-center border-l-4 border-amber-500 {bg_lane_label} p-2 z-20">
                                        <i class="fas fa-crown text-amber-500 text-lg mb-1"></i>
                                        <p class="text-[9px] font-bold text-amber-600 uppercase tracking-widest text-center">Zona<br>Direksi</p>
                                    </div>
                                    <div class="flex-1 relative h-full">
                                        <!-- Route Line (Dir Ops -> Dirut -> Dir Keu) -->
                                        <!-- From x[3] to x[1] going LEFT -->
                                        <div class="absolute left-[{x[1]}%] right-[{100-x[3]}%] top-1/2 h-1 {route_bg_inactive} -translate-y-1/2 z-0 rounded-full"></div>
                                        <i class="fas fa-chevron-left absolute left-[{x[2]}%] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-left absolute left-[{x[1]+10}%] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        
                                        <!-- Path coming up from GM Ops (x[2] to x[3]) -> we draw a diagonal or just a horizontal+vertical -->
                                        <!-- We'll draw vertical from Ops Lane x[2] to Dir Ops x[3] using a corner or diagonal -->
                                        <!-- Instead of diagonal, let's just make Dir Ops at x[2] to keep vertical straight? -->
                                        <!-- If Dir Ops is at x[2], it overlaps with GM Ops. Let's just drop a vertical line from DirOps x[3] to Ops Lane x[3] and connect GM Ops to x[3] in Ops Lane -->

                                        <!-- Node 5: Dir Ops -->
                                        <div class="absolute left-[{x[3]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-md mb-1 z-10 text-amber-500 font-bold text-xs">5</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Direktur<br>Operasi</h4>
                                        </div>

                                        <!-- Node 6: Dirut -->
                                        <div class="absolute left-[{x[2]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-md mb-1 z-10 text-amber-500 font-bold text-xs">6</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Direktur<br>Utama</h4>
                                        </div>

                                        <!-- Node 7: Dir Keuangan -->
                                        <div class="absolute left-[{x[1]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-md mb-1 z-10 text-amber-500 font-bold text-xs">7</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Direktur<br>Keuangan</h4>
                                        </div>
                                    </div>
                                </div>

                                <!-- ZONA 2: SDM & UMUM -->
                                <div class="flex relative z-10 border-b {border_lane} border-dashed h-28 items-stretch">
                                    <div class="w-28 flex-shrink-0 flex flex-col items-center justify-center border-l-4 border-violet-500 {bg_lane_label} p-2 z-20">
                                        <i class="fas fa-users-cog text-violet-500 text-lg mb-1"></i>
                                        <p class="text-[9px] font-bold text-violet-600 uppercase tracking-widest text-center">Zona<br>SDM/Umum</p>
                                    </div>
                                    <div class="flex-1 relative h-full">
                                        <!-- Path dropping to Ops -->
                                        <div class="absolute left-[{x[0]}%] top-1/2 h-28 w-1 bg-violet-500 z-0 -translate-x-1/2 shadow-[0_0_8px_rgba(139,92,246,0.5)]"></div>
                                        <i class="fas fa-chevron-down absolute left-[{x[0]}%] bottom-0 -translate-x-1/2 text-violet-500 z-10 text-[10px]"></i>

                                        <!-- Node 1: SDM/Umum -->
                                        <div class="absolute left-[{x[0]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-violet-500 flex items-center justify-center shadow-md mb-1 z-10 text-violet-500 font-bold text-xs">1</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Bagian<br>Umum</h4>
                                        </div>
                                    </div>
                                </div>

                                <!-- ZONA 3: OPERASIONAL -->
                                <div class="flex relative z-10 border-b {border_lane} border-dashed h-28 items-stretch">
                                    <div class="w-28 flex-shrink-0 flex flex-col items-center justify-center border-l-4 border-blue-500 {bg_lane_label} p-2 z-20">
                                        <i class="fas fa-boxes text-blue-500 text-lg mb-1"></i>
                                        <p class="text-[9px] font-bold text-blue-600 uppercase tracking-widest text-center">Zona<br>Operasi</p>
                                    </div>
                                    <div class="flex-1 relative h-full">
                                        <!-- Route Line -->
                                        <div class="absolute left-[{x[0]}%] right-[{100-x[3]}%] top-1/2 h-1 bg-blue-500 -translate-y-1/2 z-0 rounded-full shadow-[0_0_8px_rgba(59,130,246,0.5)]"></div>
                                        
                                        <!-- Path going UP to Dir Ops from x[3] -->
                                        <!-- It spans from Lane 3 center to Lane 1 center (Height = 28 + 28 = 56) -->
                                        <div class="absolute left-[{x[3]}%] bottom-1/2 h-56 w-1 bg-blue-500 z-0 -translate-x-1/2 shadow-[0_0_8px_rgba(59,130,246,0.5)]"></div>
                                        <i class="fas fa-chevron-up absolute left-[{x[3]}%] top-0 -translate-x-1/2 text-blue-200 z-10 text-[10px]"></i>
                                        
                                        <i class="fas fa-chevron-right absolute left-[{x[0]+10}%] top-1/2 -translate-y-1/2 text-blue-200 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{x[1]+10}%] top-1/2 -translate-y-1/2 text-blue-200 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{x[2]+10}%] top-1/2 -translate-y-1/2 text-blue-200 z-10 text-[10px]"></i>

                                        <!-- Node 2: Gudang -->
                                        <div class="absolute left-[{x[0]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-1 z-10 text-blue-500 font-bold text-xs">2</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Admin<br>3WM</h4>
                                        </div>

                                        <!-- Node 3: Manajer -->
                                        <div class="absolute left-[{x[1]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-1 z-10 text-blue-500 font-bold text-xs">3</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Manajer<br>Pengadaan</h4>
                                        </div>

                                        <!-- Node 4: GM Ops -->
                                        <div class="absolute left-[{x[2]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-1 z-10 text-blue-500 font-bold text-xs">4</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">GM<br>Operasi</h4>
                                        </div>
                                    </div>
                                </div>

                                <!-- ZONA 4: KEUANGAN -->
                                <div class="flex relative z-10 h-28 items-stretch">
                                    <div class="w-28 flex-shrink-0 flex flex-col items-center justify-center border-l-4 border-emerald-500 {bg_lane_label} p-2 z-20">
                                        <i class="fas fa-wallet text-emerald-600 text-lg mb-1"></i>
                                        <p class="text-[9px] font-bold text-emerald-600 uppercase tracking-widest text-center">Zona<br>Keuangan</p>
                                    </div>
                                    <div class="flex-1 relative h-full">
                                        <!-- Path dropping from Dir Keu (Lane 1 to Lane 4) -->
                                        <!-- Dir Keu is at x[1]. Drops 3 lanes (28 * 3 = 84px... wait h-28 is 112px per lane, 3 lanes = 336px) -->
                                        <div class="absolute left-[{x[1]}%] bottom-1/2 h-[336px] w-1 {route_bg_inactive} z-0 -translate-x-1/2"></div>
                                        <i class="fas fa-chevron-down absolute left-[{x[1]}%] top-0 -translate-x-1/2 text-slate-400 z-10 text-[10px]"></i>

                                        <!-- Route Line -->
                                        <div class="absolute left-[{x[1]}%] right-[{100-x[4]}%] top-1/2 h-1 {route_bg_inactive} -translate-y-1/2 z-0 rounded-full"></div>
                                        
                                        <i class="fas fa-chevron-right absolute left-[{x[1]+10}%] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{x[2]+10}%] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{x[3]+10}%] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>

                                        <!-- Node 8: GM Keuangan -->
                                        <div class="absolute left-[{x[1]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-1 z-10 text-emerald-500 font-bold text-xs">8</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">GM<br>Keuangan</h4>
                                        </div>

                                        <!-- Node 9: Manager Keuangan -->
                                        <div class="absolute left-[{x[2]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-1 z-10 text-emerald-500 font-bold text-xs">9</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Manager<br>Keuangan</h4>
                                        </div>

                                        <!-- Node 10: Verif Pajak -->
                                        <div class="absolute left-[{x[3]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-1 z-10 text-emerald-500 font-bold text-xs">10</div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Verif<br>Pajak/Finance</h4>
                                        </div>

                                        <!-- Node 11: Komite Anggaran (End) -->
                                        <div class="absolute left-[{x[4]}%] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-24 z-10">
                                            <div class="w-8 h-8 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-[0_0_15px_rgba(16,185,129,0.5)] mb-1 z-10 text-emerald-500 font-bold text-xs"><i class="fas fa-check"></i></div>
                                            <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Komite<br>Anggaran</h4>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>"""
    return html

def replace_in_file(filepath, is_dark=False):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return

    # Find the container using regex
    start_pattern = r'<div class="p-0 (overflow-x-auto relative|relative w-full overflow-hidden)">'
    end_pattern = r'(?P<end></div>\s*</div>\s*(?:</div>|<!-- SECTION 4|<!-- SECTION 3: LOG AUDIT|<div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden mb-8">))'
    
    match = re.search(f"{start_pattern}.*?{end_pattern}", content, re.DOTALL)
    if not match:
        print(f"Could not find replacement block in {filepath}")
        return
        
    new_html = build_pipeline_html(is_dark)
    end_text = match.group('end')
    
    replaced_content = content[:match.start()] + new_html + "\n                  " + end_text[12:] 
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(replaced_content)
    print(f"Successfully updated {filepath}")

if __name__ == "__main__":
    files = [
        ("finance_dashboard.html", False),
        ("director_dashboard.html", True),
        ("spi_audit_dashboard.html", False)
    ]
    for f, dark in files:
        replace_in_file(f, dark)

import re
import os

def build_pipeline_html(is_dark=False):
    # Colors
    bg_color = "bg-[#0f172a]/50" if is_dark else "bg-white"
    bg_lane_label = "bg-slate-800/80" if is_dark else "bg-slate-50/80"
    border_lane = "border-slate-700/50" if is_dark else "border-slate-200"
    border_left_bg = "bg-slate-800 border-slate-700" if is_dark else "bg-slate-50 border-slate-200"
    text_muted = "text-slate-300" if is_dark else "text-slate-700"
    bg_node = "bg-slate-900" if is_dark else "bg-white"
    route_bg_inactive = "bg-slate-700" if is_dark else "bg-slate-200"
    
    # Coordinates (px)
    px = [40, 160, 280, 400, 520, 640, 760, 880, 1000, 1120, 1240]
    
    html = f"""
                        <div class="p-0 overflow-x-auto relative">
                            <div class="min-w-[1400px] flex flex-col relative {bg_color}">
                                
                                <!-- Background vertical lane borders -->
                                <div class="absolute left-0 top-0 bottom-0 w-36 {border_left_bg} border-r z-0"></div>

                                <!-- ZONA 1: DIREKSI (Top Lane) -->
                                <div class="flex relative z-10 border-b {border_lane} border-dashed h-32 items-center">
                                    <div class="w-36 h-full flex-shrink-0 flex items-center justify-center border-l-4 border-amber-500 {bg_lane_label} p-4">
                                        <div class="text-center">
                                          <i class="fas fa-crown text-amber-500 text-lg mb-1"></i>
                                          <p class="text-[10px] font-bold text-amber-600 uppercase tracking-widest">Zona<br>Direksi</p>
                                        </div>
                                    </div>
                                    <div class="flex-1 relative h-full">
                                        <!-- Route Line -->
                                        <div class="absolute left-[{px[4]}px] right-[{1400-px[6]}px] top-1/2 h-1 {route_bg_inactive} -translate-y-1/2 z-0 rounded-full"></div>
                                        <i class="fas fa-chevron-right absolute left-[{px[4]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{px[5]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        
                                        <!-- Path coming up from Ops -->
                                        <div class="absolute left-[{px[4]}px] top-1/2 h-32 w-1 {route_bg_inactive} z-0 -translate-x-1/2"></div>
                                        
                                        <!-- Path going down to Keuangan -->
                                        <div class="absolute left-[{px[6]}px] top-1/2 h-[400px] w-1 {route_bg_inactive} z-0 -translate-x-1/2"></div>

                                        <!-- Node 5: Dir Ops -->
                                        <div class="absolute left-[{px[4]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-md mb-2 z-10 text-amber-500 font-bold">5</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Direktur<br>Operasi</h4>
                                        </div>

                                        <!-- Node 6: Dirut -->
                                        <div class="absolute left-[{px[5]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-md mb-2 z-10 text-amber-500 font-bold">6</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Direktur<br>Utama (BOD)</h4>
                                        </div>

                                        <!-- Node 7: Dir Keuangan -->
                                        <div class="absolute left-[{px[6]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-md mb-2 z-10 text-amber-500 font-bold">7</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Direktur<br>Keuangan</h4>
                                        </div>
                                    </div>
                                </div>

                                <!-- ZONA 2: SDM & UMUM -->
                                <div class="flex relative z-10 border-b {border_lane} border-dashed h-32 items-center">
                                    <div class="w-36 h-full flex-shrink-0 flex items-center justify-center border-l-4 border-violet-500 {bg_lane_label} p-4">
                                        <div class="text-center">
                                          <i class="fas fa-users-cog text-violet-500 text-lg mb-1"></i>
                                          <p class="text-[10px] font-bold text-violet-600 uppercase tracking-widest">Zona<br>SDM & Umum</p>
                                        </div>
                                    </div>
                                    <div class="flex-1 relative h-full">
                                        <!-- Path dropping to Ops -->
                                        <div class="absolute left-[{px[0]}px] top-1/2 h-32 w-1 bg-violet-500 z-0 -translate-x-1/2 shadow-[0_0_8px_rgba(139,92,246,0.5)]"></div>
                                        <i class="fas fa-chevron-down absolute left-[{px[0]}px] bottom-0 -translate-x-1/2 text-violet-500 z-10 text-[10px]"></i>

                                        <!-- Node 1: SDM/Umum -->
                                        <div class="absolute left-[{px[0]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-violet-500 flex items-center justify-center shadow-md mb-2 z-10 text-violet-500 font-bold">1</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Bagian<br>SDM / Umum</h4>
                                            <div class="mt-2 text-center w-full">
                                                <p class="text-xs font-black text-emerald-500">Rp 480jt</p>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- ZONA 3: OPERASIONAL -->
                                <div class="flex relative z-10 border-b {border_lane} border-dashed h-32 items-center">
                                    <div class="w-36 h-full flex-shrink-0 flex items-center justify-center border-l-4 border-blue-500 {bg_lane_label} p-4">
                                        <div class="text-center">
                                          <i class="fas fa-boxes text-blue-500 text-lg mb-1"></i>
                                          <p class="text-[10px] font-bold text-blue-600 uppercase tracking-widest">Zona<br>Operasional</p>
                                        </div>
                                    </div>
                                    <div class="flex-1 relative h-full">
                                        <!-- Route Line -->
                                        <div class="absolute left-[{px[0]}px] right-[{1400-px[3]}px] top-1/2 h-1 bg-blue-500 -translate-y-1/2 z-0 rounded-full shadow-[0_0_8px_rgba(59,130,246,0.5)]"></div>
                                        <div class="absolute left-[{px[3]}px] right-[{1400-px[4]}px] top-1/2 h-1 {route_bg_inactive} -translate-y-1/2 z-0 rounded-full"></div>
                                        
                                        <i class="fas fa-chevron-right absolute left-[{px[0]+50}px] top-1/2 -translate-y-1/2 text-blue-200 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{px[1]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{px[2]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{px[3]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>

                                        <!-- Node 2: Gudang -->
                                        <div class="absolute left-[{px[1]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-2 z-10 text-blue-500 font-bold">2</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Gudang / Admin<br>(3WM)</h4>
                                        </div>

                                        <!-- Node 3: Manajer -->
                                        <div class="absolute left-[{px[2]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-2 z-10 text-blue-500 font-bold">3</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Manajer<br>Pengadaan</h4>
                                        </div>

                                        <!-- Node 4: GM Ops -->
                                        <div class="absolute left-[{px[3]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-2 z-10 text-blue-500 font-bold">4</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">GM<br>Operasi</h4>
                                        </div>
                                    </div>
                                </div>

                                <!-- ZONA 4: KEUANGAN -->
                                <div class="flex relative z-10 h-32 items-center">
                                    <div class="w-36 h-full flex-shrink-0 flex items-center justify-center border-l-4 border-emerald-500 {bg_lane_label} p-4">
                                        <div class="text-center">
                                          <i class="fas fa-wallet text-emerald-600 text-lg mb-1"></i>
                                          <p class="text-[10px] font-bold text-emerald-600 uppercase tracking-widest">Zona<br>Keuangan</p>
                                        </div>
                                    </div>
                                    <div class="flex-1 relative h-full">
                                        <!-- Route Line -->
                                        <div class="absolute left-[{px[6]}px] right-[{1400-px[10]}px] top-1/2 h-1 {route_bg_inactive} -translate-y-1/2 z-0 rounded-full"></div>
                                        
                                        <i class="fas fa-chevron-right absolute left-[{px[6]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{px[7]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{px[8]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>
                                        <i class="fas fa-chevron-right absolute left-[{px[9]+50}px] top-1/2 -translate-y-1/2 text-slate-400 z-10 text-[10px]"></i>

                                        <!-- Node 8: GM Keuangan -->
                                        <div class="absolute left-[{px[7]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-2 z-10 text-emerald-500 font-bold">8</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">GM<br>Keuangan</h4>
                                        </div>

                                        <!-- Node 9: Manager Keuangan -->
                                        <div class="absolute left-[{px[8]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-2 z-10 text-emerald-500 font-bold">9</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Manager<br>Keuangan</h4>
                                        </div>

                                        <!-- Node 10: Verif Pajak -->
                                        <div class="absolute left-[{px[9]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-2 z-10 text-emerald-500 font-bold">10</div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Verifikasi<br>Pajak/Finance</h4>
                                        </div>

                                        <!-- Node 11: Komite Anggaran (End) -->
                                        <div class="absolute left-[{px[10]}px] top-1/2 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center w-28 z-10">
                                            <div class="w-10 h-10 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-[0_0_15px_rgba(16,185,129,0.5)] mb-2 z-10 text-emerald-500 font-bold"><i class="fas fa-check"></i></div>
                                            <h4 class="text-[10px] font-bold {text_muted} text-center leading-tight">Komite<br>Anggaran</h4>
                                            <div class="mt-2 text-center border border-rose-500/50 bg-rose-500/10 p-1.5 rounded relative animate-pulse w-full">
                                                <p class="text-xs font-black text-rose-500">Rp 1,2M</p>
                                                <p class="text-[8px] font-bold text-rose-600 uppercase mt-0.5 leading-tight">Macet<br><span class="text-[7px] text-rose-600/80 normal-case font-medium">Tunggu BPJS</span></p>
                                            </div>
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
    # It starts with <div class="p-0 overflow-x-auto relative">
    # and ends right before </div></div>\n                  <!-- SECTION 4 or <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden mb-8">
    
    start_pattern = r'<div class="p-0 overflow-x-auto relative">'
    end_pattern = r'(?P<end></div>\s*</div>\s*(?:</div>|<!-- SECTION 4|<!-- SECTION 3: LOG AUDIT|<div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden mb-8">))'
    
    # We will search for the entire block
    match = re.search(f"{start_pattern}.*?{end_pattern}", content, re.DOTALL)
    if not match:
        print(f"Could not find replacement block in {filepath}")
        return
        
    new_html = build_pipeline_html(is_dark)
    end_text = match.group('end')
    
    # Actually the new_html already closes its own tags. It opens 2 divs: <div p-0><div min-w-1400> and closes them.
    # Wait, my build_pipeline_html closes </div></div> at the end.
    
    replaced_content = content[:match.start()] + new_html + "\n                  " + end_text[12:] # 12 is length of </div></div>
    
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

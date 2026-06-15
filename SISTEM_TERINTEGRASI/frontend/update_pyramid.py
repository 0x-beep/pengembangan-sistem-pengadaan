import re

def build_pipeline_html(is_dark=False):
    # Colors
    bg_color = "bg-[#0f172a]/80" if is_dark else "bg-white"
    bg_zona_bar = "bg-slate-800 border-slate-700" if is_dark else "bg-slate-50 border-slate-200"
    text_muted = "text-slate-300" if is_dark else "text-slate-700"
    text_muted_light = "text-slate-400" if is_dark else "text-slate-500"
    bg_node = "bg-slate-900" if is_dark else "bg-white"
    route_stroke = "#334155" if is_dark else "#cbd5e1"
    
    # X and Y positions
    # 11 Nodes
    x_pc = [4.5, 13.6, 22.7, 31.8, 40.9, 50.0, 59.1, 68.2, 77.3, 86.4, 95.5]
    x_svg = [int(p * 10) for p in x_pc] # 0 to 1000
    
    y_px = {
        'L1': 60,   # Direksi
        'L2': 160,  # GM
        'L3': 260,  # Manajer
        'L4': 360   # Admin/Umum
    }
    
    # Levels for each node
    levels = [
        'L4', # 1. SDM
        'L4', # 2. Gudang
        'L3', # 3. Manajer
        'L2', # 4. GM Ops
        'L1', # 5. Dir Ops
        'L1', # 6. Dirut
        'L1', # 7. Dir Keu
        'L2', # 8. GM Keu
        'L3', # 9. Man Keu
        'L4', # 10. Verif
        'L4'  # 11. Komite
    ]
    
    # SVG polyline points string
    points = " ".join([f"{x_svg[i]},{y_px[levels[i]]}" for i in range(11)])
    
    html = f"""
                        <div class="p-0 relative w-full overflow-hidden rounded-b-xl {bg_color}">
                            
                            <!-- Main Container -->
                            <div class="w-full relative h-[450px]">
                                
                                <!-- SVG Background for Lines -->
                                <svg class="absolute inset-0 w-full h-full pointer-events-none z-0" viewBox="0 0 1000 450" preserveAspectRatio="none">
                                    <!-- Glow effect -->
                                    <polyline points="{points}" fill="none" stroke="{route_stroke}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
                                    <!-- Animated Dash Line (optional, simple style) -->
                                    <polyline points="{points}" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="10 10" class="animate-[dash_20s_linear_infinite]" opacity="0.7"/>
                                </svg>
                                
                                <style>
                                @keyframes dash {{
                                  to {{
                                    stroke-dashoffset: -1000;
                                  }}
                                }}
                                </style>

                                <!-- Y-Axis Background Labels (Optional, faint lines for levels) -->
                                <div class="absolute left-0 right-0 top-[60px] h-px bg-slate-200/50 border-dashed z-0"></div>
                                <div class="absolute left-0 right-0 top-[160px] h-px bg-slate-200/50 border-dashed z-0"></div>
                                <div class="absolute left-0 right-0 top-[260px] h-px bg-slate-200/50 border-dashed z-0"></div>
                                <div class="absolute left-0 right-0 top-[360px] h-px bg-slate-200/50 border-dashed z-0"></div>

                                <!-- Node 1: SDM/Umum -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[0]}%; top: {y_px[levels[0]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-violet-500 flex items-center justify-center shadow-md mb-1 z-10 text-violet-500 font-bold text-xs relative">1</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Bagian<br>Umum</h4>
                                </div>

                                <!-- Node 2: Gudang -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[1]}%; top: {y_px[levels[1]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-1 z-10 text-blue-500 font-bold text-xs relative">2</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Admin<br>3WM</h4>
                                </div>

                                <!-- Node 3: Manajer -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[2]}%; top: {y_px[levels[2]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-1 z-10 text-blue-500 font-bold text-xs relative">3</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Manajer<br>Pengadaan</h4>
                                </div>

                                <!-- Node 4: GM Ops -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[3]}%; top: {y_px[levels[3]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-blue-500 flex items-center justify-center shadow-md mb-1 z-10 text-blue-500 font-bold text-xs relative">4</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">GM<br>Operasi</h4>
                                </div>

                                <!-- Node 5: Dir Ops -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[4]}%; top: {y_px[levels[4]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-md mb-1 z-10 text-amber-500 font-bold text-xs relative">5</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Direktur<br>Operasi</h4>
                                </div>

                                <!-- Node 6: Dirut -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[5]}%; top: {y_px[levels[5]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-[0_0_15px_rgba(245,158,11,0.5)] mb-1 z-10 text-amber-500 font-bold text-xs scale-110 relative">6</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Direktur<br>Utama</h4>
                                </div>

                                <!-- Node 7: Dir Keuangan -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[6]}%; top: {y_px[levels[6]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-amber-500 flex items-center justify-center shadow-md mb-1 z-10 text-amber-500 font-bold text-xs relative">7</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Direktur<br>Keuangan</h4>
                                </div>

                                <!-- Node 8: GM Keuangan -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[7]}%; top: {y_px[levels[7]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-1 z-10 text-emerald-500 font-bold text-xs relative">8</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">GM<br>Keuangan</h4>
                                </div>

                                <!-- Node 9: Manajer Keuangan -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[8]}%; top: {y_px[levels[8]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-1 z-10 text-emerald-500 font-bold text-xs relative">9</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Manager<br>Keuangan</h4>
                                </div>

                                <!-- Node 10: Verif Pajak -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[9]}%; top: {y_px[levels[9]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-md mb-1 z-10 text-emerald-500 font-bold text-xs relative">10</div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Verif<br>Pajak</h4>
                                </div>

                                <!-- Node 11: Komite Anggaran -->
                                <div class="absolute w-24 h-24 -translate-x-1/2 -translate-y-1/2 flex flex-col items-center z-10" style="left: {x_pc[10]}%; top: {y_px[levels[10]]}px;">
                                    <div class="w-8 h-8 rounded-full {bg_node} border-2 border-emerald-500 flex items-center justify-center shadow-[0_0_15px_rgba(16,185,129,0.5)] mb-1 z-10 text-emerald-500 font-bold text-xs relative"><i class="fas fa-check"></i></div>
                                    <h4 class="text-[9px] font-bold {text_muted} text-center leading-tight">Komite<br>Anggaran</h4>
                                </div>
                                
                                <!-- X-Axis ZONA Bar at the bottom -->
                                <div class="absolute bottom-0 left-0 right-0 h-10 {bg_zona_bar} border-t flex z-20">
                                    <!-- Zona SDM (Node 1) -> 9.1% wide -->
                                    <div class="w-[9.1%] flex items-center justify-center border-r border-slate-300/30">
                                        <span class="text-[9px] font-bold text-violet-500 uppercase tracking-wider"><i class="fas fa-users mr-1"></i> SDM/Umum</span>
                                    </div>
                                    <!-- Zona Operasional (Node 2,3,4) -> 27.3% wide -->
                                    <div class="w-[27.3%] flex items-center justify-center border-r border-slate-300/30">
                                        <span class="text-[9px] font-bold text-blue-500 uppercase tracking-wider"><i class="fas fa-boxes mr-1"></i> Operasional</span>
                                    </div>
                                    <!-- Zona Direksi (Node 5,6,7) -> 27.3% wide -->
                                    <div class="w-[27.3%] flex items-center justify-center border-r border-slate-300/30">
                                        <span class="text-[9px] font-bold text-amber-500 uppercase tracking-wider"><i class="fas fa-crown mr-1"></i> Direksi (BOD)</span>
                                    </div>
                                    <!-- Zona Keuangan (Node 8,9,10,11) -> 36.3% wide -->
                                    <div class="w-[36.3%] flex items-center justify-center">
                                        <span class="text-[9px] font-bold text-emerald-500 uppercase tracking-wider"><i class="fas fa-wallet mr-1"></i> Keuangan</span>
                                    </div>
                                </div>
                                
                                <!-- Y-Axis Level Labels (left side) -->
                                <div class="absolute left-2 top-[50px] text-[8px] font-bold uppercase tracking-widest {text_muted_light}">Level Direksi</div>
                                <div class="absolute left-2 top-[150px] text-[8px] font-bold uppercase tracking-widest {text_muted_light}">Level General Manajer</div>
                                <div class="absolute left-2 top-[250px] text-[8px] font-bold uppercase tracking-widest {text_muted_light}">Level Manajer</div>
                                <div class="absolute left-2 top-[350px] text-[8px] font-bold uppercase tracking-widest {text_muted_light}">Level Staf / Admin</div>
                                
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
    start_pattern = r'<div class="p-0 (overflow-x-auto relative|relative w-full overflow-hidden).*?">'
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

import re
with open('vendor_hub.html', 'r', encoding='utf-8') as f:
    html = f.read()

login_modal = '''
    <!-- Login Simulation Modal -->
    <div id='loginModal' class='fixed inset-0 bg-slate-900/80 backdrop-blur-sm hidden z-50 flex items-center justify-center opacity-0 transition-opacity duration-300'>
        <div class='bg-slate-800 border border-slate-700 rounded-2xl p-8 max-w-md w-full shadow-2xl transform scale-95 transition-transform duration-300' id='loginModalContent'>
            <div class='flex justify-between items-center mb-6'>
                <h3 class='text-2xl font-bold text-white' id='loginTitle'>Login Vendor</h3>
                <button onclick='closeLogin()' class='text-slate-400 hover:text-white'><i class='fas fa-times'></i></button>
            </div>
            <div class='space-y-4'>
                <div>
                    <label class='block text-sm font-medium text-slate-300 mb-1'>Username / NPWP</label>
                    <input type='text' id='loginUser' class='w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-blue-500' value='PT_KIMIA_FARMA'>
                </div>
                <div>
                    <label class='block text-sm font-medium text-slate-300 mb-1'>Password</label>
                    <input type='password' class='w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-white focus:outline-none focus:border-blue-500' value='********'>
                </div>
                <button onclick='executeLogin()' class='w-full bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white font-bold py-3 px-4 rounded-xl transition shadow-lg mt-4'>Login ke Workspace</button>
            </div>
        </div>
    </div>
    
    <script>
        let targetUrl = '';
        function openLogin(title, defaultUser, url) {
            document.getElementById('loginTitle').innerText = title;
            document.getElementById('loginUser').value = defaultUser;
            targetUrl = url;
            const modal = document.getElementById('loginModal');
            modal.classList.remove('hidden');
            setTimeout(() => {
                modal.classList.remove('opacity-0');
                document.getElementById('loginModalContent').classList.remove('scale-95');
            }, 10);
        }
        function closeLogin() {
            const modal = document.getElementById('loginModal');
            modal.classList.add('opacity-0');
            document.getElementById('loginModalContent').classList.add('scale-95');
            setTimeout(() => {
                modal.classList.add('hidden');
            }, 300);
        }
        function executeLogin() {
            window.location.href = targetUrl;
        }
    </script>
'''

if 'loginModal' not in html:
    html = html.replace('</body>', login_modal + '\n</body>')

    # Replace direct links with onclick using lambda to avoid regex escaping hell
    html = html.replace('<a href="vendor_portal.html" class="glass-card rounded-2xl p-8 relative overflow-hidden group cursor-pointer block">', 
                        '<div onclick="openLogin(\'Login Vendor Farmasi & BMHP\', \'PT_ENSEVAL_MEDIKA\', \'vendor_portal.html\')" class="glass-card rounded-2xl p-8 relative overflow-hidden group cursor-pointer block">')
                        
    html = html.replace('<a href="vendor_kso_lab_portal.html" class="glass-card rounded-2xl p-8 relative overflow-hidden group cursor-pointer block">', 
                        '<div onclick="openLogin(\'Login Mitra KSO Lab\', \'PT_PRODIA_WIDYAHUSADA\', \'vendor_kso_lab_portal.html\')" class="glass-card rounded-2xl p-8 relative overflow-hidden group cursor-pointer block">')

    # Convert closing </a> to </div> for the replaced links
    # Just a simple string replace is safer since we know the structure
    html = html.replace('''            <div class="absolute bottom-8 right-8 text-blue-400 opacity-0 group-hover:opacity-100 transform translate-x-4 group-hover:translate-x-0 transition-all duration-300">
                <i class="fas fa-arrow-right text-xl"></i>
            </div>
        </a>''', 
        '''            <div class="absolute bottom-8 right-8 text-blue-400 opacity-0 group-hover:opacity-100 transform translate-x-4 group-hover:translate-x-0 transition-all duration-300">
                <i class="fas fa-arrow-right text-xl"></i>
            </div>
        </div>''')

    html = html.replace('''            <div class="absolute bottom-8 right-8 text-amber-400 opacity-0 group-hover:opacity-100 transform translate-x-4 group-hover:translate-x-0 transition-all duration-300">
                <i class="fas fa-arrow-right text-xl"></i>
            </div>
        </a>''', 
        '''            <div class="absolute bottom-8 right-8 text-amber-400 opacity-0 group-hover:opacity-100 transform translate-x-4 group-hover:translate-x-0 transition-all duration-300">
                <i class="fas fa-arrow-right text-xl"></i>
            </div>
        </div>''')

    with open('vendor_hub.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Vendor hub updated")
else:
    print("Already updated")

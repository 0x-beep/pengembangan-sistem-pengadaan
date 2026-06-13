import os
import glob

os.chdir(r"D:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend")
files = glob.glob("*.html")

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "ai_guardian_placeholder.html" in content:
        new_content = content.replace("ai_guardian_placeholder.html", "ai_guardian.html")
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")

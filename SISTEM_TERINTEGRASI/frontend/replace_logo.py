import os
import glob

directory = r"d:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend"
html_files = glob.glob(os.path.join(directory, "*.html"))

count = 0
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'logo_kmu_1.png' in content:
        new_content = content.replace('logo_kmu_1.png', 'logo_kmu.png')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {os.path.basename(filepath)}")

print(f"Successfully updated {count} files.")

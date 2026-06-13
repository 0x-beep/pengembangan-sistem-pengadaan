import fitz
import os

pdf_path = r"D:\digitalisasi_pengadan\A_INTERNAL_DEPT_PENGADAAN\LAPISAN_AI_PENJAGA_SPO\SPO dan Pedoman\Pedoman Rev\Pedoman Pengadaan rev1.docx.pdf"
out_dir = r"D:\digitalisasi_pengadan\SISTEM_TERINTEGRASI\frontend"

doc = fitz.open(pdf_path)

# Extract images from first 3 pages
image_count = 0
for i in range(min(3, len(doc))):
    page = doc[i]
    image_list = page.get_images(full=True)
    
    for img_index, img in enumerate(image_list):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        
        # Save first image as logo_kmu.png, others as _2, _3
        if image_count == 0:
            out_path = os.path.join(out_dir, "logo_kmu.png")
        else:
            out_path = os.path.join(out_dir, f"logo_kmu_{image_count}.png")
            
        with open(out_path, "wb") as f:
            f.write(image_bytes)
        
        print(f"Extracted image to {out_path}")
        image_count += 1
        
if image_count == 0:
    print("No images found in the PDF.")

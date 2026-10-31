import os
import pypdfium2 as pdfium

pdf_path = "version2/Audition Slides - preview.pdf"
pdf = pdfium.PdfDocument(pdf_path)
print(f"Total pages: {len(pdf)}")

os.makedirs("version3/slides_png", exist_ok=True)
for i, page in enumerate(pdf):
    # 1920x1080 is 16:9
    # Render with high scale
    bitmap = page.render(scale=1920/page.get_size()[0])
    pil_image = bitmap.to_pil()
    # Resize to exact 1920x1080
    pil_image = pil_image.resize((1920, 1080))
    out_path = f"version3/slides_png/slide_{i+1:02d}.png"
    pil_image.save(out_path)
    print(f"Rendered Page {i+1} -> {out_path} ({pil_image.size})")

print("All PDF pages rendered to 1920x1080 PNG!")

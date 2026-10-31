import os
from PIL import Image, JpegImagePlugin, PngImagePlugin

slide_files = [f"version3/slides_png/slide_{i:02d}.png" for i in range(1, 12)]
images = [Image.open(f).convert("RGB") for f in slide_files]

pdf_out = "version3/Audition Slides - preview.pdf"
images[0].save(pdf_out, save_all=True, append_images=images[1:])
print(f"Updated {pdf_out} successfully!")

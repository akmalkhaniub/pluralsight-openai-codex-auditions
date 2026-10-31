import os
import win32com.client

pptx_path = os.path.abspath("version3/Audition Slides - Akmal Khan - Code Review v3.pptx")
slides_dir = os.path.abspath("version3/slides_png")
os.makedirs(slides_dir, exist_ok=True)

print(f"Checking file exists: {os.path.exists(pptx_path)}")
ppt_app = win32com.client.Dispatch("PowerPoint.Application")
try:
    pres = ppt_app.Presentations.Open(pptx_path, 1, 0, 1) # ReadOnly=1, Untitled=0, WithWindow=1
    print(f"Presentation opened. Count: {pres.Slides.Count}")
    
    # Save PDF
    pdf_path = os.path.abspath("version3/Audition Slides - preview.pdf")
    pres.SaveAs(pdf_path, 32)
    print(f"Exported PDF to {pdf_path}")
    
    for i in range(1, pres.Slides.Count + 1):
        slide = pres.Slides(i)
        out_png = os.path.join(slides_dir, f"slide_{i:02d}.png")
        slide.Export(out_png, "PNG", 1920, 1080)
        print(f"Exported Slide {i}")
        
    pres.Close()
    print("Done exporting!")
except Exception as e:
    print(f"Error: {e}")
finally:
    try:
        ppt_app.Quit()
    except:
        pass

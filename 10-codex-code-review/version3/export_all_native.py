import os
import shutil
import win32com.client

local_in = os.path.expanduser(r"~\Documents\slides_v3_export.pptx")
shutil.copy2("version3/Audition Slides - Akmal Khan - Code Review v3.pptx", local_in)

ppt_app = win32com.client.DispatchEx("PowerPoint.Application")
try:
    pres = ppt_app.Presentations.Open(local_in, False, False, False)
    print(f"PowerPoint opened presentation. Slides: {pres.Slides.Count}")
    
    # Export all 11 slides as PNG
    slides_dir = os.path.abspath("version3/slides_png")
    os.makedirs(slides_dir, exist_ok=True)
    for i in range(1, pres.Slides.Count + 1):
        s_out = os.path.expanduser(rf"~\Documents\slide_{i:02d}.png")
        pres.Slides(i).Export(s_out, "PNG", 1920, 1080)
        shutil.copy2(s_out, os.path.join(slides_dir, f"slide_{i:02d}.png"))
        if os.path.exists(s_out):
            os.remove(s_out)
        print(f"Exported Slide {i:02d} -> slide_{i:02d}.png")

    # Export PDF
    pdf_out = os.path.expanduser(r"~\Documents\preview.pdf")
    pres.SaveAs(pdf_out, 32) # 32 = ppSaveAsPDF
    shutil.copy2(pdf_out, "version3/Audition Slides - preview.pdf")
    if os.path.exists(pdf_out):
        os.remove(pdf_out)
    print("Exported updated Audition Slides - preview.pdf successfully!")

    pres.Close()
except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    if os.path.exists(local_in):
        os.remove(local_in)
    ppt_app.Quit()

import os
import shutil
import win32com.client

local_in = os.path.expanduser(r"~\Documents\slides_v3_clean.pptx")
shutil.copy2("version3/Audition Slides - Akmal Khan - Code Review v3.pptx", local_in)

ppt_app = win32com.client.DispatchEx("PowerPoint.Application")
try:
    pres = ppt_app.Presentations.Open(local_in, False, False, False)
    print(f"POWERPOINT OPENED CLEANLY! Slides count: {pres.Slides.Count}")
    # Export slide 4 to PNG
    local_out = os.path.expanduser(r"~\Documents\slide_04_native.png")
    pres.Slides(4).Export(local_out, "PNG", 1920, 1080)
    shutil.copy2(local_out, "version3/slides_png/slide_04.png")
    print("SUCCESS: Native slide 4 exported perfectly by PowerPoint!")
    
    # Also export all slides from PowerPoint directly!
    for i in range(1, pres.Slides.Count + 1):
        s_out = os.path.expanduser(rf"~\Documents\slide_{i:02d}.png")
        pres.Slides(i).Export(s_out, "PNG", 1920, 1080)
        shutil.copy2(s_out, f"version3/slides_png/slide_{i:02d}.png")
        if os.path.exists(s_out):
            os.remove(s_out)
    print("All 11 slides exported directly by PowerPoint native engine!")

    # Export preview PDF from PowerPoint
    pdf_out = os.path.expanduser(r"~\Documents\preview.pdf")
    pres.SaveAs(pdf_out, 32) # 32 = ppSaveAsPDF
    shutil.copy2(pdf_out, "version3/Audition Slides - preview.pdf")
    print("Exported native PowerPoint preview.pdf successfully!")
    if os.path.exists(pdf_out):
        os.remove(pdf_out)

    pres.Close()
except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    if os.path.exists(local_in):
        os.remove(local_in)
    ppt_app.Quit()

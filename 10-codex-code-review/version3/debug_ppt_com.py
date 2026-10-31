import os
import win32com.client
import pythoncom

pythoncom.CoInitialize()
try:
    ppt_app = win32com.client.DispatchEx("PowerPoint.Application")
    ppt_app.Visible = True
    abs_path = os.path.normpath(os.path.abspath("version3/Audition Slides - Akmal Khan - Code Review v3.pptx"))
    print(f"Trying to open: {abs_path}")
    pres = ppt_app.Presentations.Open(abs_path, False, False, True)
    print(f"SUCCESS! Slides: {pres.Slides.Count}")
    # Export slide 4 to PNG
    pres.Slides(4).Export(os.path.abspath("version3/slide_04_ppt.png"), "PNG", 1920, 1080)
    print("Exported slide 4 directly from PowerPoint!")
    pres.Close()
    ppt_app.Quit()
except Exception as e:
    import traceback
    traceback.print_exc()

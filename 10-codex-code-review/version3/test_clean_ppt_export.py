import os
import shutil
import win32com.client

# Copy to local Documents
local_in = os.path.expanduser(r"~\Documents\slides_v3.pptx")
shutil.copy2("version3/Audition Slides - Akmal Khan - Code Review v3.pptx", local_in)

ppt_app = win32com.client.DispatchEx("PowerPoint.Application")
try:
    pres = ppt_app.Presentations.Open(local_in, False, False, False)
    # Export slide 4 to PNG
    local_out = os.path.expanduser(r"~\Documents\slide_04_native.png")
    pres.Slides(4).Export(local_out, "PNG", 1920, 1080)
    shutil.copy2(local_out, "version3/slides_png/slide_04_native.png")
    print("Exported native slide 4 from PowerPoint successfully!")
    pres.Close()
except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    if os.path.exists(local_in):
        os.remove(local_in)
    ppt_app.Quit()

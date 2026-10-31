import os
import shutil
import tempfile
import win32com.client

ppt_app = win32com.client.Dispatch("PowerPoint.Application")
try:
    ppt_app.Visible = 1
except:
    pass

for p in [
    os.path.abspath("version2/Audition Slides - Akmal Khan - Code Review v2.pptx"),
    os.path.abspath("version3/Audition Slides - Akmal Khan - Code Review v3.pptx")
]:
    print(f"Testing {p}...")
    try:
        pres = ppt_app.Presentations.Open(p)
        print(f"Success! Slide count = {pres.Slides.Count}")
        pres.Close()
    except Exception as e:
        print(f"Failed: {e}")

try:
    ppt_app.Quit()
except:
    pass

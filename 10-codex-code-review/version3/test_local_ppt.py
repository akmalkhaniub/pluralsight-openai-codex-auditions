import os
import shutil
import win32com.client

ppt_app = win32com.client.DispatchEx("PowerPoint.Application")
# Copy to local C: drive
local_path = os.path.expanduser(r"~\Documents\test_slide.pptx")
shutil.copy2("version2/Audition Slides - Akmal Khan - Code Review v2.pptx", local_path)
print(f"Copied to local: {local_path}")
try:
    pres = ppt_app.Presentations.Open(local_path)
    print("SUCCESS on local path!")
    pres.Close()
except Exception as e:
    print(f"Error on local path: {e}")
finally:
    if os.path.exists(local_path):
        os.remove(local_path)
    ppt_app.Quit()

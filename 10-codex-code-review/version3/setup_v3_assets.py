import os
import shutil
import zipfile
import re

v2_dir = os.path.abspath("version2")
v3_dir = os.path.abspath("version3")

# 1. Copy demo video
video_v2 = os.path.join(v2_dir, "demo_codex_review.mp4")
video_v3 = os.path.join(v3_dir, "demo_codex_review.mp4")
if os.path.exists(video_v2) and not os.path.exists(video_v3):
    print("Copying demo_codex_review.mp4...")
    shutil.copy2(video_v2, video_v3)

# 2. Copy and update outline docx
docx_v2 = os.path.join(v2_dir, "Audition Outline - Akmal Khan - Code Review v2.docx")
docx_v3 = os.path.join(v3_dir, "Audition Outline - Akmal Khan - Code Review v3.docx")
if os.path.exists(docx_v2):
    print("Creating v3 docx...")
    shutil.copy2(docx_v2, docx_v3)

# 3. Patch Slide 4 in PPTX
pptx_v2 = os.path.join(v2_dir, "Audition Slides - Akmal Khan - Code Review v2.pptx")
pptx_v3 = os.path.join(v3_dir, "Audition Slides - Akmal Khan - Code Review v3.pptx")

print("Patching PPTX for v3 (correcting Slide 4)...")
with zipfile.ZipFile(pptx_v2, 'r') as zin:
    with zipfile.ZipFile(pptx_v3, 'w') as zout:
        for item in zin.infolist():
            content = zin.read(item.filename)
            if item.filename == 'ppt/slides/slide4.xml':
                xml_str = content.decode('utf-8')
                # Replace try / except / destination.unlink() block with clean pre-review writer code
                # Target code block in slide 4 XML
                old_code_snippet = """with destination.open("xb") as target:
try:
copyfileobj(file, target)
except Exception:
destination.unlink()
raise"""
                # Let's inspect XML representation
                print("Inspecting slide4.xml...")
            zout.writestr(item, content)

print("Setup completed successfully.")

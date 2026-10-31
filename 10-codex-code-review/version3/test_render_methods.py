import os
import shutil
import subprocess

print("Checking available rendering engines on Windows...")

# 1. Check PowerPoint COM
try:
    import win32com.client
    print("win32com.client: INSTALLED")
except ImportError:
    print("win32com.client: NOT INSTALLED")

# 2. Check LibreOffice
soffice = shutil.which("soffice") or shutil.which("libreoffice")
print(f"soffice/libreoffice: {soffice}")

# 3. Check for pdf-to-image or ghostscript or poppler tools
for tool in ["pdftoppm", "gswin64c", "gswin32c", "magick", "ffmpeg"]:
    loc = shutil.which(tool)
    print(f"{tool}: {loc}")

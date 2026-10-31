import sys
import zipfile
import xml.etree.ElementTree as ET
import os
import shutil
import win32com.client

pptx_path = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"

zin = zipfile.ZipFile(pptx_path, 'r')
files = {name: zin.read(name) for name in zin.namelist()}
zin.close()

namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}
ET.register_namespace('p', 'http://schemas.openxmlformats.org/presentationml/2006/main')
ET.register_namespace('a', 'http://schemas.openxmlformats.org/drawingml/2006/main')
ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')

tree = ET.fromstring(files['ppt/slides/slide5.xml'])
for sp in tree.findall('.//p:sp', namespaces):
    name = sp.find('.//p:cNvPr', namespaces).get('name')
    if name in ['Oval 2', 'Oval 5']:
        for p in sp.findall('.//a:p', namespaces):
            for r in p.findall('.//a:r', namespaces):
                # Ensure rPr exists and specifies Segoe UI Emoji
                rPr = r.find('a:rPr', namespaces)
                if rPr is None:
                    rPr = ET.Element('{http://schemas.openxmlformats.org/drawingml/2006/main}rPr')
                    r.insert(0, rPr)
                rPr.set('sz', '5600')
                # Add latin, ea, cs font elements
                for font_tag in ['latin', 'ea', 'cs']:
                    f_elem = rPr.find(f'a:{font_tag}', namespaces)
                    if f_elem is None:
                        f_elem = ET.SubElement(rPr, f'{{http://schemas.openxmlformats.org/drawingml/2006/main}}{font_tag}')
                    f_elem.set('typeface', 'Segoe UI Emoji')

files['ppt/slides/slide5.xml'] = ET.tostring(tree, encoding='utf-8', xml_declaration=True)

with zipfile.ZipFile(pptx_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for name, data in files.items():
        zout.writestr(name, data)

print("Updated Oval 2 and Oval 5 with explicit Segoe UI Emoji font!")

# Now test export with PowerPoint
local_in = os.path.expanduser(r"~\Documents\test_emoji.pptx")
shutil.copy2(pptx_path, local_in)

ppt_app = win32com.client.DispatchEx("PowerPoint.Application")
try:
    pres = ppt_app.Presentations.Open(local_in, False, False, False)
    test_png = os.path.expanduser(r"~\Documents\test_slide_05.png")
    pres.Slides(5).Export(test_png, "PNG", 1920, 1080)
    shutil.copy2(test_png, "version3/slides_png/slide_05.png")
    print("Exported slide 5 with Segoe UI Emoji successfully!")
    pres.Close()
except Exception as e:
    import traceback
    traceback.print_exc()
finally:
    if os.path.exists(local_in):
        os.remove(local_in)
    ppt_app.Quit()

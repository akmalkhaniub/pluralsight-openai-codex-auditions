import sys
import zipfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')
z = zipfile.ZipFile('version3/Audition Slides - Akmal Khan - Code Review v3.pptx')
namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}
tree = ET.fromstring(z.read('ppt/slides/slide5.xml'))

for sp in tree.findall('.//p:sp', namespaces):
    cNvPr = sp.find('.//p:cNvPr', namespaces)
    name = cNvPr.get('name') if cNvPr is not None else ''
    if name in ['Oval 2', 'Oval 5']:
        print(f"--- {name} ---")
        for p in sp.findall('.//a:p', namespaces):
            rPr = p.find('.//a:rPr', namespaces)
            if rPr is not None:
                print("  rPr attrib:", rPr.attrib)
            t = p.find('.//a:t', namespaces)
            if t is not None:
                print("  text:", t.text)
        xfrm = sp.find('.//a:xfrm', namespaces)
        if xfrm is not None:
            ext = xfrm.find('a:ext', namespaces)
            print("  circle size cx, cy:", ext.attrib)

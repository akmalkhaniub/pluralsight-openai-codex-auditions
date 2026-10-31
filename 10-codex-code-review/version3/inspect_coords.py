import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('version2/Audition Slides - Akmal Khan - Code Review v2.pptx')
tree = ET.fromstring(z.read('ppt/slides/slide4.xml'))
namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

for sp in tree.findall('.//p:sp', namespaces):
    cNvPr = sp.find('.//p:cNvPr', namespaces)
    sp_id = cNvPr.get('id') if cNvPr is not None else None
    xfrm = sp.find('.//a:xfrm', namespaces)
    if xfrm is not None:
        off = xfrm.find('a:off', namespaces)
        ext = xfrm.find('a:ext', namespaces)
        x, y = (off.get('x'), off.get('y')) if off is not None else (None, None)
        cx, cy = (ext.get('cx'), ext.get('cy')) if ext is not None else (None, None)
    else:
        x, y, cx, cy = None, None, None, None
    text = " ".join("".join(t.text for t in p.findall('.//a:t', namespaces) if t.text).strip() for p in sp.findall('.//a:p', namespaces)).strip()
    if text:
        try:
            print(f"ID={sp_id:4} y={y:8} text={repr(text[:40])}")
        except:
            pass

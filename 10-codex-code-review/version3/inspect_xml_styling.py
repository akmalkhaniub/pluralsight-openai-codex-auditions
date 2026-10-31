import sys
import zipfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')
z = zipfile.ZipFile('version3/Audition Slides - Akmal Khan - Code Review v3.pptx')
namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

def inspect_xml_shapes(slide_num):
    tree = ET.fromstring(z.read(f'ppt/slides/slide{slide_num}.xml'))
    print(f"=== SLIDE {slide_num} XML ===")
    for sp in tree.findall('.//p:sp', namespaces):
        cNvPr = sp.find('.//p:cNvPr', namespaces)
        name = cNvPr.get('name') if cNvPr is not None else ''
        text = " ".join("".join(t.text for t in p.findall('.//a:t', namespaces) if t.text).strip() for p in sp.findall('.//a:p', namespaces)).strip()
        solid = sp.find('.//p:spPr/a:solidFill/a:srgbClr', namespaces)
        color = solid.get('val') if solid is not None else None
        rPr = sp.find('.//a:rPr', namespaces)
        sz = rPr.get('sz') if rPr is not None else None
        print(f"  [{name}]: color={color}, sz={sz}, text={repr(text[:45])}")

inspect_xml_shapes(5)
inspect_xml_shapes(9)

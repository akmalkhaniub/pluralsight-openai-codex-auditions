import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('version2/Audition Slides - Akmal Khan - Code Review v2.pptx')
tree = ET.fromstring(z.read('ppt/slides/slide4.xml'))
namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

spTree = tree.find('.//p:spTree', namespaces)
for i, sp in enumerate(spTree.findall('p:sp', namespaces)):
    text = " ".join("".join(t.text for t in p.findall('.//a:t', namespaces) if t.text).strip() for p in sp.findall('.//a:p', namespaces)).strip()
    if text:
        print(f"Shape {i}: {repr(text)}")

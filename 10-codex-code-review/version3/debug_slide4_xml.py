import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('version2/Audition Slides - Akmal Khan - Code Review v2.pptx')
tree = ET.fromstring(z.read('ppt/slides/slide4.xml'))
namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

for sp in tree.findall('.//p:sp', namespaces):
    texts = ["".join(t.text for t in p.findall('.//a:t', namespaces) if t.text) for p in sp.findall('.//a:p', namespaces)]
    if any("copyfileobj" in t for t in texts):
        txBody = sp.find('p:txBody', namespaces)
        for i, p in enumerate(txBody.findall('a:p', namespaces)):
            p_text = "".join(t.text for t in p.findall('.//a:t', namespaces) if t.text)
            print(f"Index {i}: {repr(p_text)}")
            print("  Raw XML:", ET.tostring(p, encoding='utf-8').decode('utf-8'))

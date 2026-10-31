import zipfile
import xml.etree.ElementTree as ET

pptx_path = 'version3/Audition Slides - Akmal Khan - Code Review v3.pptx'

with zipfile.ZipFile(pptx_path, 'r') as z:
    xml_content = z.read('ppt/slides/slide4.xml').decode('utf-8')

tree = ET.fromstring(xml_content)
namespaces = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
}

# Find all paragraphs
paragraphs = tree.findall('.//a:p', namespaces)
for i, p in enumerate(paragraphs):
    texts = [t.text for t in p.findall('.//a:t', namespaces) if t.text]
    full = "".join(texts)
    if full.strip():
        print(f"P{i}: {full}")

import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('version2/Audition Slides - Akmal Khan - Code Review v2.pptx')
tree = ET.fromstring(z.read('ppt/slides/slide4.xml'))
namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

for sp in tree.findall('.//p:sp', namespaces):
    cNvPr = sp.find('.//p:cNvPr', namespaces)
    if cNvPr is not None and cNvPr.get('id') == '4':
        ext = sp.find('.//a:ext', namespaces)
        print("Card 4 size:", ext.attrib)

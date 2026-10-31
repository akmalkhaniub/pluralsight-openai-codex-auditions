import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('version2/Audition Slides - Akmal Khan - Code Review v2.pptx')
tree = ET.fromstring(z.read('ppt/slides/slide4.xml'))
namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main', 'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

# Check timing
timing = tree.find('.//p:timing', namespaces)
if timing is not None:
    print("Has timing/animations")
    for bld in timing.findall('.//p:bldLst/*', namespaces):
        print("  bld tag:", bld.tag, bld.attrib)
else:
    print("No timing on slide 4")

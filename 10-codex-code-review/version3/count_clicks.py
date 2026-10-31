import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('version3/Audition Slides - Akmal Khan - Code Review v3.pptx', 'r')
namespaces = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}

for i in range(1, 12):
    fname = f'ppt/slides/slide{i}.xml'
    tree = ET.fromstring(z.read(fname))
    timing = tree.find('.//p:timing', namespaces)
    if timing is not None:
        # count main sequence condition triggers with evt="onNext" or click triggers
        clicks = timing.findall('.//p:cond[@evt="onNext"]', namespaces)
        blds = timing.findall('.//p:bldLst/*', namespaces)
        print(f"Slide {i:02d}: clicks={len(clicks)}, bldLst={len(blds)}")
    else:
        print(f"Slide {i:02d}: NO TIMING (0 clicks)")

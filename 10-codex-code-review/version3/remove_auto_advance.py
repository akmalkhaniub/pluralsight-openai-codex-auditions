import zipfile
import xml.etree.ElementTree as ET

pptx_path = "version3/Audition Slides - Akmal Khan - Code Review v3.pptx"
zin = zipfile.ZipFile(pptx_path, 'r')
files = {name: zin.read(name) for name in zin.namelist()}
zin.close()

namespaces = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}
ET.register_namespace('p', 'http://schemas.openxmlformats.org/presentationml/2006/main')
ET.register_namespace('a', 'http://schemas.openxmlformats.org/drawingml/2006/main')
ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')

modified_count = 0
for name in list(files.keys()):
    if name.startswith('ppt/slides/slide') and name.endswith('.xml'):
        tree = ET.fromstring(files[name])
        trans = tree.find('p:transition', namespaces)
        if trans is not None and 'advTm' in trans.attrib:
            del trans.attrib['advTm']
            files[name] = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
            modified_count += 1

with zipfile.ZipFile(pptx_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for name, data in files.items():
        zout.writestr(name, data)

print(f"Removed automatic advance timings from {modified_count} slides!")

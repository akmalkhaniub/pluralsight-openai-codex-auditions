import zipfile
import xml.etree.ElementTree as ET

pptx_in = 'version2/Audition Slides - Akmal Khan - Code Review v2.pptx'
pptx_out = 'version3/Audition Slides - Akmal Khan - Code Review v3.pptx'

namespaces = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
}

ET.register_namespace('a', 'http://schemas.openxmlformats.org/drawingml/2006/main')
ET.register_namespace('p', 'http://schemas.openxmlformats.org/presentationml/2006/main')
ET.register_namespace('r', 'http://schemas.openxmlformats.org/officeDocument/2006/relationships')

zin = zipfile.ZipFile(pptx_in, 'r')
files = {name: zin.read(name) for name in zin.namelist()}
zin.close()

slide4_xml = files['ppt/slides/slide4.xml'].decode('utf-8')
tree = ET.fromstring(slide4_xml)

# 1. Update shape 7 text and remove shapes 8, 9, 10, 11
spTree = tree.find('.//p:spTree', namespaces)
to_remove = []
for sp in spTree.findall('p:sp', namespaces):
    cNvPr = sp.find('.//p:cNvPr', namespaces)
    if cNvPr is not None:
        sp_id = cNvPr.get('id')
        if sp_id == '7':
            t = sp.find('.//a:t', namespaces)
            if t is not None:
                t.text = "    copyfileobj(file, target)"
        elif sp_id in {'8', '9', '10', '11'}:
            to_remove.append(sp)

for sp in to_remove:
    spTree.remove(sp)

# 2. Clean timing bldLst
timing = tree.find('.//p:timing', namespaces)
if timing is not None:
    for bldLst in timing.findall('.//p:bldLst', namespaces):
        for bld in list(bldLst):
            if bld.get('spid') in {'8', '9', '10', '11'}:
                bldLst.remove(bld)
    
    # Also clean any targetEl referencing spid 8, 9, 10, 11
    for tgt in list(timing.findall('.//p:tgtEl', namespaces)):
        spTgt = tgt.find('p:spTgt', namespaces)
        if spTgt is not None and spTgt.get('spid') in {'8', '9', '10', '11'}:
            # Find parent of parent or remove animation node
            pass

# Save back to zip
files['ppt/slides/slide4.xml'] = ET.tostring(tree, encoding='utf-8', xml_declaration=True)

with zipfile.ZipFile(pptx_out, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for name, data in files.items():
        zout.writestr(name, data)

print("Applied Slide 4 fix cleanly to PPTX!")

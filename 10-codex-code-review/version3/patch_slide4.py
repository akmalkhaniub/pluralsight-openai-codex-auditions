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

for sp in tree.findall('.//p:sp', namespaces):
    pts = sp.findall('.//a:p', namespaces)
    texts = ["".join(t.text for t in p.findall('.//a:t', namespaces) if t.text) for p in pts]
    if any("copyfileobj" in t for t in texts):
        txBody = sp.find('p:txBody', namespaces)
        p_list = list(txBody.findall('a:p', namespaces))
        
        # We want to identify the paragraphs:
        # destination = AVATAR_DIR ...
        # with destination.open("xb") as target:
        #     copyfileobj(file, target)
        
        for p in p_list:
            p_text = "".join(t.text for t in p.findall('.//a:t', namespaces) if t.text)
            if "try:" in p_text:
                for t in p.findall('.//a:t', namespaces):
                    t.text = "    copyfileobj(file, target)"
            elif any(k in p_text for k in ["except Exception:", "destination.unlink()", "raise"]):
                txBody.remove(p)
            elif "copyfileobj" in p_text and "try" not in p_text:
                # remove the second copyfileobj line that was inside the try block
                txBody.remove(p)

new_slide4 = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
files['ppt/slides/slide4.xml'] = new_slide4

with zipfile.ZipFile(pptx_out, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for name, data in files.items():
        zout.writestr(name, data)

print("Slide 4 successfully cleaned up!")

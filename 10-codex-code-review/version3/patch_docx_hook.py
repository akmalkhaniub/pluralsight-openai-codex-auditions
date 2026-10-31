import zipfile
import xml.etree.ElementTree as ET

docx_path = "version3/Audition Outline - Akmal Khan - Code Review v3.docx"
zin = zipfile.ZipFile(docx_path, 'r')
files = {name: zin.read(name) for name in zin.namelist()}
zin.close()

doc_xml = files['word/document.xml'].decode('utf-8')
# Update the hook text
old_hook = '– Hook: "Your AI can write code in minutes. So who reviews the AI?"'
new_hook = '– Hook: "AI builds in 60s, but who reviews the AI? When nobody audits edge cases, bugs multiply."'

doc_xml = doc_xml.replace('0:00-0:15 Title slide', '0:00-0:20 Title slide')
if 'Your AI can write code in minutes' in doc_xml:
    doc_xml = doc_xml.replace('Your AI can write code in minutes. So who reviews the AI?', 'AI builds in 60s, but who reviews the AI? When nobody audits edge cases, bugs multiply.')

files['word/document.xml'] = doc_xml.encode('utf-8')

with zipfile.ZipFile(docx_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for name, data in files.items():
        zout.writestr(name, data)

print("Updated docx outline with new hook!")

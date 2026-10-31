import zipfile
import xml.etree.ElementTree as ET

docx_path = "version3/Audition Outline - Akmal Khan - Code Review v3.docx"
zin = zipfile.ZipFile(docx_path, 'r')
files = {name: zin.read(name) for name in zin.namelist()}
zin.close()

doc_xml = files['word/document.xml'].decode('utf-8')

# Replacements for Writer / Editor -> Feature Developer / Senior PR Reviewer
doc_xml = doc_xml.replace(
    "Analogy: the writer and the editor. Great writers don't edit their own first draft; /review is Codex switching hats.",
    "Analogy: The Feature Developer vs. The Senior PR Reviewer. Every Pull Request needs a second pair of eyes; /review turns Codex into your Staff PR reviewer."
)
doc_xml = doc_xml.replace(
    "Three acts: the writer, the editor, the proof.",
    "Three acts: the feature developer, the senior reviewer, the proof."
)
doc_xml = doc_xml.replace(
    "Great writers don't edit their own first draft (analogy).",
    "Every Pull Request needs a second pair of eyes (analogy)."
)
doc_xml = doc_xml.replace(
    "Writer: \"Did I build what was asked?\" Editor: \"What could go wrong?\" Same Codex, two hats, never both at once.",
    "Feature Dev: \"Did I satisfy the ticket?\" Senior Reviewer: \"What breaks in production?\" Same Codex, two hats, never in the same prompt."
)
doc_xml = doc_xml.replace(
    "The writer: ask Codex to add profile photo upload; the tests pass.",
    "The feature developer: ask Codex to add profile photo upload; the tests pass."
)
doc_xml = doc_xml.replace(
    "The editor: /review → Review uncommitted changes.",
    "The senior reviewer: /review → Review uncommitted changes."
)
doc_xml = doc_xml.replace(
    "Writer only vs writer and editor",
    "Feature dev only vs feature dev + senior reviewer"
)
doc_xml = doc_xml.replace(
    "Codex built it. The tests pass. Ship it?",
    "The PR looks green. Would you approve it?"
)

files['word/document.xml'] = doc_xml.encode('utf-8')

with zipfile.ZipFile(docx_path, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    for name, data in files.items():
        zout.writestr(name, data)

print("Updated Audition Outline docx successfully!")

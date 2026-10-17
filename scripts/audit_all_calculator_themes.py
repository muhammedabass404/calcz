import os
import re

calc_dir = "calcworld-engine/calculators"

body_classes = {}
html_classes = {}
header_types = {}
footer_types = {}
missing_inter_font = []

for f in sorted(os.listdir(calc_dir)):
    if f.endswith(".html"):
        fp = os.path.join(calc_dir, f)
        c = open(fp, "r", encoding="utf-8", errors="ignore").read()

        # HTML class
        m_html = re.search(r'<html[^>]*class=["\']([^"\']*)["\']', c, re.I)
        h_cls = m_html.group(1) if m_html else "NO_CLASS"
        html_classes[h_cls] = html_classes.get(h_cls, 0) + 1

        # Body class
        m_body = re.search(r'<body[^>]*class=["\']([^"\']*)["\']', c, re.I)
        b_cls = m_body.group(1) if m_body else "NO_CLASS"
        # Extract bg classes from body
        b_bg = ' '.join([x for x in b_cls.split() if 'bg-' in x])
        body_classes[b_bg] = body_classes.get(b_bg, 0) + 1

        # Font
        if 'Inter' not in c:
            missing_inter_font.append(f)

print("--- HTML Class Distribution ---")
for k, v in html_classes.items():
    print(f"  {k:40} : {v} files")

print("\n--- Body Background Classes Distribution ---")
for k, v in body_classes.items():
    print(f"  {k:60} : {v} files")

print(f"\nMissing Inter font: {len(missing_inter_font)}")

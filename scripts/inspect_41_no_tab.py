import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'

with open(r'calcworld-engine\scripts\classify_print_containers.py', 'r') as f:
    pass

import sys
# Run classification logic directly
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))
print_tab_regex = re.compile(r'id=["\'](tab[-_]?print|print[-_]?tab|tab[-_]?report|tabPrint|tabContent[-_]print|tab[-_]content[-_]print|printableReportSection|tabPrintView|tab[-_]print[-_]report|tab[-_]print[-_]content|printArea|print[-_]sheet[-_]content)["\']', re.I)
print_card_regex = re.compile(r'class=["\'][^"\']*(card[-_]print|print[-_]card|printable[-_]report|print[-_]dossier)[^"\']*["\']', re.I)

no_tab_files = []
for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    if not print_tab_regex.search(c) and not print_card_regex.search(c):
        no_tab_files.append(name)

print(f"Total without dedicated print container: {len(no_tab_files)}")

for name in no_tab_files:
    fpath = os.path.join(calc_dir, name)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # check for main elements
    forms = re.findall(r'<form[^>]*id=["\']([^"\']+)["\']', c, re.I)
    main_cards = re.findall(r'<div[^>]*id=["\']([^"\']*(?:result|output|card|panel|summary|display)[^"\']*)["\']', c, re.I)
    valid_cards = [x for x in main_cards if not re.search(r'btn|button|copy|icon|text|input', x, re.I)]
    print(f"{name:35} -> forms={forms[:2]} | result_cards={valid_cards[:4]}")

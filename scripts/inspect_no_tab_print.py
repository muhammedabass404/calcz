import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

no_tab_print = []
has_tab_print = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # check for print tab
    m = re.search(r'id=["\'](tab[-_]?print|print[-_]?tab|tab[-_]?report|tabPrint)["\']', c, re.I)
    if m:
        has_tab_print.append((name, m.group(1)))
    else:
        no_tab_print.append(name)

print(f"Calculators WITH tab-print: {len(has_tab_print)}")
print(f"Calculators WITHOUT tab-print: {len(no_tab_print)}")
print("\nFirst 20 without tab-print:")
for name in no_tab_print[:20]:
    fpath = os.path.join(calc_dir, name)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    # find results container
    res = re.findall(r'id=["\']([^"\']*(?:result|output|summary|card|chart)[^"\']*)["\']', c, re.I)
    tabs = re.findall(r'id=["\'](tab[-_][a-z0-9_-]+)["\']', c, re.I)
    print(f"{name}:")
    print(f"   tabs: {tabs[:5]}")
    print(f"   results ids: {res[:5]}")

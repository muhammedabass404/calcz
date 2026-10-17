import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

print_report_defs = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    matches = re.findall(r'function\s+printReport\s*\(|window\.printReport\s*=', c)
    if matches:
        print_report_defs.append((name, matches))

print(f"Calculators defining printReport: {len(print_report_defs)}")
for name, m in print_report_defs[:10]:
    print(f"  {name}: {m}")

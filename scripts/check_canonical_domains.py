import glob
import os
import re
import sys
import datetime

sys.stdout.reconfigure(encoding='utf-8')

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
root_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

print(f"Total calculators: {len(files)}")

# 1. Inspect canonical tags
domain_counts = {}
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', c, re.I)
    if m:
        url = m.group(1)
        domain = re.search(r'https?://([^/]+)', url)
        d_name = domain.group(1) if domain else 'unknown'
        domain_counts[d_name] = domain_counts.get(d_name, 0) + 1
    else:
        domain_counts['NO_CANONICAL'] = domain_counts.get('NO_CANONICAL', 0) + 1

print("Canonical domains in calculators:")
for d, cnt in domain_counts.items():
    print(f"  {d}: {cnt}")

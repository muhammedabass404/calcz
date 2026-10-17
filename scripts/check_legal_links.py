import os
import re

calc_dir = 'calcworld-engine/calculators'
all_links = set()

for f in os.listdir(calc_dir):
    if f.endswith('.html'):
        c = open(os.path.join(calc_dir, f), 'r', encoding='utf-8', errors='ignore').read()
        for m in re.findall(r'href=["\']([^"\']+)["\']', c):
            if any(k in m.lower() for k in ['about', 'privacy', 'terms', 'contact', 'legal']):
                all_links.add(m)

print('Legal links in calculators:', all_links)

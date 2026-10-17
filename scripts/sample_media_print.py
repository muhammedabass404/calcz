import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

media_print_samples = {}
for f in files[:20]:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    m = re.search(r'@media\s+print\s*\{([^}]+(?:\{[^}]+\}[^}]*)*)\}', c)
    if m:
        media_print_samples[name] = m.group(0)[:300] + '...'
    else:
        media_print_samples[name] = 'NO @media print'

for k, v in list(media_print_samples.items())[:8]:
    print(f'=== {k} ===')
    print(v)
    print()

import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

print_calls_sample = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    matches = re.findall(r'<button[^>]*?(?:print|Print)[^>]*?>', c)
    if matches:
        print_calls_sample.append((name, matches[0]))

print(f"Calculators with print button tag: {len(print_calls_sample)}")
print("Sample print buttons:")
for name, btn in print_calls_sample[:15]:
    print(f"{name}: {btn}")

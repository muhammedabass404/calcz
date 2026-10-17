import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

def find_media_print(content):
    # Match @media print { ... } taking into account nested braces
    pattern = re.compile(r'@media\s+print\s*\{', re.I)
    matches = []
    for m in pattern.finditer(content):
        start = m.start()
        # count braces to find end
        open_braces = 0
        end = start
        for i in range(start, len(content)):
            if content[i] == '{':
                open_braces += 1
            elif content[i] == '}':
                open_braces -= 1
                if open_braces == 0:
                    end = i + 1
                    break
        matches.append((start, end, content[start:end]))
    return matches

total_found = 0
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    m = find_media_print(c)
    if m:
        total_found += 1

print(f"Total files where find_media_print found blocks: {total_found} / {len(files)}")

import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

short_calculators = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    m_art = re.search(r'<article[^>]*>(.*?)</article>', c, re.DOTALL | re.I)
    if m_art:
        art_text = re.sub(r'<[^>]+>', ' ', m_art.group(1))
        words = len(art_text.split())
    else:
        m_sec = re.search(r'<(?:section|div)[^>]*(?:class=["\'][^"\']*prose[^"\']*["\']|id=["\'][^"\']*guide[^"\']*["\'])(.*?)(?:</section>|</div>\s*<!--)', c, re.DOTALL | re.I)
        if m_sec:
            sec_text = re.sub(r'<[^>]+>', ' ', m_sec.group(1))
            words = len(sec_text.split())
        else:
            words = 0

    if words < 1000:
        short_calculators.append((name, words))

print(f"Total calculators with < 1000 words: {len(short_calculators)}")
print("\nSorted from shortest to longest:")
for name, words in sorted(short_calculators, key=lambda x: x[1]):
    print(f"  {name:40} : {words:4d} words")

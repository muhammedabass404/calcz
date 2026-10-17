import os
import re

ONEDRIVE_CALC_DIR = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
DESKTOP_CALC_DIR = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'

from upgrade_batch3_final5 import ARTICLES
salary_art = ARTICLES['salary-calculator.html']

for base_dir in [ONEDRIVE_CALC_DIR, DESKTOP_CALC_DIR]:
    fpath = os.path.join(base_dir, 'salary-calculator.html')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # match from <div class="mt-12 mb-8 border-t border-gray-200 to right before <!-- AdSlot 5 -->
    pattern = re.compile(r'<div class="mt-12 mb-8 border-t border-gray-200.*?</div>\s*</div>\s*(?=<!-- AdSlot 5 -->)', re.DOTALL)
    if pattern.search(c):
        c = pattern.sub(lambda _: salary_art + '\n', c)
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Replaced salary guide in {base_dir}!")
    else:
        print(f"Pattern did not match in {base_dir}")

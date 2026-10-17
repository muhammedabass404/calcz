import os
import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

ONEDRIVE_CALC_DIR = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
DESKTOP_CALC_DIR = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'

from upgrade_batch3_final5 import ARTICLES

# 1. Update sales-tax-calculator.html
sales_tax_art = ARTICLES['sales-tax-calculator.html']
for base_dir in [ONEDRIVE_CALC_DIR, DESKTOP_CALC_DIR]:
    fpath = os.path.join(base_dir, 'sales-tax-calculator.html')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # replace FAQ div with our article
    c = re.sub(r'<div class="bg-white dark:bg-gray-800 p-6 rounded-lg shadow my-8">.*?</div>\s*</div>\s*(?=<script)', lambda _: sales_tax_art + '\n</div>\n', c, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Updated sales-tax-calculator.html successfully!")

# 2. Update salary-calculator.html
salary_art = ARTICLES['salary-calculator.html']
for base_dir in [ONEDRIVE_CALC_DIR, DESKTOP_CALC_DIR]:
    fpath = os.path.join(base_dir, 'salary-calculator.html')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # find where guide begins in salary-calculator
    c = re.sub(r'<div class="bg-white dark:bg-gray-800 rounded-2xl shadow-lg border border-gray-100 dark:border-gray-700 p-6 sm:p-8.*?Frequently Asked Questions \(FAQ\).*?</div>\s*</div>\s*</div>', lambda _: salary_art, c, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)

print("Updated salary-calculator.html successfully!")

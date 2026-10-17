import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

print_tab_calls = 0
direct_prints = 0

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # check if print triggers tab switch
    if re.search(r'switchTab\([\'"]print', c) or re.search(r'switchTab\([\'"]tab-print', c) or re.search(r'showTab\([\'"]print', c):
        print_tab_calls += 1
    elif 'window.print()' in c:
        direct_prints += 1

print(f"Calculators that switch tab on print: {print_tab_calls}")
print(f"Calculators with direct window.print(): {direct_prints}")

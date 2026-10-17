import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'

sample_names = [
    'age-calculator.html',
    'annuity-calculator.html',
    'army-body-fat-calculator.html',
    'gas-mileage-calculator.html',
    'sleep-calculator.html',
    'tire-size-calculator.html',
    'tip-calculator.html'
]

for name in sample_names:
    fpath = os.path.join(calc_dir, name)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    print(f"=== {name} ===")
    
    # check how tab-print is defined
    m = re.search(r'(<div[^>]*id=["\'](?:tab[-_]?print|tabPrint|print[-_]?tab)["\'][^>]*>)(.*?)(</div>\s*</div>|\Z)', c, re.DOTALL)
    if m:
        print("  tab-print opening:", m.group(1))
        inner = m.group(2)[:300].replace('\n', ' ')
        print("  tab-print content sample:", inner)
    else:
        print("  tab-print not found by regex")
        
    # check if there is an updatePrint or print function in JS
    js_print = re.findall(r'function\s+([a-zA-Z0-9_]*print[a-zA-Z0-9_]*)\s*\(', c, re.I)
    print("  JS print functions:", js_print)
    print()

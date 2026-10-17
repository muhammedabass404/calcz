import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

print_update_patterns = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # search for functions with print in name
    funcs = re.findall(r'function\s+([a-zA-Z0-9_]*print[a-zA-Z0-9_]*)\s*\(', c, re.I)
    
    # search for window.print calls and what precedes them
    w_prints = re.findall(r'([^\n;{}]{0,60}window\.print\(\)[^\n;{}]*)', c)
    
    # search for onbeforeprint
    has_beforeprint = 'beforeprint' in c
    
    if funcs or w_prints:
        print_update_patterns.append({
            'name': name,
            'funcs': funcs,
            'w_prints': w_prints[:2],
            'beforeprint': has_beforeprint
        })

print(f"Calculators with print functions or window.print: {len(print_update_patterns)}")
print("\nSample (first 10):")
for p in print_update_patterns[:10]:
    print(f"{p['name']}:")
    print(f"  funcs: {p['funcs']}")
    print(f"  w_prints: {p['w_prints']}")

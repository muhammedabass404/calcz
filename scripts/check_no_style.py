import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

no_style = []
for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    if '</style>' not in c:
        no_style.append(name)

print(f"Files without </style>: {len(no_style)}")
if no_style:
    print("Examples:", no_style)

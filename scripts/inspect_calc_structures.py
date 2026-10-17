import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'

sample_files = [
    '401k-calculator.html',
    'mortgage-calculator.html',
    'bmi-calculator.html',
    'body-fat-calculator.html',
    'compound-interest-calculator.html',
    'scientific-calculator.html',
    'age-calculator.html',
    'gas-mileage-calculator.html'
]

for name in sample_files:
    fpath = os.path.join(calc_dir, name)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    print(f"=== {name} ===")
    # Find tab buttons
    tab_btns = re.findall(r'data-tab=["\']([^"\']+)["\']', c)
    if not tab_btns:
        tab_btns = re.findall(r'onclick=["\'](?:switchTab|showTab|changeTab)\(["\']([^"\']+)["\']', c)
    print("  Tabs detected:", tab_btns)
    
    # Check print button
    p_btn = re.findall(r'<button[^>]*?(?:print|Print)[^>]*?>.*?</button>', c, re.DOTALL | re.I)
    print(f"  Print buttons count: {len(p_btn)}")
    if p_btn:
        print("  First print button:", p_btn[0][:150].replace('\n', ' '))
        
    # Check what container holds the report or results
    results_div = re.findall(r'id=["\']([^"\']*(?:result|output|summary|report|dossier|card-print|tab-print)[^"\']*)["\']', c, re.I)
    print("  Candidate result/report IDs:", results_div[:8])
    print()

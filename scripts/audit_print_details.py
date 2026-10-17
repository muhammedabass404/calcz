import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

print(f'Total calculators: {len(files)}')

with_print_tab = []
with_card_print = []
with_print_btn = []
has_media_print = []
no_print_anything = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    has_ptab = bool(re.search(r'id=["\'](?:tab-print|tabPrint|print-tab|tab-report|tabReport)["\']', c, re.I))
    has_cprint = bool(re.search(r'class=["\'][^"\']*(?:card-print|print-card|printable-report|print-dossier)[^"\']*["\']', c, re.I))
    has_pbtn = bool(re.search(r'window\.print\(|printReport\(', c))
    has_mprint = bool('@media print' in c)

    if has_ptab:
        with_print_tab.append(name)
    if has_cprint:
        with_card_print.append(name)
    if has_pbtn:
        with_print_btn.append(name)
    if has_mprint:
        has_media_print.append(name)
    if not has_ptab and not has_cprint and not has_pbtn:
        no_print_anything.append(name)

print(f'Has print tab (tab-print etc): {len(with_print_tab)}')
print(f'Has card-print class: {len(with_card_print)}')
print(f'Has print button / call: {len(with_print_btn)}')
print(f'Has @media print: {len(has_media_print)}')
print(f'No print tab, no card-print, no print button: {len(no_print_anything)}')
print('Examples with NO print anything:', no_print_anything[:10])

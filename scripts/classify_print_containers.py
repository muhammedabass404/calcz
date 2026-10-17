import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

print_tab_regex = re.compile(r'id=["\'](tab[-_]?print|print[-_]?tab|tab[-_]?report|tabPrint|tabContent[-_]print|tab[-_]content[-_]print|printableReportSection|tabPrintView|tab[-_]print[-_]report|tab[-_]print[-_]content|printArea|print[-_]sheet[-_]content)["\']', re.I)
print_card_regex = re.compile(r'class=["\'][^"\']*(card[-_]print|print[-_]card|printable[-_]report|print[-_]dossier)[^"\']*["\']', re.I)
results_regex = re.compile(r'id=["\']([^"\']*(?:results?[-_]?(?:card|section|container|area|wrapper)|output[-_]?(?:card|container|section)|tab[-_]summary|tabSummary)[^"\']*)["\']', re.I)

calc_info = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    ptab_match = print_tab_regex.search(c)
    pcard_match = print_card_regex.search(c)
    res_matches = results_regex.findall(c)
    
    # filter button ids from res_matches
    valid_res = [r for r in res_matches if not re.search(r'btn|button|copy|toggle', r, re.I)]
    
    has_print_btn = bool(re.search(r'window\.print\(|printReport\(', c))
    
    calc_info.append({
        'name': name,
        'ptab': ptab_match.group(1) if ptab_match else None,
        'pcard': pcard_match.group(1) if pcard_match else None,
        'results': valid_res[:3],
        'has_print_btn': has_print_btn
    })

print(f"Total files: {len(calc_info)}")
has_ptab_count = sum(1 for x in calc_info if x['ptab'])
has_pcard_count = sum(1 for x in calc_info if x['pcard'] and not x['ptab'])
has_neither_count = sum(1 for x in calc_info if not x['ptab'] and not x['pcard'])

print(f"Has Print Tab: {has_ptab_count}")
print(f"Has Print Card (without Print Tab): {has_pcard_count}")
print(f"Has Neither: {has_neither_count}")

print("\nFiles with Neither (showing results container):")
for x in [x for x in calc_info if not x['ptab'] and not x['pcard']]:
    print(f"  {x['name']}: results={x['results']}, print_btn={x['has_print_btn']}")

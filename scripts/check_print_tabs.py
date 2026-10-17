import glob, os, re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = glob.glob(os.path.join(calc_dir, '*.html'))

has_print_tab = []
no_print_tab = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    if re.search(r'id=[\'"](?:tab-print|tabPrint|print-tab)[\'"]', c):
        has_print_tab.append(name)
    else:
        no_print_tab.append(name)

print(f'Files with print tab: {len(has_print_tab)}')
print(f'Files WITHOUT print tab: {len(no_print_tab)}')
print('Examples with print tab:', has_print_tab[:10])
print('Examples without print tab:', no_print_tab[:10])

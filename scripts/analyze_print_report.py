import glob, os, re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = glob.glob(os.path.join(calc_dir, '*.html'))

print_patterns = {}
for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    has_print_card = bool(re.search(r'class=[\'"][^\'"]*(?:print-card|card-print|printable-report|print-dossier)[^\'"]*[\'"]', c))
    has_tab_print = bool(re.search(r'id=[\'"](?:tab-print|tabPrint|print-tab|tab-report)[^\'"]*[\'"]', c))
    has_print_only = bool(re.search(r'class=[\'"][^\'"]*print-only[^\'"]*[\'"]', c))
    has_window_print = bool(re.search(r'window\.print\(', c))
    
    key = (has_print_card, has_tab_print, has_print_only, has_window_print)
    print_patterns.setdefault(key, []).append(name)

print(f'Total files: {len(files)}')
for k, flist in print_patterns.items():
    print(f'Pattern (print_card={k[0]}, tab_print={k[1]}, print_only={k[2]}, window_print={k[3]}): {len(flist)} files')
    print('  Example:', flist[0])

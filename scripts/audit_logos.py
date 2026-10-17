import os, glob, re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = glob.glob(os.path.join(calc_dir, '*.html'))

logo_types = {}
no_logo_files = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # search for header
    h_match = re.search(r'<header.*?</header>', c, re.DOTALL)
    if not h_match:
        no_logo_files.append((name, 'no <header> tag'))
        continue
    
    h = h_match.group(0)
    m = re.search(r'<a\s+href="[^"]*index\.html"[^>]*>.*?</a>', h, re.DOTALL)
    if m:
        snippet = re.sub(r'\s+', ' ', m.group(0)).strip()
        logo_types.setdefault(snippet, []).append(name)
    else:
        no_logo_files.append((name, 'no index.html link in header'))

print(f'Total files: {len(files)}')
print(f'Distinct logo snippets: {len(logo_types)}')
for snippet, flist in logo_types.items():
    print(f'\nCount: {len(flist)}')
    print(f'Snippet: {snippet[:150]}...')
    if len(flist) < 10:
        print('Files:', flist)

if no_logo_files:
    print('\nFiles with NO logo in header:', len(no_logo_files))
    for f in no_logo_files:
        print(' ', f)

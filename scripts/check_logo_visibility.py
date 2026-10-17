import os, glob, re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = glob.glob(os.path.join(calc_dir, '*.html'))

issues = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # check if 'brand' is missing in tailwind.config
    m_tw = re.search(r'tailwind\.config\s*=\s*(\{.*?\n\s*\})', c, re.DOTALL)
    if m_tw:
        tw_str = m_tw.group(1)
        if 'brand' not in tw_str:
            issues.append((name, 'missing brand in tailwind.config'))
    else:
        issues.append((name, 'no tailwind.config found'))

print(f'Total files with missing brand config: {len(issues)}')
print('First 10:', issues[:10])

import os, glob, re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = glob.glob(os.path.join(calc_dir, '*.html'))

all_broken = {}

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()
    
    scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', html, re.DOTALL)
    js = '\n'.join(scripts)
    
    issues = []
    
    # Check direct calls: document.getElementById('xxx').something
    direct_calls = re.findall(r'document\.getElementById\([\'"]([a-zA-Z0-9_-]+)[\'"]\)\s*\.([a-zA-Z0-9_]+)', js)
    for ref_id, method in direct_calls:
        if not re.search(rf'id=[\'"]{re.escape(ref_id)}[\'"]', html):
            issues.append(f"Direct: document.getElementById('{ref_id}').{method}")
            
    # Check variable assignments: const x = document.getElementById('xxx'); ... x.something
    var_assigns = re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*document\.getElementById\([\'"]([a-zA-Z0-9_-]+)[\'"]\)', js)
    for varname, ref_id in var_assigns:
        if not re.search(rf'id=[\'"]{re.escape(ref_id)}[\'"]', html):
            # check if varname is used like `varname.`
            usage = re.findall(rf'\b{re.escape(varname)}\s*\.\s*([a-zA-Z0-9_]+)', js)
            if usage:
                # check if there is an if check right before it
                guarded = re.search(rf'if\s*\(\s*{re.escape(varname)}\s*\)', js)
                if not guarded:
                    issues.append(f"Variable: {varname} (id='{ref_id}') accessed as .{usage[0]}")

    if issues:
        all_broken[name] = issues

print(f'Total files checked: {len(files)}')
print(f'Total files with fatal JS null dereferences: {len(all_broken)}')
for fname, issues in all_broken.items():
    print(f'\n{fname}:')
    for iss in issues[:5]:
        print(f'  {iss}')
    if len(issues) > 5:
        print(f'  ... and {len(issues) - 5} more')

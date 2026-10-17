import os, glob, re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = glob.glob(os.path.join(calc_dir, '*.html'))

report = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()
    
    scripts = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', html, re.DOTALL)
    js = '\n'.join(scripts)
    
    file_issues = []
    
    # 1. Check for unguarded document.getElementById('...').addEventListener
    unguarded_listeners = re.findall(r'document\.getElementById\([\'"]([a-zA-Z0-9_-]+)[\'"]\)\.addEventListener', js)
    for ref_id in unguarded_listeners:
        if not re.search(rf'id=[\'"]{re.escape(ref_id)}[\'"]', html):
            file_issues.append(f"Missing element for unguarded listener: #{ref_id}")
            
    # 2. Check for unguarded variable.addEventListener where variable is assigned from getElementById
    var_assigns = re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*document\.getElementById\([\'"]([a-zA-Z0-9_-]+)[\'"]\)\s*;', js)
    for varname, ref_id in var_assigns:
        if not re.search(rf'id=[\'"]{re.escape(ref_id)}[\'"]', html):
            # check if varname.addEventListener is called without guard
            if re.search(rf'\b{re.escape(varname)}\.addEventListener', js):
                # check if there's if (varname) before it
                if not re.search(rf'if\s*\(\s*{re.escape(varname)}\s*\)\s*\{{[^}}]*{re.escape(varname)}\.addEventListener', js):
                    file_issues.append(f"Missing element variable for listener: {varname} (#{ref_id})")
                    
    # 3. Check for inline onclick="functionName(...)" where functionName is not defined in script or window
    onclicks = re.findall(r'onclick=[\'"]([a-zA-Z0-9_]+)\(', html)
    for fn in set(onclicks):
        if fn in ['print', 'toggleMobileDrawer']:  # standard browser/header functions
            continue
        # check if function fn exists in js
        fn_pattern = rf'(?:function\s+{re.escape(fn)}\b|window\.{re.escape(fn)}\s*=|const\s+{re.escape(fn)}\s*=\s*(?:function|\()|let\s+{re.escape(fn)}\s*=\s*(?:function|\())'
        if not re.search(fn_pattern, js):
            file_issues.append(f"Inline onclick function undefined: {fn}()")
            
    # 4. Check for preset buttons existence vs handler
    has_preset_markup = bool(re.search(r'class=[\'"][^\'"]*preset[^\'"]*[\'"]', html) or re.search(r'id=[\'"][^\'"]*preset[^\'"]*[\'"]', html, re.I))
    has_preset_handler = bool(re.search(r'preset', js, re.I))
    if has_preset_markup and not has_preset_handler:
        file_issues.append("Preset markup found but no preset handler in script")

    # 5. Check for tab buttons markup vs handler
    has_tab_markup = bool(re.search(r'class=[\'"][^\'"]*tab-btn[^\'"]*[\'"]', html))
    has_tab_handler = bool(re.search(r'tab-btn|tabBtns|switchTab|data-tab|data-target', js))
    if has_tab_markup and not has_tab_handler:
        file_issues.append("Tab markup found but no tab switching handler in script")

    if file_issues:
        report.append((name, file_issues))

print(f"Total files checked: {len(files)}")
print(f"Files with interaction issues: {len(report)}")
for name, issues in report:
    print(f"\n{name}:")
    for iss in issues:
        print(f"  - {iss}")

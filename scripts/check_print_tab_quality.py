import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

empty_or_placeholder_print_tabs = []
full_print_tabs = []

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    m = re.search(r'<div[^>]*id=["\'](?:tab[-_]?print|tabPrint|tabContent[-_]print|printableReportSection)["\'][^>]*>(.*?)(?:</div>\s*</div>|\Z)', c, re.DOTALL)
    if m:
        content = m.group(1).strip()
        # check if it only has email input or placeholder lead-box
        if 'type="email"' in content and len(content) < 800 and not re.search(r'<table|dossier|certificate|report|metric|result', content, re.I):
            empty_or_placeholder_print_tabs.append((name, len(content)))
        else:
            full_print_tabs.append((name, len(content)))

print(f"Full / rich print tabs: {len(full_print_tabs)}")
print(f"Empty or email-only placeholder print tabs: {len(empty_or_placeholder_print_tabs)}")
if empty_or_placeholder_print_tabs:
    print("Examples of placeholder print tabs:")
    for name, length in empty_or_placeholder_print_tabs[:10]:
        print(f"  {name} (length {length})")

import os
import re

calc_path = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators\body-fat-calculator.html'

with open(calc_path, 'r', encoding='utf-8') as f:
    content = f.read()

from test_print_generator import generate_print_css, PRINT_CORE_JS, PRINT_TAB_REGEX, PRINT_CARD_REGEX
from test_brace_matcher import find_media_print

has_ptab = bool(PRINT_TAB_REGEX.search(content) or PRINT_CARD_REGEX.search(content))
new_css = generate_print_css(has_ptab)

matches = find_media_print(content)
if matches:
    for i in range(len(matches) - 1, 0, -1):
        s, e, _ = matches[i]
        content = content[:s] + content[e:]
    s0, e0, _ = matches[0]
    content = content[:s0] + new_css + content[e0:]
else:
    content = content.replace('</style>', new_css + '\n</style>', 1)

if 'id="calcworld-print-core"' not in content:
    content = content.replace('</body>', PRINT_CORE_JS + '\n</body>', 1)

with open(calc_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated body-fat-calculator.html (has_ptab={has_ptab}) successfully!")

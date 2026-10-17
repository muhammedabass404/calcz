import re

with open(r'calcworld-engine\calculators\401k-calculator.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if re.search(r'id=["\']tab-print["\']', line):
        print(f"Line {i+1}: {line.strip()}")
        for j in range(i, min(i+40, len(lines))):
            print(f"  {j+1}: {lines[j].rstrip()}")
        break

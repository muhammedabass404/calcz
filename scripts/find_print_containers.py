import glob
import os
import re

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

print_elements = {}

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # find all IDs with 'print'
    print_ids = re.findall(r'id=["\']([^"\']*print[^"\']*)["\']', c, re.I)
    print_classes = re.findall(r'class=["\']([^"\']*(?:card-print|print-card|printable-report|print-dossier)[^"\']*)["\']', c, re.I)
    
    # find print onclick or event listeners
    print_calls = re.findall(r'window\.print\(|printReport\(', c)
    
    print_elements[name] = {
        'ids': list(set(print_ids)),
        'classes': list(set(print_classes)),
        'has_call': len(print_calls) > 0
    }

# Summarize the print container IDs across all files
container_ids = {}
for name, data in print_elements.items():
    for pid in data['ids']:
        # filter out button ids like btn-print
        if not re.search(r'btn|button', pid, re.I):
            container_ids[pid] = container_ids.get(pid, 0) + 1

print("Top Print Container IDs:")
for pid, count in sorted(container_ids.items(), key=lambda x: -x[1])[:25]:
    print(f"  {pid}: {count}")

no_print_id = [name for name, data in print_elements.items() if not [x for x in data['ids'] if not re.search(r'btn|button', x, re.I)]]
print(f"\nFiles without any print container ID: {len(no_print_id)}")
print("First 20 without print container ID:", no_print_id[:20])

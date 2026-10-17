import glob
import os
import re

print("--- DEEP AUDIT OF ALL INTERNAL LINKS ACROSS ENTIRE PROJECT ---")
all_files = sorted(glob.glob("calcworld-engine/**/*.html", recursive=True))

broken_links = []
total_links_checked = 0

for file_path in all_files:
    rel_file = os.path.relpath(file_path, "calcworld-engine").replace("\\", "/")
    file_dir = os.path.dirname(file_path)
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as fp:
        content = fp.read()
    
    # Find all href="..."
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', content)
    for href in hrefs:
        # Ignore external, anchors, mailto, javascript, tel
        if href.startswith(('http://', 'https://', '#', 'mailto:', 'tel:', 'javascript:')):
            continue
        
        total_links_checked += 1
        clean_href = href.split('?')[0].split('#')[0]
        if not clean_href:
            continue
            
        # If root-relative:
        if clean_href.startswith('/'):
            target_path = os.path.join("calcworld-engine", clean_href.lstrip('/'))
        else:
            # Relative to file_dir
            target_path = os.path.join(file_dir, clean_href)
            
        target_path = os.path.normpath(target_path)
        
        # Check existence
        exists = False
        if os.path.isfile(target_path):
            exists = True
        elif os.path.isdir(target_path):
            # check if index.html exists inside
            if os.path.isfile(os.path.join(target_path, "index.html")):
                exists = True
        elif os.path.isfile(target_path + ".html"):
            exists = True
            
        if not exists:
            broken_links.append((rel_file, href, target_path))

print(f"Total HTML files: {len(all_files)}")
print(f"Total internal links checked: {total_links_checked}")
print(f"Total broken internal links found: {len(broken_links)}")

# Group broken links by target
from collections import defaultdict
grouped = defaultdict(list)
for src, href, tgt in broken_links:
    grouped[href].append(src)

for href, sources in sorted(grouped.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"\nBroken link '{href}' ({len(sources)} occurrences), e.g. in:")
    for s in sources[:4]:
        print(f"  - {s}")

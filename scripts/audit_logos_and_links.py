import glob
import re
from collections import Counter

print("--- AUDITING LOGOS & NAV LINKS ---")
calc_files = sorted(glob.glob("calcworld-engine/calculators/*.html"))
legal_files = sorted(glob.glob("calcworld-engine/legal-pages/*.html"))
root_files = sorted(glob.glob("calcworld-engine/*.html"))
all_pages = sorted(glob.glob("calcworld-engine/**/*.html", recursive=True))

logo_counter = Counter()

for f in all_pages:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        html = fp.read()
    # Find brand link / logo
    matches = re.findall(r'<a\s+[^>]*href=["\'][^"\']*index\.html["\'][^>]*>.*?</a>', html, re.DOTALL | re.IGNORECASE)
    if matches:
        # Check if it has SVG or "CalcWorld"
        for m in matches:
            if "CalcWorld" in m or "Calc" in m:
                # normalize
                norm = re.sub(r'\s+', ' ', m.strip())
                logo_counter[norm[:140]] += 1
                break
    else:
        # Check for other logo formats
        alt_matches = re.findall(r'<a\s+[^>]*class=["\'][^"\']*logo[^"\']*["\'][^>]*>.*?</a>', html, re.DOTALL | re.IGNORECASE)
        if alt_matches:
            norm = re.sub(r'\s+', ' ', alt_matches[0].strip())
            logo_counter[norm[:140]] += 1
        else:
            logo_counter[f"NO_LOGO: {f}"] += 1

print(f"Total HTML files checked: {len(all_pages)}")
print("\nUnique Logo Patterns:")
for pattern, count in logo_counter.most_common(10):
    print(f"[{count} files]: {pattern}\n")

# Now check for relative link issues in legal-pages, about-us, etc.
print("\n--- CHECKING RELATIVE LINKS IN ALL FOLDERS ---")
for f in all_pages:
    rel_path = f.replace("\\", "/")
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        html = fp.read()
    
    # check for links like href="about.html", href="privacy.html", href="terms.html", href="contact.html"
    broken_rel = re.findall(r'href=["\'](about\.html|privacy\.html|terms\.html|contact\.html|index\.html)["\']', html, re.IGNORECASE)
    if broken_rel and not rel_path.endswith("calcworld-engine/index.html") and not "legal-pages" in rel_path:
        print(f"File {rel_path} has relative link: {broken_rel}")

import os
import re

calc_dir = "calcworld-engine/calculators"
not_dark = []

for f in sorted(os.listdir(calc_dir)):
    if f.endswith(".html"):
        fp = os.path.join(calc_dir, f)
        c = open(fp, "r", encoding="utf-8", errors="ignore").read()
        m = re.search(r'<html[^>]*class=["\']([^"\']*)["\']', c, re.I)
        cls = m.group(1) if m else ""
        if "dark" not in cls.split():
            not_dark.append(f)

print(f"Total missing dark class ({len(not_dark)}):", not_dark)

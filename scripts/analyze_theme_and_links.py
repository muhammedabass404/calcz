import os
import re

calc_dir = "calcworld-engine/calculators"
index_path = "calcworld-engine/index.html"

# 1. Analyze legal links
links_map = {}
for root, dirs, files in os.walk("calcworld-engine"):
    for f in files:
        if f.endswith(".html"):
            fp = os.path.join(root, f)
            with open(fp, "r", encoding="utf-8", errors="ignore") as fl:
                c = fl.read()
            for m in re.findall(r'href=["\']([^"\']*(?:about|privacy|terms|contact)[^"\']*)["\']', c, re.I):
                links_map[m] = links_map.get(m, 0) + 1

print("--- Legal Links Breakdown ---")
for k, v in sorted(links_map.items(), key=lambda x: -x[1]):
    print(f"  {k:55} : {v} files")

# 2. Analyze UI/UX Theme inconsistencies across all calculators
# Standard CalcWorld attributes:
# - class="dark" on <html>
# - Inter font
# - Tailwind CDN
# - CalcWorld header with logo and theme toggle
print("\n--- UI / Theme Inconsistencies ---")
missing_dark_class = []
missing_tailwind = []
missing_header_logo = []
missing_theme_toggle = []
different_bg_color = []

for f in sorted(os.listdir(calc_dir)):
    if f.endswith(".html"):
        fp = os.path.join(calc_dir, f)
        with open(fp, "r", encoding="utf-8", errors="ignore") as fl:
            c = fl.read()

        # Check html tag
        if not re.search(r'<html[^>]*class=["\'][^"\']*dark', c, re.I):
            missing_dark_class.append(f)

        # Check tailwind
        if "tailwindcss.com" not in c:
            missing_tailwind.append(f)

        # Check header logo branding (CalcWorld)
        if "CalcWorld" not in c and "calcworld" not in c:
            missing_header_logo.append(f)

        # Check theme toggle button
        if "themeToggle" not in c and "theme-toggle" not in c and "toggleTheme" not in c and "darkModeToggle" not in c:
            missing_theme_toggle.append(f)

print(f"Missing dark class on <html>: {len(missing_dark_class)} -> {missing_dark_class[:10]}")
print(f"Missing Tailwind CDN: {len(missing_tailwind)} -> {missing_tailwind[:10]}")
print(f"Missing CalcWorld branding in header: {len(missing_header_logo)} -> {missing_header_logo[:10]}")
print(f"Missing theme toggle: {len(missing_theme_toggle)} -> {missing_theme_toggle[:10]}")

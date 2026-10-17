import os
import re

calc_dir = "calcworld-engine/calculators"

files_with_dollar_inline = []
files_with_mathjax = []

for f in os.listdir(calc_dir):
    if f.endswith(".html"):
        fp = os.path.join(calc_dir, f)
        with open(fp, "r", encoding="utf-8", errors="ignore") as fl:
            c = fl.read()
        if "mathjax" in c.lower():
            files_with_mathjax.append(f)
        if "['$', '$']" in c or '["$", "$"]' in c:
            files_with_dollar_inline.append(f)

print(f"Total with MathJax: {len(files_with_mathjax)}")
print(f"Total with dollar inline math: {len(files_with_dollar_inline)}")
print("Sample with dollar inline:", files_with_dollar_inline[:10])

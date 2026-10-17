import os
import re

calc_dir = "calcworld-engine/calculators"

issues = []

for f in sorted(os.listdir(calc_dir)):
    if f.endswith(".html"):
        fp = os.path.join(calc_dir, f)
        with open(fp, "r", encoding="utf-8", errors="ignore") as fl:
            c = fl.read()

        # Check for HTML tags inside LaTeX constructs
        # e.g., \frac{...<sup>...</sup>...} or \left[ ... <sup> ... \right]
        m_latex_html = re.findall(r'(\\(?:frac|left|right|times|alpha|beta|gamma|sigma|mu|pi|sqrt)[^\n<]*<(?:sup|sub|span|strong|em)[^>]*>[\s\S]*?</(?:sup|sub|span|strong|em)>)', c)
        if m_latex_html:
            issues.append((f, "HTML inside LaTeX", m_latex_html[:3]))

        # Check for \frac outside math delimiters when MathJax is present
        if "mathjax" in c.lower():
            # Check lines with \frac
            for l_idx, line in enumerate(c.split("\n")):
                if "\\frac" in line and not ("$$" in line or "\\(" in line or "\\[" in line or ("$" in line and line.count("$") >= 2)):
                    issues.append((f, f"Raw \\frac line {l_idx+1}", line.strip()[:100]))
                    break

print(f"Total files with detected Math syntax issues: {len(issues)}")
for item in issues[:20]:
    print(item[0], ":", item[1], "->", item[2])

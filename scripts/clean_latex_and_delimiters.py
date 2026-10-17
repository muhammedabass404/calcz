# -*- coding: utf-8 -*-
"""
Precise cleaner for LaTeX formulas and MathJax syntax across all calculators:
1. Fix tab characters created by \\t in python strings (\\text, \\theta, \\times, \\tau)
2. Fix carriage returns created by \\r in python strings (\\rho)
3. Fix HTML tags inside math formulas (<sup>n</sup> -> ^{n}, etc.)
4. Fix stray math delimiters (\\pi$ -> $\\pi$, etc.)
5. Ensure desktop directory is synchronized
"""

import os
import re

calc_dir = "calcworld-engine/calculators"
desktop_dir = "C:/Users/Muham/Desktop/Calc/calcworld-engine/calculators"

def fix_content(c):
    orig = c

    # 1. Fix tab character followed by math command names
    c = c.replace('\text{', '\\text{')
    c = c.replace('\times', '\\times')
    c = c.replace('\theta', '\\theta')
    c = c.replace('\tau', '\\tau')

    # 2. Fix carriage return followed by math command names
    c = c.replace('\rho', '\\rho')

    # 3. Fix <sup> and <sub> inside LaTeX formulas and div.font-mono
    c = re.sub(r'\\frac\{([^\}]*?)<sup>(.*?)</sup>([^\}]*?)\}', r'\\frac{\1^{\2}\3}', c)
    c = re.sub(r'\((1 \+ r)\)<sup>n</sup>', r'(1 + r)^{n}', c)
    c = re.sub(r'\((1 \+ r)\)<sup>-n</sup>', r'(1 + r)^{-n}', c)
    c = re.sub(r'<sup>(\d+)</sup>', r'^{\1}', c)
    c = re.sub(r'<sup>(-?\w+)</sup>', r'^{\1}', c)
    c = re.sub(r'<sub>(\w+)</sub>', r'_{\1}', c)

    # 4. Fix stray \pi$ or \alpha$ without opening $
    # (e.g. " \pi$ " preceded by space or word without $)
    c = re.sub(r'(?<!\$)\\pi\$', r'$\\pi$', c)
    c = re.sub(r'(?<!\$)\\alpha\$', r'$\\alpha$', c)
    c = re.sub(r'(?<!\$)\\beta\$', r'$\\beta$', c)
    c = re.sub(r'(?<!\$)\\gamma\$', r'$\\gamma$', c)
    c = re.sub(r'(?<!\$)\\sigma\$', r'$\\sigma$', c)

    # 5. Fix \times without $ or \(\) when surrounded by math symbols
    # e.g., in HTML font-mono divs, ensure proper display
    return c, c != orig

def main():
    modified = 0
    for f in sorted(os.listdir(calc_dir)):
        if f.endswith('.html'):
            fp = os.path.join(calc_dir, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as fl:
                c = fl.read()

            new_c, changed = fix_content(c)
            if changed:
                with open(fp, 'w', encoding='utf-8') as fl:
                    fl.write(new_c)
                modified += 1
                if os.path.exists(desktop_dir):
                    dfp = os.path.join(desktop_dir, f)
                    with open(dfp, 'w', encoding='utf-8') as fl:
                        fl.write(new_c)

    print(f"Cleaned LaTeX and delimiters in {modified} calculators!")

if __name__ == "__main__":
    main()

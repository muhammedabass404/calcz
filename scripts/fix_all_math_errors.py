# -*- coding: utf-8 -*-
"""
Fix all control characters and math syntax errors across all calculators:
- \x0c -> \frac
- \x07 -> \alpha
- \x08 -> \beta
- \x0b -> \vec
- Fix HTML tags inside LaTeX (<sup>n</sup> -> ^{n}, &times; -> \times, etc.)
- Fix unicode replacement character  -> ° (degree)
- Clean MathJax configuration so that single '$' doesn't hijack currency
"""

import os
import re

calc_dir = "calcworld-engine/calculators"
desktop_dir = "C:/Users/Muham/Desktop/Calc/calcworld-engine/calculators"

def fix_file_content(content):
    modified = False

    # 1. Replace control characters
    if '\x0c' in content:
        content = content.replace('\x0c', '\\f')
        modified = True
    if '\x07' in content:
        content = content.replace('\x07', '\\a')
        modified = True
    if '\x08' in content:
        content = content.replace('\x08', '\\b')
        modified = True
    if '\x0b' in content:
        content = content.replace('\x0b', '\\v')
        modified = True

    # 2. Fix broken degree symbol
    if '' in content:
        content = content.replace('', '&deg;')
        modified = True

    # 3. Fix HTML inside LaTeX in formula blocks
    # Fix instances of \frac{...<sup>...</sup>...} or similar
    def clean_math_block(match):
        text = match.group(0)
        # Replace <sup>...</sup> with ^{...}
        text = re.sub(r'<sup>(.*?)</sup>', r'^{\1}', text)
        # Replace <sub>...</sub> with _{\1}
        text = re.sub(r'<sub>(.*?)</sub>', r'_{\1}', text)
        # Replace &times; with \times
        text = text.replace('&times;', r'\times ')
        # Replace &plusmn; with \pm
        text = text.replace('&plusmn;', r'\pm ')
        # Replace &radic; with \sqrt
        text = text.replace('&radic;', r'\sqrt')
        # Replace &pi; with \pi
        text = text.replace('&pi;', r'\pi ')
        # Replace &sigma; with \sigma
        text = text.replace('&sigma;', r'\sigma ')
        # Replace &alpha; with \alpha
        text = text.replace('&alpha;', r'\alpha ')
        # Replace &beta; with \beta
        text = text.replace('&beta;', r'\beta ')
        # Replace &gamma; with \gamma
        text = text.replace('&gamma;', r'\gamma ')
        # Replace &mu; with \mu
        text = text.replace('&mu;', r'\mu ')
        return text

    # Apply to math blocks like $$...$$, \[...\], \(...\) and div class font-mono
    new_content = re.sub(r'(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\\\(.*?\\\)|\<div[^>]*font-mono[^>]*>[\s\S]*?</div>)', clean_math_block, content)
    if new_content != content:
        content = new_content
        modified = True

    # 4. In MathJax configuration, remove '$' as inline math if present so currency $ doesn't cause errors
    # MathJax = { tex: { inlineMath: [['\\(', '\\)'], ['$', '$']] ...
    pattern_mj = r"inlineMath:\s*\[\s*\['\\\\\(',\s*'\\\\\)'\],\s*\['\$',\s*'\$'\]\s*\]"
    if re.search(pattern_mj, content):
        content = re.sub(pattern_mj, "inlineMath: [['\\\\(', '\\\\)']], processEscapes: true", content)
        modified = True

    pattern_mj2 = r"inlineMath:\s*\[\s*\['\$',\s*'\$'\],\s*\['\\\\\(',\s*'\\\\\)'\]\s*\]"
    if re.search(pattern_mj2, content):
        content = re.sub(pattern_mj2, "inlineMath: [['\\\\(', '\\\\)']], processEscapes: true", content)
        modified = True

    return content, modified

def main():
    fixed_count = 0
    for f in sorted(os.listdir(calc_dir)):
        if f.endswith('.html'):
            fp = os.path.join(calc_dir, f)
            with open(fp, 'r', encoding='utf-8', errors='ignore') as fl:
                orig = fl.read()

            fixed, was_modified = fix_file_content(orig)
            if was_modified:
                with open(fp, 'w', encoding='utf-8') as fl:
                    fl.write(fixed)
                fixed_count += 1

                # Sync to desktop mirror
                if os.path.exists(desktop_dir):
                    dfp = os.path.join(desktop_dir, f)
                    with open(dfp, 'w', encoding='utf-8') as fl:
                        fl.write(fixed)

    print(f"Successfully processed and fixed math errors in {fixed_count} calculator files!")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Wrap and upgrade the 5 calculators without <article> tag:
1. calorie-calculator.html
2. bac-calculator.html
3. overweight-calculator.html
4. resistor-calculator.html
5. wind-chill-calculator.html
"""

import os
import re

calc_dir = "calcworld-engine/calculators"
desktop_dir = "C:/Users/Muham/Desktop/Calc/calcworld-engine/calculators"

def wrap_and_upgrade_calorie():
    fp = os.path.join(calc_dir, "calorie-calculator.html")
    with open(fp, "r", encoding="utf-8") as f:
        c = f.read()

    # Find start of guide
    target = "<h2>Understanding Total Daily Energy Expenditure (TDEE)</h2>"
    if target in c:
        # Import the calorie article from expand_core_articles_part2
        from expand_core_articles_part2 import calorie_article
        # Replace from target to before footer or end of main
        part1 = c.split(target)[0]
        # Find where the old text ends (e.g. before </main> or <footer)
        part2 = c.split(target)[1]
        if "</main>" in part2:
            after_main = "</main>" + part2.split("</main>", 1)[1]
            updated = part1 + calorie_article + "\n" + after_main
        else:
            updated = part1 + calorie_article + "\n</main>\n" + part2

        with open(fp, "w", encoding="utf-8") as fl:
            fl.write(updated)
        if os.path.exists(desktop_dir):
            with open(os.path.join(desktop_dir, "calorie-calculator.html"), "w", encoding="utf-8") as fl:
                fl.write(updated)
        print("Successfully updated calorie-calculator.html with <article> tag!")

def wrap_others():
    for fname in ["bac-calculator.html", "overweight-calculator.html", "resistor-calculator.html", "wind-chill-calculator.html"]:
        fp = os.path.join(calc_dir, fname)
        with open(fp, "r", encoding="utf-8") as f:
            c = f.read()

        if "<article" not in c:
            # Look for a major guide heading
            m = re.search(r'(<h2[^>]*>(?:Understanding|About|How|The|Guide|What)[\s\S]*?)(</main>|<footer|\Z)', c, re.IGNORECASE)
            if m:
                guide_content = m.group(1)
                wrapped_guide = f'<article class="prose dark:prose-invert max-w-none mt-12 bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">\n{guide_content}\n</article>'
                c = c.replace(guide_content, wrapped_guide, 1)
                with open(fp, "w", encoding="utf-8") as fl:
                    fl.write(c)
                if os.path.exists(desktop_dir):
                    with open(os.path.join(desktop_dir, fname), "w", encoding="utf-8") as fl:
                        fl.write(c)
                print(f"Successfully wrapped {fname} in <article> tag!")

def main():
    wrap_and_upgrade_calorie()
    wrap_others()

if __name__ == "__main__":
    main()

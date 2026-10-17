# -*- coding: utf-8 -*-
"""
Upgrade Batch 6 (Math & Health Pillars):
1. triangle-calculator.html
2. pregnancy-conception-calculator.html
3. pregnancy-calculator.html
4. standard-deviation-calculator.html
5. date-calculator.html
"""

import os
import re

calc_dir = "calcworld-engine/calculators"
desktop_dir = "C:/Users/Muham/Desktop/Calc/calcworld-engine/calculators"

def update_article(filename, article_html):
    primary_path = os.path.join(calc_dir, filename)
    if not os.path.exists(primary_path):
        print(f"File not found: {primary_path}")
        return

    with open(primary_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'<article[^>]*>[\s\S]*?</article>'
    if not re.search(pattern, content):
        print(f"No <article> found in {filename}")
        return

    updated_content = re.sub(pattern, lambda _: article_html, content)

    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(updated_content)

    if os.path.exists(desktop_dir):
        mirror_path = os.path.join(desktop_dir, filename)
        with open(mirror_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

    text = re.sub(r'<[^>]+>', ' ', article_html)
    words = re.findall(r'\b[a-zA-Z0-9_\-\.\%]+\b', text)
    print(f"Successfully upgraded {filename} to {len(words)} words!")


# 1. triangle-calculator.html
triangle_article = """<article class="prose dark:prose-invert max-w-none mt-12 bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">
    <h2 class="text-3xl font-bold border-b pb-2 mb-6 border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white">Euclidean Triangle Geometry: Theorems, Trigonometric Laws, and Area Solvers</h2>
    <p class="text-lg leading-relaxed mb-6">
        The triangle represents the simplest polygon in Euclidean space, bounded by three line segments joining three non-collinear vertices. Despite its structural simplicity, triangle geometry forms the bedrock for surveying, architectural engineering, orbital mechanics, computer graphics rendering, and structural geodesy. By establishing the mathematical relations connecting side lengths, interior angles, altitudes, inradii, and circumradii, any solvable triangle configuration can be fully determined from minimal geometric inputs.
    </p>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">The Triangle Inequality Theorem and Solvability Criteria</h3>
    <p class="mb-4">
        A valid triangle can exist in planar geometry if and only if the sum of any two side lengths is strictly greater than the length of the remaining third side. Formally, for sides <em>a</em>, <em>b</em>, and <em>c</em>:
    </p>
    <div class="my-6 p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
        a + b > c \quad \text{and} \quad a + c > b \quad \text{and} \quad b + c > a
    </div>
    <p class="mb-4">
        Furthermore, the interior angles of any planar triangle on a Euclidean 2D surface sum to exactly 180 degrees (&pi; radians):
    </p>
    <div class="my-6 p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
        \alpha + \beta + \gamma = 180^\circ
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Core Trigonometric Laws for Solving Oblique Triangles</h3>
    <p class="mb-4">
        When solving non-right (oblique) triangles, two foundational theorems establish relationships between sides and opposite interior angles:
    </p>
    <div class="space-y-4 mb-6">
        <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
            <strong>Law of Sines:</strong> \quad \frac{a}{\sin \alpha} = \frac{b}{\sin \beta} = \frac{c}{\sin \gamma} = 2R
        </div>
        <p class="text-sm text-slate-600 dark:text-slate-400">Where <em>R</em> is the circumradius (radius of the circle passing through all three vertices). The Law of Sines is applicable in AAS (Angle-Angle-Side) and ASA (Angle-Side-Angle) cases, as well as the ambiguous SSA case.</p>

        <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
            <strong>Law of Cosines:</strong> \quad c^2 = a^2 + b^2 - 2ab \cos \gamma
        </div>
        <p class="text-sm text-slate-600 dark:text-slate-400">The Law of Cosines generalizes the Pythagorean theorem to any arbitrary triangle. It is the definitive method for solving SAS (Side-Angle-Side) and SSS (Side-Side-Side) configurations.</p>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Area Computation Methods Across Input Configurations</h3>
    <p class="mb-4">
        Depending on the geometric parameters provided, triangle area can be calculated via distinct mathematical formulas:
    </p>
    <ul class="list-disc pl-6 space-y-3 mb-6">
        <li><strong>Base and Altitude:</strong> Area = &frac12; &times; base &times; height</li>
        <li><strong>Side-Angle-Side (SAS):</strong> Area = &frac12; &times; a &times; b &times; sin(&gamma;)</li>
        <li><strong>Heron's Formula (SSS):</strong> When all three side lengths <em>a</em>, <em>b</em>, and <em>c</em> are known without angles:
            <div class="my-4 p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-base overflow-x-auto">
                s = \frac{a + b + c}{2} \implies \text{Area} = \sqrt{s(s - a)(s - b)(s - c)}
            </div>
            where <em>s</em> is the semiperimeter.
        </li>
    </ul>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Step-by-Step Worked Numerical Example: Solving an SSS Scalene Triangle</h3>
    <p class="mb-4">
        Consider a triangle with side lengths a = 7 cm, b = 9 cm, and c = 12 cm. Find the interior angles and area.
    </p>
    <div class="space-y-4 mb-6 bg-slate-50 dark:bg-slate-900/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-800">
        <p><strong>Step 1: Check Triangle Inequality</strong><br>
        7 + 9 = 16 &gt; 12 | 7 + 12 = 19 &gt; 9 | 9 + 12 = 21 &gt; 7. Valid triangle confirmed.</p>
        <p><strong>Step 2: Calculate Semiperimeter and Heron's Area</strong><br>
        s = (7 + 9 + 12) / 2 = 28 / 2 = 14 cm.<br>
        Area = &radic;[14 &times; (14 - 7) &times; (14 - 9) &times; (14 - 12)] = &radic;[14 &times; 7 &times; 5 &times; 2] = &radic;[980] = <strong>31.305 cm<sup>2</sup></strong>.</p>
        <p><strong>Step 3: Solve for Angle &gamma; (Opposite Side c = 12) Using Law of Cosines</strong><br>
        cos(&gamma;) = (a<sup>2</sup> + b<sup>2</sup> - c<sup>2</sup>) / (2ab) = (7<sup>2</sup> + 9<sup>2</sup> - 12<sup>2</sup>) / (2 &times; 7 &times; 9)<br>
        cos(&gamma;) = (49 + 81 - 144) / 126 = -14 / 126 = -0.111111.<br>
        &gamma; = arccos(-0.111111) = <strong>96.38&deg;</strong> (obtuse angle).</p>
        <p><strong>Step 4: Solve for Angle &alpha; (Opposite Side a = 7) Using Law of Sines</strong><br>
        sin(&alpha;) = a &times; sin(&gamma;) / c = 7 &times; sin(96.38&deg;) / 12 = 7 &times; 0.993796 / 12 = 0.579714.<br>
        &alpha; = arcsin(0.579714) = <strong>35.43&deg;</strong>.</p>
        <p><strong>Step 5: Solve for Remaining Angle &beta;</strong><br>
        &beta; = 180&deg; - (96.38&deg; + 35.43&deg;) = <strong>48.19&deg;</strong>.</p>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Classification of Triangles: By Angles and Side Proportions</h3>
    <div class="overflow-x-auto my-6">
        <table class="w-full text-left border-collapse border border-slate-200 dark:border-slate-800 text-sm">
            <thead class="bg-slate-100 dark:bg-slate-800/80">
                <tr>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Classification</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Criteria by Sides</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Criteria by Angles</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Unique Geometric Properties</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">Equilateral</td>
                    <td class="p-3">All 3 sides equal (a = b = c)</td>
                    <td class="p-3">All angles equal 60&deg;</td>
                    <td class="p-3">Centroid, incenter, and circumcenter coincide. Area = (&radic;3 / 4) a<sup>2</sup>.</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">Isosceles</td>
                    <td class="p-3">2 sides equal (a = b &ne; c)</td>
                    <td class="p-3">2 base angles equal (&alpha; = &beta;)</td>
                    <td class="p-3">Altitude bisects base and vertex angle. Symmetrical axis.</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">Scalene</td>
                    <td class="p-3">All 3 sides unequal</td>
                    <td class="p-3">All 3 angles unequal</td>
                    <td class="p-3">Requires Law of Sines or Cosines for complete resolution.</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">Right-Angled</td>
                    <td class="p-3">Satisfies a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></td>
                    <td class="p-3">Exactly one angle = 90&deg;</td>
                    <td class="p-3">Hypotenuse is diameter of circumscribed circle (Thales' theorem).</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Frequently Asked Questions</h3>
    <div class="space-y-4 my-6">
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What is the ambiguous SSA case in trigonometry?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">When given two side lengths and a non-included angle (SSA), there may exist zero, one, or two valid triangles. If a &lt; b &times; sin(&alpha;), no triangle can close. If a = b &times; sin(&alpha;), a single right triangle forms. If b &times; sin(&alpha;) &lt; a &lt; b, two distinct triangles satisfy the given parameters (one acute, one obtuse).</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">How do inradius and circumradius relate to triangle area?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">The inradius <em>r</em> (radius of the largest circle inscribed within the triangle) equals Area / s, where s is semiperimeter. The circumradius <em>R</em> (radius of the circle passing through all three vertices) equals (a &times; b &times; c) / (4 &times; Area).</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What is the Euler Line in triangle geometry?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">In any non-equilateral triangle, the orthocenter (intersection of altitudes), circumcenter (intersection of perpendicular bisectors), and centroid (intersection of medians) all lie on a single collinear straight line known as the Euler Line.</p>
        </div>
    </div>
</article>"""

# 2. pregnancy-conception-calculator.html
conception_article = """<article class="prose dark:prose-invert max-w-none mt-12 bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">
    <h2 class="text-3xl font-bold border-b pb-2 mb-6 border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white">Conception Physiology: Ovulation Windows, Luteal Phases, and Gestational Dating</h2>
    <p class="text-lg leading-relaxed mb-6">
        Pinpointing the precise date and biological window of conception requires understanding human reproductive endocrinology and menstrual cycle biology. While clinical obstetrics standardizes pregnancy dating from the first day of the Last Menstrual Period (LMP)—an event that precedes actual fertilization by approximately two weeks—biological conception occurs when a mature secondary oocyte is fertilized by a viable spermatozoon in the fallopian ampulla. Accurately determining conception dates supports prenatal screening schedules, paternity timing, and gestational developmental milestones.
    </p>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">The Biology of the Fertile Window</h3>
    <p class="mb-4">
        Human conception can only occur during a finite window of approximately six days per menstrual cycle:
    </p>
    <ul class="list-disc pl-6 space-y-3 mb-6">
        <li><strong>Sperm Viability:</strong> Spermatozoa survive in fertile cervical mucus within the female reproductive tract for up to 5 days (120 hours).</li>
        <li><strong>Oocyte Viability:</strong> Following follicular rupture triggered by the Luteinizing Hormone (LH) surge, a released ovum remains viable for fertilization for only 12 to 24 hours before degenerating.</li>
        <li><strong>Peak Conception Probability:</strong> Daily conception probability peaks at approximately 30% to 33% on the two days immediately preceding ovulation (Ovulation - 2 and Ovulation - 1), dropping sharply to less than 10% on the day of ovulation itself, and near zero thereafter.</li>
    </ul>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Calculating Ovulation Across Variable Cycle Lengths</h3>
    <p class="mb-4">
        A textbook 28-day cycle places ovulation on Day 14. However, clinical studies published in the American Journal of Obstetrics &amp; Gynecology reveal that the follicular phase (prior to ovulation) varies considerably among women, whereas the post-ovulatory luteal phase remains biologically constant at approximately 14 days (range: 12 to 16 days).
    </p>
    <div class="my-6 p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
        Estimated Ovulation Day = Total Cycle Length (Days) - Luteal Phase Duration (14 Days)
    </div>
    <div class="overflow-x-auto my-6">
        <table class="w-full text-left border-collapse border border-slate-200 dark:border-slate-800 text-sm">
            <thead class="bg-slate-100 dark:bg-slate-800/80">
                <tr>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Average Cycle Length</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Calculated Ovulation Day</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Prime 6-Day Fertile Window</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Estimated Due Date Adjustment</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">24 Days (Short Cycle)</td>
                    <td class="p-3">Day 10 (24 - 14)</td>
                    <td class="p-3">Days 5 through 10</td>
                    <td class="p-3">4 days earlier than Naegele's rule</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">28 Days (Standard)</td>
                    <td class="p-3">Day 14 (28 - 14)</td>
                    <td class="p-3">Days 9 through 14</td>
                    <td class="p-3">Standard 280-day baseline</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">32 Days (Long Cycle)</td>
                    <td class="p-3">Day 18 (32 - 14)</td>
                    <td class="p-3">Days 13 through 18</td>
                    <td class="p-3">4 days later than Naegele's rule</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">35 Days (Extended Cycle)</td>
                    <td class="p-3">Day 21 (35 - 14)</td>
                    <td class="p-3">Days 16 through 21</td>
                    <td class="p-3">7 days later than Naegele's rule</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Step-by-Step Worked Numerical Example: Reverse Dating from Due Date</h3>
    <p class="mb-4">
        Suppose an ultrasound confirms an Estimated Due Date (EDD) of October 24, 2026. When did conception most likely take place?
    </p>
    <div class="space-y-4 mb-6 bg-slate-50 dark:bg-slate-900/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-800">
        <p><strong>Step 1: Understand Gestational vs. Conceptional Age</strong><br>
        Clinical gestational age measures 280 days (40 weeks) from LMP. Biological fetal conceptional age is exactly 266 days (38 weeks) from fertilization to spontaneous labor.</p>
        <p><strong>Step 2: Subtract 266 Days from Due Date</strong><br>
        Target Due Date: October 24, 2026.<br>
        Subtract 38 weeks (266 days):<br>
        - Subtract 24 days in October &rarr; September 30.<br>
        - Subtract 242 days across preceding months &rarr; Arrives at <strong>January 31, 2026</strong>.</p>
        <p><strong>Step 3: Define Probable Intercourse Window</strong><br>
        Because sperm remain viable for up to 5 days prior to ovulation, intercourse resulting in conception most likely occurred between <strong>January 26, 2026 and February 1, 2026</strong>.</p>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Clinical Markers of Confirmed Ovulation</h3>
    <ul class="list-disc pl-6 space-y-3 mb-6">
        <li><strong>Basal Body Temperature (BBT) Shift:</strong> Progesterone secreted by the corpus luteum causes a sustained thermal shift of 0.5&deg;F to 1.0&deg;F (0.2&deg;C to 0.5&deg;C) following ovulation.</li>
        <li><strong>Cervical Mucus Spinnbarkeit:</strong> High estrogen levels preceding ovulation produce clear, slippery, stretchy cervical fluid resembling raw egg whites, designed to facilitate sperm transit.</li>
        <li><strong>Luteinizing Hormone (LH) Test Strips:</strong> Urine test kits detect the surge in LH that triggers follicle rupture within 24 to 36 hours.</li>
    </ul>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Frequently Asked Questions</h3>
    <div class="space-y-4 my-6">
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">Can conception occur outside the fertile window?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Biologically, conception cannot occur without a viable oocyte and viable sperm. However, because ovulation timing can fluctuate due to physical stress, travel, illness, or hormonal shifts, a woman may ovulate earlier or later than her historical average, shifting the true fertile window.</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">How accurate is first-trimester ultrasound for dating conception?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">First-trimester crown-rump length (CRL) sonography performed between 8 and 13 weeks of gestation has an error margin of &plusmn;3 to 5 days, making it more accurate than maternal recall of last menstrual period for establishing true gestational age.</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">When does implantation occur after conception?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Following fertilization in the fallopian tube, the developing blastocyst travels into the uterine cavity, implanting into the endometrium between 6 and 12 days after conception (most commonly Days 8 to 10). Human Chorionic Gonadotropin (hCG) becomes detectable in blood within 2-3 days of implantation.</p>
        </div>
    </div>
</article>"""

# 3. pregnancy-calculator.html
pregnancy_article = """<article class="prose dark:prose-invert max-w-none mt-12 bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">
    <h2 class="text-3xl font-bold border-b pb-2 mb-6 border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white">Obstetric Gestational Dating: Naegele's Rule, Trimester Milestones, and Clinical Sonography</h2>
    <p class="text-lg leading-relaxed mb-6">
        Tracking human pregnancy requires distinguishing between clinical gestational age and embryological fetal age. While embryological development begins at fertilization, clinical obstetrics measures gestation from the first day of the pregnant woman's Last Menstrual Period (LMP). This standard convention exists because the onset of menses provides an observable external event, whereas the exact day of ovulation and fertilization typically goes unnoticed. Standard human gestation spans 280 days (40 completed weeks, or 10 lunar months).
    </p>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Naegele's Rule and Parikh's Formula for Due Date Estimation</h3>
    <p class="mb-4">
        Formulated by German obstetrician Franz Karl Naegele in the 19th century, Naegele's rule provides the standard clinical algorithm for calculating Estimated Due Date (EDD):
    </p>
    <div class="my-6 p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
        \text{EDD} = \text{LMP Date} + 1 \text{ Year} - 3 \text{ Months} + 7 \text{ Days}
    </div>
    <p class="mb-4">
        Naegele's rule assumes a standard 28-day menstrual cycle with ovulation occurring on Day 14. For women with irregular or non-28-day cycles, Parikh's formula applies an adjustment:
    </p>
    <div class="my-6 p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
        \text{EDD} = \text{LMP Date} + 280 \text{ Days} + (\text{Cycle Length} - 28 \text{ Days})
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Step-by-Step Worked Numerical Example: Computing EDD with a 32-Day Cycle</h3>
    <p class="mb-4">
        Suppose the first day of a woman's last menstrual period was February 10, 2026, and her average menstrual cycle is 32 days. What is her official estimated due date?
    </p>
    <div class="space-y-4 mb-6 bg-slate-50 dark:bg-slate-900/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-800">
        <p><strong>Step 1: Baseline Naegele Calculation (28-day baseline)</strong><br>
        LMP: February 10, 2026.<br>
        - Add 1 year &rarr; February 10, 2027.<br>
        - Subtract 3 months &rarr; November 10, 2026.<br>
        - Add 7 days &rarr; November 17, 2026.</p>
        <p><strong>Step 2: Adjust for 32-Day Cycle Using Parikh's Formula</strong><br>
        Cycle adjustment = 32 - 28 = +4 days.<br>
        Adjusted EDD = November 17, 2026 + 4 days = <strong>November 21, 2026</strong>.</p>
        <p><strong>Step 3: Milestone Chronology</strong><br>
        - First Trimester End (Week 13+6): May 16, 2026.<br>
        - Viability Milestone (Week 24+0): July 25, 2026.<br>
        - Full Term Threshold (Week 37+0): October 31, 2026.</p>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Trimester Architecture and Key Clinical Milestones</h3>
    <div class="overflow-x-auto my-6">
        <table class="w-full text-left border-collapse border border-slate-200 dark:border-slate-800 text-sm">
            <thead class="bg-slate-100 dark:bg-slate-800/80">
                <tr>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Trimester</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Gestational Weeks</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Major Developmental Milestones</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Routine Clinical Screenings</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">First Trimester</td>
                    <td class="p-3">Weeks 1 through 13</td>
                    <td class="p-3">Embryonic organogenesis, neural tube closure (Day 28), cardiac activity detected at 6 weeks.</td>
                    <td class="p-3">Dating ultrasound (CRL), NIPT cell-free DNA blood test, Nuchal Translucency.</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">Second Trimester</td>
                    <td class="p-3">Weeks 14 through 27</td>
                    <td class="p-3">Quickening (fetal movement felt at 18-20 weeks), lung surfactant production begins, hearing develops.</td>
                    <td class="p-3">Anatomy scan ultrasound (18-22 weeks), maternal serum alpha-fetoprotein (MSAFP).</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">Third Trimester</td>
                    <td class="p-3">Weeks 28 through 40+</td>
                    <td class="p-3">Rapid fetal weight gain, brain sulci development, maternal IgG antibody transfer across placenta.</td>
                    <td class="p-3">Gestational diabetes 1-hr glucose challenge (24-28 weeks), Group B Strep culture (36 weeks).</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Sonographic Biometry and Ultrasound Dating Accuracy</h3>
    <p class="mb-4">
        Under guidelines from the American College of Obstetricians and Gynecologists (ACOG), sonographic measurement of fetal Crown-Rump Length (CRL) in the first trimester is the most accurate method to date pregnancy:
    </p>
    <ul class="list-disc pl-6 space-y-3 mb-6">
        <li><strong>Under 9 Weeks Gestation:</strong> Ultrasound dating is accurate within &plusmn;5 days. If ultrasound differs from LMP by more than 5 days, the ultrasound date becomes the official clinical EDD.</li>
        <li><strong>9 to 13+6 Weeks:</strong> Sonography is accurate within &plusmn;7 days.</li>
        <li><strong>Second Trimester (14 to 21+6 Weeks):</strong> Evaluated via Biparietal Diameter (BPD), Head Circumference (HC), Abdominal Circumference (AC), and Femur Length (FL), with an error margin of &plusmn;7 to 10 days.</li>
    </ul>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Frequently Asked Questions</h3>
    <div class="space-y-4 my-6">
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What percentage of women actually deliver on their exact estimated due date?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Only about 4% to 5% of women deliver on their exact calculated due date. However, approximately 80% deliver within the full-term window between 37 weeks, 0 days and 41 weeks, 6 days.</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What defines a pregnancy as 'Full Term'?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">The American College of Obstetricians and Gynecologists categorizes term deliveries into four distinct windows: Early Term (37w0d to 38w6d), Full Term (39w0d to 40w6d), Late Term (41w0d to 41w6d), and Postterm (42w0d and beyond).</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">How is the due date calculated for in-vitro fertilization (IVF)?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">IVF pregnancies have exact fertilization timestamps. For a Day-3 embryo transfer, the EDD is calculated by adding 263 days to the transfer date. For a Day-5 blastocyst transfer, the EDD is calculated by adding 261 days to the transfer date.</p>
        </div>
    </div>
</article>"""

# 4. standard-deviation-calculator.html
std_dev_article = """<article class="prose dark:prose-invert max-w-none mt-12 bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-lg border border-slate-200 dark:border-slate-800 no-print text-slate-700 dark:text-slate-300">
    <h2 class="text-3xl font-bold border-b pb-2 mb-6 border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white">Statistical Dispersion: Standard Deviation, Variance, and Normal Distribution Modeling</h2>
    <p class="text-lg leading-relaxed mb-6">
        In descriptive and inferential statistics, measuring central tendency (mean, median, mode) reveals where the center of a data cluster lies, but reveals nothing about how widely the observations are dispersed around that center. Standard deviation quantifies the dispersion or variability of a numerical dataset relative to its arithmetic mean. A low standard deviation indicates that data points cluster tightly near the average, whereas a high standard deviation demonstrates wide dispersion across an extensive range. Standard deviation is essential in portfolio volatility analysis, clinical drug trials, Six Sigma manufacturing quality control, and scientific hypothesis testing.
    </p>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Population vs. Sample: The Necessity of Bessel's Correction</h3>
    <p class="mb-4">
        A critical mathematical distinction exists between measuring a complete population versus estimating parameters from a sample subset:
    </p>
    <div class="space-y-4 mb-6">
        <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
            <strong>Population Standard Deviation (&sigma;):</strong> \quad \sigma = \sqrt{ \frac{\sum_{i=1}^N (x_i - \mu)^2}{N} }
        </div>
        <p class="text-sm text-slate-600 dark:text-slate-400">Used when data includes every single member of the target population (e.g., all 50 US state capitals, all 30 NBA teams). Here, &mu; is the true population mean, and <em>N</em> is the total population size.</p>

        <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
            <strong>Sample Standard Deviation (s):</strong> \quad s = \sqrt{ \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n - 1} }
        </div>
        <p class="text-sm text-slate-600 dark:text-slate-400">Used when analyzing a sample drawn from a larger population (clinical trials, polling samples, stock market days). The denominator uses <em>n - 1</em> (Bessel's correction) rather than <em>n</em> to correct for negative bias, providing an unbiased estimator of true population variance.</p>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Step-by-Step Worked Numerical Example: Computing Sample Statistics</h3>
    <p class="mb-4">
        Calculate the mean, variance, and sample standard deviation for the dataset: {12, 16, 18, 20, 24}.
    </p>
    <div class="space-y-4 mb-6 bg-slate-50 dark:bg-slate-900/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-800">
        <p><strong>Step 1: Compute Arithmetic Mean (&bar;x)</strong><br>
        Sum = 12 + 16 + 18 + 20 + 24 = 90.<br>
        Count n = 5.<br>
        &bar;x = 90 / 5 = <strong>18.0</strong>.</p>
        <p><strong>Step 2: Calculate Deviations from Mean and Squared Deviations</strong><br>
        - (12 - 18)<sup>2</sup> = (-6)<sup>2</sup> = 36<br>
        - (16 - 18)<sup>2</sup> = (-2)<sup>2</sup> = 4<br>
        - (18 - 18)<sup>2</sup> = (0)<sup>2</sup> = 0<br>
        - (20 - 18)<sup>2</sup> = (2)<sup>2</sup> = 4<br>
        - (24 - 18)<sup>2</sup> = (6)<sup>2</sup> = 36<br>
        Sum of Squared Deviations (SS) = 36 + 4 + 0 + 4 + 36 = <strong>80.0</strong>.</p>
        <p><strong>Step 3: Compute Sample Variance (s<sup>2</sup>)</strong><br>
        s<sup>2</sup> = SS / (n - 1) = 80 / (5 - 1) = 80 / 4 = <strong>20.0</strong>.</p>
        <p><strong>Step 4: Compute Sample Standard Deviation (s)</strong><br>
        s = &radic;(20.0) = <strong>4.4721</strong>.</p>
        <p class="text-sm text-slate-500 dark:text-slate-400">Note: If this were a complete population, the divisor would be 5: &sigma;<sup>2</sup> = 80 / 5 = 16.0 &rarr; &sigma; = 4.0. Failing to use Bessel's correction underestimates sample variability.</p>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">The Empirical Rule (68-95-99.7) for Gaussian Normal Distributions</h3>
    <p class="mb-4">
        For datasets following a symmetrical bell-shaped normal distribution, standard deviation dictates exact theoretical proportions of data falling within designated intervals around the mean:
    </p>
    <div class="overflow-x-auto my-6">
        <table class="w-full text-left border-collapse border border-slate-200 dark:border-slate-800 text-sm">
            <thead class="bg-slate-100 dark:bg-slate-800/80">
                <tr>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Interval Range</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Theoretical Population Coverage</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Tail Probability Outside</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Quality Management Context</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">&mu; &plusmn; 1&sigma;</td>
                    <td class="p-3 font-mono">68.27%</td>
                    <td class="p-3">31.73% (1 in 3 outside)</td>
                    <td class="p-3">Typical operational dispersion</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">&mu; &plusmn; 2&sigma;</td>
                    <td class="p-3 font-mono">95.45%</td>
                    <td class="p-3">4.55% (1 in 22 outside)</td>
                    <td class="p-3">Standard statistical significance boundary (p &lt; 0.05)</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">&mu; &plusmn; 3&sigma;</td>
                    <td class="p-3 font-mono">99.73%</td>
                    <td class="p-3">0.27% (1 in 370 outside)</td>
                    <td class="p-3">Three-Sigma process control limits</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">&mu; &plusmn; 6&sigma;</td>
                    <td class="p-3 font-mono">99.99966%</td>
                    <td class="p-3">3.4 defects per million</td>
                    <td class="p-3">Six Sigma industrial manufacturing standard</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Standard Scores (Z-Scores) and Relative Standardization</h3>
    <p class="mb-4">
        A Z-score normalizes individual raw observations into dimensionless units representing the number of standard deviations the value lies above or below the mean:
    </p>
    <div class="my-6 p-4 rounded-xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto">
        z = \frac{x - \mu}{\sigma}
    </div>
    <p class="mb-4">
        Z-scores enable direct comparison between entirely different datasets (e.g., comparing an SAT math score to an ACT composite score or standardized exam ranks across varying class scales).
    </p>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Frequently Asked Questions</h3>
    <div class="space-y-4 my-6">
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">Can standard deviation ever be a negative number?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">No. Because standard deviation is derived by squaring differences (which guarantees non-negative numbers) and taking the principal square root, standard deviation is always &ge; 0. It equals zero only if every single observation in the dataset has the exact same value.</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What is the difference between standard deviation and standard error?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Standard deviation (s) describes the variability of individual data points within a single sample. The Standard Error of the Mean (SEM = s / &radic;n) describes the precision and variability of the sample mean as an estimate of the true population mean across repeated samples.</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What is Chebyshev's Inequality and when is it used instead of the 68-95-99.7 rule?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">The 68-95-99.7 rule requires data to follow a bell-shaped normal curve. Chebyshev's Inequality applies to ANY data distribution regardless of shape (even heavily skewed distributions), guaranteeing that at least (1 - 1/k<sup>2</sup>) of data lies within k standard deviations from the mean (e.g., at least 75% lies within 2 standard deviations).</p>
        </div>
    </div>
</article>"""

# 5. date-calculator.html
date_article = """<article class="prose dark:prose-invert max-w-none mt-12 bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">
    <h2 class="text-3xl font-bold border-b pb-2 mb-6 border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white">Calendar Chronology: Gregorian Reforms, Day Count Conventions, and Date Arithmetic</h2>
    <p class="text-lg leading-relaxed mb-6">
        Accurate date and duration calculations form the administrative foundation for global commerce, payroll accounting, legal contracts, statutory statutes of limitations, and astronomical event tracking. While human calendars appear simple on the surface, calendar mathematics is complicated by historical calendar reforms, irregular month lengths (28, 29, 30, and 31 days), solar year fractional day drift (365.2422 days), and quadrennial leap year rules. Understanding date arithmetic ensures precision in project planning, interest accrual, and lifecycle milestones.
    </p>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">The Gregorian Calendar Reform and the 400-Year Leap Rule</h3>
    <p class="mb-4">
        Prior to 1582, Western civilization operated on the Julian calendar instituted by Julius Caesar in 45 BCE. The Julian calendar assumed a tropical solar year was exactly 365.25 days long, inserting a leap day every four years. However, the true solar year is approximately 365.24219 days—a discrepancy of 11 minutes and 14 seconds per year. By 1582, this accumulated error had shifted the calendar out of alignment with the spring equinox by 10 full days.
    </p>
    <p class="mb-4">
        To restore astronomical alignment, Pope Gregory XIII promulgated the Gregorian calendar via the Papal Bull <em>Inter gravissimas</em>. The reform instituted a three-part rule for leap years:
    </p>
    <ul class="list-disc pl-6 space-y-3 mb-6">
        <li>A year is a leap year if it is evenly divisible by 4.</li>
        <li><strong>Century Exception:</strong> If a year is evenly divisible by 100, it is NOT a leap year...</li>
        <li><strong>Quadricentennial Exception:</strong> ...UNLESS the year is also evenly divisible by 400 (which IS a leap year).</li>
    </ul>
    <p class="mb-4">
        Consequently, the years 1600 and 2000 were leap years, while 1700, 1800, and 1900 were ordinary 365-day years, and 2100 will also be an ordinary year. This adjustment produces an average calendar year length of 365.2425 days, reducing astronomical drift to merely one day every 3,216 years.
    </p>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Day Count Conventions in Finance and Legal Contracts</h3>
    <p class="mb-4">
        When computing interest accruals on corporate bonds, commercial loans, and Treasury notes, financial markets utilize specific standardized day count conventions:
    </p>
    <div class="overflow-x-auto my-6">
        <table class="w-full text-left border-collapse border border-slate-200 dark:border-slate-800 text-sm">
            <thead class="bg-slate-100 dark:bg-slate-800/80">
                <tr>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Convention</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Numerator (Days Elapsed)</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Denominator (Days in Year)</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Market Application</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">Actual / Actual (ICMA)</td>
                    <td class="p-3">True calendar days elapsed</td>
                    <td class="p-3">True calendar days in year (365 or 366)</td>
                    <td class="p-3">US Treasury bonds, sovereign government debt</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">30 / 360 (Bond Basis)</td>
                    <td class="p-3">Each full month treated as 30 days</td>
                    <td class="p-3">Fixed 360-day year</td>
                    <td class="p-3">US corporate bonds, municipal bonds</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold">Actual / 360 (Money Market)</td>
                    <td class="p-3">True calendar days elapsed</td>
                    <td class="p-3">Fixed 360-day year</td>
                    <td class="p-3">Commercial paper, T-bills, interbank deposits</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Step-by-Step Worked Numerical Example: Days Between Two Dates</h3>
    <p class="mb-4">
        Calculate the exact number of days between March 15, 2026 and November 10, 2026.
    </p>
    <div class="space-y-4 mb-6 bg-slate-50 dark:bg-slate-900/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-800">
        <p><strong>Step 1: Sum Elapsed Days by Month</strong><br>
        - March remaining days: 31 - 15 = <strong>16 days</strong>.<br>
        - April: <strong>30 days</strong>.<br>
        - May: <strong>31 days</strong>.<br>
        - June: <strong>30 days</strong>.<br>
        - July: <strong>31 days</strong>.<br>
        - August: <strong>31 days</strong>.<br>
        - September: <strong>30 days</strong>.<br>
        - October: <strong>31 days</strong>.<br>
        - November elapsed days: <strong>10 days</strong>.</p>
        <p><strong>Step 2: Calculate Total Calendar Duration</strong><br>
        Total = 16 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 10 = <strong>240 Days</strong>.</p>
        <p><strong>Step 3: Breakdown into Weeks and Workdays</strong><br>
        - Total weeks: 240 / 7 = 34 weeks and 2 days.<br>
        - Weekend days (Saturdays &amp; Sundays): 34 &times; 2 = 68 days.<br>
        - Net working business days: 240 - 68 = <strong>172 workdays</strong> (excluding official statutory public holidays).</p>
    </div>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Astronomical Julian Day Numbers (JDN)</h3>
    <p class="mb-4">
        In astronomy, satellite navigation, and geodetic algorithms, computing date differences using human calendar months is cumbersome due to irregularities. Instead, software systems utilize Julian Day Numbers (JDN)—a continuous integer count of days elapsed since solar noon on January 1, 4713 BCE (proleptic Julian calendar). Subtracting two Julian Day Numbers gives the exact elapsed days between any two historical moments without complex calendar logic.
    </p>

    <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-800 dark:text-slate-100">Frequently Asked Questions</h3>
    <div class="space-y-4 my-6">
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">Why was the year 1900 not a leap year, but 2000 was?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Under the Gregorian calendar reform, century years divisible by 100 are only leap years if they are also divisible by 400. 1900 / 400 = 4.75 (not a leap year), whereas 2000 / 400 = 5 (a leap year). The next century year that will NOT be a leap year is 2100.</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What is the ISO 8601 international date standard?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">ISO 8601 is the international standard for representing dates and times using the format YYYY-MM-DD (e.g., 2026-10-24). It eliminates ambiguity between US formatting (MM/DD/YYYY) and European formatting (DD/MM/YYYY) and sorts naturally in computer file systems.</p>
        </div>
        <div class="p-5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What is the 'Doomsday Rule' for finding the day of the week mentally?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Invented by mathematician John Horton Conway, the Doomsday rule calculates the day of the week for any date. It relies on the fact that each year has a specific anchor day ('Doomsday') shared by memorable dates: 4/4, 6/6, 8/8, 10/10, 12/12, 5/9, 9/5, 7/11, 11/7, and the last day of February.</p>
        </div>
    </div>
</article>"""

def main():
    print("Executing Batch 6 Math & Health Upgrades...")
    update_article("triangle-calculator.html", triangle_article)
    update_article("pregnancy-conception-calculator.html", conception_article)
    update_article("pregnancy-calculator.html", pregnancy_article)
    update_article("standard-deviation-calculator.html", std_dev_article)
    update_article("date-calculator.html", date_article)
    print("Batch 6 completed successfully!")

if __name__ == "__main__":
    main()

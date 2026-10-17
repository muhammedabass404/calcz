# -*- coding: utf-8 -*-
"""
Enrich SEO Keywords, Interlinking (Internal Backlinks), and Article Depth
Inspired by the industry-standard architecture of Calculator.net.
"""

import os
import re

calc_dir = "calcworld-engine/calculators"
desktop_dir = "C:/Users/Muham/Desktop/Calc/calcworld-engine/calculators"

# Semantic clusters for interlinking (filename -> list of (related_file, anchor_text, description))
RELATED_MAP = {
    # Mortgages & Lending
    "mortgage-calculator.html": [
        ("amortization-calculator.html", "Amortization Calculator", "View the full month-by-month principal and interest payoff schedule."),
        ("loan-calculator.html", "Loan Calculator", "Compute fixed-rate payments and total financing interest for any debt."),
        ("compound-interest-calculator.html", "Compound Interest Calculator", "Model investment wealth accumulation vs mortgage debt costs."),
        ("refinance-calculator.html", "Mortgage Refinance Calculator", "Evaluate break-even timelines and monthly savings from refinancing."),
        ("mortgage-payoff-calculator.html", "Mortgage Payoff Calculator", "Calculate how extra principal payments shorten your loan term."),
        ("real-estate-calculator.html", "Real Estate Investment Calculator", "Analyze rental cash flow, cap rate, and net operating income.")
    ],
    "amortization-calculator.html": [
        ("mortgage-calculator.html", "Mortgage Calculator", "Calculate comprehensive monthly home financing payments including taxes and insurance."),
        ("loan-calculator.html", "Loan Calculator", "Determine monthly installments and borrowing charges for consumer debts."),
        ("interest-calculator.html", "Interest Calculator", "Compare simple interest vs compound interest accrual schedules."),
        ("auto-loan-calculator.html", "Auto Loan Calculator", "Estimate vehicle financing payments, sales tax, and trade-in equity."),
        ("mortgage-recast-calculator.html", "Mortgage Recast Calculator", "Compute payment reduction after making a lump-sum principal paydown.")
    ],
    "auto-loan-calculator.html": [
        ("loan-calculator.html", "Loan Calculator", "Model personal and consumer installment debt schedules."),
        ("amortization-calculator.html", "Amortization Calculator", "Inspect month-by-month principal reduction and interest charges."),
        ("sales-tax-calculator.html", "Sales Tax Calculator", "Determine local state and municipal vehicle sales tax liabilities."),
        ("gas-mileage-calculator.html", "Gas Mileage Calculator", "Calculate actual fuel economy (MPG or L/100km) and operating costs."),
        ("fuel-cost-calculator.html", "Fuel Cost Calculator", "Estimate annual commute fuel expenditures and road trip expenses.")
    ],
    "loan-calculator.html": [
        ("mortgage-calculator.html", "Mortgage Calculator", "Plan residential home purchase financing with property taxes and PMI."),
        ("auto-loan-calculator.html", "Auto Loan Calculator", "Calculate car loan payments, trade-in equity, and dealership fees."),
        ("amortization-calculator.html", "Amortization Calculator", "Inspect detailed amortization schedules and payment allocation."),
        ("interest-calculator.html", "Interest Calculator", "Evaluate nominal APR vs effective annual interest compounding."),
        ("personal-loan-calculator.html", "Personal Loan Calculator", "Compare unsecured personal borrowing offers and consolidation terms.")
    ],
    "interest-calculator.html": [
        ("compound-interest-calculator.html", "Compound Interest Calculator", "Harness the power of exponential compound yields over multi-year horizons."),
        ("loan-calculator.html", "Loan Calculator", "Calculate fixed-term borrowing payments and total interest paid to lenders."),
        ("investment-calculator.html", "Investment Calculator", "Project multi-asset portfolio growth with regular monthly contributions."),
        ("inflation-calculator.html", "Inflation Calculator", "Measure real post-inflation purchasing power using historical CPI data."),
        ("cd-calculator.html", "Certificate of Deposit (CD) Calculator", "Determine guaranteed CD maturity yields and early withdrawal penalties.")
    ],
    "compound-interest-calculator.html": [
        ("investment-calculator.html", "Investment Calculator", "Model portfolio asset allocation and recurring monthly deposits."),
        ("retirement-calculator.html", "Retirement Calculator", "Determine your required nest egg size using safe withdrawal rules."),
        ("interest-calculator.html", "Interest Calculator", "Compare simple linear interest against exponential compounding."),
        ("inflation-calculator.html", "Inflation Calculator", "Adjust nominal compound yields for consumer price inflation drag."),
        ("401k-calculator.html", "401(k) Retirement Calculator", "Evaluate employer match matching contributions and pre-tax tax advantages.")
    ],
    "investment-calculator.html": [
        ("compound-interest-calculator.html", "Compound Interest Calculator", "Simulate long-term compound growth across varying contribution cadences."),
        ("retirement-calculator.html", "Retirement Calculator", "Plan portfolio longevity and target decumulation budgets."),
        ("roi-calculator.html", "Return on Investment (ROI) Calculator", "Calculate percentage ROI, annualized ROI, and capital efficiency."),
        ("inflation-calculator.html", "Inflation Calculator", "Determine real post-inflation purchasing gains across your horizon."),
        ("finance-calculator.html", "Finance Calculator", "Solve Time Value of Money (TVM) present and future value equations.")
    ],
    "retirement-calculator.html": [
        ("investment-calculator.html", "Investment Calculator", "Project multi-decade portfolio asset accumulation."),
        ("compound-interest-calculator.html", "Compound Interest Calculator", "Calculate exponential yields and contribution reinvestment."),
        ("inflation-calculator.html", "Inflation Calculator", "Forecast future living expense inflation over 30-year retirements."),
        ("401k-calculator.html", "401(k) Calculator", "Optimize tax-deferred workplace retirement savings and employer match."),
        ("social-security-calculator.html", "Social Security Calculator", "Estimate lifetime retirement benefits across claim ages 62 to 70.")
    ],
    "finance-calculator.html": [
        ("investment-calculator.html", "Investment Calculator", "Simulate long-term capital accumulation with periodic cash additions."),
        ("amortization-calculator.html", "Amortization Calculator", "Deconstruct installment payments into principal and interest fractions."),
        ("compound-interest-calculator.html", "Compound Interest Calculator", "Model exponential growth across daily, monthly, and annual compounding."),
        ("present-value-calculator.html", "Present Value Calculator", "Discount future expected cash flows back to present liquid dollars."),
        ("future-value-calculator.html", "Future Value Calculator", "Determine nominal portfolio terminal value at maturity.")
    ],
    "inflation-calculator.html": [
        ("investment-calculator.html", "Investment Calculator", "Determine required nominal returns to achieve positive real wealth growth."),
        ("salary-calculator.html", "Salary Calculator", "Evaluate real wage adjustments across inflation regimes."),
        ("retirement-calculator.html", "Retirement Calculator", "Protect retirement spending power against persistent CPI price rises."),
        ("compound-interest-calculator.html", "Compound Interest Calculator", "Model nominal growth against consumer price index erosion."),
        ("cost-of-living-calculator.html", "Cost of Living Calculator", "Compare purchasing power across metropolitan regions.")
    ],
    "income-tax-calculator.html": [
        ("salary-calculator.html", "Salary Calculator", "Convert annual gross salary to net bi-weekly and hourly take-home pay."),
        ("1099-vs-w2-calculator.html", "1099 vs W2 Calculator", "Compare independent contractor tax liabilities against W-2 employee benefits."),
        ("sales-tax-calculator.html", "Sales Tax Calculator", "Compute state and municipal sales tax on retail transactions."),
        ("capital-gains-tax-calculator.html", "Capital Gains Tax Calculator", "Calculate short-term vs long-term capital gains tax rates."),
        ("retirement-calculator.html", "Retirement Calculator", "Optimize tax-deferred vs Roth tax-exempt decumulation strategies.")
    ],
    # Fitness & Health
    "bmi-calculator.html": [
        ("body-fat-calculator.html", "Body Fat Calculator", "Measure adipose tissue percentage using US Navy circumference tape methods."),
        ("bmr-calculator.html", "BMR Calculator", "Compute basal metabolic rate using Mifflin-St Jeor and Katch-McArdle equations."),
        ("calorie-calculator.html", "Calorie Calculator", "Determine daily caloric requirements for weight maintenance, loss, or gain."),
        ("ideal-weight-calculator.html", "Ideal Weight Calculator", "Compare optimal weight ranges across Devine, Robinson, and Miller formulas."),
        ("macro-calculator.html", "Macro Calculator", "Split daily caloric intake into optimal protein, carbohydrate, and fat targets.")
    ],
    "bmr-calculator.html": [
        ("calorie-calculator.html", "Calorie Calculator", "Multiply BMR by physical activity multipliers to establish Total Daily Energy Expenditure."),
        ("body-fat-calculator.html", "Body Fat Calculator", "Estimate lean mass percentage for precise Katch-McArdle BMR calculations."),
        ("bmi-calculator.html", "BMI Calculator", "Screen general weight-to-height classification across WHO categories."),
        ("tdee-calculator.html", "TDEE Calculator", "Calculate daily maintenance calories based on occupational activity level."),
        ("macro-calculator.html", "Macro Calculator", "Determine macronutrient gram distributions for fat loss or muscle hypertrophy.")
    ],
    "body-fat-calculator.html": [
        ("bmi-calculator.html", "BMI Calculator", "Compare body fat classification against standard height-weight metrics."),
        ("bmr-calculator.html", "BMR Calculator", "Calculate resting metabolic rate from measured lean body tissue mass."),
        ("ideal-weight-calculator.html", "Ideal Weight Calculator", "Determine target weight corresponding to athletic body fat percentages."),
        ("calorie-calculator.html", "Calorie Calculator", "Design caloric deficit plans to preserve lean muscle while burning adipose tissue."),
        ("lean-body-mass-calculator.html", "Lean Body Mass Calculator", "Separate skeletal muscle, bone, and water mass from fat reserves.")
    ],
    "pregnancy-calculator.html": [
        ("pregnancy-conception-calculator.html", "Pregnancy Conception Calculator", "Pinpoint probable fertilization dates and the 6-day fertile intercourse window."),
        ("due-date-calculator.html", "Due Date Calculator", "Calculate official clinical EDD using Naegele's rule and ultrasound biometry."),
        ("ovulation-calculator.html", "Ovulation Calculator", "Track menstrual cycle phases, LH surges, and peak fertility windows."),
        ("pregnancy-weight-gain-calculator.html", "Pregnancy Weight Gain Calculator", "Track healthy gestational weight gain guidelines by trimester based on IOM standards."),
        ("bra-size-calculator.html", "Bra Size Calculator", "Measure accurate supportive maternity and nursing bra sizing.")
    ],
    "pregnancy-conception-calculator.html": [
        ("pregnancy-calculator.html", "Pregnancy Calculator", "Track gestational age milestones, trimester transitions, and fetal biometry."),
        ("due-date-calculator.html", "Due Date Calculator", "Estimate delivery dates based on last menstrual period or ultrasound measurements."),
        ("ovulation-calculator.html", "Ovulation Calculator", "Predict upcoming ovulation windows and optimal conception timing."),
        ("pregnancy-weight-gain-calculator.html", "Pregnancy Weight Gain Calculator", "Monitor recommended gestational weight curves."),
        ("date-calculator.html", "Date Calculator", "Calculate exact days and weeks between pregnancy milestones.")
    ],
    # Math & Geometry
    "triangle-calculator.html": [
        ("pythagorean-theorem-calculator.html", "Pythagorean Theorem Calculator", "Solve right triangle hypotenuses and missing legs using a^2 + b^2 = c^2."),
        ("area-calculator.html", "Area Calculator", "Compute two-dimensional surface areas for regular and irregular geometric shapes."),
        ("volume-calculator.html", "Volume Calculator", "Determine three-dimensional capacities for prisms, pyramids, cones, and cylinders."),
        ("square-footage-calculator.html", "Square Footage Calculator", "Calculate residential and commercial floor plans with waste allowances."),
        ("scientific-calculator.html", "Scientific Calculator", "Perform advanced trigonometric, logarithmic, and exponential operations.")
    ],
    "percentage-calculator.html": [
        ("fraction-calculator.html", "Fraction Calculator", "Add, subtract, multiply, and divide proper and improper fractions."),
        ("sales-tax-calculator.html", "Sales Tax Calculator", "Calculate retail sales tax additions and reverse pre-tax sub-totals."),
        ("discount-calculator.html", "Discount Calculator", "Determine percentage discount savings and final retail purchase prices."),
        ("compound-interest-calculator.html", "Compound Interest Calculator", "Apply recurring percentage interest yields to investment balances."),
        ("markup-calculator.html", "Markup Calculator", "Calculate gross profit margins and retail markups on wholesale merchandise.")
    ],
    "standard-deviation-calculator.html": [
        ("mean-median-mode-calculator.html", "Mean, Median, Mode Calculator", "Evaluate measures of central tendency across numerical datasets."),
        ("z-score-calculator.html", "Z-Score Calculator", "Compute standardized normal scores and Gaussian probability percentiles."),
        ("confidence-interval-calculator.html", "Confidence Interval Calculator", "Determine inferential margin of error and population parameter intervals."),
        ("probability-calculator.html", "Probability Calculator", "Calculate independent, dependent, and mutually exclusive event probabilities."),
        ("sample-size-calculator.html", "Sample Size Calculator", "Determine statistical sample size required for survey confidence levels.")
    ],
    "date-calculator.html": [
        ("day-counter.html", "Day Counter", "Count calendar days and business days between two dates with holiday exclusion."),
        ("time-duration-calculator.html", "Time Duration Calculator", "Compute elapsed hours, minutes, and seconds between timestamps."),
        ("day-of-the-week-calculator.html", "Day of the Week Calculator", "Determine day of the week using Zeller's congruence and Conway's doomsday rule."),
        ("hours-calculator.html", "Hours Calculator", "Calculate shift work durations and decimal hours for payroll accounting."),
        ("time-card-calculator.html", "Time Card Calculator", "Audit weekly timesheets with unpaid lunch deductions and overtime rates.")
    ]
}

def generate_interlinking_section(filename):
    items = RELATED_MAP.get(filename, [])
    if not items:
        # Fallback to general category tools
        if "mortgage" in filename or "loan" in filename:
            items = RELATED_MAP["mortgage-calculator.html"][:4]
        elif "tax" in filename or "salary" in filename:
            items = RELATED_MAP["income-tax-calculator.html"][:4]
        elif "weight" in filename or "calorie" in filename or "fitness" in filename:
            items = RELATED_MAP["bmi-calculator.html"][:4]
        elif "triangle" in filename or "circle" in filename or "area" in filename:
            items = RELATED_MAP["triangle-calculator.html"][:4]
        else:
            items = RELATED_MAP["date-calculator.html"][:4]

    cards_html = ""
    for target_file, title, desc in items:
        cards_html += f"""
        <a href="{target_file}" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
            <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                <span>{title}</span>
                <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
            </div>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">{desc}</p>
        </a>"""

    section = f"""
    <section class="my-10 pt-8 border-t border-slate-200 dark:border-slate-800 not-prose">
        <div class="flex items-center space-x-2 mb-4">
            <div class="w-2 h-6 bg-emerald-500 rounded-full"></div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white">Related Calculators &amp; Contextual Financial Tools</h3>
        </div>
        <p class="text-sm text-slate-600 dark:text-slate-400 mb-6">
            Compare scenarios, verify calculations, and explore connected financial models across our specialized calculation network:
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {cards_html}
        </div>
    </section>
    """
    return section

def inject_interlinking(filename):
    primary_path = os.path.join(calc_dir, filename)
    if not os.path.exists(primary_path):
        return

    with open(primary_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Don't inject if already has Related Calculators section
    if "Related Calculators &amp; Contextual" in content or "Related Calculators & Contextual" in content:
        return

    section_html = generate_interlinking_section(filename)

    # Inject right before </article> if present, or before </footer>
    if "</article>" in content:
        content = content.replace("</article>", f"{section_html}\n</article>", 1)
    elif "</main>" in content:
        content = content.replace("</main>", f"{section_html}\n</main>", 1)

    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    if os.path.exists(desktop_dir):
        dfp = os.path.join(desktop_dir, filename)
        with open(dfp, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"Injected rich interlinking network into {filename}")

def main():
    print("Injecting Calculator.net architecture interlinking across all calculators...")
    count = 0
    for f in sorted(os.listdir(calc_dir)):
        if f.endswith(".html"):
            inject_interlinking(f)
            count += 1
    print(f"Finished processing {count} calculators with internal backlink clusters!")

if __name__ == "__main__":
    main()

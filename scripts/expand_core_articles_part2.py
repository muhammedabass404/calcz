# -*- coding: utf-8 -*-
"""
Expand Core Calculator Articles Part 2:
- loan-calculator.html
- amortization-calculator.html
- percentage-calculator.html
- calorie-calculator.html
- due-date-calculator.html
- salary-calculator.html
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
    print(f"Successfully upgraded {filename} with {len(words)} words & contextual backlinks!")


# 1. loan-calculator.html
loan_article = """<article class="prose prose-slate dark:prose-invert max-w-none mt-12 bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">
    <h2 class="text-3xl font-extrabold border-b pb-4 mb-8 border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white">Comprehensive Loan Guide: Borrowing Costs, Fixed Monthly Payments, APR, and Debt Structuring</h2>
    
    <p class="text-lg leading-relaxed mb-6">
        A loan is a contractual financial agreement where a lender provides capital to a borrower in exchange for future repayment of the principal balance plus accrued interest. In modern consumer credit and corporate finance, loans fund residential real estate, higher education, capital equipment acquisitions, small business expansions, and debt consolidation. However, borrowers frequently focus solely on the monthly payment figure advertised by lenders while overlooking origination fees, interest rate capitalization, compounding frequencies, and total financing interest charges.
    </p>
    <p class="leading-relaxed mb-6">
        To properly evaluate any debt obligation, you must understand the mathematical mechanics of loan amortization schedules. For real estate mortgages, use our specialized <a href="mortgage-calculator.html" class="text-emerald-600 dark:text-emerald-400 font-semibold underline hover:text-emerald-500">Mortgage Calculator</a>; for motor vehicles, explore our <a href="auto-loan-calculator.html" class="text-emerald-600 dark:text-emerald-400 font-semibold underline hover:text-emerald-500">Auto Loan Calculator</a>; and to examine the month-by-month principal reduction table, review our <a href="amortization-calculator.html" class="text-emerald-600 dark:text-emerald-400 font-semibold underline hover:text-emerald-500">Amortization Calculator</a>.
    </p>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">Secured Loans vs. Unsecured Loans</h3>
    <p class="mb-4">
        Financial institutions categorize credit risk primarily by the presence or absence of pledged collateral:
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6 not-prose">
        <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">Secured Borrowing (Collateralized Debt)</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed mb-3">
                Backed by a specific tangible asset pledged to the lender (e.g., residential mortgages backed by real property, or auto loans backed by the vehicle title). If the borrower defaults, the creditor holds legal authority to foreclose or repossess the pledged collateral.
            </p>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-400">Lower Interest Rates (Prime Pricing)</span>
        </div>
        <div class="p-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">Unsecured Borrowing (Signature Debt)</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed mb-3">
                Issued solely on the basis of the borrower's credit score, verifiable income, and legal promise to repay (e.g., personal installment loans, credit cards, student debt). In the event of default, the lender must pursue formal civil lawsuits to garnish wages.
            </p>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-amber-100 text-amber-800 dark:bg-amber-950/60 dark:text-amber-400">Higher Interest Rates (Risk Premium Added)</span>
        </div>
    </div>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">The Fixed Monthly Installment Equation</h3>
    <p class="mb-4">
        Standard amortizing consumer credit uses the annuity installment formulation to ensure equal monthly payments throughout the term:
    </p>
    <div class="my-6 p-6 rounded-2xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-lg overflow-x-auto text-slate-900 dark:text-emerald-300">
        \[ M = P \cdot \frac{r(1 + r)^n}{(1 + r)^n - 1} \]
    </div>
    <p class="mb-4">
        Where \(P\) is the borrowed principal balance, \(r\) is the monthly interest rate (annual APR divided by 12), and \(n\) is the total count of monthly payment periods.
    </p>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">Step-by-Step Worked Numerical Example: Personal Consolidation Loan</h3>
    <p class="mb-4">
        Suppose an individual consolidates $20,000 of high-interest revolving credit card balances into a fixed-rate 36-month (3-year) personal loan at an interest rate of 8.5% APR:
    </p>
    <div class="space-y-4 mb-6 bg-slate-50 dark:bg-slate-900/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-800">
        <p><strong>Step 1: Determine Monthly Rate and Compounding Term</strong><br>
        Monthly interest rate: \(r = 0.085 / 12 = 0.00708333\).<br>
        Compounding duration: \(n = 36\) months.</p>
        <p><strong>Step 2: Solve the Amortization Factor</strong><br>
        \((1 + 0.00708333)^{36} = (1.00708333)^{36} = 1.288928\).<br>
        Numerator: \(0.00708333 \times 1.288928 = 0.0091300\).<br>
        Denominator: \(1.288928 - 1 = 0.288928\).<br>
        Factor: \(0.0091300 / 0.288928 = 0.031600\).</p>
        <p><strong>Step 3: Calculate Monthly Installment</strong><br>
        \(M = \$20,000 \times 0.031600 = \mathbf{\$631.32 \text{ per month}}\).</p>
        <p><strong>Step 4: Compute Total Cost and Interest Charges</strong><br>
        Total cash paid over 3 years: \(\$631.32 \times 36 = \mathbf{\$22,727.52}\).<br>
        Total interest paid: \(\$22,727.52 - \$20,000.00 = \mathbf{\$2,727.52}\).<br>
        Compared to leaving the debt on credit cards at 24% APR (where interest would exceed $8,200), the personal loan saves over <strong>$5,400 in net interest</strong>.</p>
    </div>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">Debt-to-Income (DTI) Ratios and Underwriting Benchmarks</h3>
    <p class="mb-4">
        Underwriting models evaluate borrower capacity using Debt-to-Income (DTI) metrics before approving financing:
    </p>
    <div class="overflow-x-auto my-6">
        <table class="w-full text-left border-collapse border border-slate-200 dark:border-slate-800 text-sm">
            <thead class="bg-slate-100 dark:bg-slate-800/80">
                <tr>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">DTI Bracket</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Financial Interpretation</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Lender Approval Probability</th>
                    <th class="p-3 border border-slate-200 dark:border-slate-700">Interest Pricing Tier</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold text-emerald-600 dark:text-emerald-400">Below 25%</td>
                    <td class="p-3">Superior financial liquidity</td>
                    <td class="p-3">Instant Automated Approval</td>
                    <td class="p-3">Prime Tier 1 (Lowest available rates)</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold">25% – 35%</td>
                    <td class="p-3">Healthy and sustainable debt burden</td>
                    <td class="p-3">Standard Approval</td>
                    <td class="p-3">Competitive Market Rate</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800">
                    <td class="p-3 font-semibold text-amber-600 dark:text-amber-400">36% – 43%</td>
                    <td class="p-3">Moderate financial strain; CFPB qualified mortgage threshold</td>
                    <td class="p-3">Conditional Approval (Manual Underwriting)</td>
                    <td class="p-3">Moderate Rate Premiums</td>
                </tr>
                <tr class="border-b border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-slate-900/30">
                    <td class="p-3 font-semibold text-rose-600 dark:text-rose-400">Above 43%</td>
                    <td class="p-3">Severe debt service risk</td>
                    <td class="p-3">Frequent Rejection or Co-Signer Required</td>
                    <td class="p-3">Subprime Pricing</td>
                </tr>
            </tbody>
        </table>
    </div>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">Frequently Asked Questions</h3>
    <div class="space-y-4 my-6 not-prose">
        <div class="p-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What is the difference between nominal interest rate and APR on a personal loan?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">The nominal interest rate is the percentage applied to your loan balance to compute monthly interest. The Annual Percentage Rate (APR) incorporates all mandatory lender fees, including upfront origination fees (typically 1% to 8% deducted from disbursed proceeds). APR reflects your true annual borrowing cost.</p>
        </div>
        <div class="p-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">Can paying extra principal shorten my loan term?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Yes. Making additional principal-only payments directly reduces the remaining loan balance, cutting down all future monthly interest calculations. On a 5-year loan, an extra 10% monthly payment can eliminate 6 to 9 months of payments and save hundreds of dollars in interest.</p>
        </div>
        <div class="p-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What happens if a borrower defaults on an unsecured loan?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Defaulting on an unsecured personal loan triggers late fees, collections agency action, and credit bureau reporting that drops FICO scores by 100+ points for up to 7 years. Lenders may obtain a court judgment to garnish wages or levy non-exempt bank accounts.</p>
        </div>
    </div>

    <section class="my-10 pt-8 border-t border-slate-200 dark:border-slate-800 not-prose">
        <div class="flex items-center space-x-2 mb-4">
            <div class="w-2 h-6 bg-emerald-500 rounded-full"></div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white">Related Lending &amp; Debt Calculators</h3>
        </div>
        <p class="text-sm text-slate-600 dark:text-slate-400 mb-6">
            Compare borrowing options, view amortization schedules, and evaluate compounding interest charges across our specialized tools:
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <a href="mortgage-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Mortgage Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Calculate residential home mortgage payments with property taxes, home insurance, and PMI.</p>
            </a>
            <a href="auto-loan-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Auto Loan Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Model car financing payments, trade-in equity, sales taxes, and vehicle depreciation curves.</p>
            </a>
            <a href="amortization-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Amortization Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Inspect month-by-month principal reduction, balance decay, and cumulative interest charges.</p>
            </a>
            <a href="interest-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Interest Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Compare simple linear interest against exponential compounding schedules.</p>
            </a>
            <a href="compound-interest-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Compound Interest Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Simulate investment accumulation and wealth compounding across multi-year horizons.</p>
            </a>
            <a href="investment-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Investment Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Forecast portfolio growth, asset class yields, and recurring contribution cadences.</p>
            </a>
        </div>
    </section>
</article>"""

# 2. calorie-calculator.html
calorie_article = """<article class="prose prose-slate dark:prose-invert max-w-none mt-12 bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300">
    <h2 class="text-3xl font-extrabold border-b pb-4 mb-8 border-slate-200 dark:border-slate-800 text-slate-900 dark:text-white">Daily Calorie Calculator Guide: Energy Balance, TDEE, Weight Loss Deficits, and Macronutrients</h2>
    
    <p class="text-lg leading-relaxed mb-6">
        Human body weight management operates on the fundamental physical laws of thermodynamics: energy can neither be created nor destroyed, only transformed from one form to another. In human physiology, calories represent units of heat energy derived from food nutrients (carbohydrates, proteins, fats, and alcohol) that fuel physiological metabolic processes and physical movement. When daily caloric intake matches Total Daily Energy Expenditure (TDEE), body mass remains constant; consuming fewer calories induces fat loss (energy deficit), while consuming surplus calories drives weight gain.
    </p>
    <p class="leading-relaxed mb-6">
        Accurately determining your daily caloric target requires evaluating your Basal Metabolic Rate (BMR) and physical activity levels. You can check your general weight category with our <a href="bmi-calculator.html" class="text-emerald-600 dark:text-emerald-400 font-semibold underline hover:text-emerald-500">BMI Calculator</a>, inspect resting energy burn on our <a href="bmr-calculator.html" class="text-emerald-600 dark:text-emerald-400 font-semibold underline hover:text-emerald-500">BMR Calculator</a>, measure adipose tissue via our <a href="body-fat-calculator.html" class="text-emerald-600 dark:text-emerald-400 font-semibold underline hover:text-emerald-500">Body Fat Calculator</a>, or partition daily calories using our <a href="macro-calculator.html" class="text-emerald-600 dark:text-emerald-400 font-semibold underline hover:text-emerald-500">Macro Calculator</a>.
    </p>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">The 4 Components of Total Daily Energy Expenditure (TDEE)</h3>
    <p class="mb-4">
        Your daily caloric expenditure is the cumulative sum of four distinct physiological energy drains:
    </p>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-6 not-prose">
        <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 class="font-bold text-slate-900 dark:text-white mb-1">1. Basal Metabolic Rate (BMR) ~ 60% to 75% of TDEE</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400">The baseline energy expended at complete rest in a thermo-neutral environment to sustain autonomic life functions (heart contraction, lung respiration, kidney filtration, cellular ion exchange, and brain activity).</p>
        </div>
        <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 class="font-bold text-slate-900 dark:text-white mb-1">2. Non-Exercise Activity Thermogenesis (NEAT) ~ 15% to 20%</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400">Energy consumed by daily physical movements that are not deliberate athletic exercise: walking, standing, typing, household chores, fidgeting, and maintaining posture.</p>
        </div>
        <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 class="font-bold text-slate-900 dark:text-white mb-1">3. Thermic Effect of Food (TEF) ~ 8% to 10% of TDEE</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400">The metabolic energy required to digest, absorb, and metabolize consumed nutrients. Protein has the highest TEF (20%-30%), carbohydrates (5%-10%), and dietary fats (0%-3%).</p>
        </div>
        <div class="p-5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700">
            <h4 class="font-bold text-slate-900 dark:text-white mb-1">4. Exercise Activity Thermogenesis (EAT) ~ 5% to 15%</h4>
            <p class="text-sm text-slate-600 dark:text-slate-400">Calories burned through planned physical workouts: resistance training, running, swimming, cycling, and competitive sports.</p>
        </div>
    </div>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">Calculating BMR: Mifflin-St Jeor Equation</h3>
    <p class="mb-4">
        Validated as the most accurate predictive formula by the American Dietetic Association (ADA), the Mifflin-St Jeor equation calculates resting baseline calories based on gender, mass, stature, and chronological age:
    </p>
    <div class="space-y-3 mb-6 p-6 rounded-2xl bg-slate-100 dark:bg-slate-800/60 font-mono text-center text-base overflow-x-auto text-slate-900 dark:text-emerald-300">
        <p><strong>Men:</strong> \[ \text{BMR} = 10 \times \text{Weight (kg)} + 6.25 \times \text{Height (cm)} - 5 \times \text{Age (years)} + 5 \]</p>
        <p><strong>Women:</strong> \[ \text{BMR} = 10 \times \text{Weight (kg)} + 6.25 \times \text{Height (cm)} - 5 \times \text{Age (years)} - 161 \]</p>
    </div>
    <p class="mb-4">
        TDEE is then calculated by multiplying BMR by the corresponding PAL (Physical Activity Level) multiplier:
    </p>
    <ul class="list-disc pl-6 space-y-2 mb-6">
        <li><strong>Sedentary (desk job, minimal movement):</strong> BMR &times; 1.200</li>
        <li><strong>Lightly Active (light exercise 1 to 3 days/week):</strong> BMR &times; 1.375</li>
        <li><strong>Moderately Active (moderate training 3 to 5 days/week):</strong> BMR &times; 1.550</li>
        <li><strong>Very Active (hard training 6 to 7 days/week):</strong> BMR &times; 1.725</li>
        <li><strong>Extra Active (physical job &amp; double daily training):</strong> BMR &times; 1.900</li>
    </ul>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">Step-by-Step Worked Numerical Example: Designing a 1 lb/Week Fat Loss Deficit</h3>
    <p class="mb-4">
        Consider a 32-year-old male standing 5 feet 11 inches (180.34 cm), weighing 195 lbs (88.45 kg), working a desk job with moderate gym training 4 days per week (Moderately Active multiplier = 1.55).
    </p>
    <div class="space-y-4 mb-6 bg-slate-50 dark:bg-slate-900/50 p-6 rounded-2xl border border-slate-200 dark:border-slate-800">
        <p><strong>Step 1: Compute Basal Metabolic Rate (BMR)</strong><br>
        \(\text{BMR} = (10 \times 88.45) + (6.25 \times 180.34) - (5 \times 32) + 5\)<br>
        \(\text{BMR} = 884.5 + 1,127.1 - 160 + 5 = \mathbf{1,856.6 \text{ kcal/day}}\).</p>
        <p><strong>Step 2: Calculate Maintenance TDEE</strong><br>
        \(\text{TDEE} = 1,856.6 \times 1.55 = \mathbf{2,877.7 \text{ kcal/day}}\). This is the exact caloric intake required to maintain 195 lbs.</p>
        <p><strong>Step 3: Establish the 3,500 kcal Rule for 1 lb Fat Loss</strong><br>
        One pound of human adipose tissue stores approximately 3,500 kcal of chemical energy. To lose 1.0 lb of body fat per week, create a daily deficit of \(3,500 / 7 = 500 \text{ kcal/day}\):<br>
        Target Intake: \(2,878 - 500 = \mathbf{2,378 \text{ kcal/day}}\).</p>
        <p><strong>Step 4: Macronutrient Allocation (via Macro Calculator)</strong><br>
        - <strong>Protein (1.0g per lb of body weight):</strong> 195g &times; 4 kcal/g = 780 kcal (32.8%).<br>
        - <strong>Fat (0.35g per lb of body weight):</strong> 68g &times; 9 kcal/g = 612 kcal (25.7%).<br>
        - <strong>Carbohydrates (remaining energy balance):</strong> (2,378 - 780 - 612) / 4 kcal/g = 986 / 4 = <strong>246.5g</strong> (41.5%).</p>
    </div>

    <h3 class="text-2xl font-bold mt-10 mb-4 text-slate-800 dark:text-slate-100">Frequently Asked Questions</h3>
    <div class="space-y-4 my-6 not-prose">
        <div class="p-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">What is metabolic adaptation during prolonged weight loss diets?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">As body mass drops, your BMR decreases because a smaller body requires fewer calories to maintain. Furthermore, subconscious NEAT movement declines and thyroid hormone output (T3) slows. This natural biological response means caloric deficits must be periodically recalculated every 10 to 15 lbs of weight loss.</p>
        </div>
        <div class="p-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">Can a caloric deficit cause loss of muscle tissue?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">Yes, if the deficit is excessively steep (greater than 25% of TDEE) or if protein intake is insufficient. To preserve lean muscle mass during a fat-loss phase, maintain a moderate 15% to 20% deficit, consume 0.8g to 1.2g of protein per pound of body weight, and continue progressive resistance training.</p>
        </div>
        <div class="p-6 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900">
            <h4 class="font-bold text-slate-900 dark:text-white mb-2">Is the 3,500 kcal per pound rule completely accurate?</h4>
            <p class="text-sm leading-relaxed text-slate-600 dark:text-slate-400">The Max Wishnofsky 3,500 kcal rule provides a solid clinical baseline. However, as demonstrated by the National Institutes of Health (NIH) Body Weight Planner, dynamic metabolic slowing makes long-term weight loss slightly non-linear over months.</p>
        </div>
    </div>

    <section class="my-10 pt-8 border-t border-slate-200 dark:border-slate-800 not-prose">
        <div class="flex items-center space-x-2 mb-4">
            <div class="w-2 h-6 bg-emerald-500 rounded-full"></div>
            <h3 class="text-xl font-bold text-slate-900 dark:text-white">Related Nutrition &amp; Body Composition Calculators</h3>
        </div>
        <p class="text-sm text-slate-600 dark:text-slate-400 mb-6">
            Fine-tune your nutritional macros, calculate basal metabolic requirements, and monitor body composition goals:
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <a href="bmr-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>BMR Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Calculate resting basal metabolic energy burn using validated clinical formulas.</p>
            </a>
            <a href="macro-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Macro Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Distribute daily calories into protein, carbohydrate, and fat gram targets.</p>
            </a>
            <a href="body-fat-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Body Fat Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Estimate adipose tissue percentage using US Navy body circumference methods.</p>
            </a>
            <a href="bmi-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>BMI Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Screen adult body weight categories against international WHO health benchmarks.</p>
            </a>
            <a href="ideal-weight-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Ideal Weight Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Compare healthy target body weights across Devine, Robinson, and Miller formulas.</p>
            </a>
            <a href="pace-calculator.html" class="block p-4 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900/60 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-md transition-all group">
                <div class="font-bold text-slate-900 dark:text-white group-hover:text-emerald-600 dark:group-hover:text-emerald-400 transition-colors flex items-center justify-between">
                    <span>Pace Calculator</span>
                    <svg class="w-4 h-4 ml-1 opacity-60 group-hover:opacity-100 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                </div>
                <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 leading-relaxed">Compute running pace per mile or kilometer to optimize aerobic calorie burn.</p>
            </a>
        </div>
    </section>
</article>"""

def main():
    print("Executing Core Articles Expansion Part 2...")
    update_article("loan-calculator.html", loan_article)
    update_article("calorie-calculator.html", calorie_article)
    print("Part 2 complete!")

if __name__ == "__main__":
    main()

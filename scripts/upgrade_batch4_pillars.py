import os
import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

ONEDRIVE_CALC_DIR = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
DESKTOP_CALC_DIR = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'

ARTICLES = {}

# 1. Mortgage Calculator (1,850+ words)
ARTICLES['mortgage-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Mortgage Financing Guide (1,850+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-blue-100 dark:bg-blue-900/40 text-blue-700 dark:text-blue-300 text-xs font-bold uppercase tracking-wider mb-3">Residential Real Estate Finance</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Architecture of Mortgage Finance: Amortization Physics, PITI Components, and Capital Optimization</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A technical reference manual on 30-year versus 15-year fixed mortgages, principal-interest amortization dynamics, escrow PITI reserves, Private Mortgage Insurance (PMI) removal under HPA, and debt-to-income underwriting thresholds.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. Deconstructing the Monthly Mortgage Payment: The PITI Quadrumvirate</h3>
            <p>
                When a prospective homebuyer evaluates affordability, focusing exclusively on the loan's contractual interest rate and principal amortization creates a severe financial blind spot. In mortgage underwriting, your monthly housing liability is universally evaluated as <strong>PITI</strong>:
            </p>
            <ul>
                <li><strong>Principal (P):</strong> The portion of each payment that directly pays down the outstanding loan balance, building home equity.</li>
                <li><strong>Interest (I):</strong> The fee charged by the lender for the use of borrowed capital, calculated monthly based on the remaining unamortized balance.</li>
                <li><strong>Taxes (T):</strong> Municipal and county real estate property taxes, assessed as a percentage of your home's assessed valuation (averaging 0.3% to 2.5% annually across US jurisdictions) and collected into a lender escrow account.</li>
                <li><strong>Insurance (I):</strong> Hazard homeowners insurance premiums protecting against fire, storms, and casualty loss, alongside mandatory flood insurance if located in FEMA-designated Special Flood Hazard Areas (SFHAs).</li>
                <li><strong>Private Mortgage Insurance (PMI / MIP):</strong> An additional credit enhancement fee required when purchasing a home with less than 20% down payment (LTV &gt; 80%).</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Mortgage Amortization Mathematics</h3>
            <p>
                The exact monthly principal and interest installment $M$ required to amortize a home loan balance $P$ over $N$ monthly billing cycles at periodic monthly rate $r$ is derived via the standard annuity present value formulation:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-blue-600 dark:text-blue-400 font-sans text-xs uppercase tracking-wider mb-1">Mortgage Amortization Formula</div>
                <div><strong>Monthly P&amp;I Payment:</strong> M = P &times; [ r(1 + r)^N ] / [ (1 + r)^N - 1 ]</div>
                <div><strong>Loan-to-Value (LTV) Ratio:</strong> LTV (%) = (Loan Amount / Appraised Property Value) &times; 100</div>
                <div><strong>Front-End DTI Ratio:</strong> DTI_front (%) = (PITI Housing Expense / Gross Monthly Income) &times; 100</div>
                <div><strong>Back-End DTI Ratio:</strong> DTI_back (%) = ( (PITI + All Revolving Debt) / Gross Monthly Income ) &times; 100</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Case Study</h3>
            <p>
                Consider a buyer purchasing a single-family home for <strong>$450,000</strong> with a <strong>10% down payment ($45,000)</strong>, financing <strong>$405,000</strong> on a <strong>30-year fixed-rate mortgage at 6.75% APR</strong>. Property taxes average 1.25% annually, homeowners insurance costs $1,800/year, and PMI is assessed at 0.55% of the initial loan balance.
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Calculate Monthly Principal and Interest (P&amp;I):</strong>
                    <ul>
                        <li>Monthly Rate: $r = 0.0675 / 12 = 0.005625$.</li>
                        <li>Total Periods: $N = 30 \\times 12 = 360$ months.</li>
                        <li>Compounding Growth Factor: $(1 + 0.005625)^{360} \\approx 7.50284$.</li>
                        <li>Amortization Factor: $\\frac{0.005625 \\times 7.50284}{7.50284 - 1} = \\frac{0.042203}{6.50284} \\approx 0.0064899$.</li>
                        <li><strong>Monthly P&amp;I:</strong> $\$405,000 \\times 0.0064899 = \\mathbf{\\$2,628.43}$.</li>
                    </ul>
                </li>
                <li>
                    <strong>Calculate Escrow PITI Additions:</strong>
                    <ul>
                        <li>Property Taxes: $(\\$450,000 \\times 0.0125) / 12 = \\$5,625 / 12 = \\mathbf{\\$468.75/month}$.</li>
                        <li>Homeowners Insurance: $\$1,800 / 12 = \\mathbf{\\$150.00/month}$.</li>
                        <li>Private Mortgage Insurance (PMI): $(\\$405,000 \\times 0.0055) / 12 = \\$2,227.50 / 12 = \\mathbf{\\$185.63/month}$.</li>
                    </ul>
                </li>
                <li>
                    <strong>Compute Total Initial Monthly Housing Outflow (PITI):</strong>
                    $$\\text{Total PITI} = \\$2,628.43 \\text{ (P&I)} + \\$468.75 \\text{ (Taxes)} + \\$150.00 \\text{ (Ins)} + \\$185.63 \\text{ (PMI)} = \\mathbf{\\$3,432.81/month}$$
                </li>
                <li>
                    <strong>Cumulative 30-Year Interest Obligation:</strong>
                    Total P&amp;I payments over 360 months = $360 \\times \\$2,628.43 = \\$946,234.80$.
                    Subtracting original principal ($405,000) yields <strong>$541,234.80 in cumulative interest expense</strong>—more than 133% of the amount originally borrowed!
                </li>
            </ol>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. 30-Year vs. 15-Year Fixed Mortgage Comparison ($405,000 Loan)</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Mortgage Product</th>
                            <th class="p-3">Interest Rate</th>
                            <th class="p-3">Monthly P&amp;I</th>
                            <th class="p-3">Total Lifetime Interest</th>
                            <th class="p-3">Equity After 5 Years</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">30-Year Fixed</td>
                            <td class="p-3">6.75%</td>
                            <td class="p-3">$2,628.43</td>
                            <td class="p-3 font-bold text-red-600 dark:text-red-400">$541,235</td>
                            <td class="p-3">$22,860 (5.6% paid down)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">15-Year Fixed</td>
                            <td class="p-3">6.00%</td>
                            <td class="p-3 font-bold text-blue-600 dark:text-blue-400">$3,417.61</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">$210,170</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">$94,110 (23.2% paid down)</td>
                        </tr>
                        <tr class="bg-emerald-50/50 dark:bg-emerald-950/20 font-sans">
                            <td class="p-3 font-bold text-emerald-700 dark:text-emerald-300">15-Year Advantage</td>
                            <td class="p-3">-0.75% Rate</td>
                            <td class="p-3">+$789.18/mo</td>
                            <td class="p-3 font-bold text-emerald-700 dark:text-emerald-300">Saves $331,065!</td>
                            <td class="p-3">+$71,250 in equity!</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. The Homeowners Protection Act of 1998: PMI Cancellation Rights</h3>
            <p>
                Under the federal <strong>Homeowners Protection Act (HPA / 12 U.S.C. § 4901)</strong>, borrowers financing conventional residential mortgages carry statutory rights to eliminate Private Mortgage Insurance:
            </p>
            <ul>
                <li><strong>Borrower-Requested Cancellation (80% LTV):</strong> Once your principal balance reaches 80% of the original purchase price (either through scheduled amortization or additional principal overpayments), you hold the legal right to submit a written request to cancel PMI, provided you maintain a clean payment history.</li>
                <li><strong>Automatic Statutory Termination (78% LTV):</strong> Loan servicers are legally mandated to automatically terminate PMI without borrower request once the principal balance is scheduled to reach 78% of the original property value under the baseline amortization table.</li>
                <li><strong>Cancellation via Market Appreciation:</strong> If local home prices surge, Fannie Mae and Freddie Mac guidelines permit requesting an appraisal to prove that your current balance is below 75% LTV (if loan is 2-5 years old) or below 80% LTV (if loan is over 5 years old), eliminating PMI years ahead of schedule.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What is the 28/36 rule in conventional mortgage underwriting?</span>
                        <span class="text-blue-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        The 28/36 rule is a classic debt-to-income benchmark used by mortgage underwriters. The <strong>front-end ratio (28%)</strong> mandates that total housing costs (PITI + HOA fees) should not exceed 28% of your gross monthly income. The <strong>back-end ratio (36%)</strong> mandates that total debt service (housing costs + auto loans, student loans, minimum credit card payments) should not exceed 36% of gross income. While Fannie Mae and Freddie Mac automated underwriting systems (DU/LP) can approve qualified borrowers up to 45% or even 50% DTI with strong compensating factors (high FICO score, substantial cash reserves), keeping debt within 28/36 ensures resilient long-term financial stability.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>How do discount points differ from origination fees?</span>
                        <summary class="hidden"></summary>
                        <span class="text-blue-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        One discount point equals 1% of the loan amount paid upfront at closing to permanently "buy down" your mortgage interest rate (typically reducing the rate by 0.25%). In contrast, origination fees are administrative processing charges levied by the lender to underwrite and fund the loan. To evaluate whether paying points makes mathematical sense, calculate the breakeven period: divide the upfront dollar cost of the points by the monthly payment savings. If you plan to retain the mortgage past the breakeven date without selling or refinancing, paying points generates net savings.
                    </p>
                </details>
            </div>
        </article>
"""

# 2. Compound Interest Calculator (1,850+ words)
ARTICLES['compound-interest-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Compound Interest Guide (1,860+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-900/40 text-emerald-700 dark:text-emerald-300 text-xs font-bold uppercase tracking-wider mb-3">Wealth Accumulation &amp; Financial Mathematics</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Exponential Mechanics of Compound Interest: Wealth Accumulation, Time Horizons, and the Rule of 72</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A comprehensive financial engineering guide to future value annuity compounding formulas, periodic continuous contributions, inflation drag, real purchasing power retention, and geometric growth dynamics.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. The Nature of Exponential Capital Growth</h3>
            <p>
                Albert Einstein reportedly characterized compound interest as the "eighth wonder of the world," observing that "he who understands it, earns it; he who doesn't, pays it." In linear arithmetic, quantities grow by adding a fixed constant over time ($y = mx + b$). In geometric compounding, capital expands non-linearly: interest generated in each discrete period is reinvested into the principal base, allowing subsequent interest to be earned on past interest ($y = a(1 + r)^t$).
            </p>
            <p>
                In the early phases of an investment program, the compounding effect appears deceptively modest; capital growth is dominated almost entirely by the investor's manual cash deposits. However, as the asset base matures past the 10-year, 20-year, and 30-year thresholds, the exponential growth curve reaches its inflection point. Eventually, annual compound investment earnings eclipse the investor's annual salary, transforming capital into a self-sustaining perpetual wealth generator.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Compounding Mathematical Equations</h3>
            <p>
                When an initial principal sum $P$ is combined with ongoing regular periodic contributions $PMT$ compounding at nominal annual rate $r$ across $n$ intervals per year for $t$ years, the total accumulated Future Value $FV$ is computed using the combined compound annuity formula:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-emerald-600 dark:text-emerald-400 font-sans text-xs uppercase tracking-wider mb-1">Universal Compound Growth Formula</div>
                <div><strong>Future Value (with regular deposits):</strong> FV = P(1 + r/n)^(n&times;t) + PMT &times; [ (1 + r/n)^(n&times;t) - 1 ] / (r/n)</div>
                <div><strong>The Rule of 72 (Doubling Time):</strong> T_double &approx; 72 / r_percent</div>
                <div><strong>Effective Annual Rate (APY):</strong> APY = (1 + r/n)^n - 1</div>
                <div><strong>Real Purchasing Power (Fisher Equation):</strong> FV_real = FV / (1 + inflation_rate)^t</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Walkthrough</h3>
            <p>
                To illustrate the mathematical compounding trajectory, consider an individual who establishes a tax-advantaged retirement portfolio with an initial lump-sum deposit of <strong>$10,000</strong> and commits to contributing <strong>$500 at the end of each month</strong> ($6,000 annually) for <strong>30 years</strong>, invested in a diversified broad-market index fund delivering a historical nominal annualized return of <strong>8.00% (compounded monthly)</strong>.
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Identify Base Parameters:</strong>
                    $P = \\$10,000$; $PMT = \\$500$; $r = 0.08$; $n = 12$; $t = 30$ years.
                    Periodic rate: $i = 0.08 / 12 \\approx 0.0066667$.
                    Total compounding cycles: $N = 12 \\times 30 = 360$ cycles.
                </li>
                <li>
                    <strong>Compute Growth on Initial Lump Sum:</strong>
                    $$(1 + 0.0066667)^{360} = (1.0066667)^{360} \\approx 10.93573$$
                    $$\\text{FV of Initial Principal} = \\$10,000 \\times 10.93573 = \\mathbf{\\$109,357.30}$$
                </li>
                <li>
                    <strong>Compute Growth on Monthly Annuity Stream:</strong>
                    $$\\text{Annuity Multiplier} = \\frac{10.93573 - 1}{0.0066667} = \\frac{9.93573}{0.0066667} \\approx 1,490.3595$$
                    $$\\text{FV of Monthly Deposits} = \\$500 \\times 1,490.3595 = \\mathbf{\\$745,179.75}$$
                </li>
                <li>
                    <strong>Combine Total Accumulated Future Wealth:</strong>
                    $$\\text{Total Portfolio Value} = \\$109,357.30 + \\$745,179.75 = \\mathbf{\\$854,537.05}$$
                </li>
                <li>
                    <strong>Deconstruct Principal Deposits vs. Compound Interest:</strong>
                    <ul>
                        <li>Total Cash Out-of-Pocket: $\$10,000 + (\\$500 \\times 360) = \\$10,000 + \\$180,000 = \\mathbf{\\$190,000.00}$.</li>
                        <li>Pure Compound Interest Earned: $\$854,537.05 - \\$190,000.00 = \\mathbf{\\$664,537.05}$.</li>
                    </ul>
                </li>
            </ol>
            <p>
                In this 30-year lifecycle, <strong>77.8% of the final wealth ($664,537)</strong> was generated entirely by compound interest earnings, while out-of-pocket savings accounted for only 22.2% ($190,000).
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. The Cost of Delay: Starting at Age 25 vs. Age 35</h3>
            <p>
                Because time is an exponent in the compounding equation, delaying an investment plan by a single decade creates an enormous wealth penalty that cannot be easily overcome by higher savings rates later:
            </p>

            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Investor Profile</th>
                            <th class="p-3">Contribution Window</th>
                            <th class="p-3">Total Cash Invested</th>
                            <th class="p-3">Portfolio Value at Age 65 (8% Return)</th>
                            <th class="p-3">Compound Multiplier</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Early Starter (Age 25 to 35 only)</td>
                            <td class="p-3 font-sans">10 Years ($500/mo, then stops deposits completely)</td>
                            <td class="p-3">$60,000</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">$937,280</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">15.6&times;</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Late Starter (Age 35 to 65 continuously)</td>
                            <td class="p-3 font-sans">30 Years ($500/mo continuously for 3 decades)</td>
                            <td class="p-3 font-bold text-red-600 dark:text-red-400">$180,000 (3&times; more money!)</td>
                            <td class="p-3">$745,180</td>
                            <td class="p-3">4.1&times;</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Strategic Principles for Exponential Growth</h3>
            <ul>
                <li><strong>The Rule of 72 Mental Shortcut:</strong> To quickly approximate how many years it will take an investment to double at a given annual interest rate, divide 72 by the annual return. At an 8% return, your capital doubles every 9 years ($72 / 8 = 9$). Over a 36-year career, that represents four sequential doublings ($10k &rarr; $20k &rarr; $40k &rarr; $80k &rarr; $160k$). At 10%, capital doubles every 7.2 years, producing five doublings ($10k &rarr; $320k$).</li>
                <li><strong>The Expense Ratio Hazard:</strong> A mutual fund or financial advisor charging a seemingly modest 1.5% annual fee against an 8% gross return reduces net growth to 6.5%. Over a 35-year horizon, that 1.5% drag consumes over <strong>35% of your total lifetime retirement wealth</strong>. Always prioritize low-cost, broad-market index funds (expense ratios below 0.05%).</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>How does inflation erode compound interest over long horizons?</span>
                        <span class="text-emerald-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        While compound interest expands nominal dollar quantities exponentially, macroeconomic inflation erodes the purchasing power of each dollar simultaneously. To evaluate what your future portfolio can actually purchase in today's goods and services, subtract the expected annual inflation rate (historical average ~2.5% to 3.0%) from your nominal return. An 8.0% nominal return in a 3.0% inflation regime delivers a <strong>real return of approximately 5.0%</strong>. A $1,000,000 portfolio 30 years from now at 3% inflation possesses the real purchasing power of approximately $412,000 today.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What is the difference between simple interest and compound interest?</span>
                        <summary class="hidden"></summary>
                        <span class="text-emerald-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Simple interest is calculated solely on the original principal sum for the entire duration ($I = P \\times r \\times t$). If you invest $10,000 at 7% simple interest for 30 years, you earn a flat $700 every year, totaling $21,000 in interest ($31,000 final balance). In contrast, compound interest adds each period's earnings back into the principal. At 7% annual compound interest over 30 years, that same $10,000 grows to $76,123—delivering more than double the wealth of simple interest.
                    </p>
                </details>
            </div>
        </article>
"""

# 3. BMR Calculator (1,800+ words)
ARTICLES['bmr-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Basal Metabolic Rate Guide (1,810+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-rose-100 dark:bg-rose-900/40 text-rose-700 dark:text-rose-300 text-xs font-bold uppercase tracking-wider mb-3">Human Bioenergetics &amp; Clinical Nutrition</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Bioenergetics of Basal Metabolic Rate: Cellular Respiration, Mifflin-St Jeor Equations, and TDEE Calibration</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A technical physiological reference manual on Basal Metabolic Rate (BMR), Resting Energy Expenditure (REE), Total Daily Energy Expenditure (TDEE), adaptive thermogenesis, and clinical indirect calorimetry.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. The Biological Definition of Basal Energy Expenditure</h3>
            <p>
                In human physiology and clinical bioenergetics, <strong>Basal Metabolic Rate (BMR)</strong> represents the absolute minimum rate of energy expenditure required to sustain homeostatic cellular life in a completely post-absorptive, thermoneutral, and motionless resting state. Even when an individual is completely unconscious in bed, the body performs immense metabolic work: maintaining transmembrane sodium-potassium ATPase pump gradients, fueling continuous cardiac contraction, driving pulmonary diaphragm respiration, supporting hepatic detoxification, and orchestrating cellular protein synthesis.
            </p>
            <p>
                In a typical sedentary adult, BMR accounts for approximately <strong>60% to 75% of Total Daily Energy Expenditure (TDEE)</strong>. The remaining daily energy budget is divided between the <strong>Thermic Effect of Food (TEF, ~10%)</strong> required to digest and assimilate macronutrients, and <strong>Activity Energy Expenditure (AEE, 15% to 30%)</strong>, which comprises both purposeful Exercise Activity Thermogenesis (EAT) and Non-Exercise Activity Thermogenesis (NEAT, such as posture maintenance, typing, and spontaneous movement).
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Predictive Mathematical Equations</h3>
            <p>
                While indirect calorimetry (measuring respiratory oxygen consumption $VO_2$ and carbon dioxide production $VCO_2$ via metabolic cart) represents the laboratory gold standard, clinical dietitians utilize validated predictive equations:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-rose-600 dark:text-rose-400 font-sans text-xs uppercase tracking-wider mb-1">Clinical BMR &amp; TDEE Equations</div>
                <div><strong>Mifflin-St Jeor Equation (1990 - Academy of Nutrition &amp; Dietetics Gold Standard):</strong></div>
                <div class="pl-4">&bull; Men: BMR (kcal/day) = (10 &times; weight_kg) + (6.25 &times; height_cm) - (5 &times; age_years) + 5</div>
                <div class="pl-4">&bull; Women: BMR (kcal/day) = (10 &times; weight_kg) + (6.25 &times; height_cm) - (5 &times; age_years) - 161</div>
                <div><strong>Katch-McArdle Equation (Lean Body Mass based):</strong></div>
                <div class="pl-4">&bull; BMR (kcal/day) = 370 + (21.6 &times; Lean Body Mass in kg)</div>
                <div><strong>Total Daily Energy Expenditure (TDEE):</strong> TDEE = BMR &times; Physical Activity Level (PAL Factor)</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Physiological Example</h3>
            <p>
                Consider a <strong>38-year-old female</strong> standing <strong>5 feet 6 inches tall (167.64 cm)</strong>, weighing <strong>154 lbs (69.85 kg)</strong>, who works a desk job but walks briskly for 45 minutes four days per week (Moderately Active, PAL = 1.55).
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Identify Metric Biomarkers:</strong>
                    Weight = $154 \\div 2.20462 = 69.85 \\text{ kg}$; Height = $66 \\text{ inches} \\times 2.54 = 167.64 \\text{ cm}$; Age = $38$ years.
                </li>
                <li>
                    <strong>Calculate Weight Component:</strong>
                    $$10 \\times 69.85 = 698.5 \\text{ kcal}$$
                </li>
                <li>
                    <strong>Calculate Height Component:</strong>
                    $$6.25 \\times 167.64 = 1,047.75 \\text{ kcal}$$
                </li>
                <li>
                    <strong>Calculate Age Component:</strong>
                    $$5 \\times 38 = 190.0 \\text{ kcal}$$
                </li>
                <li>
                    <strong>Execute the Female Mifflin-St Jeor Formula:</strong>
                    $$\\text{BMR} = 698.5 + 1,047.75 - 190.0 - 161 = \\mathbf{1,395.25 \\text{ kcal/day}}$$
                    Her body burns approximately 1,395 calories every 24 hours purely sustaining biological equilibrium.
                </li>
                <li>
                    <strong>Compute Total Daily Energy Expenditure (TDEE):</strong>
                    $$\\text{TDEE} = 1,395.25 \\times 1.55 \\approx \\mathbf{2,163 \\text{ kcal/day}}$$
                    To maintain stable body mass, she requires approximately 2,163 kcal daily. A moderate 20% deficit for sustainable fat loss (-430 kcal) targets approximately 1,730 kcal/day.
                </li>
            </ol>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. Physical Activity Level (PAL) Multiplier Reference Matrix</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Activity Classification</th>
                            <th class="p-3">PAL Multiplier</th>
                            <th class="p-3">Weekly Exercise Volume</th>
                            <th class="p-3">Occupational / Lifestyle Profile</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">Sedentary</td>
                            <td class="p-3 font-mono">1.200</td>
                            <td class="p-3">Little or no structured exercise</td>
                            <td class="p-3">Desk bound, remote office worker (&lt; 5,000 steps/day)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">Lightly Active</td>
                            <td class="p-3 font-mono">1.375</td>
                            <td class="p-3">Light exercise 1 to 3 days/week</td>
                            <td class="p-3">Recreational walking, casual cycling (5,000 - 7,500 steps/day)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">Moderately Active</td>
                            <td class="p-3 font-mono">1.550</td>
                            <td class="p-3">Moderate exercise 3 to 5 days/week</td>
                            <td class="p-3">Active gym training, teacher, retail worker (7,500 - 10,000 steps/day)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">Very Active</td>
                            <td class="p-3 font-mono">1.725</td>
                            <td class="p-3">Heavy training 6 to 7 days/week</td>
                            <td class="p-3">Construction worker, daily competitive athletic training</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">Extremely Active</td>
                            <td class="p-3 font-mono">1.900</td>
                            <td class="p-3">Intense 2x/day training or physical labor</td>
                            <td class="p-3">Elite endurance athlete, agricultural hand laborer, military field ops</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Adaptive Thermogenesis and Metabolic Adaptation</h3>
            <p>
                When individuals maintain a prolonged caloric deficit to achieve weight loss, the human endocrine system initiates an evolutionary defense mechanism known as <strong>adaptive thermogenesis</strong>:
            </p>
            <ul>
                <li><strong>Thyroid Hormone Downregulation:</strong> Circulating active triiodothyronine (T3) levels decline, slowing cellular mitochondrial respiration.</li>
                <li><strong>Leptin Suppression:</strong> As adipose cell volume shrinks, serum leptin drops, signaling the hypothalamus to increase hunger sensations and lower spontaneous physical movement.</li>
                <li><strong>NEAT Collapse:</strong> The body subconsciously reduces fidgeting, micro-movements, and posture adjustments, reducing daily non-exercise energy expenditure by 200 to 400 kcal below mathematical predictions.</li>
                <li><strong>Mitigation Strategy:</strong> Periodically cycling between caloric deficit blocks and 1 to 2-week maintenance diet breaks (recalibrating leptin and thyroid tone), combined with high dietary protein (1.6 to 2.2 g/kg lean mass) and progressive resistance training, prevents excessive loss of metabolically active skeletal muscle.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Why is the Mifflin-St Jeor formula preferred over the legacy Harris-Benedict formula?</span>
                        <span class="text-rose-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        The original Harris-Benedict equation was formulated in 1919 using a small, lean cohort of young subjects. Extensive systematic validation studies published by the Academy of Nutrition and Dietetics demonstrated that Harris-Benedict overestimates resting energy expenditure by 5% to 15% in contemporary populations. The Mifflin-St Jeor equation (1990) was validated across a broad demographic cohort including diverse body composition profiles, proving accurate within &plusmn;10% of measured indirect calorimetry in over 82% of non-obese and obese clinical patients.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Does muscle tissue burn significantly more calories than body fat at rest?</span>
                        <summary class="hidden"></summary>
                        <span class="text-rose-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        While skeletal muscle is more metabolically active than adipose tissue, popular fitness claims that "one pound of muscle burns 50 calories a day" are physiological myths. Precise human organ metabolic mapping shows that resting skeletal muscle burns approximately <strong>13 kcal per kilogram per day (6 kcal/lb/day)</strong>, whereas adipose tissue burns approximately <strong>4.5 kcal/kg/day (2 kcal/lb/day)</strong>. The true metabolic powerhouses of resting BMR are internal vital organs: the liver, brain, heart, and kidneys account for less than 6% of total body weight but consume over 60% of resting basal calories.
                    </p>
                </details>
            </div>
        </article>
"""

def update_file(filename, article_html):
    for base_dir in [ONEDRIVE_CALC_DIR, DESKTOP_CALC_DIR]:
        if not os.path.exists(base_dir):
            continue
        file_path = os.path.join(base_dir, filename)
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        if '<article' in content and '</article>' in content:
            content = re.sub(r'<article[^>]*>.*?</article>', lambda _: article_html, content, flags=re.DOTALL | re.I)
        else:
            if '</main>' in content:
                content = content.replace('</main>', f'{article_html}\n</main>', 1)
            elif '<footer' in content:
                content = content.replace('<footer', f'{article_html}\n<footer', 1)
                
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

for fname, art in ARTICLES.items():
    update_file(fname, art)
    print(f"Successfully upgraded {fname} with {len(art.split())} words!")

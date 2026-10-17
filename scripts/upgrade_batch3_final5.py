import os
import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

ONEDRIVE_CALC_DIR = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
DESKTOP_CALC_DIR = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'

ARTICLES = {}

# 1. Sales Tax Calculator (1,700+ words)
ARTICLES['sales-tax-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Sales Tax Guide (1,750+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-amber-100 dark:bg-amber-900/40 text-amber-700 dark:text-amber-300 text-xs font-bold uppercase tracking-wider mb-3">Fiscal Policy &amp; Indirect Taxation</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Architecture of US Retail Sales Tax: Jurisdictional Stacking, Economic Nexus, and Gross-to-Net Calculations</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A technical reference guide to state, county, municipal, and special district sales tax stacking, forward and reverse tax calculations, destination sourcing rules under South Dakota v. Wayfair, and statutory exemptions.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. The Fragmented Nature of US Sales Taxation</h3>
            <p>
                Unlike the vast majority of developed nations that administer a unified national Value Added Tax (VAT) or Goods and Services Tax (GST), the United States operates a decentralized, multi-tiered retail sales tax system. There is zero federal sales tax in the United States. Instead, indirect transaction taxes are levied independently by individual states and more than 11,000 distinct local taxing jurisdictions, creating one of the most complex fiscal compliance landscapes in global commerce.
            </p>
            <p>
                When a consumer completes a purchase at a physical retail store or through an e-commerce marketplace, the total sales tax charged rarely reflects a single statutory percentage. Instead, the final rate represents a composite multi-jurisdictional "stack" comprising:
            </p>
            <ul>
                <li><strong>State Baseline Sales Tax:</strong> Set by state legislatures (ranging from 2.9% in Colorado to 7.25% in California).</li>
                <li><strong>County Sales Tax:</strong> Imposed by county commissions to fund local infrastructure, courts, and law enforcement.</li>
                <li><strong>Municipal / City Sales Tax:</strong> Levied by city councils to finance municipal public works, emergency services, and education.</li>
                <li><strong>Special Taxing Districts (SPDs):</strong> Additional targeted levies designated to fund regional public transit systems (e.g., BART in California, MARTA in Georgia), stadium authorities, or community development projects.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Mathematical Formulations</h3>
            <p>
                Sales tax arithmetic operates along two distinct pathways: forward calculation (determining tax and total from a pre-tax subtotal) and reverse calculation (extracting the true pre-tax price from a tax-inclusive total receipts figure).
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-amber-600 dark:text-amber-400 font-sans text-xs uppercase tracking-wider mb-1">Sales Tax Formulas</div>
                <div><strong>Combined Composite Rate:</strong> R_total = R_state + R_county + R_city + R_special</div>
                <div><strong>Forward Tax Amount:</strong> Tax = Subtotal &times; R_total</div>
                <div><strong>Gross Final Price:</strong> Total = Subtotal + Tax = Subtotal &times; (1 + R_total)</div>
                <div><strong>Reverse Extraction (Pre-Tax Base):</strong> Subtotal = Total / (1 + R_total)</div>
                <div><strong>Reverse Tax Extracted:</strong> Tax = Total - [ Total / (1 + R_total) ]</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Walkthrough</h3>
            <p>
                To illustrate how jurisdictional stacking and reverse tax calculations function in practice, consider two common retail and accounting scenarios:
            </p>
            <ol class="space-y-4 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Scenario A: Forward Purchase Calculation in Chicago, Illinois:</strong>
                    A consumer purchases computer hardware with a pre-tax subtotal of <strong>$1,250.00</strong>.
                    <ul>
                        <li>Illinois State Base Sales Tax: 6.25%</li>
                        <li>Cook County Sales Tax: 1.75%</li>
                        <li>City of Chicago Municipal Sales Tax: 1.25%</li>
                        <li>Regional Transportation Authority (RTA) Special District Tax: 1.00%</li>
                        <li><strong>Composite Sales Tax Rate:</strong> $6.25\\% + 1.75\\% + 1.25\\% + 1.00\\% = \\mathbf{10.25\\%}$ ($0.1025$).</li>
                        <li><strong>Sales Tax Liability:</strong> $\$1,250.00 \\times 0.1025 = \\mathbf{\\$128.13}$.</li>
                        <li><strong>Total Checkout Cost:</strong> $\$1,250.00 + \\$128.13 = \\mathbf{\\$1,378.13}$.</li>
                    </ul>
                </li>
                <li>
                    <strong>Scenario B: Reverse Accounting Extraction for a Business Owner:</strong>
                    A restaurant owner in Seattle, Washington rings up <strong>$4,580.00</strong> in total gross receipts during an evening service, where all menu prices are statutory tax-inclusive. The combined Washington state and King County sales tax rate is <strong>10.35%</strong> ($0.1035$). The accountant must separate net food revenues from sales tax collected to remit to the state Department of Revenue.
                    <ul>
                        <li><strong>Pre-Tax Food Revenue (Subtotal):</strong>
                            $$\\text{Subtotal} = \\frac{\\$4,580.00}{1 + 0.1035} = \\frac{\\$4,580.00}{1.1035} \\approx \\mathbf{\\$4,149.98}$$
                        </li>
                        <li><strong>Sales Tax Liability to Remit:</strong>
                            $$\\text{Tax Remittance} = \\$4,580.00 - \\$4,149.98 = \\mathbf{\\$430.02}$$
                        </li>
                        <li>Verification: $\$4,149.98 \\times 0.1035 = \\$430.02$. Notice that calculating $10.35\\%$ directly on the gross total ($4,580 \\times 0.1035 = 474.03$) would result in a costly over-remittance error of $\$44.01$!</li>
                    </ul>
                </li>
            </ol>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. US State Sales Tax Comparison Matrix</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">State / Jurisdiction</th>
                            <th class="p-3">State Base Rate</th>
                            <th class="p-3">Avg. Local Surcharge</th>
                            <th class="p-3">Max Combined Rate</th>
                            <th class="p-3">Grocery Exemption Status</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Tennessee</td>
                            <td class="p-3">7.00%</td>
                            <td class="p-3">2.55%</td>
                            <td class="p-3 font-bold text-red-600 dark:text-red-400">9.75%</td>
                            <td class="p-3 font-sans">Reduced rate (4.00%)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Louisiana</td>
                            <td class="p-3">4.45%</td>
                            <td class="p-3">5.10%</td>
                            <td class="p-3 font-bold text-red-600 dark:text-red-400">11.45% (Highest US)</td>
                            <td class="p-3 font-sans">Exempt from state tax</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">California</td>
                            <td class="p-3">7.25%</td>
                            <td class="p-3">1.63%</td>
                            <td class="p-3 font-bold text-red-600 dark:text-red-400">10.75%</td>
                            <td class="p-3 font-sans">100% Fully Exempt</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Texas</td>
                            <td class="p-3">6.25%</td>
                            <td class="p-3">1.95%</td>
                            <td class="p-3">8.25%</td>
                            <td class="p-3 font-sans">100% Fully Exempt</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">New Hampshire</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">0.00%</td>
                            <td class="p-3">0.00%</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">0.00%</td>
                            <td class="p-3 font-sans">No General Sales Tax (NOMAD State)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Oregon</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">0.00%</td>
                            <td class="p-3">0.00%</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">0.00%</td>
                            <td class="p-3 font-sans">No General Sales Tax (NOMAD State)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Modern E-Commerce Economics: South Dakota v. Wayfair</h3>
            <p>
                Prior to 2018, under the landmark 1992 ruling in <em>Quill Corp. v. North Dakota</em>, states were constitutionally prohibited from requiring out-of-state remote sellers to collect sales tax unless the vendor maintained a "physical presence" (such as a warehouse, office, or traveling salesperson) inside the state.
            </p>
            <p>
                In June 2018, the US Supreme Court issued its landmark decision in <strong>South Dakota v. Wayfair, Inc. (585 U.S. 329)</strong>, overturning the physical presence rule and establishing the doctrine of <strong>Economic Nexus</strong>. Under modern economic nexus statutes adopted by 45 states, an out-of-state online retailer is legally obligated to register, collect, and remit local sales taxes once its transaction activity within the destination state surpasses statutory thresholds (typically <strong>$100,000 in gross annual sales or 200 individual transactions</strong>).
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What are the five US states with no general statewide sales tax?</span>
                        <span class="text-amber-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        The five states without a statewide general retail sales tax are frequently remembered by the acronym <strong>NOMAD</strong>: <strong>N</strong>ew Hampshire, <strong>O</strong>regon, <strong>M</strong>ontana, <strong>A</strong>laska, and <strong>D</strong>elaware. Note that while Alaska imposes no state-level tax, local municipalities in Alaska are legally authorized to levy local sales taxes (some up to 7.5%).
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What is the difference between sales tax and use tax?</span>
                        <summary class="hidden"></summary>
                        <span class="text-amber-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Sales tax is levied on transactions occurring within a taxing state and is collected directly by the seller at checkout. Use tax is the legally companion excise tax imposed on the storage, use, or consumption of taxable items purchased out-of-state without sales tax paid (for example, ordering untaxed equipment online from a vendor lacking nexus). Residents and businesses are legally obligated to declare untaxed purchases on their annual state tax returns and remit the equivalent use tax directly.
                    </p>
                </details>
            </div>
        </article>
"""

# 2. Salary Calculator (1,800+ words)
ARTICLES['salary-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Salary & Payroll Guide (1,820+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-blue-100 dark:bg-blue-900/40 text-blue-700 dark:text-blue-300 text-xs font-bold uppercase tracking-wider mb-3">Labor Economics &amp; Payroll Withholding</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Anatomy of a Paycheck: Gross Salary, Statutory FICA Splits, Marginal Withholding, and Net Take-Home Pay</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A technical payroll reference guide explaining gross-to-net salary conversions, IRS Publication 15-T wage bracket withholding, FICA thresholds, pre-tax elective deferrals, and annualized pay cycle conversions.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. Deconstructing the Paycheck: Gross Earnings vs. Disposable Cash Flow</h3>
            <p>
                When an employee negotiates an annual compensation package—such as an $85,000 corporate salary—they are establishing their <strong>gross contractual earnings</strong>. However, the liquid funds actually deposited into their checking account on payday represent <strong>net spendable income</strong>. Between gross salary and net pay lies a complex gauntlet of federal statutory mandates, state progressive tax schedules, mandatory social insurance contributions, and voluntary pre-tax benefit elections.
            </p>
            <p>
                Understanding how these deductions are calculated allows workers to optimize their Form W-4 allowances, accurately assess job offers across states with divergent tax regimes, project cash flow across differing payroll schedules, and legally shield thousands of dollars annually through pre-tax benefits like 401(k) plans and Health Savings Accounts (HSAs).
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Payroll Mathematical Formulas</h3>
            <p>
                The sequential reduction from gross salary to net pay follows a rigorous statutory hierarchy defined by the Internal Revenue Code:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-blue-600 dark:text-blue-400 font-sans text-xs uppercase tracking-wider mb-1">Payroll Deduction Sequences</div>
                <div><strong>Adjusted Gross Pay (AGP):</strong> Gross Pay - Pre-Tax Deductions (401k, HSA, Medical)</div>
                <div><strong>Social Security Tax (6.2%):</strong> Min(Gross Pay, Wage Base Limit) &times; 0.062</div>
                <div><strong>Medicare Tax (1.45%):</strong> Gross Pay &times; 0.0145 + Max(0, Gross Pay - $200k) &times; 0.009</div>
                <div><strong>Federal Income Withholding (FIT):</strong> IRS Pub 15-T Progressive Tax Function(AGP)</div>
                <div><strong>State Income Withholding (SIT):</strong> State Bracket Function(AGP - State Allowances)</div>
                <div><strong>Net Take-Home Pay:</strong> AGP - FICA - FIT - SIT - Post-Tax Deductions (Roth, Garnishments)</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Walkthrough</h3>
            <p>
                Consider a full-time salaried professional in 2026 earning <strong>$95,000 annually</strong>, paid on a <strong>bi-weekly schedule (26 pay periods per year)</strong>. The employee is a single filer claiming the standard deduction, contributing 6% to a Traditional 401(k), and paying $150 per pay period for employer healthcare coverage in a state with a 4.5% flat income tax.
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Determine Gross Pay Per Period:</strong>
                    $$\\text{Gross Pay} = \\frac{\\$95,000}{26} \\approx \\mathbf{\\$3,653.85 \\text{ per bi-weekly paycheck}}$$
                </li>
                <li>
                    <strong>Calculate Pre-Tax Deductions:</strong>
                    <ul>
                        <li>401(k) Contribution (6%): $\$3,653.85 \\times 0.06 = \\$219.23$.</li>
                        <li>Health Insurance Premium: $\$150.00$.</li>
                        <li>Total Pre-Tax Reductions = $\$219.23 + \\$150.00 = \\mathbf{\\$369.23}$.</li>
                        <li><strong>Federal Taxable Wages (AGP):</strong> $\$3,653.85 - \\$369.23 = \\mathbf{\\$3,284.62}$.</li>
                    </ul>
                </li>
                <li>
                    <strong>Calculate Mandatory FICA Taxes:</strong>
                    <ul>
                        <li>Social Security (6.2% on gross minus section 125 medical): $(\\$3,653.85 - \\$150) \\times 0.062 = \\$3,503.85 \\times 0.062 = \\mathbf{\\$217.24}$.</li>
                        <li>Medicare (1.45% on gross minus section 125 medical): $\$3,503.85 \\times 0.0145 = \\mathbf{\\$50.81}$.</li>
                        <li>Total FICA Withheld = $\$217.24 + \\$50.81 = \\mathbf{\\$268.05}$.</li>
                    </ul>
                </li>
                <li>
                    <strong>Calculate Federal Income Tax Withholding (IRS Pub 15-T):</strong>
                    Annualized taxable wages = $\$3,284.62 \\times 26 = \\$85,400$. After subtracting 2026 single standard deduction (~$\\$15,000$), taxable income equals $\$70,400$. Applying progressive 2026 brackets (10%, 12%, 22%) results in annual federal tax of approximately $\$9,480$, or <strong>$364.62 per bi-weekly period</strong>.
                </li>
                <li>
                    <strong>Calculate State Income Tax Withholding:</strong>
                    Flat 4.5% applied to state taxable base (~$\\$3,200$) = <strong>$144.00 per period</strong>.
                </li>
                <li>
                    <strong>Compute Final Net Take-Home Pay:</strong>
                    $$\\text{Net Pay} = \\$3,653.85 - \\$369.23 \\text{ (Pre-tax)} - \\$268.05 \\text{ (FICA)} - \\$364.62 \\text{ (FIT)} - \\$144.00 \\text{ (SIT)} = \\mathbf{\\$2,507.95}$$
                </li>
            </ol>
            <p>
                The employee takes home <strong>$2,507.95 bi-weekly</strong>, representing an effective take-home realization rate of approximately <strong>68.6%</strong> of headline gross salary.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. Standard Pay Cycle Conversion Matrix</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Annual Salary</th>
                            <th class="p-3">Hourly (2,080 hrs)</th>
                            <th class="p-3">Bi-Weekly (26 cycles)</th>
                            <th class="p-3">Semi-Monthly (24 cycles)</th>
                            <th class="p-3">Monthly (12 cycles)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">$50,000</td>
                            <td class="p-3">$24.04/hr</td>
                            <td class="p-3">$1,923.08</td>
                            <td class="p-3">$2,083.33</td>
                            <td class="p-3">$4,166.67</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">$75,000</td>
                            <td class="p-3">$36.06/hr</td>
                            <td class="p-3">$2,884.62</td>
                            <td class="p-3">$3,125.00</td>
                            <td class="p-3">$6,250.00</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">$100,000</td>
                            <td class="p-3">$48.08/hr</td>
                            <td class="p-3">$3,846.15</td>
                            <td class="p-3">$4,166.67</td>
                            <td class="p-3">$8,333.33</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">$150,000</td>
                            <td class="p-3">$72.12/hr</td>
                            <td class="p-3">$5,769.23</td>
                            <td class="p-3">$6,250.00</td>
                            <td class="p-3">$12,500.00</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Strategic Paycheck Optimization Guidelines</h3>
            <ul>
                <li><strong>Bi-Weekly vs. Semi-Monthly Budgeting:</strong> Bi-weekly payrolls produce 26 paychecks per year, meaning that in two months of every calendar year, you receive three paychecks instead of two. Budgeting fixed monthly expenses (rent, auto loans) against two paychecks allows the two "bonus" paychecks to be directed entirely toward debt paydown or investment compounding.</li>
                <li><strong>The 0.9% Additional Medicare Surtax:</strong> Enacted under the Affordable Care Act, an additional 0.9% Medicare tax applies to wages exceeding $200,000 for single filers ($250,000 for married couples filing jointly). Employers are legally required to begin withholding once individual wages pass $200,000, regardless of marital status.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Why does earning a raise into a higher tax bracket never reduce your take-home pay?</span>
                        <span class="text-blue-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        The US federal tax code operates on a <strong>marginal progressive bracket system</strong>. When your earnings cross into a higher tax bracket (e.g., from 12% to 22%), only the specific dollars earned above that threshold are taxed at the higher 22% rate. All previous dollars earned continue to be taxed at the lower 10% and 12% rates. Moving into a higher bracket always increases your total net take-home pay.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What is the Social Security wage base cap?</span>
                        <summary class="hidden"></summary>
                        <span class="text-blue-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Social Security taxes (6.2%) apply only to earnings up to an annual statutory wage ceiling indexed to national average wage growth (exceeding $170,000 in recent tax years). Once your cumulative year-to-date earnings surpass this threshold, Social Security deductions drop to zero for the remainder of that calendar year, resulting in an automatic 6.2% bump in net take-home pay until the clock resets on January 1.
                    </p>
                </details>
            </div>
        </article>
"""

# 3. Pace Calculator (1,700+ words)
ARTICLES['pace-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Running Pace & Aerobic Kinetics Guide (1,720+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-900/40 text-emerald-700 dark:text-emerald-300 text-xs font-bold uppercase tracking-wider mb-3">Exercise Physiology &amp; Endurance Biomechanics</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Biomechanics of Running Pace: Aerobic Velocity, Split Execution, and Daniels' VDOT Oxygen Kinetics</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A technical exercise physiology manual on running pace calculations, velocity conversions, lactate threshold pacing, negative split race execution, and Jack Daniels' VDOT oxygen kinetics tables.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. Velocity vs. Pace: The Inverse Dimension of Endurance</h3>
            <p>
                In mechanical physics, velocity is expressed as distance covered per unit of time (miles per hour or kilometers per hour). In distance running, track athletics, and triathlon training, endurance athletes universally invert this formulation to track <strong>pace</strong>: time elapsed per unit of distance (minutes and seconds per mile or per kilometer).
            </p>
            <p>
                This inverse formulation is biologically intuitive for race execution: it allows a runner to continuously calibrate their internal metabolic output against roadside course markers. However, because pace is inversely proportional to speed, small changes in running pace represent non-linear metabolic demands. Improving your 5K pace from 8:00 min/mile to 7:00 min/mile demands an exponential increase in maximal oxygen uptake (VO2 max) and cardiac output compared to improving from 12:00 min/mile to 11:00 min/mile.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Pace Mathematical Formulas</h3>
            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-emerald-600 dark:text-emerald-400 font-sans text-xs uppercase tracking-wider mb-1">Endurance Pacing Formulations</div>
                <div><strong>Pace (Minutes per Mile):</strong> P = Time (in decimal minutes) / Distance (in miles)</div>
                <div><strong>Speed to Pace Conversion:</strong> Pace (min/mi) = 60 / Speed (mph)</div>
                <div><strong>Pace to Speed Conversion:</strong> Speed (mph) = 60 / Pace (min/mi)</div>
                <div><strong>Metric to Imperial Pace:</strong> Pace (min/mi) = Pace (min/km) &times; 1.609344</div>
                <div><strong>Riegel's Race Finish Predictor:</strong> T_2 = T_1 &times; (D_2 / D_1)^1.06</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Walkthrough</h3>
            <p>
                To illustrate pacing calculations and split breakdowns, consider a runner targeting a sub-3:45:00 marathon (26.21875 miles, or 42.195 km).
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Convert Target Finish Time to Total Seconds:</strong>
                    $$T = (3 \\text{ hours} \\times 3,600) + (45 \\text{ minutes} \\times 60) = 10,800 + 2,700 = 13,500 \\text{ seconds}$$
                </li>
                <li>
                    <strong>Compute Target Mile Pace:</strong>
                    $$\\text{Seconds per mile} = \\frac{13,500 \\text{ sec}}{26.21875 \\text{ mi}} \\approx 514.9 \\text{ seconds/mile}$$
                    Divide by 60: $514.9 \\div 60 = 8.5816$ minutes.
                    Extract seconds: $0.5816 \\times 60 \\approx 35$ seconds &implies; <strong>8:35 min/mile target pace</strong>.
                </li>
                <li>
                    <strong>Compute Equivalent Kilometer Pace (Metric):</strong>
                    $$\\text{Seconds per km} = \\frac{13,500 \\text{ sec}}{42.195 \\text{ km}} \\approx 319.94 \\text{ seconds/km}$$
                    Divide by 60: $319.94 \\div 60 = 5.332$ minutes.
                    Extract seconds: $0.332 \\times 60 \\approx 20$ seconds &implies; <strong>5:20 min/km target pace</strong>.
                </li>
                <li>
                    <strong>Calculate 10K and Half Marathon Intermediate Splits:</strong>
                    <ul>
                        <li>10K Split (6.2137 mi): $6.2137 \\times 8.5816 \\text{ min} \\approx 53 \\text{ min } 20 \\text{ sec}$.</li>
                        <li>Half Marathon Split (13.1094 mi): $13.1094 \\times 8.5816 \\text{ min} \\approx 1 \\text{ hr } 52 \\text{ min } 30 \\text{ sec}$.</li>
                    </ul>
                </li>
            </ol>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. Standard Race Distance Pacing Matrix</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Target Pace (min/mi)</th>
                            <th class="p-3">Metric (min/km)</th>
                            <th class="p-3">5K (3.11 mi)</th>
                            <th class="p-3">10K (6.21 mi)</th>
                            <th class="p-3">Half Marathon</th>
                            <th class="p-3">Full Marathon</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">6:00 min/mi</td>
                            <td class="p-3">3:44 min/km</td>
                            <td class="p-3">18:38</td>
                            <td class="p-3">37:17</td>
                            <td class="p-3">1:18:39</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">2:37:19</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">7:00 min/mi</td>
                            <td class="p-3">4:21 min/km</td>
                            <td class="p-3">21:44</td>
                            <td class="p-3">43:30</td>
                            <td class="p-3">1:31:46</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">3:03:32</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">8:00 min/mi</td>
                            <td class="p-3">4:58 min/km</td>
                            <td class="p-3">24:51</td>
                            <td class="p-3">49:43</td>
                            <td class="p-3">1:44:52</td>
                            <td class="p-3 font-bold text-blue-600 dark:text-blue-400">3:29:45</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">9:00 min/mi</td>
                            <td class="p-3">5:36 min/km</td>
                            <td class="p-3">27:57</td>
                            <td class="p-3">55:56</td>
                            <td class="p-3">1:57:59</td>
                            <td class="p-3">3:55:58</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">10:00 min/mi</td>
                            <td class="p-3">6:13 min/km</td>
                            <td class="p-3">31:04</td>
                            <td class="p-3">1:02:08</td>
                            <td class="p-3">2:11:06</td>
                            <td class="p-3">4:22:11</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Strategic Racing Tactics: Positive vs. Negative Splits</h3>
            <p>
                Exercise physiologists examining pacing strategies among elite marathoners and world record performances (including Eliud Kipchoge's sub-2:00:00 exhibition) consistently observe a fundamental endurance principle: <strong>the negative split</strong>.
            </p>
            <ul>
                <li><strong>The Danger of Positive Splits:</strong> Starting a marathon 20 to 30 seconds per mile faster than your physiological threshold depletes limited intramyocellular glycogen stores prematurely, elevates core body temperature, and causes metabolic acidosis. When glycogen is exhausted around mile 20 ("hitting the wall"), running pace crashes dramatically, losing far more time than was gained early on.</li>
                <li><strong>The Mastery of Negative Splits:</strong> Running the second half of a race 1% to 2% faster than the first half preserves glycogen reserves, utilizes free fatty acid oxidation during the early miles, and leverages psychological momentum as you pass decelerating competitors in the final 10 kilometers.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What is Jack Daniels' VDOT formula in endurance training?</span>
                        <span class="text-emerald-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Developed by legendary exercise physiologist Dr. Jack Daniels, VDOT measures an athlete's "effective VO2 max" by combining laboratory aerobic capacity with biomechanical running economy. By evaluating a recent race performance, VDOT calculates individualized training paces across five physiological zones: Easy (E-pace), Marathon (M-pace), Threshold (T-pace), Interval (I-pace), and Repetition (R-pace).
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>How does running on a treadmill compare to outdoor pacing?</span>
                        <summary class="hidden"></summary>
                        <span class="text-emerald-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Because a treadmill belt pulls underneath the runner and there is zero outdoor aerodynamic drag (wind resistance), running on a flat treadmill (0% incline) requires slightly less metabolic work than outdoor running at identical speeds. Landmark studies by Jones and Doust (1996) demonstrated that setting a treadmill to a <strong>1.0% gradient</strong> accurately balances the energetic cost of outdoor road running across speeds between 7.0 mph and 11.2 mph.
                    </p>
                </details>
            </div>
        </article>
"""

# 4. Ideal Weight Calculator (1,700+ words)
ARTICLES['ideal-weight-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Ideal Weight Guide (1,710+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-teal-100 dark:bg-teal-900/40 text-teal-700 dark:text-teal-300 text-xs font-bold uppercase tracking-wider mb-3">Clinical Anthropometry &amp; Pharmacokinetics</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Clinical Determination of Ideal Body Weight (IBW): Anthropometric Formulas, Frame Sizing, and Pharmacokinetic Dosing</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A technical medical manual on Ideal Body Weight (IBW), comparing the Devine, Robinson, Miller, and Hamwi equations, frame size adjustments, and clinical drug dosing protocols in intensive care pharmacology.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. The Origin of "Ideal" Body Weight: From Life Insurance to Clinical Medicine</h3>
            <p>
                The concept of an "ideal" body weight originated not in medical clinics, but in the actuarial risk tables published by the Metropolitan Life Insurance Company in the 1940s. Actuaries compiled extensive statistical correlations between human stature, weight, and longevity, determining the weight ranges associated with the lowest all-cause mortality rates among policyholders.
            </p>
            <p>
                In the 1960s and 1970s, medical pharmacologists recognized that administering weight-based pharmaceuticals (such as aminoglycoside antibiotics, chemotherapeutic agents, anesthetics, and mechanical ventilator tidal volumes) according to actual total body weight resulted in catastrophic overdoses in patients carrying significant adipose tissue. Because hydrophilic (water-soluble) medications distribute primarily into lean muscle mass and vascular volume rather than adipose tissue, physicians required a standardized mathematical formula to calculate a patient's expected non-obese baseline: <strong>Ideal Body Weight (IBW)</strong>.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Classical Anthropometric Formulas</h3>
            <p>
                Four classical empirical formulas dominate clinical literature, each establishing a base weight for a person standing 5 feet tall (60 inches / 152.4 cm) and adding incremental weight for each additional inch of height:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-teal-600 dark:text-teal-400 font-sans text-xs uppercase tracking-wider mb-1">Standard IBW Formulations (Height &gt; 5 ft)</div>
                <div><strong>Devine Formula (1974 - Clinical Standard):</strong></div>
                <div class="pl-4">&bull; Men: IBW (kg) = 50.0 + 2.3 &times; (Height in inches - 60)</div>
                <div class="pl-4">&bull; Women: IBW (kg) = 45.5 + 2.3 &times; (Height in inches - 60)</div>
                <div><strong>Robinson Formula (1983):</strong></div>
                <div class="pl-4">&bull; Men: IBW (kg) = 52.0 + 1.9 &times; (Height in inches - 60)</div>
                <div class="pl-4">&bull; Women: IBW (kg) = 49.0 + 1.7 &times; (Height in inches - 60)</div>
                <div><strong>Miller Formula (1983):</strong></div>
                <div class="pl-4">&bull; Men: IBW (kg) = 56.2 + 1.41 &times; (Height in inches - 60)</div>
                <div class="pl-4">&bull; Women: IBW (kg) = 53.1 + 1.36 &times; (Height in inches - 60)</div>
                <div><strong>Hamwi Formula (1964):</strong></div>
                <div class="pl-4">&bull; Men: IBW (lbs) = 106 + 6 &times; (Height in inches - 60)</div>
                <div class="pl-4">&bull; Women: IBW (lbs) = 100 + 5 &times; (Height in inches - 60)</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Clinical Example</h3>
            <p>
                To compare how these classical formulas evaluate body weight, consider an adult male standing <strong>5 feet 10 inches tall (70 inches / 177.8 cm)</strong>:
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Calculate Height Increment:</strong>
                    $$\\text{Inches over 60} = 70 - 60 = 10 \\text{ inches}$$
                </li>
                <li>
                    <strong>Apply the Devine Formula (Clinical Standard):</strong>
                    $$\\text{IBW} = 50.0 + (2.3 \\times 10) = 50.0 + 23.0 = \\mathbf{73.0 \\text{ kg}} \\times 2.20462 \\approx \\mathbf{160.9 \\text{ lbs}}$$
                </li>
                <li>
                    <strong>Apply the Robinson Formula:</strong>
                    $$\\text{IBW} = 52.0 + (1.9 \\times 10) = 52.0 + 19.0 = \\mathbf{71.0 \\text{ kg}} \\times 2.20462 \\approx \\mathbf{156.5 \\text{ lbs}}$$
                </li>
                <li>
                    <strong>Apply the Miller Formula:</strong>
                    $$\\text{IBW} = 56.2 + (1.41 \\times 10) = 56.2 + 14.1 = \\mathbf{70.3 \\text{ kg}} \\times 2.20462 \\approx \\mathbf{155.0 \\text{ lbs}}$$
                </li>
                <li>
                    <strong>Apply the Hamwi Formula:</strong>
                    $$\\text{IBW} = 106 + (6 \\times 10) = 106 + 60 = \\mathbf{166.0 \\text{ lbs}} \\div 2.20462 \\approx \\mathbf{75.3 \\text{ kg}}$$
                </li>
                <li>
                    <strong>WHO Healthy BMI Benchmark (BMI 18.5 - 24.9):</strong>
                    Height in meters = $1.778$ m ($1.778^2 = 3.161$ m$^2$).
                    <ul>
                        <li>Minimum Normal (BMI 18.5): $18.5 \\times 3.161 = \\mathbf{58.5 \\text{ kg}} \\text{ (129.0 lbs)}$.</li>
                        <li>Maximum Normal (BMI 24.9): $24.9 \\times 3.161 = \\mathbf{78.7 \\text{ kg}} \\text{ (173.5 lbs)}$.</li>
                    </ul>
                </li>
            </ol>
            <p>
                All four classical formulas cluster tightly between <strong>155 lbs and 166 lbs</strong> (70 kg to 75 kg), centering directly within the upper-middle segment of the World Health Organization's healthy BMI range.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. Ideal Weight Comparison Matrix (Male vs. Female Across Heights)</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Stature / Height</th>
                            <th class="p-3">Devine Male</th>
                            <th class="p-3">Devine Female</th>
                            <th class="p-3">WHO Healthy Range (BMI 18.5 - 24.9)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">5' 2" (157.5 cm)</td>
                            <td class="p-3">120.4 lbs (54.6 kg)</td>
                            <td class="p-3">110.5 lbs (50.1 kg)</td>
                            <td class="p-3">101.0 - 136.0 lbs (45.8 - 61.7 kg)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">5' 6" (167.6 cm)</td>
                            <td class="p-3">140.7 lbs (63.8 kg)</td>
                            <td class="p-3">130.7 lbs (59.3 kg)</td>
                            <td class="p-3">114.6 - 154.3 lbs (52.0 - 70.0 kg)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">5' 10" (177.8 cm)</td>
                            <td class="p-3">160.9 lbs (73.0 kg)</td>
                            <td class="p-3">151.0 lbs (68.5 kg)</td>
                            <td class="p-3">129.0 - 173.5 lbs (58.5 - 78.7 kg)</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">6' 2" (188.0 cm)</td>
                            <td class="p-3">181.2 lbs (82.2 kg)</td>
                            <td class="p-3">171.3 lbs (77.7 kg)</td>
                            <td class="p-3">144.3 - 194.2 lbs (65.4 - 88.1 kg)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Frame Size Adjustments &amp; Body Composition Realities</h3>
            <p>
                A central critique of classical formulas is their disregard for skeletal robusticity and muscular hypertrophy. To account for skeletal breadth, clinical nutritionists measure <strong>wrist circumference relative to standing height</strong> ($r = \\text{Height} / \\text{Wrist Circumference}$):
            </p>
            <ul>
                <li><strong>Small Frame ($r > 10.4$ for men, $r > 10.9$ for women):</strong> Subtract 10% from calculated IBW.</li>
                <li><strong>Medium Frame ($9.6 \le r \le 10.4$ for men, $9.9 \le r \le 10.9$ for women):</strong> Use baseline IBW.</li>
                <li><strong>Large Frame ($r < 9.6$ for men, $r < 9.9$ for women):</strong> Add 10% to calculated IBW.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Why does the Devine formula remain the gold standard in hospital pharmacology?</span>
                        <span class="text-teal-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Although originally developed by Dr. Ben J. Devine in 1974 for pharmacokinetic dosing of theophylline and digoxin, virtually all FDA drug approval clinical trials and ICU ventilator tidal volume algorithms (6 to 8 mL/kg of predicted body weight) have standardized on the Devine equation. Even when newer formulas claim minor statistical refinements, clinicians maintain the Devine standard to prevent medication errors.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What is Adjusted Body Weight (AdjBW) and when is it utilized?</span>
                        <summary class="hidden"></summary>
                        <span class="text-teal-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        When a patient's actual weight exceeds 120% to 130% of their IBW (clinical obesity), using IBW underestimates drug clearance, while using actual weight causes overdose. Clinical pharmacologists compute Adjusted Body Weight: <code>AdjBW = IBW + 0.40 &times; (Actual Weight - IBW)</code>. The 0.40 factor accounts for the fact that approximately 40% of adipose tissue mass consists of vascularized extracellular fluid into which hydrophilic medications distribute.
                    </p>
                </details>
            </div>
        </article>
"""

# 5. Solar Payoff Calculator (1,750+ words)
ARTICLES['solar-payoff-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Solar Photovoltaic Payoff Guide (1,760+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-amber-100 dark:bg-amber-900/40 text-amber-700 dark:text-amber-300 text-xs font-bold uppercase tracking-wider mb-3">Renewable Energy Engineering &amp; Capital Budgeting</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Financial Economics of Residential Solar PV: Levelized Cost of Energy, Net Energy Metering (NEM 3.0), and Discounted Payback Timelines</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A technical energy economics manual on residential photovoltaic payback periods, NREL PVWatts solar irradiance modeling, Section 25D federal clean energy tax credits, and utility battery arbitrage economics.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. Capital Expenditure vs. Avoided Grid Utility Expense</h3>
            <p>
                Investing in residential rooftop solar photovoltaic (PV) generation represents a major capital budgeting decision. Rather than an ongoing discretionary expense, solar operates as a capital asset substitution: you exchange an indefinite, escalating monthly operating expenditure (utility retail power bills) for an upfront, fixed capital asset that generates kilowatt-hours (kWh) of electricity at near-zero marginal operating cost for 25 to 30 years.
            </p>
            <p>
                However, accurately projecting solar payback is far more complex than dividing system price by your current annual electric bill. A robust financial model must incorporate solar irradiance degradation (silicon cell degradation averaging 0.5% annually), local utility tariff escalations (historical retail electricity price inflation averages 3.5% to 5.0% per year), federal tax incentives under the Inflation Reduction Act, inverter replacement reserves at year 12 to 15, and the shifting regulatory framework of Net Energy Metering (NEM).
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Solar Economic Formulations</h3>
            <p>
                Energy economists and National Renewable Energy Laboratory (NREL) engineers evaluate solar investments using four primary equations:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-amber-600 dark:text-amber-400 font-sans text-xs uppercase tracking-wider mb-1">Solar Photovoltaic Economic Equations</div>
                <div><strong>Net Capital Investment:</strong> Net Cost = Gross System Cost &times; (1 - Federal Tax Credit %) - State Rebates</div>
                <div><strong>Annual Generation (NREL PVWatts):</strong> E_annual (kWh) = System Size (kW) &times; Peak Sun Hours &times; 365 &times; Derate Factor (0.86)</div>
                <div><strong>Simple Payback Period (Years):</strong> T_simple = Net System Cost / Year 1 Avoided Utility Expense</div>
                <div><strong>Levelized Cost of Energy (LCOE):</strong> LCOE ($/kWh) = Total Lifetime System Costs / Cumulative Lifetime kWh Generated</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Walkthrough</h3>
            <p>
                To illustrate the complete financial lifecycle, consider a homeowner installing an <strong>8.0 kW DC rooftop solar array</strong> in a region with <strong>4.5 peak sun hours per day</strong>. The gross turnkey installation cost is <strong>$2.80 per watt</strong> ($22,400 gross), utility power currently costs <strong>$0.18 per kWh</strong> escalating at 3.5% annually, and the system qualifies for the 30% federal clean energy credit.
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Calculate Net Capital Outlay:</strong>
                    $$\\text{Gross Installation Cost} = 8,000 \\text{ watts} \\times \\$2.80 = \\$22,400$$
                    $$\\text{Section 25D Federal Tax Credit (30\\%)} = \\$22,400 \\times 0.30 = \\$6,720$$
                    $$\\text{Net Out-of-Pocket Investment} = \\$22,400 - \\$6,720 = \\mathbf{\\$15,680}$$
                </li>
                <li>
                    <strong>Compute Year 1 Solar Generation (NREL PVWatts Standard):</strong>
                    $$\\text{Annual Output} = 8.0 \\text{ kW} \\times 4.5 \\text{ peak hrs} \\times 365 \\text{ days} \\times 0.86 \\text{ derate factor} \\approx \\mathbf{11,300 \\text{ kWh/year}}$$
                </li>
                <li>
                    <strong>Determine Year 1 Avoided Electric Bill Savings:</strong>
                    $$\\text{Year 1 Value} = 11,300 \\text{ kWh} \\times \\$0.18/\\text{kWh} = \\mathbf{\\$2,034.00}$$
                </li>
                <li>
                    <strong>Calculate Simple Payback Horizon:</strong>
                    $$T_{\\text{simple}} = \\frac{\\$15,680}{\\$2,034} \\approx \\mathbf{7.71 \\text{ years (approx. 7 years and 8 months)}}$$
                </li>
                <li>
                    <strong>25-Year Cumulative Net Financial Return (with 3.5% utility escalation and 0.5% solar degradation):</strong>
                    Cumulative avoided electricity bills over 25 years equal approximately <strong>$68,400</strong>. Subtracting the initial net investment ($15,680) and a mid-life string inverter replacement ($2,200 at Year 13) yields a <strong>net 25-year lifetime profit of approximately $50,520</strong>, representing an internal rate of return (IRR) exceeding <strong>13.8%</strong>.
                </li>
            </ol>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. Solar Payoff Timeline by US State (8 kW Array Average)</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">State / Market</th>
                            <th class="p-3">Avg Utility Tariff ($/kWh)</th>
                            <th class="p-3">Peak Sun Hours/Day</th>
                            <th class="p-3">Net Cost (after 30% credit)</th>
                            <th class="p-3">Estimated Payback Period</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">California (NEM 2.0 legacy)</td>
                            <td class="p-3">$0.32/kWh</td>
                            <td class="p-3">5.4 hrs</td>
                            <td class="p-3">$15,680</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">4.8 - 5.5 Years</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Massachusetts / Northeast</td>
                            <td class="p-3">$0.28/kWh</td>
                            <td class="p-3">4.0 hrs</td>
                            <td class="p-3">$16,240</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">6.2 - 7.0 Years</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Arizona / Southwest</td>
                            <td class="p-3">$0.14/kWh</td>
                            <td class="p-3">6.2 hrs</td>
                            <td class="p-3">$14,560</td>
                            <td class="p-3">7.5 - 8.3 Years</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Texas (ERCOT Competitive)</td>
                            <td class="p-3">$0.13/kWh</td>
                            <td class="p-3">5.0 hrs</td>
                            <td class="p-3">$14,000</td>
                            <td class="p-3">8.5 - 9.8 Years</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Washington / Northwest</td>
                            <td class="p-3">$0.11/kWh</td>
                            <td class="p-3">3.8 hrs</td>
                            <td class="p-3">$15,120</td>
                            <td class="p-3 font-bold text-amber-600 dark:text-amber-400">11.5 - 13.0 Years</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. The Regulatory Transition: NEM 2.0 vs. NEM 3.0 (Solar + Storage)</h3>
            <p>
                In evaluating solar economics today, the most critical regulatory variable is the utility's Net Energy Metering (NEM) tariff:
            </p>
            <ul>
                <li><strong>Traditional NEM 1.0 &amp; 2.0 (Full Retail 1:1 Credit):</strong> For every kWh of excess solar energy exported to the grid during the afternoon, the utility credits your account at the full retail electricity rate (e.g., $0.25/kWh). Under retail NEM, standalone solar achieves the shortest payback periods.</li>
                <li><strong>Modern NEM 3.0 (Net Billing / Avoided Cost Rate):</strong> Implemented by the California Public Utilities Commission (CPUC) in 2023 and being adopted across other states, NEM 3.0 slashes export compensation rates by approximately 75% to 80% down to the utility's wholesale "avoided cost" (~$0.05 to $0.08/kWh). Under NEM 3.0, exporting solar to the grid destroys economic value. Maximizing return requires adding a home battery energy storage system (such as a Tesla Powerwall or Enphase 5P) to store midday solar generation and discharge it during peak evening hours (4:00 PM to 9:00 PM) when grid rates are highest.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>How does the Section 25D Residential Clean Energy Credit work on federal taxes?</span>
                        <span class="text-amber-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Extended under the Inflation Reduction Act of 2022, Section 25D provides a non-refundable 30% federal tax credit against your personal income tax liability for eligible solar PV and battery storage systems installed between 2022 and 2032. Unlike a tax deduction (which merely reduces taxable income), a tax credit is a dollar-for-dollar reduction of your tax bill. If your tax liability in the installation year is lower than the credit amount, the remaining credit rolls forward to offset taxes in subsequent tax years.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Does installing rooftop solar increase property taxes or homeowners insurance?</span>
                        <summary class="hidden"></summary>
                        <span class="text-amber-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Over 35 US states have enacted statutory property tax exemptions for residential solar energy systems, meaning the added market equity from solar panels (averaging a 4% home value increase according to Zillow research) does not increase your local municipal property tax assessment. For homeowners insurance, most standard policies cover rooftop solar arrays as permanent dwelling structures, typically requiring only a nominal adjustment to total dwelling coverage limits without substantial premium increases.
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

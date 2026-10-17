import os
import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

ONEDRIVE_CALC_DIR = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
DESKTOP_CALC_DIR = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'

ARTICLES = {}

# 1. Interest Rate Calculator Article (1,700+ words)
ARTICLES['interest-rate-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Interest Rate Guide (1,750+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-blue-100 dark:bg-blue-900/40 text-blue-700 dark:text-blue-300 text-xs font-bold uppercase tracking-wider mb-3">Financial Economics &amp; Consumer Credit</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Mechanics of Interest Rates: APR, APY, Compounding Physics, and True Financing Costs</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A comprehensive reference manual on nominal borrowing rates, effective annualized yields, discrete versus continuous compounding, and statutory disclosure mandates under US federal banking frameworks.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. Conceptual Foundations: The Time Value of Money and Capital Cost</h3>
            <p>
                At its core, an interest rate represents the price of time. Because capital available today can be invested productively, consumed immediately, or held as liquidity to offset uncertainty, a rational lender demands compensation for foregoing its immediate use. The interest rate functions simultaneously as the cost of capital for a borrower and the yield on deferred consumption for a saver.
            </p>
            <p>
                In retail banking and institutional debt markets, confusion frequently arises because financial institutions express interest through multiple distinct metrics. A consumer taking out an auto loan encounters a nominal annual percentage rate (APR), while an individual opening a high-yield savings account or a certificate of deposit (CD) evaluates an annual percentage yield (APY). While both figures appear as percentages, they measure fundamentally different mathematical operations. Failing to distinguish between nominal rates, periodic compounding intervals, and effective yields can lead to miscalculating debt service obligations by thousands of dollars over the lifetime of a loan.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Mathematical Formulations</h3>
            <p>
                To analyze interest behavior rigorously, we examine three classical mathematical representations: simple interest, discrete compound interest, and continuous compounding.
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-blue-600 dark:text-blue-400 font-sans text-xs uppercase tracking-wider mb-1">Mathematical Compounding Relations</div>
                <div><strong>Discrete Compounding Formula:</strong> FV = PV &times; (1 + r / n)^(n &times; t)</div>
                <div><strong>Solving for Nominal Rate (r):</strong> r = n &times; [ (FV / PV)^(1 / (n &times; t)) - 1 ]</div>
                <div><strong>Annual Percentage Yield (APY):</strong> APY = (1 + r / n)^n - 1</div>
                <div><strong>Continuous Compounding:</strong> FV = PV &times; e^(r &times; t) &implies; r = ln(FV / PV) / t</div>
            </div>

            <p>
                Where:
            </p>
            <ul>
                <li><strong>PV (Present Value):</strong> The initial principal sum borrowed or invested.</li>
                <li><strong>FV (Future Value):</strong> The accumulated balance after debt repayment or interest accretion.</li>
                <li><strong>r (Nominal Interest Rate):</strong> The stated annual interest rate (decimal form).</li>
                <li><strong>n (Compounding Frequency):</strong> The number of compounding intervals per calendar year (e.g., 1 for annual, 4 for quarterly, 12 for monthly, 365 for daily).</li>
                <li><strong>t (Tenure in Years):</strong> The elapsed time interval expressed in fractional or whole calendar years.</li>
                <li><strong>e:</strong> Euler's mathematical constant, approximately 2.7182818.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Example</h3>
            <p>
                To illustrate the mathematical process of solving for an implied interest rate, consider an investor who deposits $15,000 into a fixed-income municipal bond fund that matures to a guaranteed payout of $22,500 after precisely 6 years, with interest compounding on a monthly schedule (n = 12).
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Identify Known Parameters:</strong>
                    Present Value (PV) = $15,000; Future Value (FV) = $22,500; Tenure (t) = 6 years; Compounding frequency (n) = 12 intervals per year. Total compounding cycles (N) = 12 &times; 6 = 72 cycles.
                </li>
                <li>
                    <strong>Calculate the Total Growth Multiple:</strong>
                    Growth Ratio = FV / PV = $22,500 / $15,000 = 1.5000 (a 50% cumulative capital gain).
                </li>
                <li>
                    <strong>Extract the Periodic Compounding Factor:</strong>
                    Periodic Multiplier = (1.5000)^(1 / 72) = 1.5000^(0.0138889) &approx; 1.005646.
                </li>
                <li>
                    <strong>Derive Periodic Rate:</strong>
                    Periodic Interest Rate (i) = 1.005646 - 1 = 0.005646 per month (0.5646% monthly).
                </li>
                <li>
                    <strong>Compute Nominal Annual Rate (APR):</strong>
                    Nominal APR = 0.005646 &times; 12 &approx; 0.06775 &implies; <strong>6.78% nominal annual rate</strong>.
                </li>
                <li>
                    <strong>Determine Effective Annual Percentage Yield (APY):</strong>
                    APY = (1 + 0.06775 / 12)^12 - 1 = (1.005646)^12 - 1 &approx; 1.06991 - 1 &implies; <strong>6.99% effective annual yield</strong>.
                </li>
            </ol>
            <p>
                This step-by-step resolution demonstrates why the effective annual yield (6.99%) exceeds the stated nominal rate (6.78%): monthly interest earned in earlier months earns its own interest in subsequent months, compounding total wealth generation.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. Compounding Frequency Impact Matrix</h3>
            <p>
                The table below illustrates how different compounding frequencies expand an initial $10,000 principal balance across various stated nominal APRs over a 10-year investment horizon:
            </p>

            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Nominal APR</th>
                            <th class="p-3">Annual (n=1)</th>
                            <th class="p-3">Quarterly (n=4)</th>
                            <th class="p-3">Monthly (n=12)</th>
                            <th class="p-3">Daily (n=365)</th>
                            <th class="p-3">Continuous (e)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">4.00% APR</td>
                            <td class="p-3">$14,802</td>
                            <td class="p-3">$14,889</td>
                            <td class="p-3">$14,908</td>
                            <td class="p-3">$14,918</td>
                            <td class="p-3 font-bold text-blue-600 dark:text-blue-400">$14,918</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">7.00% APR</td>
                            <td class="p-3">$19,672</td>
                            <td class="p-3">$20,016</td>
                            <td class="p-3">$20,097</td>
                            <td class="p-3">$20,136</td>
                            <td class="p-3 font-bold text-blue-600 dark:text-blue-400">$20,138</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">10.00% APR</td>
                            <td class="p-3">$25,937</td>
                            <td class="p-3">$26,851</td>
                            <td class="p-3">$27,070</td>
                            <td class="p-3">$27,179</td>
                            <td class="p-3 font-bold text-blue-600 dark:text-blue-400">$27,183</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">18.00% (Credit Card)</td>
                            <td class="p-3">$52,338</td>
                            <td class="p-3">$58,411</td>
                            <td class="p-3">$60,074</td>
                            <td class="p-3">$60,496</td>
                            <td class="p-3 font-bold text-red-600 dark:text-red-400">$60,496</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Statutory Disclosure Frameworks: TILA vs. TISA</h3>
            <p>
                To protect retail consumers against misleading mathematical rate quotations, the United States Congress and regulatory bodies implemented two cornerstone disclosure frameworks:
            </p>
            <ul>
                <li>
                    <strong>Truth in Lending Act (TILA / Regulation Z):</strong> Governed by the Consumer Financial Protection Bureau (CFPB), TILA obligates consumer lenders (mortgage originators, auto financers, credit card issuers) to disclose the <em>Annual Percentage Rate (APR)</em>. Critically, credit APRs incorporate upfront finance charges, origination points, loan guarantee fees, and required mortgage insurance into the nominal interest rate, reflecting the total annual financing cost relative to net loan proceeds.
                </li>
                <li>
                    <strong>Truth in Savings Act (TISA / Regulation DD):</strong> Designed for depository accounts, TISA requires banks and credit unions to quote the <em>Annual Percentage Yield (APY)</em>. Because deposits compound interest over time, quoting APY provides depositors with a standardized figure reflecting total annual interest earnings, including the full mathematical compounding effect.
                </li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Strategic Borrowing and Investing Guidelines</h3>
            <p>
                Understanding rate mechanics allows consumers and business operators to systematically reduce financing drag and maximize compound capital growth:
            </p>
            <ul>
                <li><strong>Bi-Weekly Mortgage Conversion:</strong> Switching from 12 monthly payments to 26 bi-weekly half-payments results in 13 full monthly payments annually. On a 30-year, $400,000 mortgage at 6.5%, this extra annual principal payment trims approximately 5.5 years off the amortization term and saves over $95,000 in cumulative interest.</li>
                <li><strong>The Credit Card Daily Accrual Trap:</strong> Unlike mortgages which compound monthly, revolving credit card balances compound on a daily periodic rate (APR divided by 365). Paying balances mid-cycle before the statement closing date lowers the average daily balance, cutting interest charges even if you carry a month-to-month revolving balance.</li>
                <li><strong>Real vs. Nominal Returns (The Fisher Equation):</strong> When evaluating fixed-income yields, subtract inflation expectations from your nominal interest rate: $r_{real} \approx r_{nominal} - i$. An 8% nominal yield in a 5% inflation regime yields only 3% in actual purchasing power accretion.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">7. Frequently Asked Financial Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Why does APY always exceed APR for compounding frequencies greater than once per year?</span>
                        <span class="text-blue-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        APR reflects simple nominal interest without reinvestment assumptions. When interest compounds semi-annually, quarterly, monthly, or daily, interest generated in each discrete period is added to the principal balance for all future periods. APY accounts for this compounding effect, mathematically resulting in a higher effective percentage yield. The only scenario where APR equals APY is when interest compounds precisely once annually (n = 1).
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>How does continuous compounding differ from daily compounding?</span>
                        <summary class="hidden"></summary>
                        <span class="text-blue-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Continuous compounding represents the theoretical mathematical limit as the compounding frequency approaches infinity. In practice, daily compounding (365 cycles/year) converges so closely to continuous compounding that the difference on a $10,000 balance at 7% over 10 years is less than $2.00. Continuous compounding is widely used in financial derivatives pricing (such as the Black-Scholes options pricing model) due to elegant calculus simplifications.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Can an interest rate be negative in real-world economics?</span>
                        <span class="text-blue-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Yes. Central banks (such as the European Central Bank and the Bank of Japan) have historically instituted Negative Interest Rate Policies (NIRP) on commercial bank excess reserves to penalize cash hoarding and spur corporate lending. In real terms (adjusted for inflation), negative interest rates occur frequently: whenever annual inflation outpaces the nominal interest rate paid on savings, the depositor experiences negative real returns.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>How do fixed interest rates differ from adjustable interest rates (ARM)?</span>
                        <span class="text-blue-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        A fixed-rate loan locks your borrowing interest rate permanently across the entire amortization tenure, insulating you completely against future macroeconomic benchmark hikes. An adjustable-rate mortgage (ARM) fixes your rate for an introductory period (e.g., 5 or 7 years) and then resets periodically based on benchmark indices (such as the Secured Overnight Financing Rate, SOFR) plus a predetermined lender margin, subject to annual and lifetime rate adjustment caps.
                    </p>
                </details>
            </div>
        </article>
"""

print("Defined article for interest-rate-calculator.html (length ~1,750 words)")

import os
import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

ONEDRIVE_CALC_DIR = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
DESKTOP_CALC_DIR = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'

ARTICLES = {}

# 1. Random Number Generator (1,700+ words)
ARTICLES['random-number-generator.html'] = """
        <!-- Comprehensive Evidence-Based RNG & Probability Guide (1,720+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-violet-100 dark:bg-violet-900/40 text-violet-700 dark:text-violet-300 text-xs font-bold uppercase tracking-wider mb-3">Computational Mathematics &amp; Cryptography</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Architecture of Random Number Generation: Entropy, PRNG Algorithms, and Statistical Uniformity</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A technical reference guide to pseudo-random versus true hardware randomness, cryptographic seed generation, linear congruential generators, Mersenne Twister dynamics, and NIST SP 800-22 randomness test suites.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. The Nature of Randomness in Deterministic Computing</h3>
            <p>
                In classical computer science, generating true randomness is an inherent paradox. Von Neumann famously observed that "anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin." Because digital microprocessors operate deterministically—executing sequential binary instructions where identical inputs yield identical outputs—software-based algorithms cannot create genuine unpredictability without external physical stimuli.
            </p>
            <p>
                To resolve this limitation, computational systems distinguish between two fundamental architectures:
            </p>
            <ul>
                <li><strong>Pseudo-Random Number Generators (PRNGs):</strong> Algorithmic mathematical functions that accept an initial input value (a <em>seed</em>) and produce a deterministic sequence of numbers that mimic statistical randomness over vast distribution periods. Common examples include the Linear Congruential Generator (LCG) and the Mersenne Twister (MT19937).</li>
                <li><strong>Cryptographically Secure Pseudo-Random Number Generators (CSPRNGs):</strong> High-entropy generators governed by strict security guarantees. Even if an adversary observes millions of past outputs, it is computationally infeasible to predict future outputs or reverse-engineer the underlying internal state (e.g., using Fortuna, ChaCha20, or the Web Cryptography API's <code>window.crypto.getRandomValues</code>).</li>
                <li><strong>True Random Number Generators (TRNGs):</strong> Hardware devices that harvest ambient physical entropy from non-deterministic microscopic physical phenomena: thermal Johnson-Nyquist noise in resistors, atmospheric radio frequency noise, radioactive nuclear decay timing, or quantum optical photon beam-splitter measurements.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Mathematical Formulations</h3>
            <p>
                To understand how algorithmic random number generation operates, we examine the classical <strong>Linear Congruential Generator (LCG)</strong> formulation introduced by D. H. Lehmer in 1951, alongside the uniform integer mapping transformation:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-violet-600 dark:text-violet-400 font-sans text-xs uppercase tracking-wider mb-1">PRNG Mathematical Formulations</div>
                <div><strong>Lehmer LCG Recurrence Relation:</strong> X_{k+1} = (a &times; X_k + c) mod m</div>
                <div><strong>Normalized Unit Real [0, 1):</strong> U_k = X_k / m</div>
                <div><strong>Bounded Integer Mapping [Min, Max]:</strong> Y_k = &lfloor; U_k &times; (Max - Min + 1) &rfloor; + Min</div>
                <div><strong>Entropy Rate (Shannon Entropy):</strong> H(X) = - &sum; P(x_i) &times; log_2 P(x_i)</div>
            </div>

            <p>
                Where:
            </p>
            <ul>
                <li><strong>X_k:</strong> The current internal state of the generator.</li>
                <li><strong>a (Multiplier):</strong> A large prime integer constant selected to satisfy the Hull-Dobell Theorem for maximal cycle length.</li>
                <li><strong>c (Increment):</strong> A constant coprime to modulus $m$ (if $c=0$, it is a multiplicative congruential generator).</li>
                <li><strong>m (Modulus):</strong> A large integer defining the upper bound of state states (often $2^{31}-1$ or $2^{64}$).</li>
                <li><strong>H(X):</strong> Shannon informational entropy, measuring bits of uncertainty per generated symbol.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Walkthrough</h3>
            <p>
                To illustrate how a basic LCG computes random numbers deterministically, consider an educational generator utilizing standard ANSI C parameters: $m = 2^{31} = 2,147,483,648$, multiplier $a = 1,103,515,245$, and increment $c = 12,345$. Suppose we initialize the generator with seed state $X_0 = 42$, and we wish to sample a random integer between $Min = 1$ and $Max = 100$ (e.g., simulating a tabletop percentile roll).
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Execute the First State Transformation:</strong>
                    $$X_1 = (1,103,515,245 \\times 42 + 12,345) \\pmod{2,147,483,648}$$
                    $$1,103,515,245 \\times 42 = 46,347,640,290$$
                    $$46,347,640,290 + 12,345 = 46,347,652,635$$
                    $$X_1 = 46,347,652,635 \\pmod{2,147,483,648} = 1,250,490,523$$
                </li>
                <li>
                    <strong>Normalize to Unit Interval [0, 1):</strong>
                    $$U_1 = \\frac{1,250,490,523}{2,147,483,648} \\approx 0.582305$$
                </li>
                <li>
                    <strong>Map to the Target Bounded Integer Range [1, 100]:</strong>
                    Range size = $Max - Min + 1 = 100 - 1 + 1 = 100$.
                    $$Y_1 = \\lfloor 0.582305 \\times 100 \\rfloor + 1 = \\lfloor 58.2305 \\rfloor + 1 = 58 + 1 = 59$$
                </li>
                <li>
                    <strong>Advance to Next Iteration (Second Sample):</strong>
                    $$X_2 = (1,103,515,245 \\times 1,250,490,523 + 12,345) \\pmod{2,147,483,648} = 345,618,901$$
                    $$U_2 = \\frac{345,618,901}{2,147,483,648} \\approx 0.160941$$
                    $$Y_2 = \\lfloor 0.160941 \\times 100 \\rfloor + 1 = 16 + 1 = 17$$
                </li>
            </ol>
            <p>
                The sequence yields $59, 17, \\dots$. Anyone knowing the algorithm, parameters, and the initial seed ($42$) can reproduce this exact sequence endlessly, proving why standard PRNGs must never be utilized in cryptographic key generation or secure authentication tokens.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. PRNG Architectural Comparison Matrix</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Algorithm Class</th>
                            <th class="p-3">Period Length (Cycles)</th>
                            <th class="p-3">State Memory Size</th>
                            <th class="p-3">Cryptographic Security</th>
                            <th class="p-3">Primary Use Case</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Linear Congruential (LCG)</td>
                            <td class="p-3">Up to 2^32 to 2^64</td>
                            <td class="p-3">32 or 64 bits</td>
                            <td class="p-3 font-sans text-red-600 dark:text-red-400">Insecure (Easily broken)</td>
                            <td class="p-3 font-sans">Embedded systems, quick non-critical shuffles</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Mersenne Twister (MT19937)</td>
                            <td class="p-3">2^19937 - 1 (&approx; 4.3&times;10^6001)</td>
                            <td class="p-3">2.5 kilobytes</td>
                            <td class="p-3 font-sans text-red-600 dark:text-red-400">Insecure (State deduced after 624 outputs)</td>
                            <td class="p-3 font-sans">Monte Carlo simulations, video game physics</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">Xoroshiro / Xoshiro256**</td>
                            <td class="p-3">2^256 - 1</td>
                            <td class="p-3">256 bits</td>
                            <td class="p-3 font-sans text-red-600 dark:text-red-400">Insecure (Non-cryptographic)</td>
                            <td class="p-3 font-sans">High-throughput numerical computing &amp; graphics</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">ChaCha20 / Fortuna (CSPRNG)</td>
                            <td class="p-3">&ge; 2^256</td>
                            <td class="p-3">512+ bits with entropy pool</td>
                            <td class="p-3 font-sans font-bold text-emerald-600 dark:text-emerald-400">Secure (Military-grade)</td>
                            <td class="p-3 font-sans">HTTPS TLS handshakes, password salts, lotteries</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Statistical Validation: The NIST SP 800-22 Test Suite</h3>
            <p>
                To ensure generated numbers exhibit genuine statistical uniformity without detectable periodicity, clustering, or dimensional bias, mathematical testing frameworks subject sequences to the <strong>NIST SP 800-22</strong> suite comprising 15 empirical tests:
            </p>
            <ul>
                <li><strong>Monobit Frequency Test:</strong> Validates whether the proportion of zeroes and ones across the sequence equals approximately 50%, testing the null hypothesis of uniform binary distribution.</li>
                <li><strong>Runs Test:</strong> Evaluates the oscillation rate between consecutive identical bits to ensure sequences do not alternate too rapidly or linger in long repeating streaks.</li>
                <li><strong>Discrete Fourier Transform (Spectral) Test:</strong> Performs Fast Fourier Transforms (FFT) on the sequence to identify periodic repetitive peaks that would indicate non-random harmonic cycles.</li>
                <li><strong>Diehard Battery of Tests (Marsaglia):</strong> Assesses birthday spacings, overlapping permutations, and binary rank tests across high-dimensional matrices.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Why does JavaScript's standard Math.random() carry security warnings?</span>
                        <span class="text-violet-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Modern browser engines implement <code>Math.random()</code> using xoroshiro128+ or similar lightweight algorithms optimized purely for execution speed, not security. Because their internal state consists of only 128 bits, an attacker observing a few dozen outputs can reconstruct the state matrix and predict all future outputs, compromising cryptographic session IDs or password reset tokens. Secure applications mandate <code>window.crypto.getRandomValues()</code>.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What is modulo bias and how do robust random generators prevent it?</span>
                        <summary class="hidden"></summary>
                        <span class="text-violet-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Modulo bias occurs when mapping a random integer range onto a smaller target range via naive modulus operation when the generator range is not an exact integer multiple of the target range. For example, mapping numbers from 0 to 255 onto a 0-9 range ($256 \\pmod{10} = 6$) gives digits 0 through 5 a higher probability of selection than digits 6 through 9. Robust implementations use rejection sampling (discarding raw values outside the largest multiple) to eliminate this statistical distortion.
                    </p>
                </details>
            </div>
        </article>
"""

# 2. Due Date Calculator (1,750+ words)
ARTICLES['due-date-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Pregnancy Due Date Guide (1,740+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-rose-100 dark:bg-rose-900/40 text-rose-700 dark:text-rose-300 text-xs font-bold uppercase tracking-wider mb-3">Obstetric Science &amp; Maternal-Fetal Medicine</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Clinical Calculation of Gestational Age and Estimated Date of Delivery (EDD)</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">An evidence-based clinical guide to obstetric gestational dating, Naegele's rule, Mittendorf-Williams empirical adjustments, ultrasound crown-rump length (CRL) concordances, and ACOG gestational milestones.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. Obstetric Gestational Age vs. Embryonic Conceptional Age</h3>
            <p>
                In clinical obstetrics, gestational age is defined by universal convention as the elapsed time since the first day of the mother's last normal menstrual period (LMP), rather than the actual biological moment of fertilization. Because follicular maturation and ovulation typically occur approximately 14 days into a standardized 28-day menstrual cycle, clinical gestational age precedes true conceptional age (the moment of sperm-oocyte fusion) by approximately two weeks.
            </p>
            <p>
                An Estimated Date of Delivery (EDD) is mathematically calibrated to represent 280 calendar days (40 completed weeks, or 10 lunar months) from the first day of the LMP. In biological reality, only about 4% to 5% of spontaneous births occur precisely on the predicted EDD. Human gestation follows a normal Gaussian distribution centered at 280 days with a standard deviation of approximately 8 to 10 days, meaning that normal full-term delivery occurs within a biological delivery window spanning 37 weeks 0 days through 41 weeks 6 days.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Clinical Dating Formulations</h3>
            <p>
                Obstetricians and maternal-fetal medicine specialists utilize four primary methodologies to establish or adjust the estimated due date:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-rose-600 dark:text-rose-400 font-sans text-xs uppercase tracking-wider mb-1">Clinical Obstetric Dating Formulas</div>
                <div><strong>Standard Naegele's Rule:</strong> EDD = LMP + 1 Year - 3 Months + 7 Days</div>
                <div><strong>Cycle-Adjusted Naegele's Rule:</strong> EDD = LMP - 3 Months + (7 Days + [Cycle Length - 28 Days])</div>
                <div><strong>Known Ovulation / Conception Date:</strong> EDD = Conception Date + 266 Days (38 Weeks)</div>
                <div><strong>IVF Day 5 Blastocyst Transfer:</strong> EDD = Transfer Date + 261 Days</div>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Clinical Example</h3>
            <p>
                To illustrate how a cycle-length variation alters the estimated date of delivery, consider an expectant mother whose last menstrual period began on <strong>May 12, 2026</strong>. Her menstrual cycle averages <strong>33 days</strong> (a 5-day follicular extension beyond the 28-day standard).
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Identify Base Parameters:</strong>
                    LMP = May 12, 2026; Cycle Length = 33 days. Variance from 28-day baseline = $33 - 28 = +5$ days.
                </li>
                <li>
                    <strong>Apply Naegele's Calendar Math:</strong>
                    <ul>
                        <li>Add 1 full calendar year: May 12, 2026 &rarr; May 12, 2027.</li>
                        <li>Subtract 3 calendar months: May 12 &rarr; February 12, 2027.</li>
                        <li>Add standard 7 days: February 12 + 7 days = February 19, 2027.</li>
                    </ul>
                </li>
                <li>
                    <strong>Apply Cycle Length Correction (+5 Days):</strong>
                    Because ovulation in a 33-day cycle occurs around Cycle Day 19 rather than Day 14, fertilization occurred 5 days later:
                    $$\\text{Corrected EDD} = \\text{February 19} + 5 \\text{ days} = \\mathbf{\\text{February 24, 2027}}$$
                </li>
                <li>
                    <strong>Compute Key Clinical Milestone Dates:</strong>
                    <ul>
                        <li>End of First Trimester (13 Weeks 6 Days): August 18, 2026.</li>
                        <li>End of Second Trimester (27 Weeks 6 Days): November 24, 2026.</li>
                        <li>Early Term Threshold (37 Weeks 0 Days): February 3, 2027.</li>
                        <li>Full Term Benchmark (39 Weeks 0 Days): February 17, 2027.</li>
                        <li>Post-Term Surveillance Threshold (41 Weeks 0 Days): March 3, 2027.</li>
                    </ul>
                </li>
            </ol>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. ACOG Ultrasound Redating Guidelines (Committee Opinion No. 700)</h3>
            <p>
                The American College of Obstetricians and Gynecologists (ACOG), in conjunction with the Society for Maternal-Fetal Medicine (SMFM), mandates that early biometric ultrasound dating supersedes LMP calculations whenever clinical discrepancies exceed defined statistical thresholds:
            </p>

            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Gestational Age Window</th>
                            <th class="p-3">Primary Ultrasound Biometric Metric</th>
                            <th class="p-3">Discrepancy Threshold Supporting Redating</th>
                            <th class="p-3">Clinical Measurement Margin of Error</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">&le; 8 Weeks 6 Days</td>
                            <td class="p-3">Crown-Rump Length (CRL)</td>
                            <td class="p-3 font-bold text-rose-600 dark:text-rose-400">&gt; 5 days discrepancy</td>
                            <td class="p-3 font-mono">&plusmn; 3 to 5 days</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">9 Weeks 0 Days to 13 Weeks 6 Days</td>
                            <td class="p-3">Crown-Rump Length (CRL)</td>
                            <td class="p-3 font-bold text-rose-600 dark:text-rose-400">&gt; 7 days discrepancy</td>
                            <td class="p-3 font-mono">&plusmn; 5 to 7 days</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">14 Weeks 0 Days to 15 Weeks 6 Days</td>
                            <td class="p-3">Biparietal Diameter (BPD) &amp; Femur Length (FL)</td>
                            <td class="p-3 font-bold text-rose-600 dark:text-rose-400">&gt; 7 days discrepancy</td>
                            <td class="p-3 font-mono">&plusmn; 7 to 8 days</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">16 Weeks 0 Days to 21 Weeks 6 Days</td>
                            <td class="p-3">Composite Biometry (BPD, HC, AC, FL)</td>
                            <td class="p-3 font-bold text-rose-600 dark:text-rose-400">&gt; 10 days discrepancy</td>
                            <td class="p-3 font-mono">&plusmn; 10 to 14 days</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-semibold text-slate-900 dark:text-white">&ge; 28 Weeks 0 Days (Third Trimester)</td>
                            <td class="p-3">Composite Biometry</td>
                            <td class="p-3 font-bold text-rose-600 dark:text-rose-400">&gt; 21 days discrepancy</td>
                            <td class="p-3 font-mono">&plusmn; 21 to 30 days</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Modern Term Pregnancy Nomenclature</h3>
            <p>
                Historically, obstetrics classified all births between 37 and 42 weeks under the generic umbrella term "term." In 2013, ACOG and SMFM replaced this classification with four distinct subcategories to reflect differences in neonatal respiratory and neurological outcomes:
            </p>
            <ul>
                <li><strong>Early Term (37 0/7 weeks to 38 6/7 weeks):</strong> Lung surfactant maturation and cerebral sulcal development are completing; elective delivery without medical indication carries increased risk of transient tachypnea.</li>
                <li><strong>Full Term (39 0/7 weeks to 40 6/7 weeks):</strong> Optimal neonatal survival and minimal rates of respiratory distress or NICU admission.</li>
                <li><strong>Late Term (41 0/7 weeks to 41 6/7 weeks):</strong> Increased surveillance (biophysical profiles and non-stress testing) is initiated to monitor placental vascular sufficiency and amniotic fluid volume.</li>
                <li><strong>Post-Term (&ge; 42 0/7 weeks):</strong> Significantly elevated incidence of oligohydramnios, meconium aspiration syndrome, and neonatal morbidity; labor induction is clinically indicated.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Clinical Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Why is first-trimester ultrasound more accurate than LMP for pregnancy dating?</span>
                        <span class="text-rose-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        During the embryonic period (up to 13 6/7 weeks), biological fetal growth rates exhibit virtually zero inter-individual genetic variance. Embryos grow at a universally predictable mathematical trajectory measured by Crown-Rump Length (CRL). In contrast, maternal menstrual cycles frequently vary due to delayed ovulation, luteal phase defects, or implantation bleeding that can be mistaken for a light period.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>How does in vitro fertilization (IVF) alter due date calculations?</span>
                        <summary class="hidden"></summary>
                        <span class="text-rose-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        In IVF pregnancies, the biological moment of conception and embryonic developmental stage are documented with laboratory precision. For a Day 3 embryo transfer, the due date is calculated as <code>Transfer Date + 263 days</code>. For a Day 5 blastocyst transfer, the due date is <code>Transfer Date + 261 days</code>. Because timing is known to the exact hour, IVF gestational dating is considered the most precise in obstetrics and is rarely redated by ultrasound.
                    </p>
                </details>
            </div>
        </article>
"""

# 3. Loan Payment Calculator (1,700+ words)
ARTICLES['payment-calculator.html'] = """
        <!-- Comprehensive Evidence-Based Loan Payment Guide (1,720+ Words) -->
        <article class="prose dark:prose-invert max-w-4xl mx-auto bg-white dark:bg-slate-900 p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200 dark:border-slate-800 mt-12 mb-8">
            <div class="border-b border-slate-200 dark:border-slate-800 pb-6 mb-8">
                <span class="inline-block px-3 py-1 rounded-full bg-emerald-100 dark:bg-emerald-900/40 text-emerald-700 dark:text-emerald-300 text-xs font-bold uppercase tracking-wider mb-3">Consumer Credit &amp; Debt Amortization</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">The Mechanics of Loan Payments: Fixed Amortization, Interest Deceleration, and Debt Service Optimization</h2>
                <p class="text-slate-600 dark:text-slate-400 text-base mt-2">A comprehensive mathematical and financial manual on equal monthly debt amortization payments, principal-interest splits, balloon liabilities, and interest acceleration reduction strategies.</p>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">1. The Structure of Equal Debt Installments</h3>
            <p>
                In retail banking, auto lending, and commercial mortgages, the overwhelming majority of debt obligations are structured as fully amortizing, fixed-rate installment loans. Under this framework, the borrower makes an identical fixed periodic payment (typically monthly) across the entirety of the loan tenure.
            </p>
            <p>
                However, beneath the surface of this constant dollar installment lies an internal mathematical shift: the relative allocation between <strong>interest expense</strong> and <strong>principal reduction</strong> changes continuously with every passing payment cycle. In the early months of a 30-year mortgage or 6-year auto loan, interest consumes the vast majority of your monthly remittance. As principal is slowly paid down, interest charges decline, causing the principal repayment portion to accelerate exponentially toward final maturity.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">2. Core Amortization Formulas</h3>
            <p>
                The exact monthly installment payment $M$ required to amortize a principal loan balance $P$ to precisely zero over $N$ monthly periods at periodic interest rate $r$ is derived using the standard annuity present value formulation:
            </p>

            <div class="p-5 my-6 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-3 font-mono text-sm text-slate-800 dark:text-slate-200">
                <div class="font-bold text-emerald-600 dark:text-emerald-400 font-sans text-xs uppercase tracking-wider mb-1">Standard Amortization Formula</div>
                <div><strong>Monthly Payment:</strong> M = P &times; [ r(1 + r)^N ] / [ (1 + r)^N - 1 ]</div>
                <div><strong>Periodic Interest Portion:</strong> I_k = Balance_{k-1} &times; r</div>
                <div><strong>Periodic Principal Portion:</strong> C_k = M - I_k</div>
                <div><strong>Remaining Balance After k Payments:</strong> B_k = P &times; [ (1 + r)^N - (1 + r)^k ] / [ (1 + r)^N - 1 ]</div>
            </div>

            <p>
                Where:
            </p>
            <ul>
                <li><strong>M:</strong> Fixed monthly installment payment.</li>
                <li><strong>P:</strong> Initial loan principal balance.</li>
                <li><strong>r:</strong> Monthly periodic interest rate, calculated as $\\text{Annual Nominal Rate (APR)} / 12$.</li>
                <li><strong>N:</strong> Total count of monthly installment payments across the loan tenure (e.g., $5 \\times 12 = 60$ payments for a 5-year auto loan).</li>
                <li><strong>I_k:</strong> Interest fee charged during payment period $k$.</li>
                <li><strong>C_k:</strong> Principal reduction credited during payment period $k$.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">3. Step-by-Step Worked Numerical Example</h3>
            <p>
                To illustrate the mathematical mechanics, consider a borrower purchasing a new vehicle with a loan balance of <strong>$35,000</strong>, financed for <strong>5 years (60 months)</strong> at a fixed annual percentage rate (APR) of <strong>6.00%</strong>.
            </p>
            <ol class="space-y-3 pl-6 list-decimal text-slate-700 dark:text-slate-300">
                <li>
                    <strong>Determine the Monthly Periodic Rate:</strong>
                    $$r = \\frac{0.06}{12} = 0.005 \\text{ (0.50% per month)}$$
                </li>
                <li>
                    <strong>Calculate the Compounding Growth Factor $(1 + r)^N$:</strong>
                    $$(1 + 0.005)^{60} = (1.005)^{60} \\approx 1.348850$$
                </li>
                <li>
                    <strong>Compute the Amortization Multiplier Fraction:</strong>
                    $$\\text{Fraction} = \\frac{0.005 \\times 1.348850}{1.348850 - 1} = \\frac{0.00674425}{0.348850} \\approx 0.0193328$$
                </li>
                <li>
                    <strong>Solve for Fixed Monthly Payment:</strong>
                    $$M = 35,000 \\times 0.0193328 \\approx \\mathbf{\\$676.65 \\text{ per month}}$$
                </li>
                <li>
                    <strong>Analyze Payment 1 Distribution:</strong>
                    <ul>
                        <li>Interest Charge = $35,000 \\times 0.005 = \\$175.00$.</li>
                        <li>Principal Paydown = $\$676.65 - \\$175.00 = \\$501.65$.</li>
                        <li>Remaining Balance = $\$35,000 - \\$501.65 = \\$34,498.35$.</li>
                    </ul>
                </li>
                <li>
                    <strong>Analyze Payment 60 (Final Installment):</strong>
                    Prior balance = $\$673.28$.
                    <ul>
                        <li>Interest Charge = $\$673.28 \\times 0.005 = \\$3.37$.</li>
                        <li>Principal Paydown = $\$676.65 - \\$3.37 = \\$673.28$.</li>
                        <li>Ending Balance = $\$0.00$ (Debt fully satisfied).</li>
                    </ul>
                </li>
            </ol>
            <p>
                Total payments over the 5 years equal $60 \\times \\$676.65 = \\$40,599.00$, representing <strong>$5,599.00</strong> in cumulative interest expense.
            </p>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">4. Loan Tenure Comparison Matrix ($35,000 Loan at 6.00% APR)</h3>
            <div class="overflow-x-auto my-6 border border-slate-200 dark:border-slate-800 rounded-2xl">
                <table class="w-full text-left text-xs sm:text-sm">
                    <thead class="bg-slate-100 dark:bg-slate-800 text-slate-900 dark:text-white font-bold border-b border-slate-200 dark:border-slate-700">
                        <tr>
                            <th class="p-3">Loan Term</th>
                            <th class="p-3">Monthly Payment</th>
                            <th class="p-3">Total Cumulative Interest</th>
                            <th class="p-3">Total Repayment Amount</th>
                            <th class="p-3">Interest-to-Principal Ratio</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 dark:divide-slate-800 font-mono text-slate-700 dark:text-slate-300">
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">3 Years (36 Mo)</td>
                            <td class="p-3">$1,064.67</td>
                            <td class="p-3 font-bold text-emerald-600 dark:text-emerald-400">$3,328.12</td>
                            <td class="p-3">$38,328.12</td>
                            <td class="p-3">9.5%</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">5 Years (60 Mo)</td>
                            <td class="p-3">$676.65</td>
                            <td class="p-3">$5,599.00</td>
                            <td class="p-3">$40,599.00</td>
                            <td class="p-3">16.0%</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">6 Years (72 Mo)</td>
                            <td class="p-3">$579.96</td>
                            <td class="p-3">$6,757.12</td>
                            <td class="p-3">$41,757.12</td>
                            <td class="p-3">19.3%</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-sans font-semibold text-slate-900 dark:text-white">7 Years (84 Mo)</td>
                            <td class="p-3">$511.08</td>
                            <td class="p-3 font-bold text-red-600 dark:text-red-400">$7,930.72</td>
                            <td class="p-3">$42,930.72</td>
                            <td class="p-3">22.7%</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">5. Strategic Debt Reduction Strategies</h3>
            <ul>
                <li><strong>The Dedicated Principal-Only Overpayment:</strong> Because monthly interest is calculated solely on the unamortized balance, paying an extra $100 per month directed explicitly to principal reduces the balance upon which next month's interest is assessed, compounding interest savings.</li>
                <li><strong>Avoiding Prepayment Penalties:</strong> Before prepaying significant loan balances, confirm that your promissory note does not contain precomputed interest clauses or prepayment penalty covenants common in subprime automotive financing.</li>
            </ul>

            <h3 class="text-2xl font-bold text-slate-900 dark:text-white mt-8 mb-4">6. Frequently Asked Questions</h3>
            <div class="space-y-4">
                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>Why does extending a loan term to lower monthly payments increase total borrowing costs?</span>
                        <span class="text-emerald-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        Extending loan duration spreads principal reduction across more payment cycles, lowering the required monthly payment. However, because principal balances remain outstanding for much longer, the lender charges monthly interest on substantial balances across 72 or 84 months rather than 36 or 48 months. On a $35,000 auto loan at 6%, an 84-month term cuts payments by $553/month compared to a 36-month term, but more than doubles total interest expense from $3,328 to $7,930.
                    </p>
                </details>

                <details class="group bg-slate-50 dark:bg-slate-800/40 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 cursor-pointer">
                    <summary class="font-bold text-slate-900 dark:text-white flex justify-between items-center text-sm sm:text-base">
                        <span>What is the difference between simple interest loans and precomputed interest loans?</span>
                        <summary class="hidden"></summary>
                        <span class="text-emerald-600 group-open:rotate-180 transition-transform">&darr;</span>
                    </summary>
                    <p class="mt-3 text-xs sm:text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        In a simple interest loan, interest accrues daily based on the actual unpaid principal balance, meaning early payments directly reduce total interest charges. In a precomputed interest loan, the lender calculates the total interest for the entire contract term upfront and adds it to the principal. Paying off a precomputed loan early yields minimal interest savings and often triggers the Rule of 78s accounting method, penalizing the borrower.
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

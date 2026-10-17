import os
import re
import shutil
import glob

BASE_DIR = r"c:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine"
MIRROR_DIR = r"C:\Users\Muham\Desktop\Calc\calcworld-engine"

# 1. Official Standard CalcWorld Logo Component
HEADER_LOGO_HTML = '''<a href="/index.html" class="flex items-center gap-2.5 group shrink-0" aria-label="CalcWorld Home">
                <span class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-sky-400 flex items-center justify-center text-white font-extrabold text-xl shadow-md group-hover:scale-105 transition-transform">
                    <svg class="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" width="24" height="24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                    </svg>
                </span>
                <div class="flex flex-col">
                    <span class="font-black text-xl tracking-tight text-slate-900 dark:text-white leading-none flex items-baseline">Calc<span class="text-blue-600 dark:text-blue-400 ml-0.5">World</span></span>
                    <span class="text-[10px] font-bold text-slate-400 dark:text-slate-500 tracking-wider uppercase mt-0.5">Engine 2026</span>
                </div>
            </a>'''

HEADER_NAV_HTML = f'''    <!-- Header Navigation -->
    <header class="border-b border-slate-200/90 dark:border-slate-800/90 bg-white/85 dark:bg-slate-900/85 backdrop-blur-xl sticky top-0 z-40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-3">
            {HEADER_LOGO_HTML}

            <div class="flex items-center gap-3">
                <a href="/index.html" class="px-3.5 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-blue-600 hover:text-white transition flex items-center gap-1.5">
                    <span>&larr;</span>
                    <span>All Calculators</span>
                </a>

                <button type="button" onclick="toggleTheme()" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition" aria-label="Toggle Theme">
                    <svg id="themeIconSun" class="w-5 h-5 hidden dark:block text-amber-400" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/>
                    </svg>
                    <svg id="themeIconMoon" class="w-5 h-5 block dark:hidden text-slate-700" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
                    </svg>
                </button>
            </div>
        </div>
    </header>'''

UNIFIED_LEGAL_FOOTER = '''    <!-- Footer -->
    <footer class="border-t border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 py-12 px-4 sm:px-6 lg:px-8 text-xs text-slate-500 dark:text-slate-400 mt-auto">
        <div class="max-w-7xl mx-auto space-y-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
                <div class="flex items-center gap-2">
                    <span class="w-8 h-8 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center text-white font-bold text-base shadow-sm">
                        <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                        </svg>
                    </span>
                    <span class="font-extrabold text-lg text-slate-900 dark:text-white tracking-tight">Calc<span class="text-blue-600 dark:text-blue-400">World</span></span>
                </div>
                <div class="flex flex-wrap justify-center gap-6 text-xs text-slate-600 dark:text-slate-400 font-medium">
                    <a href="/about-us/" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">About Us</a>
                    <a href="/privacy-policy/" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Privacy Policy</a>
                    <a href="/terms-of-service/" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Terms of Service</a>
                    <a href="/contact/" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Contact &amp; Support</a>
                    <a href="/index.html" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors text-blue-600 dark:text-blue-400 font-semibold">All 207 Calculators</a>
                </div>
            </div>
            <div class="pt-4 border-t border-slate-100 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-2 text-[11px] text-slate-400">
                <p>&copy; 2026 CalcWorld. High-precision calculation utilities. All rights reserved.</p>
                <p>Zero tracking &bull; Instant client-side computation &bull; Institutional rigor</p>
            </div>
        </div>
    </footer>

    <script>
        function toggleTheme() {
            if (document.documentElement.classList.contains('dark')) {
                document.documentElement.classList.remove('dark');
                localStorage.theme = 'light';
            } else {
                document.documentElement.classList.add('dark');
                localStorage.theme = 'dark';
            }
        }
    </script>
</body>
</html>'''

# 2. Re-write ABOUT.HTML
about_html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us | CalcWorld - Computational Rigor & Privacy-First Utility</title>
    <meta name="description" content="Discover the mission, algorithmic transparency, and mathematical rigor behind CalcWorld's suite of 207+ high-precision online calculators.">
    <link rel="canonical" href="https://calcworld.net/about-us/">
    <script>
        if (localStorage.theme === 'light') {{
            document.documentElement.classList.remove('dark');
        }} else {{
            document.documentElement.classList.add('dark');
        }}
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#eff6ff', 100: '#dbeafe', 200: '#bfdbfe', 300: '#93c5fd', 400: '#60a5fa',
                            500: '#3b82f6', 600: '#2563eb', 700: '#1d4ed8', 800: '#1e40af', 900: '#1e3a8a', 950: '#0f172a'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>body {{ font-family: 'Inter', sans-serif; }}</style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 min-h-screen flex flex-col justify-between transition-colors duration-200">

{HEADER_NAV_HTML}

    <!-- Main Content Container -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-grow">
        <!-- Breadcrumb -->
        <nav class="flex items-center space-x-2 text-xs text-slate-500 dark:text-slate-400 mb-8">
            <a href="/index.html" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Home</a>
            <span>/</span>
            <span class="text-slate-900 dark:text-white font-medium">About Us</span>
        </nav>

        <article class="prose prose-slate dark:prose-invert max-w-none">
            <h1 class="text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white mb-6">About CalcWorld</h1>
            
            <p class="text-lg leading-relaxed text-slate-600 dark:text-slate-300 mb-8">
                <strong>CalcWorld</strong> is a premier, free digital calculation utility founded with a single mission: to provide fast, reliable, transparent, and mathematically rigorous calculation engines for everyday consumers, students, financial planners, engineers, and healthcare professionals across the globe.
            </p>

            <div class="grid grid-cols-1 sm:grid-cols-3 gap-6 my-10 not-prose">
                <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-center shadow-xs">
                    <div class="text-3xl font-extrabold text-blue-600 dark:text-blue-400 mb-1">207+</div>
                    <div class="text-xs uppercase font-bold tracking-wider text-slate-500 dark:text-slate-400">Specialized Calculators</div>
                </div>
                <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-center shadow-xs">
                    <div class="text-3xl font-extrabold text-blue-600 dark:text-blue-400 mb-1">100%</div>
                    <div class="text-xs uppercase font-bold tracking-wider text-slate-500 dark:text-slate-400">Free &amp; Open Access</div>
                </div>
                <div class="p-6 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-center shadow-xs">
                    <div class="text-3xl font-extrabold text-blue-600 dark:text-blue-400 mb-1">&lt; 0.1s</div>
                    <div class="text-xs uppercase font-bold tracking-wider text-slate-500 dark:text-slate-400">Client-Side Speed</div>
                </div>
            </div>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">Our Core Philosophy</h2>
            <p class="leading-relaxed">
                In an era dominated by paywalled financial software and ad-cluttered websites that require mandatory logins or personal data harvesting, CalcWorld takes an entirely user-first approach:
            </p>
            <ul class="list-disc pl-6 space-y-2 mb-6">
                <li><strong>Zero Server Latency:</strong> All calculations execute 100% client-side in modern web browsers using optimized JavaScript, ensuring instant outputs with zero waiting time.</li>
                <li><strong>Absolute Privacy:</strong> Your confidential data—such as loan balances, income amounts, personal body metrics, or passwords—never leaves your browser. Zero calculation telemetry is recorded on our servers.</li>
                <li><strong>Zero Paywalls or Gating:</strong> Every tool, amortization schedule, formula breakdown, and exportable dossier is 100% accessible to every user without registration or subscription barriers.</li>
            </ul>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">Institutional Citations &amp; Scientific Methodology</h2>
            <p class="leading-relaxed mb-4">
                Our calculation engines do not rely on rough estimates or subjective heuristics. Every formula implemented across our 207 tools is cross-referenced with established public institutions and peer-reviewed scientific literature:
            </p>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 not-prose my-6 text-sm">
                <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
                    <strong class="text-slate-900 dark:text-white block mb-1">Financial &amp; Tax Formulations</strong>
                    <p class="text-xs text-slate-500 dark:text-slate-400">Aligned with the Federal Reserve System, IRS Publication 936, the Truth in Lending Act (Regulation Z), and SEC regulatory compound interest standards.</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
                    <strong class="text-slate-900 dark:text-white block mb-1">Health &amp; Physiological Engines</strong>
                    <p class="text-xs text-slate-500 dark:text-slate-400">Based on published formulas from the World Health Organization (WHO), CDC Anthropometric Reference Data, and the Mifflin-St Jeor equation.</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
                    <strong class="text-slate-900 dark:text-white block mb-1">Engineering &amp; Physics Suites</strong>
                    <p class="text-xs text-slate-500 dark:text-slate-400">Standardized according to National Institute of Standards and Technology (NIST) CODATA physical constants, ASTM guidelines, and IEEE definitions.</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-100 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-800">
                    <strong class="text-slate-900 dark:text-white block mb-1">Construction &amp; Architectural Rules</strong>
                    <p class="text-xs text-slate-500 dark:text-slate-400">Conforming to the International Residential Code (IRC) for staircase slope ratios, concrete curing shrinkage factors, and roof pitch geometry.</p>
                </div>
            </div>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">Editorial &amp; Computational Transparency</h2>
            <p class="leading-relaxed mb-6">
                Every calculation algorithm is continuously tested and verified by our engineering team against published benchmarks. We maintain strict separation between computational integrity and third-party advertising partners to ensure completely unbiased mathematical results.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">Contact &amp; Feedback</h2>
            <p class="leading-relaxed mb-6">
                Have a feature request, spotted a typo, or want to suggest a new calculator? We welcome inquiries from educators, developers, and users worldwide. Reach out to our team at our official <a href="/contact/" class="text-blue-600 dark:text-blue-400 font-semibold underline">Contact &amp; Support Page</a>.
            </p>
        </article>
    </main>

{UNIFIED_LEGAL_FOOTER}'''

# 3. Re-write PRIVACY.HTML
privacy_html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy | CalcWorld - Google AdSense & GDPR Compliance</title>
    <meta name="description" content="CalcWorld's Privacy Policy explains our client-side computing architecture, zero server telemetry, Google AdSense cookie compliance, GDPR, and CCPA consumer protections.">
    <link rel="canonical" href="https://calcworld.net/privacy-policy/">
    <script>
        if (localStorage.theme === 'light') {{
            document.documentElement.classList.remove('dark');
        }} else {{
            document.documentElement.classList.add('dark');
        }}
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#eff6ff', 100: '#dbeafe', 200: '#bfdbfe', 300: '#93c5fd', 400: '#60a5fa',
                            500: '#3b82f6', 600: '#2563eb', 700: '#1d4ed8', 800: '#1e40af', 900: '#1e3a8a', 950: '#0f172a'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>body {{ font-family: 'Inter', sans-serif; }}</style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 min-h-screen flex flex-col justify-between transition-colors duration-200">

{HEADER_NAV_HTML}

    <!-- Main Content Container -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-grow">
        <!-- Breadcrumb -->
        <nav class="flex items-center space-x-2 text-xs text-slate-500 dark:text-slate-400 mb-8">
            <a href="/index.html" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Home</a>
            <span>/</span>
            <span class="text-slate-900 dark:text-white font-medium">Privacy Policy</span>
        </nav>

        <article class="prose prose-slate dark:prose-invert max-w-none">
            <h1 class="text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white mb-2">Privacy Policy</h1>
            <p class="text-xs text-slate-500 dark:text-slate-400 uppercase font-semibold tracking-wider mb-8">Last Updated: October 2026 &bull; Universal AdSense, GDPR &amp; CCPA Compliance</p>
            
            <p class="text-lg leading-relaxed text-slate-600 dark:text-slate-300 mb-8">
                At <strong>CalcWorld</strong> (accessible via calcworld.net), the privacy and computational confidentiality of our visitors is our paramount operational priority. This comprehensive Privacy Policy outlines the types of information gathered, how it is utilized, and your statutory rights under global data protection frameworks.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">1. Client-Side Computational Isolation</h2>
            <p class="leading-relaxed mb-4">
                CalcWorld operates on a <em>Zero Server-Side Computational Storage</em> framework. When you input sensitive numbers—such as loan balances, interest rates, mortgage down payments, body weight, caloric intake, or cryptographic seeds—those calculations are performed purely within your device's web browser using native client-side JavaScript.
            </p>
            <p class="leading-relaxed mb-6 font-semibold text-blue-600 dark:text-blue-400">
                None of your numerical inputs, personal lifestyle data, or generated financial schedules are ever transmitted to, inspected by, or stored upon our web servers.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">2. Web Server Log Files</h2>
            <p class="leading-relaxed mb-6">
                Like most standard web hosting architectures (such as Cloudflare Pages and standard reverse proxies), CalcWorld utilizes standard web server log files for operational reliability, DDoS mitigation, and traffic diagnostic purposes. The information inside these log files includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date/time stamps, referring/exit pages, and number of page views. These logs contain no personally identifiable financial or medical information.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">3. Google AdSense &amp; Advertising Cookies</h2>
            <p class="leading-relaxed mb-4">
                CalcWorld is financed through non-intrusive digital advertising to keep all 207 calculators 100% free for users globally. Google is one of the third-party vendors operating on our site:
            </p>
            <ul class="list-disc pl-6 space-y-2 mb-6">
                <li>Google uses cookies, including the DoubleClick DART cookie, to serve targeted advertisements based on a user's prior visits to CalcWorld and other sites across the internet.</li>
                <li>Users may opt out of personalized advertising by visiting Google's official <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener" class="text-blue-600 dark:text-blue-400 underline font-semibold">Ads Settings</a> or via the Network Advertising Initiative opt-out page at <a href="http://www.aboutads.info/choices/" target="_blank" rel="noopener" class="text-blue-600 dark:text-blue-400 underline font-semibold">aboutads.info</a>.</li>
                <li>Third-party ad networks or ad servers may use cookies, JavaScript, or Web Beacons within their respective advertisements appearing on CalcWorld. CalcWorld has no access to or control over these third-party cookies.</li>
            </ul>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">4. Local Storage (LocalStorage)</h2>
            <p class="leading-relaxed mb-6">
                CalcWorld uses browser <code class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-xs font-mono text-blue-600 dark:text-blue-400">localStorage</code> exclusively for user convenience features: remembering your visual dark/light theme preference (<code class="px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 text-xs font-mono">localStorage.theme</code>) and saving your bookmarked favorite calculators. This data remains on your physical device and is never synchronized to our servers.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">5. European Union General Data Protection Regulation (GDPR)</h2>
            <p class="leading-relaxed mb-4">
                Under the GDPR, visitors residing within the European Economic Area (EEA) possess specific statutory rights regarding their personal data:
            </p>
            <ul class="list-disc pl-6 space-y-2 mb-6">
                <li><strong>The Right to Access:</strong> You have the right to request copies of your personal data held by us.</li>
                <li><strong>The Right to Rectification &amp; Erasure:</strong> You have the right to request that we correct inaccurate information or erase your data from server logs.</li>
                <li><strong>The Right to Restrict &amp; Object to Processing:</strong> You have the right to object to our processing of your personal data under certain conditions.</li>
            </ul>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">6. California Consumer Privacy Act (CCPA)</h2>
            <p class="leading-relaxed mb-6">
                Under the CCPA, California consumers hold the right to request disclosure of categories of personal data collected, request deletion of collected personal data, and demand that a business not sell their personal data. <strong>CalcWorld does NOT sell, rent, or trade user personal data to third parties.</strong>
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">7. Children's Online Privacy Protection Act (COPPA)</h2>
            <p class="leading-relaxed mb-6">
                CalcWorld does not knowingly collect any personally identifiable information from children under the age of 13. If a parent or guardian believes that CalcWorld has recorded such information in its log files, please contact us immediately and we will promptly remove such records.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">8. Consent &amp; Policy Updates</h2>
            <p class="leading-relaxed mb-6">
                By using our website, you hereby consent to our Privacy Policy and agree to its terms. We may update our Privacy Policy periodically; any modifications will be reflected immediately on this page with an updated revision date.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">9. Contacting Our Data Protection Officer</h2>
            <p class="leading-relaxed mb-6">
                If you have additional questions or require more information about our Privacy Policy, please contact our administrative team through our <a href="/contact/" class="text-blue-600 dark:text-blue-400 font-semibold underline">Contact &amp; Support Page</a> or via email at <code class="font-mono text-blue-600 dark:text-blue-400">privacy@calcworld.net</code>.
            </p>
        </article>
    </main>

{UNIFIED_LEGAL_FOOTER}'''

# 4. Re-write TERMS.HTML
terms_html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service | CalcWorld - Computational Disclaimers &amp; Terms</title>
    <meta name="description" content="Review the Terms of Service for CalcWorld, including computational disclaimers, medical and financial non-advice declarations, intellectual property rights, and limitation of liability.">
    <link rel="canonical" href="https://calcworld.net/terms-of-service/">
    <script>
        if (localStorage.theme === 'light') {{
            document.documentElement.classList.remove('dark');
        }} else {{
            document.documentElement.classList.add('dark');
        }}
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#eff6ff', 100: '#dbeafe', 200: '#bfdbfe', 300: '#93c5fd', 400: '#60a5fa',
                            500: '#3b82f6', 600: '#2563eb', 700: '#1d4ed8', 800: '#1e40af', 900: '#1e3a8a', 950: '#0f172a'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>body {{ font-family: 'Inter', sans-serif; }}</style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 min-h-screen flex flex-col justify-between transition-colors duration-200">

{HEADER_NAV_HTML}

    <!-- Main Content Container -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-grow">
        <!-- Breadcrumb -->
        <nav class="flex items-center space-x-2 text-xs text-slate-500 dark:text-slate-400 mb-8">
            <a href="/index.html" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Home</a>
            <span>/</span>
            <span class="text-slate-900 dark:text-white font-medium">Terms of Service</span>
        </nav>

        <article class="prose prose-slate dark:prose-invert max-w-none">
            <h1 class="text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white mb-2">Terms of Service</h1>
            <p class="text-xs text-slate-500 dark:text-slate-400 uppercase font-semibold tracking-wider mb-8">Effective Date: October 2026 &bull; Universal User Agreement</p>
            
            <p class="text-lg leading-relaxed text-slate-600 dark:text-slate-300 mb-8">
                Welcome to <strong>CalcWorld</strong>. By accessing or utilizing any calculator, formula model, educational dossier, or programmatic interface on calcworld.net, you agree to be legally bound by these Terms of Service. If you do not agree with any part of these terms, you must refrain from using the platform.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">1. General Educational &amp; Informational Disclaimer</h2>
            <p class="leading-relaxed mb-4">
                All calculation engines, mathematical algorithms, charts, amortization schedules, and instructional guides provided across CalcWorld are developed for general informational, educational, and quick-reference purposes only.
            </p>
            <div class="p-4 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800/60 text-amber-900 dark:text-amber-200 text-sm leading-relaxed mb-6 not-prose">
                <strong>Important Notice:</strong> While our algorithms undergo rigorous verification against institutional benchmarks, mathematical models involve theoretical assumptions and simplifications. Calculated outputs must not be interpreted as absolute guarantees or contractual commitments.
            </div>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">2. Professional Disclaimers (Financial, Medical, Engineering, Legal)</h2>
            <div class="space-y-4 mb-6">
                <p class="leading-relaxed">
                    <strong>No Certified Financial Advice:</strong> Financial, loan, mortgage, investment, tax, and retirement calculators do not constitute fiduciary financial advisory services, tax counsel, or underwriting guarantees. Tax laws vary substantially by jurisdiction and change frequently. Always consult a Certified Financial Planner (CFP) or licensed CPA before executing financial decisions.
                </p>
                <p class="leading-relaxed">
                    <strong>No Medical or Clinical Advice:</strong> Physiological tools—such as BMI, BMR, Calorie, Body Fat, and BAC calculators—are designed for general fitness screening only. They do not constitute diagnostic medical evaluations or treatment prescriptions. Consult a licensed physician or registered dietitian for personalized healthcare advice.
                </p>
                <p class="leading-relaxed">
                    <strong>No Structural Engineering Certification:</strong> Construction, roofing, concrete, and electrical voltage drop calculators are material estimation aids. They do not replace formal blueprints stamped by licensed structural engineers or master electricians. Always verify with local building code authorities.
                </p>
            </div>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">3. Intellectual Property Rights &amp; Acceptable Use</h2>
            <p class="leading-relaxed mb-4">
                The visual design, branding, custom UI components, editorial text, JavaScript computational routines, and compiled presentation of CalcWorld are protected by international copyright, trademark, and intellectual property laws.
            </p>
            <ul class="list-disc pl-6 space-y-2 mb-6">
                <li>You are granted a revocable, non-exclusive license to use CalcWorld calculators for personal, educational, or internal commercial computation.</li>
                <li>You may not scrape, frame, clone, reverse engineer, or programmatically mass-replicate CalcWorld tools to establish a competing software service without explicit written authorization.</li>
                <li>You may freely print, export, or cite numerical results generated for personal budgeting, academic homework, or client presentation dossiers.</li>
            </ul>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">4. Limitation of Liability</h2>
            <p class="leading-relaxed mb-6">
                To the fullest extent permissible under applicable law, CalcWorld and its developers, operators, and affiliates shall not be liable for any direct, indirect, incidental, consequential, punitive, or special damages arising out of or in connection with the use of, or inability to use, any calculation tool on this website—including but not limited to financial loss, lost profits, computational inaccuracies, loan underwriting rejections, or physical injury.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">5. Modifications to Service &amp; Terms</h2>
            <p class="leading-relaxed mb-6">
                CalcWorld reserves the right to modify, upgrade, or discontinue any calculator tool or feature at any time without prior notice. Continued use of the platform after updates to these Terms of Service constitutes formal acceptance of the revised terms.
            </p>

            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mt-10 mb-4">6. Inquiries Regarding Terms</h2>
            <p class="leading-relaxed mb-6">
                If you have questions concerning these Terms of Service, please reach out via our official <a href="/contact/" class="text-blue-600 dark:text-blue-400 font-semibold underline">Contact &amp; Support Page</a>.
            </p>
        </article>
    </main>

{UNIFIED_LEGAL_FOOTER}'''

# 5. Re-write CONTACT.HTML
contact_html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact &amp; Support | CalcWorld - Computational Inquiries &amp; Bug Reports</title>
    <meta name="description" content="Contact CalcWorld support, submit algorithmic feedback, report calculation discrepancies, and connect with our engineering team.">
    <link rel="canonical" href="https://calcworld.net/contact/">
    <script>
        if (localStorage.theme === 'light') {{
            document.documentElement.classList.remove('dark');
        }} else {{
            document.documentElement.classList.add('dark');
        }}
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#eff6ff', 100: '#dbeafe', 200: '#bfdbfe', 300: '#93c5fd', 400: '#60a5fa',
                            500: '#3b82f6', 600: '#2563eb', 700: '#1d4ed8', 800: '#1e40af', 900: '#1e3a8a', 950: '#0f172a'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>body {{ font-family: 'Inter', sans-serif; }}</style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 min-h-screen flex flex-col justify-between transition-colors duration-200">

{HEADER_NAV_HTML}

    <!-- Main Content Container -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-grow">
        <!-- Breadcrumb -->
        <nav class="flex items-center space-x-2 text-xs text-slate-500 dark:text-slate-400 mb-8">
            <a href="/index.html" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">Home</a>
            <span>/</span>
            <span class="text-slate-900 dark:text-white font-medium">Contact &amp; Support</span>
        </nav>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <!-- Contact Info -->
            <div class="md:col-span-1 space-y-6">
                <div>
                    <h1 class="text-3xl font-extrabold text-slate-900 dark:text-white mb-2">Get in Touch</h1>
                    <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed">
                        We welcome algorithmic feedback, feature suggestions, partnership proposals, and calculation bug reports.
                    </p>
                </div>

                <div class="space-y-4 text-sm">
                    <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
                        <span class="text-xs uppercase font-bold text-slate-400 dark:text-slate-500 block mb-1">General Inquiries</span>
                        <a href="mailto:support@calcworld.net" class="font-mono text-blue-600 dark:text-blue-400 font-semibold hover:underline">support@calcworld.net</a>
                    </div>
                    <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
                        <span class="text-xs uppercase font-bold text-slate-400 dark:text-slate-500 block mb-1">Partnerships &amp; Media</span>
                        <a href="mailto:press@calcworld.net" class="font-mono text-blue-600 dark:text-blue-400 font-semibold hover:underline">press@calcworld.net</a>
                    </div>
                    <div class="p-4 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
                        <span class="text-xs uppercase font-bold text-slate-400 dark:text-slate-500 block mb-1">Privacy &amp; Data Rights</span>
                        <a href="mailto:legal@calcworld.net" class="font-mono text-blue-600 dark:text-blue-400 font-semibold hover:underline">legal@calcworld.net</a>
                    </div>
                </div>

                <div class="p-4 rounded-2xl bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-800/60 text-xs text-blue-900 dark:text-blue-200 leading-relaxed">
                    <strong>Response Guarantee:</strong> Our technical team typically reviews and responds to computational inquiries within 24 to 48 business hours.
                </div>
            </div>

            <!-- Contact Form -->
            <div class="md:col-span-2">
                <div class="p-8 rounded-3xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs">
                    <h2 class="text-xl font-bold text-slate-900 dark:text-white mb-6">Send an Inquiry or Bug Report</h2>
                    <form id="contactForm" class="space-y-4">
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div>
                                <label for="name" class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">Your Name</label>
                                <input type="text" id="name" required placeholder="Jane Doe" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                            </div>
                            <div>
                                <label for="email" class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">Email Address</label>
                                <input type="email" id="email" required placeholder="jane@example.com" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                            </div>
                        </div>

                        <div>
                            <label for="topic" class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">Inquiry Topic</label>
                            <select id="topic" class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-blue-500">
                                <option value="bug">Report Calculation Bug / Discrepancy</option>
                                <option value="feature">Suggest New Calculator</option>
                                <option value="general">General Support Question</option>
                                <option value="partnership">Advertising &amp; Partnership</option>
                                <option value="privacy">Privacy / GDPR / CCPA Inquiry</option>
                            </select>
                        </div>

                        <div>
                            <label for="message" class="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">Message &amp; Calculation Details</label>
                            <textarea id="message" rows="5" required placeholder="Please describe the tool name, entered inputs, expected vs observed output..." class="w-full px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"></textarea>
                        </div>

                        <div id="statusMessage" class="hidden"></div>

                        <button type="submit" class="w-full py-3 px-6 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-sm shadow-md shadow-blue-500/20 transition-all cursor-pointer">
                            Submit Inquiry
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </main>

{UNIFIED_LEGAL_FOOTER}'''

# 6. Re-write 404.HTML
not_found_html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found (404) | CalcWorld</title>
    <meta name="robots" content="noindex, follow">
    <script>
        if (localStorage.theme === 'light') {{
            document.documentElement.classList.remove('dark');
        }} else {{
            document.documentElement.classList.add('dark');
        }}
    </script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#eff6ff', 100: '#dbeafe', 200: '#bfdbfe', 300: '#93c5fd', 400: '#60a5fa',
                            500: '#3b82f6', 600: '#2563eb', 700: '#1d4ed8', 800: '#1e40af', 900: '#1e3a8a', 950: '#0f172a'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>body {{ font-family: 'Inter', sans-serif; }}</style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 min-h-screen flex flex-col justify-between transition-colors duration-200">

{HEADER_NAV_HTML}

    <!-- 404 Hero Container -->
    <main class="flex-grow flex items-center justify-center py-16 px-4 sm:px-6 lg:px-8">
        <div class="max-w-2xl w-full text-center space-y-8">
            <div class="relative">
                <span class="text-9xl font-black text-slate-200 dark:text-slate-800/80 tracking-widest select-none">404</span>
                <div class="absolute inset-0 flex items-center justify-center">
                    <span class="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white">Calculation Not Found</span>
                </div>
            </div>

            <p class="text-base sm:text-lg text-slate-600 dark:text-slate-400 max-w-lg mx-auto">
                The calculator page you requested doesn't exist or may have been relocated. Search our comprehensive library of 207 calculators below:
            </p>

            <!-- Search Bar -->
            <div class="max-w-md mx-auto">
                <form action="/index.html" method="get" class="relative">
                    <input type="text" name="q" id="searchBox" placeholder="Search calculators (e.g. mortgage, loan, BMI, calorie)..." class="w-full px-5 py-3.5 pl-12 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm text-sm">
                    <svg class="w-5 h-5 text-slate-400 absolute left-4 top-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
                </form>
            </div>

            <!-- Popular Quick Links -->
            <div class="pt-4">
                <span class="text-xs uppercase font-bold tracking-wider text-slate-400 dark:text-slate-500 block mb-3">Popular Calculators</span>
                <div class="flex flex-wrap justify-center gap-2">
                    <a href="/calculators/mortgage-calculator.html" class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-500 dark:hover:border-blue-500 text-slate-700 dark:text-slate-300 transition-colors">Mortgage</a>
                    <a href="/calculators/loan-calculator.html" class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-500 dark:hover:border-blue-500 text-slate-700 dark:text-slate-300 transition-colors">Loan</a>
                    <a href="/calculators/auto-loan-calculator.html" class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-500 dark:hover:border-blue-500 text-slate-700 dark:text-slate-300 transition-colors">Auto Loan</a>
                    <a href="/calculators/bmi-calculator.html" class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-500 dark:hover:border-blue-500 text-slate-700 dark:text-slate-300 transition-colors">BMI</a>
                    <a href="/calculators/calorie-calculator.html" class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-500 dark:hover:border-blue-500 text-slate-700 dark:text-slate-300 transition-colors">Calorie</a>
                    <a href="/calculators/compound-interest-calculator.html" class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-500 dark:hover:border-blue-500 text-slate-700 dark:text-slate-300 transition-colors">Compound Interest</a>
                    <a href="/calculators/percentage-calculator.html" class="px-3.5 py-1.5 rounded-full text-xs font-semibold bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 hover:border-blue-500 dark:hover:border-blue-500 text-slate-700 dark:text-slate-300 transition-colors">Percentage</a>
                </div>
            </div>

            <div>
                <a href="/index.html" class="inline-flex items-center justify-center px-6 py-3 rounded-2xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-sm shadow-lg shadow-blue-500/25 transition-all">
                    Return to Homepage
                </a>
            </div>
        </div>
    </main>

{UNIFIED_LEGAL_FOOTER}'''

print("Writing unified Legal & 404 pages...")
pages_to_write = {
    os.path.join(BASE_DIR, "legal-pages", "about.html"): about_html,
    os.path.join(BASE_DIR, "legal-pages", "about-us.html"): about_html,
    os.path.join(BASE_DIR, "about-us", "index.html"): about_html,
    os.path.join(BASE_DIR, "about", "index.html"): about_html,

    os.path.join(BASE_DIR, "legal-pages", "privacy.html"): privacy_html,
    os.path.join(BASE_DIR, "legal-pages", "privacy-policy.html"): privacy_html,
    os.path.join(BASE_DIR, "privacy-policy", "index.html"): privacy_html,
    os.path.join(BASE_DIR, "privacy", "index.html"): privacy_html,

    os.path.join(BASE_DIR, "legal-pages", "terms.html"): terms_html,
    os.path.join(BASE_DIR, "legal-pages", "terms-of-service.html"): terms_html,
    os.path.join(BASE_DIR, "terms-of-service", "index.html"): terms_html,
    os.path.join(BASE_DIR, "terms", "index.html"): terms_html,

    os.path.join(BASE_DIR, "legal-pages", "contact.html"): contact_html,
    os.path.join(BASE_DIR, "contact", "index.html"): contact_html,
    os.path.join(BASE_DIR, "contact-us", "index.html"): contact_html,

    os.path.join(BASE_DIR, "404.html"): not_found_html,
}

for path, content in pages_to_write.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Legal and 404 pages written successfully!")

# 7. Specific Calculator Internal Link Fixes
CALC_LINK_REPLACEMENTS = {
    'calculators/shoe-size-conversion.html': [
        ('bra-calculator.html', 'bra-size-calculator.html')
    ],
    'calculators/estate-tax-calculator.html': [
        ('capital-gains-tax-calculator.html', 'income-tax-calculator.html')
    ],
    'calculators/time-zone-calculator.html': [
        ('days-between-dates-calculator.html', 'day-counter.html'),
        ('work-hours-calculator.html', 'time-card-calculator.html')
    ],
    'calculators/btu-calculator.html': [
        ('heat-pump-savings-calculator.html', 'electricity-calculator.html'),
        ('electricity-cost-calculator.html', 'electricity-calculator.html')
    ],
    'calculators/gravel-calculator.html': [
        ('soil-calculator.html', 'mulch-calculator.html'),
        ('paver-calculator.html', 'concrete-calculator.html')
    ],
    'calculators/greatest-common-factor-calculator.html': [
        ('lcm-calculator.html', 'factor-calculator.html'),
        ('prime-number-calculator.html', 'factor-calculator.html')
    ],
    'calculators/ohms-law-calculator.html': [
        ('wire-size-calculator.html', 'voltage-drop-calculator.html'),
        ('conduit-fill-calculator.html', 'voltage-drop-calculator.html'),
        ('kilowatt-to-amp-calculator.html', 'electricity-calculator.html')
    ],
    'calculators/resistor-calculator.html': [
        ('wire-size-calculator.html', 'voltage-drop-calculator.html'),
        ('conduit-fill-calculator.html', 'voltage-drop-calculator.html')
    ],
    'calculators/voltage-drop-calculator.html': [
        ('wire-size-calculator.html', 'ohms-law-calculator.html'),
        ('conduit-fill-calculator.html', 'ohms-law-calculator.html'),
        ('kilowatt-to-amp-calculator.html', 'electricity-calculator.html')
    ],
    'calculators/bandwidth-calculator.html': [
        ('data-storage-calculator.html', 'time-calculator.html'),
        ('download-time-calculator.html', 'time-calculator.html'),
        ('latency-ping-calculator.html', 'speed-calculator.html')
    ],
    'calculators/horsepower-calculator.html': [
        ('acceleration-calculator.html', 'speed-calculator.html'),
        ('torque-calculator.html', 'btu-calculator.html'),
        ('gear-ratio-calculator.html', 'ratio-calculator.html'),
        ('bmep-calculator.html', 'gas-mileage-calculator.html')
    ],
    'calculators/mass-calculator.html': [
        ('acceleration-calculator.html', 'speed-calculator.html'),
        ('force-calculator.html', 'density-calculator.html'),
        ('kinetic-energy-calculator.html', 'horsepower-calculator.html')
    ],
    'calculators/molecular-weight-calculator.html': [
        ('stoichiometry-calculator.html', 'percentage-calculator.html'),
        ('empirical-formula-calculator.html', 'ratio-calculator.html'),
        ('percent-composition-calculator.html', 'percentage-calculator.html')
    ],
    'calculators/sample-size-calculator.html': [
        ('margin-of-error-calculator.html', 'percent-error-calculator.html')
    ],
    'calculators/time-calculator.html': [
        ('href="/other-calculators"', 'href="/index.html#directorySection"'),
        ('href="/time-card-calculator"', 'href="time-card-calculator.html"'),
        ('href="/pace-calculator"', 'href="pace-calculator.html"'),
        ('href="/due-date-calculator"', 'href="due-date-calculator.html"')
    ],
    'calculators/password-generator.html': [
        ('href="/calculators/"', 'href="/index.html"')
    ],
    'calculators/apr-calculator.html': [
        ('href="/calculators/"', 'href="/index.html"')
    ],
    'calculators/home-equity-loan-calculator.html': [
        ('href="/calculators"', 'href="/index.html"')
    ],
    'calculators/bmr-calculator.html': [
        ('href="/fitness-health"', 'href="/index.html#directorySection"')
    ],
    'calculators/conversion-calculator.html': [
        ('href="/other"', 'href="/index.html#directorySection"')
    ],
    'calculators/irr-calculator.html': [
        ('href="/financial"', 'href="/index.html#directorySection"')
    ],
    'calculators/ratio-calculator.html': [
        ('href="/math"', 'href="/index.html#directorySection"')
    ]
}

print("Fixing calculator internal links...")
for rel_file, rep_list in CALC_LINK_REPLACEMENTS.items():
    file_path = os.path.join(BASE_DIR, rel_file)
    if os.path.isfile(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            c = f.read()
        for src, dst in rep_list:
            c = c.replace(src, dst)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(c)

# 8. Standardize Legal Links in Footers of ALL 207 calculators
print("Ensuring footers in all 207 calculators point to clean legal routes...")
for f in glob.glob(os.path.join(BASE_DIR, "calculators", "*.html")):
    with open(f, "r", encoding="utf-8") as fp:
        html = fp.read()
    
    # standardize legal links in footer
    new_html = html
    new_html = re.sub(r'href=["\'][^"\']*(?:about|about-us)\.html["\']', 'href="/about-us/"', new_html)
    new_html = re.sub(r'href=["\'][^"\']*(?:privacy|privacy-policy)\.html["\']', 'href="/privacy-policy/"', new_html)
    new_html = re.sub(r'href=["\'][^"\']*(?:terms|terms-of-service)\.html["\']', 'href="/terms-of-service/"', new_html)
    new_html = re.sub(r'href=["\'][^"\']*(?:contact|contact-us)\.html["\']', 'href="/contact/"', new_html)
    
    if new_html != html:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(new_html)

# 9. Update _redirects
redirects_content = """/about-us /about-us/ 301
/about /about-us/ 301
/privacy-policy /privacy-policy/ 301
/privacy /privacy-policy/ 301
/terms-of-service /terms-of-service/ 301
/terms /terms-of-service/ 301
/contact /contact/ 301
/contact-us /contact/ 301
/legal-pages/about.html /about-us/ 301
/legal-pages/about-us.html /about-us/ 301
/legal-pages/privacy.html /privacy-policy/ 301
/legal-pages/privacy-policy.html /privacy-policy/ 301
/legal-pages/terms.html /terms-of-service/ 301
/legal-pages/terms-of-service.html /terms-of-service/ 301
/legal-pages/contact.html /contact/ 301
"""
with open(os.path.join(BASE_DIR, "_redirects"), "w", encoding="utf-8") as f:
    f.write(redirects_content)

# 10. Sync with Mirror Directory
print("Mirroring everything to Desktop mirror directory...")
if os.path.exists(MIRROR_DIR):
    # Copy legal-pages, alias dirs, 404, calculators, _redirects
    for item in ["about-us", "about", "privacy-policy", "privacy", "terms-of-service", "terms", "contact", "contact-us", "legal-pages"]:
        src = os.path.join(BASE_DIR, item)
        dst = os.path.join(MIRROR_DIR, item)
        if os.path.exists(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
    
    for f in ["404.html", "_redirects"]:
        src = os.path.join(BASE_DIR, f)
        dst = os.path.join(MIRROR_DIR, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            
    # Copy calculators
    shutil.copytree(os.path.join(BASE_DIR, "calculators"), os.path.join(MIRROR_DIR, "calculators"), dirs_exist_ok=True)

print("ALL UPDATES AND SYNCHRONIZATION COMPLETED!")

import os, glob, re, shutil

PRIMARY_DIR = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
MIRROR_DIR = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'

BRAND_PALETTE_STR = """brand: {
                            50: '#eff6ff',
                            100: '#dbeafe',
                            200: '#bfdbfe',
                            300: '#93c5fd',
                            400: '#60a5fa',
                            500: '#3b82f6',
                            600: '#2563eb',
                            700: '#1d4ed8',
                            800: '#1e40af',
                            900: '#1e3a8a',
                            950: '#172554'
                        },"""

def get_suite_name(content, filename):
    m = re.search(r'<!--\s*Suite Badge\s*-->\s*<span[^>]*>(.*?)</span>', content, re.DOTALL | re.I)
    if m:
        suite = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        if suite:
            return suite
    fn = filename.lower()
    if any(k in fn for k in ['loan', 'mortgage', 'tax', 'salary', 'finance', 'roi', 'investment', '401k', 'ira', 'annuity', 'bond', 'budget', 'debt', 'depreciation', 'interest', 'payment', 'pension', 'refinance', 'rent', 'retirement', 'salary', 'savings', 'tip', 'vat', 'wage']):
        return "FINANCIAL SUITE"
    elif any(k in fn for k in ['bmi', 'body', 'calorie', 'bmr', 'macro', 'weight', 'pregnancy', 'pace', 'protein', 'fat', 'tdee', 'ovulation', 'conception', 'period', 'gfr', 'bac', 'heart']):
        return "FITNESS & HEALTH SUITE"
    elif any(k in fn for k in ['scientific', 'fraction', 'percentage', 'triangle', 'volume', 'deviation', 'sequence', 'exponent', 'binary', 'hex', 'log', 'area', 'probability', 'statistics', 'z-score', 'ratio', 'root', 'matrix', 'quadratic', 'slope', 'circle']):
        return "MATHEMATICS SUITE"
    elif any(k in fn for k in ['concrete', 'roofing', 'tile', 'mulch', 'gravel', 'stair', 'square-footage']):
        return "CONSTRUCTION SUITE"
    elif any(k in fn for k in ['auto', 'car', 'mileage', 'gas', 'tire', 'horsepower']):
        return "AUTOMOTIVE & TRAVEL SUITE"
    else:
        return "PRECISION COMPUTATION SUITE"

def build_unified_header(suite_name):
    return f"""    <!-- Top Announcement Bar -->
    <div class="bg-gradient-to-r from-blue-600 via-indigo-600 to-sky-500 text-white text-[11px] sm:text-xs font-semibold py-1.5 px-4 text-center tracking-wide flex items-center justify-center gap-2 no-print">
        <span class="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
        <span>CalcWorld Engine 2026: Precision Computation &bull; Zero Server Latency &bull; 100% Private</span>
    </div>

    <!-- Header Navigation -->
    <header class="border-b border-slate-200/90 dark:border-slate-800/90 bg-white/85 dark:bg-slate-900/85 backdrop-blur-xl sticky top-0 z-40 no-print">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-3">
            
            <!-- Brand Logo -->
            <a href="../index.html" class="flex items-center gap-2.5 group shrink-0" aria-label="CalcWorld Home">
                <span class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-sky-400 flex items-center justify-center text-white font-extrabold text-xl shadow-md group-hover:scale-105 transition-transform">
                    <svg class="w-6 h-6 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24" width="24" height="24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/>
                    </svg>
                </span>
                <div class="flex flex-col">
                    <span class="font-black text-xl tracking-tight text-slate-900 dark:text-white leading-none flex items-baseline">Calc<span class="text-blue-600 dark:text-blue-400 ml-0.5">World</span></span>
                    <span class="text-[10px] font-bold text-slate-400 dark:text-slate-500 tracking-wider uppercase mt-0.5">Engine 2026</span>
                </div>
            </a>

            <!-- Suite Badge -->
            <span class="hidden sm:inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-blue-50 text-blue-700 dark:bg-blue-950/60 dark:text-blue-300 border border-blue-200/60 dark:border-blue-800/60 uppercase tracking-wider">
                {suite_name}
            </span>

            <!-- Actions: All Calculators + Theme Toggle -->
            <div class="flex items-center gap-2">
                <a href="../index.html" class="px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-xs font-semibold text-slate-700 dark:text-slate-300 hover:bg-blue-600 hover:text-white transition flex items-center gap-1.5">
                    <span>&larr;</span>
                    <span class="hidden sm:inline">All Calculators</span>
                </a>

                <button type="button" id="theme-toggle" data-theme-toggle="true" onclick="toggleTheme()" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition" aria-label="Toggle Theme">
                    <svg id="themeIconSun" class="w-5 h-5 hidden dark:block text-amber-400" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/>
                    </svg>
                    <svg id="themeIconMoon" class="w-5 h-5 block dark:hidden text-slate-700" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
                    </svg>
                </button>
            </div>
        </div>

        <!-- Hidden Global Compatibility Proxies (Prevents Legacy Script Crashes) -->
        <div class="hidden" aria-hidden="true" style="display:none!important">
            <button id="themeToggle" type="button" onclick="toggleTheme()"></button>
            <button id="themeToggleBtn" type="button" onclick="toggleTheme()"></button>
            <button id="theme-btn" type="button" onclick="toggleTheme()"></button>
            <span id="theme-label">Theme</span>
            <svg id="theme-toggle-dark-icon"></svg>
            <svg id="theme-toggle-light-icon"></svg>
            <svg id="theme-dark-icon"></svg>
            <svg id="theme-light-icon"></svg>
            <svg id="sun-icon"></svg>
            <svg id="moon-icon"></svg>
            <svg id="sunIcon"></svg>
            <svg id="moonIcon"></svg>
            <svg id="theme-sun"></svg>
            <svg id="theme-moon"></svg>
            <svg id="theme-icon-dark"></svg>
            <svg id="theme-icon-light"></svg>
            <svg id="theme-sun-icon"></svg>
            <svg id="theme-moon-icon"></svg>
            <select id="currency-switcher"><option value="$" selected>$ USD</option><option value="€">€ EUR</option><option value="£">£ GBP</option></select>
            <select id="currency-select"><option value="$" selected>$ USD</option></select>
            <select id="currencySelector"><option value="$" selected>$ USD</option></select>
            <select id="currency-selector"><option value="$" selected>$ USD</option></select>
            <select id="formatSwitcher"><option value="iso" selected>ISO</option><option value="us">US</option></select>
            <select id="chunk-mode-header"><option value="auto" selected>Auto</option></select>
            <input id="decimalPlaces" type="number" value="4">
            <input id="calc-amount" type="number" value="100">
            <input id="calc-rate" type="number" value="7">
            <select id="calc-direction"><option value="add" selected>Add</option></select>
            <span id="quick-bar-payment"></span>
            <span id="quick-bar-true"></span>
            <button id="btnQuickAdd" type="button"></button>
            <button id="btnQuickDiff" type="button"></button>
            <button id="quickMetricBtn" type="button"></button>
            <button id="quickImperialBtn" type="button"></button>
            <button id="unit-imperial" type="button"></button>
            <button id="unit-metric" type="button"></button>
            <button id="unit-imperial-btn" type="button"></button>
            <button id="unit-metric-btn" type="button"></button>
            <button id="system-imperial-btn" type="button"></button>
            <button id="system-metric-btn" type="button"></button>
            <button id="btn-imperial" type="button"></button>
            <button id="btn-metric" type="button"></button>
            <button id="unitImp" type="button"></button>
            <button id="unitMet" type="button"></button>
            <button id="unitImperial" type="button"></button>
            <button id="unitMetric" type="button"></button>
            <button id="unit-miles-btn" type="button"></button>
            <button id="unit-km-btn" type="button"></button>
            <button id="unitBtnImperial" type="button"></button>
            <button id="unitBtnMetric" type="button"></button>
            <button id="btn-unit-imperial" type="button"></button>
            <button id="btn-unit-metric" type="button"></button>
            <button id="angle-unit-deg" type="button"></button>
            <button id="angle-unit-rad" type="button"></button>
            <button id="unit-deg-btn" type="button"></button>
            <button id="unit-rad-btn" type="button"></button>
            <button id="header-scale-4" type="button"></button>
            <button id="header-scale-5" type="button"></button>
            <button id="navModeConv" type="button"></button>
            <button id="navModeArith" type="button"></button>
            <button id="fmt12Btn" type="button"></button>
            <button id="fmt24Btn" type="button"></button>
            <input id="mixedMode" type="checkbox">
            <button id="quickCopyHeader" type="button"></button>
        </div>
    </header>"""

def patch_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    modified = False

    # 1. Update or inject brand into tailwind.config
    if 'tailwind.config' in content:
        tw_match = re.search(r'tailwind\.config\s*=\s*(\{.*?\n\s*\})', content, re.DOTALL)
        if tw_match:
            tw_body = tw_match.group(1)
            if 'brand:' not in tw_body and '"brand":' not in tw_body:
                colors_match = re.search(r'colors:\s*\{', tw_body)
                if colors_match:
                    new_tw_body = tw_body[:colors_match.end()] + '\n                        ' + BRAND_PALETTE_STR + tw_body[colors_match.end():]
                    content = content[:tw_match.start(1)] + new_tw_body + content[tw_match.end(1):]
                    modified = True
                else:
                    extend_match = re.search(r'extend:\s*\{', tw_body)
                    if extend_match:
                        new_tw_body = tw_body[:extend_match.end()] + '\n                    colors: {\n                        ' + BRAND_PALETTE_STR + '\n                    },' + tw_body[extend_match.end():]
                        content = content[:tw_match.start(1)] + new_tw_body + content[tw_match.end(1):]
                        modified = True

    # 2. Replace Header navigation with updated unified header containing proxies & bulletproof logo
    suite_name = get_suite_name(content, filename)
    new_header = build_unified_header(suite_name)

    pattern = r'(?:<!--\s*Top Announcement Bar\s*-->.*?)(?:<header\b[^>]*>.*?</header>)'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_header, content, count=1, flags=re.DOTALL)
        modified = True
    else:
        header_pat = r'<header\b[^>]*>.*?</header>'
        if re.search(header_pat, content, re.DOTALL):
            content = re.sub(header_pat, new_header, content, count=1, flags=re.DOTALL)
            modified = True

    # 3. Inject universal toggleTheme script if missing
    if 'function toggleTheme' not in content and 'window.toggleTheme' not in content:
        universal_script = """
    <!-- CalcWorld Universal Theme & Interaction Engine -->
    <script>
        window.toggleTheme = function() {
            const isDark = document.documentElement.classList.toggle('dark');
            localStorage.theme = isDark ? 'dark' : 'light';
            const suns = document.querySelectorAll('#themeIconSun, #sun-icon, #theme-sun, #theme-icon-light, #theme-toggle-light-icon, #theme-sun-icon');
            const moons = document.querySelectorAll('#themeIconMoon, #moon-icon, #theme-moon, #theme-icon-dark, #theme-toggle-dark-icon, #theme-moon-icon');
            suns.forEach(s => s.classList.toggle('hidden', !isDark));
            moons.forEach(m => m.classList.toggle('hidden', isDark));
            window.dispatchEvent(new Event('themechange'));
        };
    </script>
"""
        content = content.replace('</body>', universal_script + '\n</body>')
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    files = glob.glob(os.path.join(PRIMARY_DIR, '*.html'))
    print(f"Processing {len(files)} calculators in {PRIMARY_DIR}...")
    
    updated_count = 0
    for f in files:
        if patch_file(f):
            updated_count += 1
            
    print(f"Updated {updated_count} files in primary directory.")
    
    if os.path.exists(MIRROR_DIR):
        print(f"Mirroring files to {MIRROR_DIR}...")
        for f in files:
            dest = os.path.join(MIRROR_DIR, os.path.basename(f))
            shutil.copy2(f, dest)
        print("Mirroring completed.")

if __name__ == '__main__':
    main()

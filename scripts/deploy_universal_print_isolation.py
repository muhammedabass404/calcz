import os
import glob
import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

ONEDRIVE_CALC_DIR = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
DESKTOP_CALC_DIR = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'

PRINT_TAB_REGEX = re.compile(
    r'id=["\'](tab[-_]?print|print[-_]?tab|tab[-_]?report|tabPrint|tabContent[-_]print|tab[-_]content[-_]print|printableReportSection|tabPrintView|tab[-_]print[-_]report|tab[-_]print[-_]content|printArea|print[-_]sheet[-_]content)["\']',
    re.I
)
PRINT_CARD_REGEX = re.compile(
    r'class=["\'][^"\']*(card[-_]print|print[-_]card|printable[-_]report|print[-_]dossier)[^"\']*["\']',
    re.I
)

def find_media_print(content):
    pattern = re.compile(r'@media\s+print\s*\{', re.I)
    matches = []
    for m in pattern.finditer(content):
        start = m.start()
        open_braces = 0
        end = start
        for i in range(start, len(content)):
            if content[i] == '{':
                open_braces += 1
            elif content[i] == '}':
                open_braces -= 1
                if open_braces == 0:
                    end = i + 1
                    break
        matches.append((start, end, content[start:end]))
    return matches

def generate_print_css(has_dedicated_print):
    if has_dedicated_print:
        return """
        /* ==========================================================================
           UNIVERSAL PRINT ISOLATION STYLESHEET (TABBED PRINT DOSSIER) - CALCWORLD
           Strictly prints ONLY the official calculation report/dossier.
           Suppresses website chrome, inputs, educational articles, and FAQs.
           ========================================================================== */
        @media print {
            /* 1. Hide website chrome, navigation, ads, sidebars, and popups */
            header, footer, nav, aside,
            .no-print, .ad-slot, .ad-unit, [id*="ad-slot"], [id*="adSlot"], [class*="ad-slot"],
            [id*="adblock"], [id*="adblockRecovery"], #adblock-banner, #adblock-recovery,
            #floatingBar, #floating-bar, #mobileBottomNav, #toast, #toastNotification, .toast-notify,
            #shimmerOverlay, .shimmer, .shimmer-active,
            .preset-btn, .tab-btn, .tab-trigger, .tab-nav-btn, .tab-btn-wrapper, .tab-buttons, #tabButtons,
            .mode-btn, button, .btn-action, #presets-container, #preset-container,
            .lead-box, [id*="lead-box"], [id*="leadBox"], [id*="email-report"],
            .lg\\:col-span-4, .lg\\:col-span-5, .w-full.lg\\:w-1\\/3, aside {
                display: none !important;
            }

            /* 2. Hide all calculation input forms and controls */
            form, [id*="calc-form"], [id*="calcForm"], [id*="calculatorInputs"], [id*="inputs"],
            [id*="calculator-form"], [id*="bodyFatForm"], [id*="bmiForm"], [id*="iraForm"],
            [id*="rothForm"], [id*="mutualFundForm"], [id*="rmdForm"], [id*="discount-form"],
            [id*="loan-form"], [id*="savings-form"], [id*="lead-form"] {
                display: none !important;
            }

            /* 3. Hide all SEO educational articles, guides, and FAQ accordions */
            article, [id*="seo-article"], .prose, .faq-section, #faq-accordion, #faq-container,
            #faqSection, details, .faq-item, [id*="faq"] {
                display: none !important;
            }

            /* 4. Reset page styling for pristine high-contrast print */
            body {
                background: #ffffff !important;
                color: #000000 !important;
                padding: 0 !important;
                margin: 0 !important;
                font-size: 11pt !important;
            }

            .dark, .dark body {
                background: #ffffff !important;
                color: #000000 !important;
            }

            main, .max-w-7xl, .lg\\:col-span-8, .lg\\:col-span-7, .col-span-12, .w-full.lg\\:w-2\\/3 {
                max-width: 100% !important;
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
                display: block !important;
            }

            .grid {
                display: block !important;
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }

            /* 5. Hide all interactive non-print tabs */
            #tab-calculator, #tab-tracker, #tab-habits, #tab-inputs, #tab-input, #tab-schedule,
            #tab-amortization, #tab-visual, #tab-chart, #tab-charts, #tab-table, #tab-breakdown,
            #tab-projection, #tab-methods, #tab-milestones, #tab-activity, #tab-macros,
            #tabSummary, #tabBreakdown, #tabChart, #tabSchedule, #tabVisual, #tabTable,
            #tab-summary, #pane-chart, #pane-schedule, #pane-table, #tab-history, #tab-analysis {
                display: none !important;
            }

            /* 6. Force the Print Report Container to be the ONLY visible element */
            #tab-print, #tabPrint, #tabContent-print, #tab-content-print, #tab-print-report,
            #tab-print-content, #printableReportSection, #printableReceiptArea, #tabPrintView,
            #printArea, #print-sheet-content, .card-print, .print-card, .printable-report,
            .print-dossier, .print-only {
                display: block !important;
                visibility: visible !important;
                width: 100% !important;
                border: 1px solid #cbd5e1 !important;
                border-radius: 0.5rem !important;
                padding: 1.5rem !important;
                margin: 0 !important;
                box-shadow: none !important;
                background: #ffffff !important;
                color: #0f172a !important;
                page-break-inside: avoid !important;
            }

            /* 7. Format clean print tables and charts */
            table {
                width: 100% !important;
                border-collapse: collapse !important;
            }
            th, td {
                border-bottom: 1px solid #e2e8f0 !important;
                padding: 6px 8px !important;
                color: #0f172a !important;
            }
            canvas {
                max-width: 100% !important;
                height: auto !important;
            }
        }
"""
    else:
        return """
        /* ==========================================================================
           UNIVERSAL PRINT ISOLATION STYLESHEET (RESULTS CARD REPORT) - CALCWORLD
           Strictly prints ONLY the official calculation results summary.
           Suppresses website chrome, inputs, educational articles, and FAQs.
           ========================================================================== */
        @media print {
            /* 1. Hide website chrome, navigation, ads, sidebars, and popups */
            header, footer, nav, aside,
            .no-print, .ad-slot, .ad-unit, [id*="ad-slot"], [id*="adSlot"], [class*="ad-slot"],
            [id*="adblock"], [id*="adblockRecovery"], #adblock-banner, #adblock-recovery,
            #floatingBar, #floating-bar, #mobileBottomNav, #toast, #toastNotification, .toast-notify,
            #shimmerOverlay, .shimmer, .shimmer-active,
            .preset-btn, .tab-btn, .tab-trigger, .tab-nav-btn, .tab-btn-wrapper, .tab-buttons, #tabButtons,
            .mode-btn, button, .btn-action, #presets-container, #preset-container,
            .lead-box, [id*="lead-box"], [id*="leadBox"], [id*="email-report"],
            .lg\\:col-span-4, .lg\\:col-span-5, .w-full.lg\\:w-1\\/3, aside {
                display: none !important;
            }

            /* 2. Hide all calculation input forms and controls */
            form, [id*="calc-form"], [id*="calcForm"], [id*="calculatorInputs"], [id*="inputs"],
            [id*="calculator-form"], [id*="bodyFatForm"], [id*="bmiForm"], [id*="iraForm"],
            [id*="rothForm"], [id*="mutualFundForm"], [id*="rmdForm"], [id*="discount-form"],
            [id*="loan-form"], [id*="savings-form"], [id*="lead-form"] {
                display: none !important;
            }

            /* 3. Hide all SEO educational articles, guides, and FAQ accordions */
            article, [id*="seo-article"], .prose, .faq-section, #faq-accordion, #faq-container,
            #faqSection, details, .faq-item, [id*="faq"] {
                display: none !important;
            }

            /* 4. Reset page styling for pristine high-contrast print */
            body {
                background: #ffffff !important;
                color: #000000 !important;
                padding: 0 !important;
                margin: 0 !important;
                font-size: 11pt !important;
            }

            .dark, .dark body {
                background: #ffffff !important;
                color: #000000 !important;
            }

            main, .max-w-7xl, .lg\\:col-span-8, .lg\\:col-span-7, .col-span-12, .w-full.lg\\:w-2\\/3 {
                max-width: 100% !important;
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
                display: block !important;
            }

            .grid {
                display: block !important;
                width: 100% !important;
                margin: 0 !important;
                padding: 0 !important;
            }

            /* 5. Force the Calculation Results Container to be the ONLY visible document */
            #resultsSection, #resultsArea, #resultsContainer, #resultsWrapper, #resultsCard,
            #results-section, #results-container, #results-card, #output-container, #summaryTab,
            #pane-summary, #tab-summary, #tabSummary, .results-card, .output-card,
            .lg\\:col-span-7, .lg\\:col-span-8, .w-full.lg\\:w-2\\/3 {
                display: block !important;
                visibility: visible !important;
                width: 100% !important;
                border: 1px solid #cbd5e1 !important;
                border-radius: 0.5rem !important;
                padding: 1.5rem !important;
                margin: 0 !important;
                box-shadow: none !important;
                background: #ffffff !important;
                color: #0f172a !important;
                page-break-inside: avoid !important;
            }

            /* 6. Format clean print tables and charts */
            table {
                width: 100% !important;
                border-collapse: collapse !important;
            }
            th, td {
                border-bottom: 1px solid #e2e8f0 !important;
                padding: 6px 8px !important;
                color: #0f172a !important;
            }
            canvas {
                max-width: 100% !important;
                height: auto !important;
            }
        }
"""

PRINT_CORE_JS = """
    <!-- CalcWorld Universal Print Core Engine -->
    <script id="calcworld-print-core">
    (function() {
        window.printReport = function() {
            try {
                const printTrigger = document.querySelector('[data-tab="tab-print"], [data-tab="print"], [data-target="tab-print"], [data-tab-target="tab-print"], [data-target="#tab-print"], [onclick*="tab-print"], [onclick*="\'print\'"]');
                if (printTrigger) {
                    printTrigger.click();
                } else if (typeof switchTab === 'function') {
                    try { switchTab('print'); } catch(e) { try { switchTab('tab-print'); } catch(e2) {} }
                } else if (typeof showTab === 'function') {
                    try { showTab('print'); } catch(e) { try { showTab('tab-print'); } catch(e2) {} }
                }
            } catch(e) {}

            const updaters = ['updatePrintTab', 'updatePrintReport', 'renderPrintReport', 'generatePrintReport', 'updatePrintView', 'updatePrintDate', 'updatePrintReportFields'];
            updaters.forEach(fn => {
                if (typeof window[fn] === 'function') {
                    try { window[fn](); } catch(e) {}
                }
            });

            setTimeout(function() {
                window.print();
            }, 60);
        };

        window.addEventListener('beforeprint', function() {
            try {
                const printTrigger = document.querySelector('[data-tab="tab-print"], [data-tab="print"], [data-target="tab-print"], [data-tab-target="tab-print"], [data-target="#tab-print"], [onclick*="tab-print"], [onclick*="\'print\'"]');
                if (printTrigger && !printTrigger.classList.contains('active')) {
                    printTrigger.click();
                } else if (typeof switchTab === 'function') {
                    try { switchTab('print'); } catch(e) { try { switchTab('tab-print'); } catch(e2) {} }
                }
            } catch(e) {}

            const updaters = ['updatePrintTab', 'updatePrintReport', 'renderPrintReport', 'generatePrintReport', 'updatePrintView', 'updatePrintDate', 'updatePrintReportFields'];
            updaters.forEach(fn => {
                if (typeof window[fn] === 'function') {
                    try { window[fn](); } catch(e) {}
                }
            });

            const dateElems = document.querySelectorAll('#printDate, #print-date, #printReportDate, #printTimestamp, #print-timestamp, #printGeneratedDate, #report-date-stamp');
            const nowStr = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' });
            dateElems.forEach(el => {
                if (el && !el.textContent.trim()) el.textContent = nowStr;
            });
        });
    })();
    </script>
"""

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    has_ptab = bool(PRINT_TAB_REGEX.search(content) or PRINT_CARD_REGEX.search(content))
    new_css = generate_print_css(has_ptab)

    # Replace existing @media print blocks
    matches = find_media_print(content)
    if matches:
        # Remove subsequent matches from back to front
        for i in range(len(matches) - 1, 0, -1):
            s, e, _ = matches[i]
            content = content[:s] + content[e:]
        # Replace the first match with our new css
        s0, e0, _ = matches[0]
        content = content[:s0] + new_css + content[e0:]
    else:
        # Insert before </style>
        if '</style>' in content:
            content = content.replace('</style>', new_css + '\n</style>', 1)
        elif '</head>' in content:
            content = content.replace('</head>', f'<style>{new_css}</style>\n</head>', 1)

    # Inject print core engine if not present
    if 'id="calcworld-print-core"' not in content:
        if '</body>' in content:
            content = content.replace('</body>', PRINT_CORE_JS + '\n</body>', 1)
        else:
            content += PRINT_CORE_JS

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return has_ptab

def main():
    files = sorted(glob.glob(os.path.join(ONEDRIVE_CALC_DIR, '*.html')))
    print(f"Deploying Universal Print Isolation across {len(files)} calculators in OneDrive...")

    type1_count = 0
    type2_count = 0

    for f in files:
        has_ptab = process_file(f)
        if has_ptab:
            type1_count += 1
        else:
            type2_count += 1

    print(f"OneDrive Deployment Complete:")
    print(f"  - Type 1 (Tabbed Print Dossier): {type1_count} calculators")
    print(f"  - Type 2 (Results Card Report): {type2_count} calculators")

    # Now synchronize to Desktop directory if it exists
    if os.path.exists(DESKTOP_CALC_DIR):
        print(f"\nSynchronizing to Desktop directory: {DESKTOP_CALC_DIR}...")
        copied = 0
        for f in files:
            dest = os.path.join(DESKTOP_CALC_DIR, os.path.basename(f))
            shutil.copy2(f, dest)
            copied += 1
        print(f"Synchronized {copied} calculators to Desktop successfully!")
    else:
        print(f"\nDesktop path {DESKTOP_CALC_DIR} not found, skipped.")

if __name__ == '__main__':
    main()

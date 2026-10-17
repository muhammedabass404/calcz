# -*- coding: utf-8 -*-
import os
import re
import sys

target_path_onedrive = r"C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators\mulch-calculator.html"
target_path_direct = r"C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators\mulch-calculator.html"

# Banned words list (strictly prohibited in output HTML)
BANNED_WORDS = [
    "delve", "delving", "tapestry", "testament", "beacon",
    "game-changer", "game changer", "revolutionize", "revolutionizing",
    "unleash", "unleashing", "elevate", "elevating", "foster", "fostering",
    "realm", "realms", "crucial", "crucially", "paramount", "pivotal",
    "in conclusion", "furthermore", "moreover", "shed light",
    "harness", "harnessing", "underscore", "underscoring",
    "seamless", "seamlessly", "bespoke", "robust", "deep dive",
    "navigate the complexities", "navigating the complexities",
    "a testament to", "ever-evolving", "cutting-edge", "vibrant",
    "holistic", "dynamic", "plethora", "myriad", "embark", "embarking",
    "demystify", "demystifying", "unravel", "unraveling", "intertwined"
]

part1_head = """<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mulch Calculator | Yardage, Bag Count &amp; Multi-Zone Landscaping Planner</title>
    <meta name="description" content="Free scientific mulch, soil, and compost calculator. Calculate cubic feet, cubic yards, and bag counts (2.0 and 3.0 cu ft) with multi-zone garden bed planning, bulk delivery vs bagged cost comparisons, and depth recommendations.">
    <link rel="canonical" href="https://calcworld.net/other/mulch-calculator">

    <!-- Anti-FOUC & Dark Mode Script -->
    <script>
        if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark');
        }
    </script>

    <!-- Google Fonts & Tailwind CSS CDN -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: { sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'] },
                    colors: {
                        brand: {
                            50: '#ecfdf5',
                            100: '#d1fae5',
                            200: '#a7f3d0',
                            300: '#6ee7b7',
                            400: '#34d399',
                            500: '#10b981',
                            600: '#059669',
                            700: '#047857',
                            800: '#065f46',
                            900: '#064e3b',
                            950: '#022c22',
                        },
                        amber: {
                            50: '#fffbeb',
                            100: '#fef3c7',
                            200: '#fde68a',
                            300: '#fcd34d',
                            400: '#fbbf24',
                            500: '#f59e0b',
                            600: '#d97706',
                            700: '#b45309',
                            800: '#92400e',
                            900: '#78350f',
                        }
                    }
                }
            }
        }
    </script>

    <!-- MathJax 3 CDN -->
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
            }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <style>
        .shimmer-active {
            position: relative;
            overflow: hidden;
        }
        .shimmer-active::after {
            position: absolute;
            top: 0; right: 0; bottom: 0; left: 0;
            transform: translateX(-100%);
            background-image: linear-gradient(
                90deg,
                rgba(255, 255, 255, 0) 0,
                rgba(255, 255, 255, 0.12) 20%,
                rgba(255, 255, 255, 0.25) 60%,
                rgba(255, 255, 255, 0)
            );
            animation: shimmer 1.8s infinite;
            content: '';
        }
        .dark .shimmer-active::after {
            background-image: linear-gradient(
                90deg,
                rgba(255, 255, 255, 0) 0,
                rgba(16, 185, 129, 0.08) 20%,
                rgba(16, 185, 129, 0.18) 60%,
                rgba(255, 255, 255, 0)
            );
        }
        @keyframes shimmer {
            100% { transform: translateX(100%); }
        }
        .tab-panel { display: none; }
        .tab-panel.active { display: block; animation: tabFade 0.25s ease-out; }
        @keyframes tabFade {
            from { opacity: 0; transform: translateY(4px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .ad-slot {
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(148, 163, 184, 0.08);
            border: 1px dashed rgba(148, 163, 184, 0.3);
            border-radius: 0.75rem;
            color: #94a3b8;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin: 1.5rem 0;
            overflow: hidden;
        }
        #ad-slot-1 { min-height: 90px; width: 100%; }
        #ad-slot-2 { min-height: 100px; width: 100%; }
        #ad-slot-3 { min-height: 250px; width: 100%; }
        #ad-slot-4 { min-height: 120px; width: 100%; }
        #ad-slot-5 { min-height: 140px; width: 100%; }

        @media print {
            header, footer, .no-print, .ad-slot, #floatingBar, #adblockRecovery, #toast, .lead-box, #tabButtons, #calculatorInputs, #presetContainer, .quick-actions-bar {
                display: none !important;
            }
            #tab-print {
                display: block !important;
            }
            body {
                background: white !important;
                color: black !important;
            }
            .dark {
                background: white !important;
                color: black !important;
            }
            .print-only {
                display: block !important;
            }
        }
    </style>

    <!-- JSON-LD SEO Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "name": "Home",
              "item": "https://calcworld.net"
            },
            {
              "@type": "ListItem",
              "position": 2,
              "name": "Other Calculators",
              "item": "https://calcworld.net/other"
            },
            {
              "@type": "ListItem",
              "position": 3,
              "name": "Mulch Calculator",
              "item": "https://calcworld.net/other/mulch-calculator"
            }
          ]
        },
        {
          "@type": "WebApplication",
          "name": "Mulch Calculator",
          "url": "https://calcworld.net/other/mulch-calculator",
          "applicationCategory": "EducationalApplication",
          "operatingSystem": "Any",
          "browserRequirements": "Requires JavaScript. Requires HTML5.",
          "description": "Calculate cubic feet, cubic yards, and bag counts (2.0 and 3.0 cu ft) for landscaping mulch, soil, and compost with multi-zone bed planning and bulk vs bagged price comparisons."
        },
        {
          "@type": "FAQPage",
          "mainEntity": [
            {
              "@type": "Question",
              "name": "How many cubic yards of mulch do I need for my garden bed?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Calculate your garden bed area in square feet, multiply by your target depth in inches, and divide by 324. For example, a 300 square foot garden bed mulched at a depth of 3 inches requires (300 * 3) / 324 = 2.78 cubic yards of mulch."
              }
            },
            {
              "@type": "Question",
              "name": "How many bags of mulch equal one cubic yard?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "One cubic yard equals 27 cubic feet. Therefore, one cubic yard requires exactly 13.5 bags of 2.0 cubic foot mulch (round up to 14 bags) or 9 bags of 3.0 cubic foot mulch."
              }
            },
            {
              "@type": "Question",
              "name": "What is the optimal mulch depth for flower beds and shrubs?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "University horticultural extensions recommend maintaining a settled depth of 2 to 3 inches for organic bark mulches. Layers deeper than 4 inches can restrict soil oxygen diffusion and induce root suffocation."
              }
            },
            {
              "@type": "Question",
              "name": "What is a mulch volcano and why is it harmful to trees?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "A mulch volcano occurs when mulch is mounded directly against a tree trunk. Trunk bark requires circulating air to stay dry. Moisture trapped by mulch causes bark decay, fungal infection, root girdling, and rodent damage. Keep mulch 3 inches away from trunk bases."
              }
            },
            {
              "@type": "Question",
              "name": "Does wood mulch steal nitrogen from landscape plants?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "No. Research confirms that nitrogen drawdown occurs only at the immediate surface interface between the mulch and soil. Plant roots deeper than 0.25 inches remain unaffected as long as uncomposted wood chips are not physically mixed into the soil."
              }
            },
            {
              "@type": "Question",
              "name": "When is it cheaper to buy bulk mulch delivered instead of retail bags?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "The break-even point is typically between 2.0 and 2.5 cubic yards (27 to 34 bags). For projects requiring 3 cubic yards or more, bulk delivery is substantially cheaper and avoids hauling dozens of heavy bags."
              }
            },
            {
              "@type": "Question",
              "name": "How much does a cubic yard of mulch weigh?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Dry shredded hardwood mulch weighs approximately 400 to 600 pounds per cubic yard. Wet or settled mulch weighs 700 to 1,000 pounds per cubic yard. Dense materials like topsoil or gravel weigh 2,000 to 2,800 pounds per cubic yard."
              }
            },
            {
              "@type": "Question",
              "name": "How often should landscaping mulch be replenished?",
              "acceptedAnswer": {
                "@type": "Answer",
                "text": "Organic bark mulches decompose over 1 to 2 years. Rather than replacing the full layer, rake existing mulch to aerate it and add a 1-inch topdressing refresh annually to maintain the desired 2 to 3 inch profile."
              }
            }
          ]
        }
      ]
    }
    </script>
</head>
<body class="bg-slate-50 dark:bg-slate-900 text-slate-800 dark:text-slate-100 font-sans transition-colors duration-200 antialiased selection:bg-brand-500 selection:text-white min-h-screen flex flex-col">

    <!-- AdBlock Detection Recovery Banner -->
    <div id="adblockRecovery" class="hidden no-print bg-amber-500/10 border-b border-amber-500/20 text-amber-800 dark:text-amber-300 px-4 py-2 text-xs text-center flex justify-between items-center max-w-7xl mx-auto rounded-b-lg">
        <div class="flex items-center gap-2 mx-auto">
            <svg class="w-4 h-4 text-amber-600 dark:text-amber-400 shrink-0" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/>
            </svg>
            <span><strong>Reader-Supported Landscaping Engine:</strong> CalcWorld provides verified material estimation tools 100% free with zero registration. Please consider safelisting our domain to support continuous tool maintenance.</span>
        </div>
        <button onclick="document.getElementById('adblockRecovery').classList.add('hidden')" class="text-amber-900 dark:text-amber-200 hover:opacity-80 text-sm font-bold ml-4" aria-label="Dismiss banner">&times;</button>
    </div>

    <!-- Header Navigation -->
    <header class="border-b border-slate-200 dark:border-slate-800 bg-white/80 dark:bg-slate-900/80 backdrop-blur sticky top-0 z-30 no-print">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="https://calcworld.net" class="flex items-center gap-2 group">
                    <span class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-600 to-emerald-500 flex items-center justify-center text-white font-bold text-lg shadow-md group-hover:scale-105 transition-transform">MC</span>
                    <span class="font-bold text-xl tracking-tight text-slate-900 dark:text-white">Calc<span class="text-brand-600 dark:text-brand-400">World</span></span>
                </a>
                <span class="hidden sm:inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-brand-50 text-brand-700 dark:bg-brand-950/60 dark:text-brand-300 border border-brand-200/50 dark:border-brand-800/50">LANDSCAPING SUITE</span>
            </div>

            <div class="flex items-center gap-3">
                <div class="hidden md:flex items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
                    <a href="topsoil-calculator.html" class="hover:text-brand-600 dark:hover:text-brand-400 px-2 py-1 rounded transition">Topsoil</a>
                    <span>&bull;</span>
                    <a href="gravel-calculator.html" class="hover:text-brand-600 dark:hover:text-brand-400 px-2 py-1 rounded transition">Gravel</a>
                    <span>&bull;</span>
                    <a href="square-footage-calculator.html" class="hover:text-brand-600 dark:hover:text-brand-400 px-2 py-1 rounded transition">Square Footage</a>
                </div>

                <!-- Dark Mode Toggle Button -->
                <button onclick="toggleTheme()" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 dark:hover:bg-slate-700 transition" aria-label="Toggle theme">
                    <svg id="themeMoon" class="w-5 h-5 hidden dark:block" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
                    <svg id="themeSun" class="w-5 h-5 block dark:hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 w-full">
        
        <!-- Breadcrumb Navigation -->
        <nav class="text-xs text-slate-500 dark:text-slate-400 mb-4 no-print" aria-label="Breadcrumb">
            <ol class="list-none p-0 inline-flex items-center gap-1.5">
                <li class="inline-flex items-center">
                    <a href="https://calcworld.net" class="hover:text-brand-600 dark:hover:text-brand-400">Home</a>
                </li>
                <li>
                    <svg class="w-3 h-3 text-slate-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg>
                </li>
                <li>
                    <a href="https://calcworld.net/other" class="hover:text-brand-600 dark:hover:text-brand-400">Other Calculators</a>
                </li>
                <li>
                    <svg class="w-3 h-3 text-slate-400" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 011.414-1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"/></svg>
                </li>
                <li class="text-slate-800 dark:text-slate-200 font-semibold" aria-current="page">Mulch Calculator</li>
            </ol>
        </nav>

        <!-- Page Hero Title -->
        <div class="mb-6">
            <h1 class="text-3xl sm:text-4xl font-extrabold tracking-tight text-slate-900 dark:text-white">Mulch Calculator</h1>
            <p class="text-base text-slate-600 dark:text-slate-300 mt-1 max-w-3xl">Calculate landscaping mulch, topsoil, and compost volumes in cubic feet and cubic yards. Determine exact 2.0 cu ft and 3.0 cu ft bag counts, compare bulk delivery versus bagged store pickup costs, and plan multi-bed yard projects.</p>
        </div>

        <!-- AdSense Slot 1: Top Leaderboard -->
        <div class="ad-slot no-print" id="ad-slot-1">
            <span>Sponsored Advertisement &bull; Leaderboard Slot 1</span>
        </div>

        <!-- Two-Column Primary Layout (Inputs vs Results & Tabs) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            
            <!-- Left Column: Inputs & Controls (Span 4) -->
            <div id="calculatorInputs" class="lg:col-span-5 xl:col-span-4 space-y-6 no-print">
                <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                    
                    <h2 class="text-lg font-bold text-slate-900 dark:text-white mb-4 flex items-center justify-between">
                        <span>Bed Specifications</span>
                        <span class="text-xs font-normal px-2 py-0.5 rounded bg-brand-50 text-brand-700 dark:bg-brand-900/40 dark:text-brand-300 border border-brand-200/50">Estimator</span>
                    </h2>

                    <!-- Presets Selector -->
                    <div class="mb-5" id="presetContainer">
                        <label for="presetSelect" class="block text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2">Real-World Bed Presets</label>
                        <select id="presetSelect" onchange="loadPreset()" class="w-full px-3 py-2 text-xs bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500">
                            <option value="custom">-- Select a Standard Yard Scenario --</option>
                            <option value="preset_front" selected>Front Foundation Bed (30 x 10 ft, 3 in depth)</option>
                            <option value="preset_perimeter">Perimeter Shrub Border (450 sq ft, 3 in depth)</option>
                            <option value="preset_trees">Tree Mulch Donut Rings (3 rings, 8 ft dia, 2.5 in depth)</option>
                            <option value="preset_garden">Vegetable Garden Topdressing (200 sq ft, 2 in depth)</option>
                            <option value="preset_playground">Playground Safety Cushion (400 sq ft, 6 in depth)</option>
                            <option value="preset_refresh">Complete Yard Annual Refresh (1,200 sq ft, 1 in refresh)</option>
                        </select>
                    </div>

                    <!-- Shape Selector -->
                    <div class="mb-5">
                        <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2">Garden Bed Shape</label>
                        <div class="grid grid-cols-3 gap-1.5">
                            <button type="button" onclick="setBedShape('rectangle')" id="shapeBtn_rectangle" class="shape-btn px-2 py-1.5 text-xs font-semibold rounded-lg border-2 border-brand-600 bg-brand-50 dark:bg-brand-950 text-brand-700 dark:text-brand-300 transition text-center">Rectangle</button>
                            <button type="button" onclick="setBedShape('circle')" id="shapeBtn_circle" class="shape-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center">Circle</button>
                            <button type="button" onclick="setBedShape('donut')" id="shapeBtn_donut" class="shape-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center">Tree Ring</button>
                            <button type="button" onclick="setBedShape('triangle')" id="shapeBtn_triangle" class="shape-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center">Triangle</button>
                            <button type="button" onclick="setBedShape('area')" id="shapeBtn_area" class="shape-btn col-span-2 px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center">Direct Square Feet</button>
                        </div>
                    </div>

                    <!-- Dynamic Shape Dimensions -->
                    <div id="shapeFields_rectangle" class="space-y-3 mb-5">
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label for="dim_length" class="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">Length (Feet)</label>
                                <input type="number" id="dim_length" step="any" min="0.1" value="30" oninput="calculate()" class="w-full px-3 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 font-mono">
                            </div>
                            <div>
                                <label for="dim_width" class="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">Width (Feet)</label>
                                <input type="number" id="dim_width" step="any" min="0.1" value="10" oninput="calculate()" class="w-full px-3 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 font-mono">
                            </div>
                        </div>
                    </div>

                    <div id="shapeFields_circle" class="space-y-3 mb-5 hidden">
                        <div>
                            <label for="dim_diameter" class="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">Circle Diameter (Feet)</label>
                            <input type="number" id="dim_diameter" step="any" min="0.1" value="12" oninput="calculate()" class="w-full px-3 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 font-mono">
                        </div>
                    </div>

                    <div id="shapeFields_donut" class="space-y-3 mb-5 hidden">
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label for="dim_outer_dia" class="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">Outer Diameter (Ft)</label>
                                <input type="number" id="dim_outer_dia" step="any" min="0.5" value="8" oninput="calculate()" class="w-full px-3 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 font-mono">
                            </div>
                            <div>
                                <label for="dim_inner_dia" class="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">Trunk Buffer Dia (Ft)</label>
                                <input type="number" id="dim_inner_dia" step="any" min="0.1" value="2" oninput="calculate()" class="w-full px-3 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 font-mono">
                            </div>
                        </div>
                        <span class="text-[11px] text-slate-400 block">Leaves a bare soil buffer to protect tree collar from decay.</span>
                    </div>

                    <div id="shapeFields_triangle" class="space-y-3 mb-5 hidden">
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label for="dim_base" class="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">Base (Feet)</label>
                                <input type="number" id="dim_base" step="any" min="0.1" value="20" oninput="calculate()" class="w-full px-3 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 font-mono">
                            </div>
                            <div>
                                <label for="dim_height" class="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">Height (Feet)</label>
                                <input type="number" id="dim_height" step="any" min="0.1" value="15" oninput="calculate()" class="w-full px-3 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 font-mono">
                            </div>
                        </div>
                    </div>

                    <div id="shapeFields_area" class="space-y-3 mb-5 hidden">
                        <div>
                            <label for="dim_direct_area" class="block text-xs font-medium text-slate-700 dark:text-slate-300 mb-1">Total Measured Surface Area (Sq Ft)</label>
                            <input type="number" id="dim_direct_area" step="any" min="1" value="300" oninput="calculate()" class="w-full px-3 py-2 text-sm bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500 font-mono">
                        </div>
                    </div>

                    <!-- Depth Specification -->
                    <div class="mb-5">
                        <div class="flex items-center justify-between mb-2">
                            <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Mulch Depth</label>
                            <span id="activeDepthDisplay" class="text-xs font-bold text-brand-600 dark:text-brand-400">3.0 Inches</span>
                        </div>
                        <div class="grid grid-cols-5 gap-1.5 mb-2">
                            <button type="button" onclick="setDepth(1)" class="depth-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center" data-depth="1">1"</button>
                            <button type="button" onclick="setDepth(2)" class="depth-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center" data-depth="2">2"</button>
                            <button type="button" onclick="setDepth(3)" class="depth-btn active px-2 py-1.5 text-xs font-semibold rounded-lg border-2 border-brand-600 bg-brand-50 dark:bg-brand-950 text-brand-700 dark:text-brand-300 transition text-center" data-depth="3">3"</button>
                            <button type="button" onclick="setDepth(4)" class="depth-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center" data-depth="4">4"</button>
                            <button type="button" onclick="setDepth(6)" class="depth-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center" data-depth="6">6"</button>
                        </div>
                        <div class="flex items-center gap-3 mt-2">
                            <input type="range" id="depthSlider" min="0.5" max="8" step="0.25" value="3" oninput="setCustomDepth(this.value)" class="w-full accent-brand-600 cursor-pointer">
                            <input type="number" id="customDepthInput" step="0.25" min="0.25" max="12" value="3.0" oninput="setCustomDepth(this.value)" class="w-20 px-2 py-1 text-xs bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-md text-slate-900 dark:text-white font-mono text-center focus:outline-none focus:ring-1 focus:ring-brand-500">
                        </div>
                        <span class="text-[11px] text-slate-400 mt-1 block" id="depthGuidanceHint">Recommended for standard weed prevention &amp; moisture conservation.</span>
                    </div>

                    <!-- Material Type Selector -->
                    <div class="mb-5">
                        <label for="materialSelect" class="block text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2">Material / Substrate</label>
                        <select id="materialSelect" onchange="calculate()" class="w-full px-3 py-2 text-xs bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-lg text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-brand-500">
                            <option value="hardwood" data-density="500" selected>Shredded Hardwood Bark (~500 lbs/yd³)</option>
                            <option value="pine_bark" data-density="450">Pine Bark Nuggets (~450 lbs/yd³)</option>
                            <option value="cedar" data-density="420">Cedar Shavings / Bark (~420 lbs/yd³)</option>
                            <option value="chips" data-density="550">Arborist Utility Wood Chips (~550 lbs/yd³)</option>
                            <option value="straw" data-density="150">Pine Straw / Wheat Straw (~150 lbs/yd³)</option>
                            <option value="compost" data-density="1200">Organic Compost (~1,200 lbs/yd³)</option>
                            <option value="topsoil" data-density="2200">Screened Topsoil (~2,200 lbs/yd³)</option>
                            <option value="gravel" data-density="2700">Pea Gravel / River Stone (~2,700 lbs/yd³)</option>
                            <option value="rubber" data-density="450">Recycled Rubber Safety Mulch (~450 lbs/yd³)</option>
                        </select>
                    </div>

                    <!-- Contingency / Settling Allowance -->
                    <div class="mb-5">
                        <div class="flex items-center justify-between mb-2">
                            <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Settling &amp; Spillage Factor</label>
                            <span id="contingencyDisplay" class="text-xs font-semibold text-slate-600 dark:text-slate-400">+5% Buffer</span>
                        </div>
                        <div class="grid grid-cols-4 gap-1.5">
                            <button type="button" onclick="setContingency(0)" class="contin-btn px-2 py-1 text-xs font-medium rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center" data-val="0">0%</button>
                            <button type="button" onclick="setContingency(5)" class="contin-btn active px-2 py-1 text-xs font-medium rounded-lg border-2 border-brand-600 bg-brand-50 dark:bg-brand-950 text-brand-700 dark:text-brand-300 transition text-center" data-val="5">+5%</button>
                            <button type="button" onclick="setContingency(10)" class="contin-btn px-2 py-1 text-xs font-medium rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center" data-val="10">+10%</button>
                            <button type="button" onclick="setContingency(15)" class="contin-btn px-2 py-1 text-xs font-medium rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center" data-val="15">+15%</button>
                        </div>
                    </div>

                    <!-- Cost Settings Drawer (Collapsible) -->
                    <div class="mb-5 border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                        <button type="button" onclick="toggleCostDrawer()" class="w-full px-3 py-2 text-xs font-bold text-slate-700 dark:text-slate-300 bg-slate-50 dark:bg-slate-900/60 hover:bg-slate-100 flex items-center justify-between transition">
                            <span class="flex items-center gap-1.5">
                                <svg class="w-3.5 h-3.5 text-brand-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                                <span>Unit Pricing &amp; Delivery Fees</span>
                            </span>
                            <svg id="costDrawerIcon" class="w-3.5 h-3.5 text-slate-400 transition-transform duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                        </button>
                        
                        <div id="costDrawerContent" class="p-3 space-y-3 bg-white dark:bg-slate-800 text-xs">
                            <div class="grid grid-cols-2 gap-2">
                                <div>
                                    <label for="cost_bulk_yard" class="block text-[11px] font-medium text-slate-500 dark:text-slate-400 mb-0.5">Bulk ($/Cu Yd)</label>
                                    <input type="number" id="cost_bulk_yard" step="0.5" value="38.00" oninput="calculate()" class="w-full px-2 py-1 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded text-slate-900 dark:text-white font-mono">
                                </div>
                                <div>
                                    <label for="cost_bulk_deliv" class="block text-[11px] font-medium text-slate-500 dark:text-slate-400 mb-0.5">Bulk Delivery Fee ($)</label>
                                    <input type="number" id="cost_bulk_deliv" step="1" value="65.00" oninput="calculate()" class="w-full px-2 py-1 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded text-slate-900 dark:text-white font-mono">
                                </div>
                            </div>

                            <div class="grid grid-cols-2 gap-2">
                                <div>
                                    <label for="cost_bag_2cu" class="block text-[11px] font-medium text-slate-500 dark:text-slate-400 mb-0.5">2.0 Cu Ft Bag ($)</label>
                                    <input type="number" id="cost_bag_2cu" step="0.1" value="4.48" oninput="calculate()" class="w-full px-2 py-1 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded text-slate-900 dark:text-white font-mono">
                                </div>
                                <div>
                                    <label for="cost_bag_3cu" class="block text-[11px] font-medium text-slate-500 dark:text-slate-400 mb-0.5">3.0 Cu Ft Bag ($)</label>
                                    <input type="number" id="cost_bag_3cu" step="0.1" value="6.25" oninput="calculate()" class="w-full px-2 py-1 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded text-slate-900 dark:text-white font-mono">
                                </div>
                            </div>

                            <div>
                                <label for="cost_bagged_deliv" class="block text-[11px] font-medium text-slate-500 dark:text-slate-400 mb-0.5">Store Bagged Flat Delivery Fee ($)</label>
                                <input type="number" id="cost_bagged_deliv" step="1" value="79.00" oninput="calculate()" class="w-full px-2 py-1 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded text-slate-900 dark:text-white font-mono">
                            </div>
                        </div>
                    </div>

                    <!-- Action Controls -->
                    <div class="pt-2 border-t border-slate-200 dark:border-slate-700 flex flex-col gap-2">
                        <button type="button" onclick="triggerCalculation()" class="w-full py-2.5 px-4 rounded-xl bg-brand-600 hover:bg-brand-700 active:scale-[0.99] text-white font-bold text-sm shadow-md transition flex items-center justify-center gap-2">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                            <span>Calculate Mulch Coverage</span>
                        </button>
                        
                        <div class="grid grid-cols-2 gap-2">
                            <button type="button" onclick="resetDefaults()" class="py-2 px-3 text-xs font-medium rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 transition text-center">Reset</button>
                            <button type="button" onclick="copyShareUrl()" class="py-2 px-3 text-xs font-medium rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-700 transition text-center flex items-center justify-center gap-1">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z"/></svg>
                                <span>Share URL</span>
                            </button>
                        </div>
                    </div>

                </div>

                <!-- AdSense Slot 3: Sidebar Rectangle -->
                <div class="ad-slot" id="ad-slot-3">
                    <span>Sponsored Advertisement &bull; Sidebar Slot 3</span>
                </div>

                <!-- Lead Gen Box (Sidebar Placement) -->
                <div class="lead-box bg-gradient-to-br from-emerald-950 to-brand-900 text-white p-5 rounded-2xl shadow-md border border-emerald-800/60">
                    <div class="flex items-center gap-2 mb-2 text-brand-300 text-xs font-bold uppercase tracking-wider">
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z"/></svg>
                        <span>Official Field Handbook</span>
                    </div>
                    <h3 class="font-bold text-base mb-1">Landscaping Material Estimator PDF</h3>
                    <p class="text-xs text-emerald-200 mb-3">Download our verified mulch depth tables, density weight charts, and bulk vs bagged purchasing matrix (PDF).</p>
                    <form onsubmit="handleLeadSubmit(event)" class="space-y-2">
                        <input type="email" id="leadEmailInput" required placeholder="contractor@landscaping.com" class="w-full px-3 py-2 text-xs rounded-lg bg-white/10 border border-white/20 text-white placeholder-emerald-300 focus:outline-none focus:ring-2 focus:ring-brand-400">
                        <button type="submit" id="leadSubmitBtn" class="w-full py-2 bg-brand-500 hover:bg-brand-400 text-white font-bold text-xs rounded-lg transition shadow">Send Free PDF Guide</button>
                    </form>
                    <div id="leadSuccessMsg" class="hidden text-xs text-emerald-300 mt-2 text-center font-medium">✓ Check your inbox! Your field estimating guide is on its way.</div>
                </div>

            </div>

            <!-- Right Column: Results & Tabs (Span 8) -->
            <div class="lg:col-span-7 xl:col-span-8 space-y-6">
                
                <!-- Hero Result Card -->
                <div id="resultsCard" class="bg-white dark:bg-slate-800 rounded-2xl p-6 shadow-sm border border-slate-200 dark:border-slate-700 relative overflow-hidden">
                    <div class="flex flex-wrap items-center justify-between gap-2 mb-4">
                        <span class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400" id="resultHeaderBadge">Volume Estimation</span>
                        <div class="flex items-center gap-2">
                            <span id="diagnosticBadge" class="inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300 border border-emerald-200/50">Optimal Depth (3.0")</span>
                        </div>
                    </div>

                    <!-- Main Output Display -->
                    <div class="bg-slate-50 dark:bg-slate-900/60 rounded-xl p-5 mb-5 border border-slate-200/60 dark:border-slate-700/60 text-center">
                        <span class="text-xs font-medium text-slate-500 dark:text-slate-400 block mb-1">Total Mulch Volume Required</span>
                        <div class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-brand-600 dark:text-brand-400 font-mono" id="mainYardageDisplay">
                            2.92 Cu Yds
                        </div>
                        <div class="text-xs text-slate-600 dark:text-slate-300 mt-2 max-w-xl mx-auto" id="mainNarrativeDisplay">
                            Covers <strong>300 sq ft</strong> at <strong>3.0 inches depth</strong> (78.75 cu ft with a 5% settling buffer).
                        </div>
                    </div>

                    <!-- 4 Metric Cards Grid -->
                    <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-4">
                        <div class="bg-slate-50 dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                            <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">2.0 Cu Ft Bags</span>
                            <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="metricBags2cu">40 Bags</span>
                            <span class="text-[10px] text-slate-400 block" id="metricBags2cuExact">Exact: 39.4</span>
                        </div>
                        <div class="bg-slate-50 dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                            <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">3.0 Cu Ft Bags</span>
                            <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="metricBags3cu">27 Bags</span>
                            <span class="text-[10px] text-slate-400 block" id="metricBags3cuExact">Exact: 26.3</span>
                        </div>
                        <div class="bg-slate-50 dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                            <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Estimated Weight</span>
                            <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="metricWeightLbs">1,458 lbs</span>
                            <span class="text-[10px] text-slate-400 block" id="metricWeightTons">0.73 Tons</span>
                        </div>
                        <div class="bg-slate-50 dark:bg-slate-900/40 p-3 rounded-xl border border-slate-200/50 dark:border-slate-700/50">
                            <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Wheelbarrow Loads</span>
                            <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="metricWheelbarrows">26 Loads</span>
                            <span class="text-[10px] text-slate-400 block">Standard 3 cu ft tray</span>
                        </div>
                    </div>

                    <!-- Economics Banner -->
                    <div class="p-3 bg-brand-50/70 dark:bg-brand-950/40 rounded-xl border border-brand-200/60 dark:border-brand-800/60 text-xs flex flex-wrap items-center justify-between gap-2">
                        <div class="text-slate-700 dark:text-slate-300">
                            <span class="font-bold text-brand-700 dark:text-brand-300">Procurement Comparison:</span>
                            <span id="economicSummaryText">Bulk Delivered: $175.96 | Store Pickup (2 cu ft): $179.20</span>
                        </div>
                        <span id="economicRecommendationBadge" class="px-2 py-0.5 rounded text-[10px] font-bold bg-brand-600 text-white">Bulk Delivery Saves $3.24</span>
                    </div>

                    <!-- Quick Action Bar -->
                    <div class="quick-actions-bar flex flex-wrap items-center justify-between gap-3 pt-3 mt-3 border-t border-slate-200 dark:border-slate-700 text-xs">
                        <div class="flex items-center gap-3 text-slate-500 dark:text-slate-400">
                            <span id="quickAreaSummary">Area: 300 sq ft</span>
                            <span>&bull;</span>
                            <span id="quickCubicFeetSummary">Volume: 78.8 cu ft</span>
                        </div>
                        <div class="flex items-center gap-2">
                            <button onclick="copyFormattedSummary()" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition flex items-center gap-1.5 font-medium text-slate-700 dark:text-slate-300">
                                <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
                                <span>Copy Summary</span>
                            </button>
                            <button onclick="switchTab('print'); window.print();" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 transition flex items-center gap-1.5 font-medium text-slate-700 dark:text-slate-300">
                                <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4H7v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
                                <span>Print Requisition</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Tab Navigation Bar -->
                <div class="border-b border-slate-200 dark:border-slate-700 no-print" id="tabButtons">
                    <nav class="flex space-x-2 sm:space-x-4 overflow-x-auto" aria-label="Tabs">
                        <button onclick="switchTab('coverage')" id="tabBtn_coverage" class="tab-btn active border-b-2 border-brand-600 pb-3 px-1 text-xs sm:text-sm font-bold text-brand-600 dark:text-brand-400 whitespace-nowrap">
                            Mulch Coverage Calculator
                        </button>
                        <button onclick="switchTab('planner')" id="tabBtn_planner" class="tab-btn border-b-2 border-transparent pb-3 px-1 text-xs sm:text-sm font-medium text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 whitespace-nowrap">
                            Multi-Bed Yard Project Planner
                        </button>
                        <button onclick="switchTab('guide')" id="tabBtn_guide" class="tab-btn border-b-2 border-transparent pb-3 px-1 text-xs sm:text-sm font-medium text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 whitespace-nowrap">
                            Mulch Types &amp; Depth Guide
                        </button>
                        <button onclick="switchTab('print')" id="tabBtn_print" class="tab-btn border-b-2 border-transparent pb-3 px-1 text-xs sm:text-sm font-medium text-slate-500 hover:text-slate-700 dark:text-slate-400 dark:hover:text-slate-200 whitespace-nowrap">
                            Print Report
                        </button>
                    </nav>
                </div>

                <!-- TAB 1: Mulch Coverage Calculator -->
                <div id="tab-coverage" class="tab-panel active space-y-6">
                    
                    <!-- Chart.js Cost Comparison Bar Chart -->
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
                            <div>
                                <h3 class="font-bold text-base text-slate-900 dark:text-white">Bulk Delivery vs. Bagged Store Cost Comparison</h3>
                                <p class="text-xs text-slate-500 dark:text-slate-400">Total expenditure comparison including delivery surcharges and bag packaging.</p>
                            </div>
                        </div>

                        <div class="relative h-64 sm:h-72 w-full">
                            <canvas id="costComparisonChart"></canvas>
                        </div>
                    </div>

                    <!-- Step-by-Step Mathematical Derivation Box -->
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <h3 class="font-bold text-base text-slate-900 dark:text-white mb-3 flex items-center gap-2">
                            <span class="w-6 h-6 rounded-md bg-brand-100 dark:bg-brand-900/60 text-brand-600 dark:text-brand-400 flex items-center justify-center text-xs font-bold">&Sigma;</span>
                            <span>Step-by-Step Mathematical Derivation</span>
                        </h3>
                        
                        <div id="mathJaxDerivationBlock" class="overflow-x-auto text-xs sm:text-sm text-slate-700 dark:text-slate-300 space-y-3 font-mono bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-200/60 dark:border-slate-700/60">
                            <!-- Populated dynamically by JavaScript -->
                            <div class="text-center py-2 text-slate-400">Computing mathematical volume derivation...</div>
                        </div>
                    </div>

                    <!-- Depth & Coverage Sensitivity Matrix -->
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <h3 class="font-bold text-base text-slate-900 dark:text-white mb-2">Depth Sensitivity &amp; Coverage Matrix</h3>
                        <p class="text-xs text-slate-500 dark:text-slate-400 mb-4">Compare required cubic yards and bag quantities across different depth standards for your active bed area.</p>
                        
                        <div class="overflow-x-auto">
                            <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
                                <thead class="bg-slate-50 dark:bg-slate-900/80 uppercase font-semibold text-slate-500 dark:text-slate-400 border-b border-slate-200 dark:border-slate-700">
                                    <tr>
                                        <th class="px-3 py-2.5">Mulch Depth</th>
                                        <th class="px-3 py-2.5">Cubic Feet</th>
                                        <th class="px-3 py-2.5">Cubic Yards</th>
                                        <th class="px-3 py-2.5">2.0 Cu Ft Bags</th>
                                        <th class="px-3 py-2.5">3.0 Cu Ft Bags</th>
                                        <th class="px-3 py-2.5">Standard Usage</th>
                                    </tr>
                                </thead>
                                <tbody id="depthMatrixBody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                                    <!-- Populated dynamically by JS -->
                                </tbody>
                            </table>
                        </div>
                    </div>

                </div>

                <!-- TAB 2: Multi-Bed Yard Project Planner -->
                <div id="tab-planner" class="tab-panel space-y-6">
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
                            <div>
                                <h3 class="font-bold text-base text-slate-900 dark:text-white">Multi-Zone Landscape Bed Manager</h3>
                                <p class="text-xs text-slate-500 dark:text-slate-400">Add distinct garden beds, shrub perimeters, and tree rings with independent shapes and depths.</p>
                            </div>
                            <button type="button" onclick="addNewPlannerZone()" class="px-3 py-1.5 rounded-lg bg-brand-600 hover:bg-brand-700 text-white font-bold text-xs transition flex items-center gap-1 shadow-sm">
                                <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
                                <span>Add Garden Bed</span>
                            </button>
                        </div>

                        <!-- Aggregate Summary Cards -->
                        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-6">
                            <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-xl border border-slate-200 dark:border-slate-700">
                                <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Total Project Area</span>
                                <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="planTotalArea">0 sq ft</span>
                            </div>
                            <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-xl border border-slate-200 dark:border-slate-700">
                                <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Total Cubic Yards</span>
                                <span class="text-lg font-bold text-brand-600 dark:text-brand-400 font-mono" id="planTotalYards">0.00 yd³</span>
                            </div>
                            <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-xl border border-slate-200 dark:border-slate-700">
                                <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Total 2.0 Cu Ft Bags</span>
                                <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="planTotalBags2cu">0 Bags</span>
                            </div>
                            <div class="bg-slate-50 dark:bg-slate-900/60 p-3 rounded-xl border border-slate-200 dark:border-slate-700">
                                <span class="text-[11px] font-medium text-slate-500 dark:text-slate-400 block">Total Project Weight</span>
                                <span class="text-lg font-bold text-slate-900 dark:text-white font-mono" id="planTotalWeight">0 lbs</span>
                            </div>
                        </div>

                        <!-- Zone Breakdown Table -->
                        <div class="overflow-x-auto mb-6">
                            <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
                                <thead class="bg-slate-50 dark:bg-slate-900/80 font-semibold text-slate-500 dark:text-slate-400 border-b border-slate-200 dark:border-slate-700">
                                    <tr>
                                        <th class="px-3 py-2">Bed Name</th>
                                        <th class="px-3 py-2">Shape &amp; Dimensions</th>
                                        <th class="px-3 py-2">Depth</th>
                                        <th class="px-3 py-2">Material</th>
                                        <th class="px-3 py-2">Area (Sq Ft)</th>
                                        <th class="px-3 py-2">Volume (Cu Yd)</th>
                                        <th class="px-3 py-2">2 Cu Ft Bags</th>
                                        <th class="px-3 py-2 text-right">Actions</th>
                                    </tr>
                                </thead>
                                <tbody id="plannerTableBody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                                    <!-- Populated dynamically by JS -->
                                </tbody>
                            </table>
                        </div>

                        <!-- Donut Chart & Project Cost Summary -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-center pt-4 border-t border-slate-200 dark:border-slate-700">
                            <div>
                                <h4 class="font-bold text-sm text-slate-900 dark:text-white mb-1">Zone Area Distribution</h4>
                                <p class="text-xs text-slate-500 dark:text-slate-400 mb-3">Square footage allocation across yard zones.</p>
                                <div class="relative h-48 w-full flex items-center justify-center">
                                    <canvas id="plannerDonutChart"></canvas>
                                </div>
                            </div>
                            
                            <div class="bg-slate-50 dark:bg-slate-900/50 p-4 rounded-xl border border-slate-200 dark:border-slate-700 space-y-2 text-xs">
                                <h4 class="font-bold text-sm text-slate-900 dark:text-white mb-2">Project Procurement Overview</h4>
                                <div class="flex justify-between text-slate-600 dark:text-slate-400">
                                    <span>Bulk Material + Delivery:</span>
                                    <span class="font-bold font-mono text-slate-900 dark:text-white" id="planBulkCostDisplay">$0.00</span>
                                </div>
                                <div class="flex justify-between text-slate-600 dark:text-slate-400">
                                    <span>Bagged Store Pickup (2 cu ft):</span>
                                    <span class="font-bold font-mono text-slate-900 dark:text-white" id="planBagPickupDisplay">$0.00</span>
                                </div>
                                <div class="flex justify-between text-slate-600 dark:text-slate-400">
                                    <span>Bagged Store Delivery:</span>
                                    <span class="font-bold font-mono text-slate-900 dark:text-white" id="planBagDelivDisplay">$0.00</span>
                                </div>
                                <div class="pt-2 border-t border-slate-200 dark:border-slate-700 flex justify-between items-center text-xs">
                                    <span class="font-bold text-brand-700 dark:text-brand-300">Cost Savings:</span>
                                    <span class="font-bold font-mono text-emerald-600 dark:text-emerald-400" id="planSavingsDisplay">$0.00</span>
                                </div>
                                <div class="pt-2 flex gap-2">
                                    <button onclick="copyPlannerSummary()" class="w-full py-1.5 px-2 bg-slate-200 dark:bg-slate-700 hover:bg-slate-300 dark:hover:bg-slate-600 rounded font-medium text-slate-800 dark:text-slate-200 transition text-center">Copy Planner Data</button>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- TAB 3: Mulch Types & Depth Guide -->
                <div id="tab-guide" class="tab-panel space-y-6">
                    <div class="bg-white dark:bg-slate-800 rounded-2xl p-5 sm:p-6 shadow-sm border border-slate-200 dark:border-slate-700">
                        <h3 class="font-bold text-base text-slate-900 dark:text-white mb-1">Comprehensive Mulch Specifications</h3>
                        <p class="text-xs text-slate-500 dark:text-slate-400 mb-4">Technical characteristics, decomposition timelines, and ideal landscaping environments.</p>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <!-- Hardwood -->
                            <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-900/30">
                                <div class="flex items-center justify-between mb-1">
                                    <h4 class="font-bold text-sm text-slate-900 dark:text-white">Shredded Hardwood Bark</h4>
                                    <span class="text-[10px] px-2 py-0.5 rounded bg-brand-50 text-brand-700 dark:bg-brand-950 dark:text-brand-300 font-semibold">Most Popular</span>
                                </div>
                                <p class="text-xs text-slate-600 dark:text-slate-300 mb-2">Triple-shredded or double-shredded deciduous tree bark that mats securely on slopes and prevents washouts.</p>
                                <ul class="text-[11px] space-y-1 text-slate-500 dark:text-slate-400">
                                    <li>&bull; <strong>Recommended Depth:</strong> 2 to 3 inches</li>
                                    <li>&bull; <strong>Decomposition:</strong> 1 to 2 years (enriches soil humus)</li>
                                    <li>&bull; <strong>Density:</strong> 500 &ndash; 800 lbs per cubic yard</li>
                                    <li>&bull; <strong>Best For:</strong> Sloped borders, perennial beds, foundation shrubbery</li>
                                </ul>
                            </div>

                            <!-- Pine Bark Nuggets -->
                            <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-900/30">
                                <div class="flex items-center justify-between mb-1">
                                    <h4 class="font-bold text-sm text-slate-900 dark:text-white">Pine Bark Nuggets</h4>
                                    <span class="text-[10px] px-2 py-0.5 rounded bg-amber-50 text-amber-700 dark:bg-amber-950 dark:text-amber-300 font-semibold">Long Lasting</span>
                                </div>
                                <p class="text-xs text-slate-600 dark:text-slate-300 mb-2">Coarse, chunky pine bark chunks that resist compacting and break down slowly.</p>
                                <ul class="text-[11px] space-y-1 text-slate-500 dark:text-slate-400">
                                    <li>&bull; <strong>Recommended Depth:</strong> 2.5 to 3.5 inches</li>
                                    <li>&bull; <strong>Decomposition:</strong> 2 to 3 years</li>
                                    <li>&bull; <strong>Density:</strong> 400 &ndash; 600 lbs per cubic yard</li>
                                    <li>&bull; <strong>Best For:</strong> Flat beds, azaleas, rhododendrons (may float in heavy runoff)</li>
                                </ul>
                            </div>

                            <!-- Cedar Mulch -->
                            <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-900/30">
                                <div class="flex items-center justify-between mb-1">
                                    <h4 class="font-bold text-sm text-slate-900 dark:text-white">Cedar Mulch &amp; Shavings</h4>
                                    <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300 font-semibold">Insect Repelling</span>
                                </div>
                                <p class="text-xs text-slate-600 dark:text-slate-300 mb-2">Contains natural aromatic thujaplicin oils that deter unwanted insects and resist decay.</p>
                                <ul class="text-[11px] space-y-1 text-slate-500 dark:text-slate-400">
                                    <li>&bull; <strong>Recommended Depth:</strong> 2 to 3 inches</li>
                                    <li>&bull; <strong>Decomposition:</strong> 2 to 3 years</li>
                                    <li>&bull; <strong>Density:</strong> 400 &ndash; 550 lbs per cubic yard</li>
                                    <li>&bull; <strong>Best For:</strong> Home perimeter beds, shaded pathways, decorative borders</li>
                                </ul>
                            </div>

                            <!-- Arborist Wood Chips -->
                            <div class="p-4 rounded-xl border border-slate-200 dark:border-slate-700 bg-slate-50/50 dark:bg-slate-900/30">
                                <div class="flex items-center justify-between mb-1">
                                    <h4 class="font-bold text-sm text-slate-900 dark:text-white">Arborist Utility Wood Chips</h4>
                                    <span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300 font-semibold">Budget Choice</span>
                                </div>
                                <p class="text-xs text-slate-600 dark:text-slate-300 mb-2">Fresh tree service trimmings containing wood, twigs, and bark. Exceptional weed suppression.</p>
                                <ul class="text-[11px] space-y-1 text-slate-500 dark:text-slate-400">
                                    <li>&bull; <strong>Recommended Depth:</strong> 3 to 4 inches</li>
                                    <li>&bull; <strong>Decomposition:</strong> 2 to 4 years</li>
                                    <li>&bull; <strong>Density:</strong> 550 &ndash; 850 lbs per cubic yard</li>
                                    <li>&bull; <strong>Best For:</strong> Large acreage tree rings, utility easements, nature trails</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 4: Print Report -->
                <div id="tab-print" class="tab-panel space-y-6">
                    <div id="printableReportSection" class="bg-white dark:bg-slate-800 p-6 sm:p-8 rounded-2xl border border-slate-200 dark:border-slate-700 space-y-6 text-slate-800 dark:text-slate-100">
                        
                        <!-- Print Header -->
                        <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-700 pb-4">
                            <div>
                                <span class="text-xs font-bold uppercase tracking-wider text-brand-600 dark:text-brand-400 block">CalcWorld Landscaping Engine</span>
                                <h3 class="text-xl sm:text-2xl font-extrabold text-slate-900 dark:text-white">Material Requisition &amp; Estimate Sheet</h3>
                            </div>
                            <div class="text-right text-xs text-slate-500 dark:text-slate-400">
                                <div><strong>Date:</strong> <span id="reportTimestamp">--</span></div>
                                <div><strong>Ref Code:</strong> <span id="reportRefCode">MC-9021</span></div>
                            </div>
                        </div>

                        <!-- Client / Project Information Form -->
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs bg-slate-50 dark:bg-slate-900/50 p-3 rounded-xl border border-slate-200 dark:border-slate-700">
                            <div>
                                <label class="block font-semibold text-slate-500 dark:text-slate-400">Project / Client Name</label>
                                <input type="text" id="reportClientName" value="Residential Landscape Upgrade" class="w-full mt-0.5 px-2 py-1 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded text-slate-900 dark:text-white font-medium">
                            </div>
                            <div>
                                <label class="block font-semibold text-slate-500 dark:text-slate-400">Site Address</label>
                                <input type="text" id="reportClientAddress" value="Client Property Site" class="w-full mt-0.5 px-2 py-1 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded text-slate-900 dark:text-white font-medium">
                            </div>
                            <div>
                                <label class="block font-semibold text-slate-500 dark:text-slate-400">Contractor / Estimator</label>
                                <input type="text" id="reportEstimator" value="Lead Project Manager" class="w-full mt-0.5 px-2 py-1 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded text-slate-900 dark:text-white font-medium">
                            </div>
                        </div>

                        <!-- Primary Metrics Table -->
                        <div>
                            <h4 class="font-bold text-xs uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2">Total Project Material Quantities</h4>
                            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
                                <div class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-xl border border-slate-200 dark:border-slate-700">
                                    <span class="text-[10px] text-slate-500 dark:text-slate-400 uppercase block font-semibold">Total Area</span>
                                    <span class="text-base sm:text-lg font-bold font-mono text-slate-900 dark:text-white" id="reportTotalArea">--</span>
                                </div>
                                <div class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-xl border border-slate-200 dark:border-slate-700">
                                    <span class="text-[10px] text-slate-500 dark:text-slate-400 uppercase block font-semibold">Cubic Yards</span>
                                    <span class="text-base sm:text-lg font-bold font-mono text-brand-600 dark:text-brand-400" id="reportTotalYards">--</span>
                                </div>
                                <div class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-xl border border-slate-200 dark:border-slate-700">
                                    <span class="text-[10px] text-slate-500 dark:text-slate-400 uppercase block font-semibold">2.0 Cu Ft Bags</span>
                                    <span class="text-base sm:text-lg font-bold font-mono text-slate-900 dark:text-white" id="reportBags2cu">--</span>
                                </div>
                                <div class="p-3 bg-slate-50 dark:bg-slate-900/50 rounded-xl border border-slate-200 dark:border-slate-700">
                                    <span class="text-[10px] text-slate-500 dark:text-slate-400 uppercase block font-semibold">Weight Estimate</span>
                                    <span class="text-base sm:text-lg font-bold font-mono text-slate-900 dark:text-white" id="reportTotalWeight">--</span>
                                </div>
                            </div>
                        </div>

                        <!-- Itemized Zone Table -->
                        <div>
                            <h4 class="font-bold text-xs uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-2">Itemized Landscape Zones</h4>
                            <div class="overflow-x-auto">
                                <table class="w-full text-xs text-left border-collapse border border-slate-200 dark:border-slate-700">
                                    <thead class="bg-slate-50 dark:bg-slate-900/80 font-semibold text-slate-600 dark:text-slate-400 border-b border-slate-200 dark:border-slate-700">
                                        <tr>
                                            <th class="p-2 border-r border-slate-200 dark:border-slate-700">Zone Name</th>
                                            <th class="p-2 border-r border-slate-200 dark:border-slate-700">Dimensions</th>
                                            <th class="p-2 border-r border-slate-200 dark:border-slate-700">Depth</th>
                                            <th class="p-2 border-r border-slate-200 dark:border-slate-700">Area (Sq Ft)</th>
                                            <th class="p-2 border-r border-slate-200 dark:border-slate-700">Volume (Cu Yd)</th>
                                            <th class="p-2">2 Cu Ft Bags</th>
                                        </tr>
                                    </thead>
                                    <tbody id="reportItemizedTableBody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                                        <!-- Synchronized dynamically -->
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        <!-- Horticultural Application Standards Notice -->
                        <div class="p-3 bg-slate-50 dark:bg-slate-900/40 rounded-xl border border-slate-200 dark:border-slate-700 text-xs space-y-1">
                            <strong class="font-bold text-slate-900 dark:text-white block">University Extension Application Protocol:</strong>
                            <p class="text-slate-600 dark:text-slate-400">1. Maintain 2 to 3 inches settled depth. 2. Keep mulch 3 inches away from tree trunk flares to prevent collar rot. 3. Water down material immediately following spreading to settle dust and activate beneficial soil microbiology.</p>
                        </div>

                        <!-- Print Action -->
                        <div class="text-right no-print pt-2">
                            <button onclick="window.print()" class="px-4 py-2 bg-brand-600 hover:bg-brand-700 text-white font-bold text-xs rounded-lg transition shadow">Print Document</button>
                        </div>

                    </div>
                </div>

                <!-- AdSense Slot 2: Under-Result Display Ad -->
                <div class="ad-slot no-print" id="ad-slot-2">
                    <span>Sponsored Advertisement &bull; Under-Result Slot 2</span>
                </div>

            </div>
        </div>

        <!-- AdSense Slot 4: Mid-Guide Content Ad -->
        <div class="ad-slot no-print mt-10" id="ad-slot-4">
            <span>Sponsored Advertisement &bull; Mid-Article Slot 4</span>
        </div>
"""

part3_faq_footer_script = """
        <!-- Comprehensive FAQ Section -->
        <section class="mt-12 bg-white dark:bg-slate-800 rounded-2xl p-6 sm:p-10 shadow-sm border border-slate-200 dark:border-slate-700 no-print">
            <h2 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">Frequently Asked Questions</h2>
            <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mb-6">Expert answers on landscape material volume estimation, application depth, and purchasing economics.</p>

            <div class="space-y-3" id="faqAccordion">
                <!-- Q1 -->
                <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                    <button type="button" onclick="toggleFaq(1)" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
                        <span>How many cubic yards of mulch do I need for my garden bed?</span>
                        <svg id="faqIcon_1" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div id="faqAns_1" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
                        Multiply your garden bed area in square feet by your target depth in inches, and divide by 324. For example, a 300 square foot bed mulched 3 inches deep requires (300 &times; 3) / 324 = 2.78 cubic yards. Adding a 5% settling contingency increases this requirement to 2.92 cubic yards.
                    </div>
                </div>

                <!-- Q2 -->
                <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                    <button type="button" onclick="toggleFaq(2)" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
                        <span>How many bags of mulch equal one cubic yard?</span>
                        <svg id="faqIcon_2" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div id="faqAns_2" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
                        One cubic yard contains 27 cubic feet. A standard 2.0 cubic foot retail bag provides 2.0 cu ft, requiring 13.5 bags (round up to 14 bags) per cubic yard. A larger 3.0 cubic foot bag requires exactly 9 bags per cubic yard.
                    </div>
                </div>

                <!-- Q3 -->
                <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                    <button type="button" onclick="toggleFaq(3)" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
                        <span>What is the optimal mulch depth for flowers, trees, and shrubs?</span>
                        <svg id="faqIcon_3" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div id="faqAns_3" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
                        University horticultural extensions (Cornell, Penn State, Texas A&amp;M AgriLife) recommend a settled depth of 2 to 3 inches for organic bark mulches. Layers deeper than 4 inches can restrict soil aeration, cause root suffocation, and encourage roots to grow upward into the mulch layer where they dry out.
                    </div>
                </div>

                <!-- Q4 -->
                <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                    <button type="button" onclick="toggleFaq(4)" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
                        <span>What is a "mulch volcano" and why is it dangerous?</span>
                        <svg id="faqIcon_4" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div id="faqAns_4" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
                        A mulch volcano occurs when mulch is mounded high against the trunk of a tree. Bark requires oxygen and dry air to remain intact. Constant moisture trapped by mulch decays the protective bark layer, invites wood-boring pests, facilitates fungal girdling (*Phytophthora*), and attracts burrowing rodents that strip the tree cambium.
                    </div>
                </div>

                <!-- Q5 -->
                <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                    <button type="button" onclick="toggleFaq(5)" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
                        <span>Does wood mulch steal nitrogen from garden plants?</span>
                        <svg id="faqIcon_5" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div id="faqAns_5" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
                        No. Studies confirm that nitrogen immobilization occurs strictly at the immediate microscopic contact surface between the mulch and soil. Plant roots deeper than 0.25 inches remain unaffected. As long as uncomposted high-carbon wood chips are kept as a surface mulch rather than tilled into the root zone, established shrubs and flowers experience no nitrogen deficiency.
                    </div>
                </div>

                <!-- Q6 -->
                <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                    <button type="button" onclick="toggleFaq(6)" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
                        <span>When is it cheaper to buy bulk mulch delivered instead of retail bags?</span>
                        <svg id="faqIcon_6" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div id="faqAns_6" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
                        The financial break-even threshold generally lies between 2.0 and 2.5 cubic yards (27 to 34 bags). For smaller jobs (under 2 yards), store pickup saves money by avoiding flat bulk delivery charges ($50 to $85). For larger projects requiring 3 yards or more, bulk delivery saves money and prevents hauling dozens of heavy bags in consumer vehicles.
                    </div>
                </div>

                <!-- Q7 -->
                <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                    <button type="button" onclick="toggleFaq(7)" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
                        <span>How much does a cubic yard of mulch weigh?</span>
                        <svg id="faqIcon_7" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div id="faqAns_7" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
                        Dry shredded hardwood weighs approximately 400 to 600 pounds per cubic yard. Wet or tightly settled mulch weighs 700 to 1,000 pounds per yard. Denser materials such as compost weigh 1,000 to 1,400 lbs, topsoil weighs 2,000 to 2,400 lbs, and gravel weighs 2,600 to 2,800 lbs per cubic yard.
                    </div>
                </div>

                <!-- Q8 -->
                <div class="border border-slate-200 dark:border-slate-700 rounded-xl overflow-hidden">
                    <button type="button" onclick="toggleFaq(8)" class="w-full p-4 text-left font-bold text-sm sm:text-base text-slate-900 dark:text-white flex items-center justify-between bg-slate-50/70 dark:bg-slate-900/40 hover:bg-slate-100 dark:hover:bg-slate-900/80 transition">
                        <span>How often should landscaping mulch be replenished?</span>
                        <svg id="faqIcon_8" class="w-4 h-4 text-slate-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
                    </button>
                    <div id="faqAns_8" class="p-4 text-xs sm:text-sm text-slate-600 dark:text-slate-300 leading-relaxed border-t border-slate-100 dark:border-slate-800 hidden">
                        Organic bark mulches break down over 1 to 2 years. Do not pile fresh mulch over an undisturbed deep crust. Instead, rake the old mulch in spring to break up surface crusts and add a 1-inch topdressing refresh to maintain the optimal 2 to 3-inch profile without suffocating roots.
                    </div>
                </div>
            </div>
        </section>

        <!-- AdSense Slot 5: Bottom Multiplex Native Grid -->
        <div class="ad-slot no-print mt-10" id="ad-slot-5">
            <span>Sponsored Advertisement &bull; Multiplex Native Grid Slot 5</span>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 py-12 px-4 sm:px-6 lg:px-8 mt-16 text-slate-600 dark:text-slate-400 text-xs no-print">
        <div class="max-w-7xl mx-auto space-y-6">
            <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-6">
                <div class="flex items-center gap-2">
                    <span class="w-7 h-7 rounded-lg bg-brand-600 flex items-center justify-center text-white font-bold text-sm">MC</span>
                    <span class="font-bold text-base text-slate-900 dark:text-white tracking-tight">CalcWorld</span>
                    <span class="text-[11px] text-slate-400 ml-2">&copy; 2026 CalcWorld Landscaping &amp; Construction Network. All rights reserved.</span>
                </div>
                <div class="flex flex-wrap items-center gap-4 text-xs">
                    <a href="https://calcworld.net/privacy" class="hover:text-brand-600 dark:hover:text-brand-400 transition">Privacy Policy</a>
                    <a href="https://calcworld.net/terms" class="hover:text-brand-600 dark:hover:text-brand-400 transition">Terms of Service</a>
                    <a href="https://calcworld.net/about" class="hover:text-brand-600 dark:hover:text-brand-400 transition">About Us</a>
                    <a href="https://calcworld.net/contact" class="hover:text-brand-600 dark:hover:text-brand-400 transition">Contact</a>
                </div>
            </div>

            <div class="text-[11px] leading-relaxed text-slate-500 dark:text-slate-500">
                <p><strong>Horticultural &amp; Construction Notice:</strong> CalcWorld Mulch Calculator implements mathematical volume estimations based on geometric spatial equations and university extension standards (Cornell University Cooperative Extension, Penn State Extension, Texas A&amp;M AgriLife). Settling, soil contour irregularities, and moisture weight variations will impact final bulk load densities. Always verify site measurements with your local landscape material supplier prior to placing non-refundable bulk orders.</p>
            </div>
        </div>
    </footer>

    <!-- Floating Quick-Switcher Bar (Pill Bar) -->
    <aside id="floatingBar" class="fixed bottom-4 left-1/2 -translate-x-1/2 z-40 bg-white/95 dark:bg-slate-800/95 backdrop-blur-md px-4 py-2 rounded-full shadow-lg border border-slate-200 dark:border-slate-700 flex items-center gap-2 text-xs font-medium text-slate-700 dark:text-slate-300 no-print transition-all">
        <span class="text-slate-400 font-semibold uppercase tracking-wider text-[10px] hidden sm:inline">Related Tools:</span>
        <a href="topsoil-calculator.html" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700/60 hover:bg-brand-50 hover:text-brand-600 dark:hover:text-brand-300 transition">Topsoil</a>
        <a href="gravel-calculator.html" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700/60 hover:bg-brand-50 hover:text-brand-600 dark:hover:text-brand-300 transition">Gravel</a>
        <a href="square-footage-calculator.html" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700/60 hover:bg-brand-50 hover:text-brand-600 dark:hover:text-brand-300 transition">Square Footage</a>
        <a href="grass-seed-calculator.html" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-700/60 hover:bg-brand-50 hover:text-brand-600 dark:hover:text-brand-300 transition hidden sm:inline">Grass Seed</a>
    </aside>

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-20 left-1/2 -translate-x-1/2 z-50 bg-slate-900 text-white px-4 py-2 rounded-xl shadow-2xl flex items-center gap-2 text-xs opacity-0 pointer-events-none transition-opacity duration-300 border border-slate-700" role="alert">
        <svg class="w-4 h-4 text-emerald-400 shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
        <span id="toastMsg">Summary copied to clipboard!</span>
    </div>

<script>
    // Global Application State
    let currentShape = 'rectangle'; // 'rectangle', 'circle', 'donut', 'triangle', 'area'
    let currentDepth = 3.0;
    let contingencyPct = 5.0;
    let costChart = null;
    let plannerDonut = null;
    let lastCalc = {};

    // Multi-Bed Project Planner State (Initial Realistic Landscape Beds)
    let plannerZones = [
        { id: 1, name: "Front Foundation Bed", shape: "rectangle", length: 35, width: 4, depth: 3.0, material: "hardwood", area: 140, cuYds: 1.30, bags2cu: 18 },
        { id: 2, name: "Backyard Tree Rings (2x)", shape: "donut", outerDia: 8, innerDia: 2, depth: 2.5, material: "pine_bark", area: 94.25, cuYds: 0.73, bags2cu: 10 },
        { id: 3, name: "Perimeter Shrub Border", shape: "area", directArea: 280, depth: 3.0, material: "hardwood", area: 280, cuYds: 2.59, bags2cu: 35 },
        { id: 4, name: "Vegetable Garden Paths", shape: "rectangle", length: 24, width: 3, depth: 2.0, material: "chips", area: 72, cuYds: 0.44, bags2cu: 6 }
    ];

    // DOM Ready Initialization
    window.addEventListener('DOMContentLoaded', () => {
        parseUrlParams();
        calculate();
        initPlannerTable();
        updatePlannerDonut();

        // AdBlock Detection Check
        setTimeout(() => {
            const adSlot = document.getElementById('ad-slot-1');
            if (adSlot && adSlot.offsetHeight === 0) {
                const notice = document.getElementById('adblockRecovery');
                if (notice) notice.classList.remove('hidden');
            }
        }, 1200);
    });

    // --- Shape & Dimension Handlers ---
    function setBedShape(shape) {
        currentShape = shape;
        ['rectangle', 'circle', 'donut', 'triangle', 'area'].forEach(s => {
            const fields = document.getElementById('shapeFields_' + s);
            const btn = document.getElementById('shapeBtn_' + s);
            if (fields) {
                if (s === shape) fields.classList.remove('hidden');
                else fields.classList.add('hidden');
            }
            if (btn) {
                if (s === shape) {
                    btn.className = "shape-btn px-2 py-1.5 text-xs font-semibold rounded-lg border-2 border-brand-600 bg-brand-50 dark:bg-brand-950 text-brand-700 dark:text-brand-300 transition text-center";
                } else {
                    btn.className = "shape-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center";
                }
            }
        });
        calculate();
    }

    // --- Depth Handlers ---
    function setDepth(d) {
        currentDepth = parseFloat(d);
        document.getElementById('depthSlider').value = currentDepth;
        document.getElementById('customDepthInput').value = currentDepth.toFixed(1);
        updateDepthButtons();
        calculate();
    }

    function setCustomDepth(val) {
        const d = parseFloat(val);
        if (!isNaN(d) && d > 0) {
            currentDepth = d;
            document.getElementById('depthSlider').value = d;
            document.getElementById('customDepthInput').value = d;
            updateDepthButtons();
            calculate();
        }
    }

    function updateDepthButtons() {
        document.getElementById('activeDepthDisplay').textContent = currentDepth.toFixed(1) + ' Inches';
        document.querySelectorAll('.depth-btn').forEach(btn => {
            const btnDepth = parseFloat(btn.getAttribute('data-depth'));
            if (btnDepth === currentDepth) {
                btn.className = "depth-btn active px-2 py-1.5 text-xs font-semibold rounded-lg border-2 border-brand-600 bg-brand-50 dark:bg-brand-950 text-brand-700 dark:text-brand-300 transition text-center";
            } else {
                btn.className = "depth-btn px-2 py-1.5 text-xs font-semibold rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center";
            }
        });

        // Update guidance hint
        const hint = document.getElementById('depthGuidanceHint');
        const badge = document.getElementById('diagnosticBadge');
        if (currentDepth < 2.0) {
            hint.textContent = "1.0 - 1.5 in: Ideal for annual topdressing refresh. Insufficient for initial weed suppression.";
            if (badge) {
                badge.textContent = `Light Topdressing (${currentDepth.toFixed(1)}")`;
                badge.className = "inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-amber-50 text-amber-700 dark:bg-amber-950/60 dark:text-amber-300 border border-amber-200/50";
            }
        } else if (currentDepth <= 3.5) {
            hint.textContent = "2.0 - 3.5 in: Horticultural standard for weed prevention & moisture retention.";
            if (badge) {
                badge.textContent = `Optimal Depth (${currentDepth.toFixed(1)}")`;
                badge.className = "inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300 border border-emerald-200/50";
            }
        } else if (currentDepth <= 4.5) {
            hint.textContent = "4.0 in: High weed suppression. Ensure material is kept away from woody stems.";
            if (badge) {
                badge.textContent = `Deep Layer (${currentDepth.toFixed(1)}")`;
                badge.className = "inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-blue-50 text-blue-700 dark:bg-blue-950/60 dark:text-blue-300 border border-blue-200/50";
            }
        } else {
            hint.textContent = "6.0+ in: Recommended for playground fall safety cushioning or unplanted utility paths.";
            if (badge) {
                badge.textContent = `Playground / Path (${currentDepth.toFixed(1)}")`;
                badge.className = "inline-flex items-center px-2 py-0.5 rounded text-[11px] font-semibold bg-purple-50 text-purple-700 dark:bg-purple-950/60 dark:text-purple-300 border border-purple-200/50";
            }
        }
    }

    // --- Contingency Handlers ---
    function setContingency(pct) {
        contingencyPct = parseFloat(pct);
        document.getElementById('contingencyDisplay').textContent = contingencyPct === 0 ? "Exact Net" : `+${contingencyPct}% Buffer`;
        document.querySelectorAll('.contin-btn').forEach(btn => {
            const val = parseFloat(btn.getAttribute('data-val'));
            if (val === contingencyPct) {
                btn.className = "contin-btn active px-2 py-1 text-xs font-medium rounded-lg border-2 border-brand-600 bg-brand-50 dark:bg-brand-950 text-brand-700 dark:text-brand-300 transition text-center";
            } else {
                btn.className = "contin-btn px-2 py-1 text-xs font-medium rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 hover:border-brand-500 transition text-center";
            }
        });
        calculate();
    }

    // --- Cost Drawer Toggle ---
    function toggleCostDrawer() {
        const content = document.getElementById('costDrawerContent');
        const icon = document.getElementById('costDrawerIcon');
        if (content.classList.contains('hidden')) {
            content.classList.remove('hidden');
            icon.style.transform = 'rotate(180deg)';
        } else {
            content.classList.add('hidden');
            icon.style.transform = 'rotate(0deg)';
        }
    }

    // --- Core Calculation Engine ---
    function calculate() {
        // 1. Calculate Surface Area
        let areaSqFt = 0;
        let dimDesc = "";

        if (currentShape === 'rectangle') {
            const l = Math.max(0.01, parseFloat(document.getElementById('dim_length').value) || 0);
            const w = Math.max(0.01, parseFloat(document.getElementById('dim_width').value) || 0);
            areaSqFt = l * w;
            dimDesc = `${l}' &times; ${w}'`;
        } else if (currentShape === 'circle') {
            const d = Math.max(0.01, parseFloat(document.getElementById('dim_diameter').value) || 0);
            const r = d / 2;
            areaSqFt = Math.PI * r * r;
            dimDesc = `Dia: ${d}'`;
        } else if (currentShape === 'donut') {
            const od = Math.max(0.1, parseFloat(document.getElementById('dim_outer_dia').value) || 0);
            const id = Math.max(0, parseFloat(document.getElementById('dim_inner_dia').value) || 0);
            const rOut = od / 2;
            const rIn = Math.min(rOut - 0.05, id / 2);
            areaSqFt = Math.PI * (rOut * rOut - rIn * rIn);
            dimDesc = `Ring: Outer ${od}', Inner ${id}'`;
        } else if (currentShape === 'triangle') {
            const b = Math.max(0.01, parseFloat(document.getElementById('dim_base').value) || 0);
            const h = Math.max(0.01, parseFloat(document.getElementById('dim_height').value) || 0);
            areaSqFt = 0.5 * b * h;
            dimDesc = `Base: ${b}', H: ${h}'`;
        } else {
            areaSqFt = Math.max(0.1, parseFloat(document.getElementById('dim_direct_area').value) || 0);
            dimDesc = `Direct Area`;
        }

        // 2. Volumetric Calculations
        const netCuFt = areaSqFt * (currentDepth / 12);
        const grossCuFt = netCuFt * (1 + (contingencyPct / 100));
        const netCuYds = netCuFt / 27;
        const grossCuYds = grossCuFt / 27;

        // Bag Counts
        const bags2cuExact = grossCuFt / 2.0;
        const bags2cuWhole = Math.ceil(bags2cuExact);
        const bags3cuExact = grossCuFt / 3.0;
        const bags3cuWhole = Math.ceil(bags3cuExact);

        // Material Density & Weight
        const matSelect = document.getElementById('materialSelect');
        const density = parseFloat(matSelect.options[matSelect.selectedIndex].getAttribute('data-density')) || 500;
        const weightLbs = grossCuYds * density;
        const weightTons = weightLbs / 2000;
        const wheelbarrows = Math.ceil(grossCuFt / 3.0); // 3 cu ft wheelbarrow tray

        // Cost Modeling
        const bulkPriceYard = parseFloat(document.getElementById('cost_bulk_yard').value) || 38.00;
        const bulkDelivFee = parseFloat(document.getElementById('cost_bulk_deliv').value) || 65.00;
        const bag2cuPrice = parseFloat(document.getElementById('cost_bag_2cu').value) || 4.48;
        const bag3cuPrice = parseFloat(document.getElementById('cost_bag_3cu').value) || 6.25;
        const bagDelivFee = parseFloat(document.getElementById('cost_bagged_deliv').value) || 79.00;

        const totalBulkDeliveredCost = (grossCuYds * bulkPriceYard) + bulkDelivFee;
        const totalBagPickupCost = bags2cuWhole * bag2cuPrice;
        const totalBagDeliveredCost = (bags2cuWhole * bag2cuPrice) + bagDelivFee;
        const totalBag3cuPickupCost = bags3cuWhole * bag3cuPrice;

        // Save last calculation state
        lastCalc = {
            shape: currentShape,
            dimDesc,
            areaSqFt,
            depth: currentDepth,
            contingency: contingencyPct,
            netCuFt,
            grossCuFt,
            netCuYds,
            grossCuYds,
            bags2cuExact,
            bags2cuWhole,
            bags3cuExact,
            bags3cuWhole,
            density,
            weightLbs,
            weightTons,
            wheelbarrows,
            bulkCost: totalBulkDeliveredCost,
            bagPickupCost: totalBagPickupCost,
            bagDelivCost: totalBagDeliveredCost,
            bag3cuCost: totalBag3cuPickupCost
        };

        // Render Outputs to UI
        document.getElementById('mainYardageDisplay').textContent = `${grossCuYds.toFixed(2)} Cu Yds`;
        document.getElementById('mainNarrativeDisplay').innerHTML = `Covers <strong>${areaSqFt.toFixed(1)} sq ft</strong> at <strong>${currentDepth.toFixed(1)} inches depth</strong> (${grossCuFt.toFixed(2)} cu ft with ${contingencyPct}% buffer).`;

        document.getElementById('metricBags2cu').textContent = `${bags2cuWhole} Bags`;
        document.getElementById('metricBags2cuExact').textContent = `Exact: ${bags2cuExact.toFixed(1)}`;
        document.getElementById('metricBags3cu').textContent = `${bags3cuWhole} Bags`;
        document.getElementById('metricBags3cuExact').textContent = `Exact: ${bags3cuExact.toFixed(1)}`;

        document.getElementById('metricWeightLbs').textContent = `${Math.round(weightLbs).toLocaleString()} lbs`;
        document.getElementById('metricWeightTons').textContent = `${weightTons.toFixed(2)} Tons`;
        document.getElementById('metricWheelbarrows').textContent = `${wheelbarrows} Loads`;

        // Economic Summary Banner
        document.getElementById('economicSummaryText').textContent = `Bulk Delivered: $${totalBulkDeliveredCost.toFixed(2)} | Store Pickup (2 cu ft): $${totalBagPickupCost.toFixed(2)}`;
        const recBadge = document.getElementById('economicRecommendationBadge');
        if (totalBulkDeliveredCost < totalBagPickupCost) {
            const savings = totalBagPickupCost - totalBulkDeliveredCost;
            recBadge.textContent = `Bulk Delivery Saves $${savings.toFixed(2)}`;
            recBadge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-brand-600 text-white";
        } else {
            const savings = totalBulkDeliveredCost - totalBagPickupCost;
            recBadge.textContent = `Store Pickup Saves $${savings.toFixed(2)}`;
            recBadge.className = "px-2 py-0.5 rounded text-[10px] font-bold bg-blue-600 text-white";
        }

        document.getElementById('quickAreaSummary').textContent = `Area: ${Math.round(areaSqFt)} sq ft`;
        document.getElementById('quickCubicFeetSummary').textContent = `Volume: ${grossCuFt.toFixed(1)} cu ft`;

        // Update Components
        renderDerivation(lastCalc);
        renderDepthMatrix(areaSqFt);
        updateCostChart(lastCalc);
        updatePrintReport(lastCalc);
        updateShareUrl(lastCalc);
    }

    // --- MathJax Derivation Block ---
    function renderDerivation(c) {
        const block = document.getElementById('mathJaxDerivationBlock');
        if (!block) return;

        let shapeEquation = "";
        if (c.shape === 'rectangle') {
            const l = parseFloat(document.getElementById('dim_length').value) || 0;
            const w = parseFloat(document.getElementById('dim_width').value) || 0;
            shapeEquation = `\\text{Area} = \\text{Length} \\times \\text{Width} = ${l} \\text{ ft} \\times ${w} \\text{ ft} = ${c.areaSqFt.toFixed(2)} \\text{ sq ft}`;
        } else if (c.shape === 'circle') {
            const d = parseFloat(document.getElementById('dim_diameter').value) || 0;
            shapeEquation = `\\text{Area} = \\pi \\times r^2 = 3.1416 \\times (${(d/2).toFixed(2)})^2 = ${c.areaSqFt.toFixed(2)} \\text{ sq ft}`;
        } else if (c.shape === 'donut') {
            shapeEquation = `\\text{Area} = \\pi \\times (R_{\\text{out}}^2 - R_{\\text{in}}^2) = ${c.areaSqFt.toFixed(2)} \\text{ sq ft}`;
        } else if (c.shape === 'triangle') {
            shapeEquation = `\\text{Area} = 0.5 \\times \\text{Base} \\times \\text{Height} = ${c.areaSqFt.toFixed(2)} \\text{ sq ft}`;
        } else {
            shapeEquation = `\\text{Area} = ${c.areaSqFt.toFixed(2)} \\text{ sq ft (Direct Entry)}`;
        }

        const depthFraction = (c.depth / 12).toFixed(4);
        const continFactor = (1 + c.contingency / 100).toFixed(2);

        block.innerHTML = `
            <div><strong>Step 1: Surface Area Computation:</strong></div>
            <div class="pl-3 text-slate-800 dark:text-slate-200">$$${shapeEquation}$$</div>

            <div class="mt-2"><strong>Step 2: Depth Conversion to Feet:</strong></div>
            <div class="pl-3 text-slate-800 dark:text-slate-200">$$\\text{Depth (ft)} = \\frac{${c.depth.toFixed(1)}\\text{ inches}}{12} = ${depthFraction}\\text{ ft}$$</div>

            <div class="mt-2"><strong>Step 3: Cubic Feet with Settling Contingency (${c.contingency}%):</strong></div>
            <div class="pl-3 text-slate-800 dark:text-slate-200">$$\\text{Volume (cu ft)} = (${c.areaSqFt.toFixed(2)} \\times ${depthFraction}) \\times ${continFactor} = ${c.grossCuFt.toFixed(2)}\\text{ cu ft}$$</div>

            <div class="mt-2"><strong>Step 4: Conversion to Wholesale Cubic Yards:</strong></div>
            <div class="pl-3 text-slate-800 dark:text-slate-200">$$\\text{Volume (cu yds)} = \\frac{${c.grossCuFt.toFixed(2)}}{27} = ${c.grossCuYds.toFixed(2)}\\text{ yd}^3$$</div>

            <div class="mt-2"><strong>Step 5: Retail Bag Requisitions:</strong></div>
            <div class="pl-3 text-slate-800 dark:text-slate-200">$$\\text{Bags (2.0 cu ft)} = \\frac{${c.grossCuFt.toFixed(2)}}{2.0} = ${c.bags2cuExact.toFixed(2)} \\implies \\mathbf{${c.bags2cuWhole}\\text{ Bags (rounded up)}}$$</div>
            <div class="pl-3 text-slate-800 dark:text-slate-200">$$\\text{Bags (3.0 cu ft)} = \\frac{${c.grossCuFt.toFixed(2)}}{3.0} = ${c.bags3cuExact.toFixed(2)} \\implies \\mathbf{${c.bags3cuWhole}\\text{ Bags (rounded up)}}$$</div>
        `;

        if (window.MathJax && window.MathJax.typesetPromise) {
            window.MathJax.typesetPromise([block]);
        }
    }

    // --- Depth Sensitivity Table ---
    function renderDepthMatrix(area) {
        const tbody = document.getElementById('depthMatrixBody');
        if (!tbody) return;

        const depths = [
            { d: 1.0, label: "Topdressing Refresh" },
            { d: 2.0, label: "Annual Flowerbeds" },
            { d: 3.0, label: "Perennials & Shrubs" },
            { d: 4.0, label: "Weed Barrier Slopes" },
            { d: 6.0, label: "Playground Cushion" }
        ];

        const rows = depths.map(item => {
            const cuFt = area * (item.d / 12) * (1 + contingencyPct / 100);
            const cuYd = cuFt / 27;
            const b2 = Math.ceil(cuFt / 2.0);
            const b3 = Math.ceil(cuFt / 3.0);
            const isSelected = Math.abs(item.d - currentDepth) < 0.1;

            return `
            <tr class="${isSelected ? 'bg-brand-50/70 dark:bg-brand-950/40 font-bold text-brand-700 dark:text-brand-300' : 'hover:bg-slate-50 dark:hover:bg-slate-800/40'}">
                <td class="px-3 py-2">${item.d.toFixed(1)}" ${isSelected ? '★' : ''}</td>
                <td class="px-3 py-2">${cuFt.toFixed(1)}</td>
                <td class="px-3 py-2 font-bold">${cuYd.toFixed(2)} yd³</td>
                <td class="px-3 py-2">${b2} bags</td>
                <td class="px-3 py-2">${b3} bags</td>
                <td class="px-3 py-2 font-sans text-[11px] text-slate-500">${item.label}</td>
            </tr>`;
        }).join('');

        tbody.innerHTML = rows;
    }

    // --- Chart.js Cost Comparison Bar Chart ---
    function updateCostChart(c) {
        const ctx = document.getElementById('costComparisonChart');
        if (!ctx) return;

        if (costChart) {
            costChart.destroy();
            costChart = null;
        }

        const isDark = document.documentElement.classList.contains('dark');
        const gridColor = isDark ? 'rgba(255, 255, 255, 0.08)' : 'rgba(0, 0, 0, 0.06)';
        const textColor = isDark ? '#94a3b8' : '#64748b';

        costChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: [
                    'Bulk Delivery',
                    'Bagged Store Pickup (2 cu ft)',
                    'Bagged Delivery (2 cu ft)',
                    'Bagged Store Pickup (3 cu ft)'
                ],
                datasets: [{
                    label: 'Total Cost ($ USD)',
                    data: [
                        c.bulkCost,
                        c.bagPickupCost,
                        c.bagDelivCost,
                        c.bag3cuCost
                    ],
                    backgroundColor: [
                        'rgba(16, 185, 129, 0.65)',
                        'rgba(59, 130, 246, 0.65)',
                        'rgba(245, 158, 11, 0.65)',
                        'rgba(99, 102, 241, 0.65)'
                    ],
                    borderColor: [
                        '#10b981',
                        '#3b82f6',
                        '#f59e0b',
                        '#6366f1'
                    ],
                    borderWidth: 2,
                    borderRadius: 8,
                    barPercentage: 0.6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: (ctx) => `Expenditure: $${ctx.raw.toFixed(2)}`
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        grid: { color: gridColor },
                        ticks: {
                            color: textColor,
                            font: { family: 'Inter', size: 10 },
                            callback: (v) => '$' + v
                        }
                    },
                    x: {
                        grid: { display: false },
                        ticks: {
                            color: textColor,
                            font: { family: 'Inter', size: 10, weight: '600' }
                        }
                    }
                }
            }
        });
    }

    // --- Multi-Bed Project Planner Module (Tab 2) ---
    function initPlannerTable() {
        const tbody = document.getElementById('plannerTableBody');
        if (!tbody) return;

        let totalArea = 0;
        let totalCuYds = 0;
        let totalBags2cu = 0;
        let totalWeightLbs = 0;

        tbody.innerHTML = plannerZones.map((z, idx) => {
            totalArea += z.area;
            totalCuYds += z.cuYds;
            totalBags2cu += z.bags2cu;
            const density = z.material === 'compost' ? 1200 : (z.material === 'topsoil' ? 2200 : 500);
            totalWeightLbs += z.cuYds * density;

            let dimText = "";
            if (z.shape === 'rectangle') dimText = `${z.length}' &times; ${z.width}'`;
            else if (z.shape === 'circle') dimText = `Dia: ${z.outerDia}'`;
            else if (z.shape === 'donut') dimText = `Outer ${z.outerDia}', Inner ${z.innerDia}'`;
            else dimText = `${z.area} sq ft`;

            return `
            <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40">
                <td class="px-3 py-2 font-bold text-slate-900 dark:text-white">${z.name}</td>
                <td class="px-3 py-2">${dimText}</td>
                <td class="px-3 py-2">${z.depth.toFixed(1)}"</td>
                <td class="px-3 py-2 capitalize font-sans text-slate-500">${z.material.replace('_', ' ')}</td>
                <td class="px-3 py-2">${z.area.toFixed(1)}</td>
                <td class="px-3 py-2 font-bold text-brand-600 dark:text-brand-400">${z.cuYds.toFixed(2)}</td>
                <td class="px-3 py-2">${z.bags2cu}</td>
                <td class="px-3 py-2 text-right">
                    <button onclick="removePlannerZone(${z.id})" class="text-rose-500 hover:text-rose-700 px-1 font-bold text-xs" title="Remove Zone">&times;</button>
                </td>
            </tr>`;
        }).join('');

        // Update Aggregate Cards
        document.getElementById('planTotalArea').textContent = `${Math.round(totalArea)} sq ft`;
        document.getElementById('planTotalYards').textContent = `${totalCuYds.toFixed(2)} yd³`;
        document.getElementById('planTotalBags2cu').textContent = `${totalBags2cu} Bags`;
        document.getElementById('planTotalWeight').textContent = `${Math.round(totalWeightLbs).toLocaleString()} lbs`;

        // Update Procurement Summary
        const bulkPrice = parseFloat(document.getElementById('cost_bulk_yard').value) || 38.0;
        const bulkDeliv = parseFloat(document.getElementById('cost_bulk_deliv').value) || 65.0;
        const bagPrice = parseFloat(document.getElementById('cost_bag_2cu').value) || 4.48;
        const bagDeliv = parseFloat(document.getElementById('cost_bagged_deliv').value) || 79.0;

        const totalBulk = (totalCuYds * bulkPrice) + bulkDeliv;
        const totalBagPickup = totalBags2cu * bagPrice;
        const totalBagDeliv = (totalBags2cu * bagPrice) + bagDeliv;

        document.getElementById('planBulkCostDisplay').textContent = `$${totalBulk.toFixed(2)}`;
        document.getElementById('planBagPickupDisplay').textContent = `$${totalBagPickup.toFixed(2)}`;
        document.getElementById('planBagDelivDisplay').textContent = `$${totalBagDeliv.toFixed(2)}`;

        const savings = totalBagPickup - totalBulk;
        const savingsEl = document.getElementById('planSavingsDisplay');
        if (savings > 0) {
            savingsEl.textContent = `Bulk Saves $${savings.toFixed(2)}`;
            savingsEl.className = "font-bold font-mono text-emerald-600 dark:text-emerald-400";
        } else {
            savingsEl.textContent = `Bagged Saves $${Math.abs(savings).toFixed(2)}`;
            savingsEl.className = "font-bold font-mono text-blue-600 dark:text-blue-400";
        }
    }

    function addNewPlannerZone() {
        const nextId = plannerZones.length > 0 ? Math.max(...plannerZones.map(z => z.id)) + 1 : 1;
        const name = prompt("Enter Garden Bed Name (e.g. Side Yard Shrub Border):", `Garden Bed #${nextId}`);
        if (!name) return;

        const l = parseFloat(prompt("Enter Bed Length in feet:", "20")) || 20;
        const w = parseFloat(prompt("Enter Bed Width in feet:", "4")) || 4;
        const d = parseFloat(prompt("Enter Mulch Depth in inches (e.g. 3):", "3")) || 3;

        const area = l * w;
        const cuFt = area * (d / 12) * 1.05;
        const cuYds = cuFt / 27;
        const bags = Math.ceil(cuFt / 2.0);

        plannerZones.push({
            id: nextId,
            name: name,
            shape: "rectangle",
            length: l,
            width: w,
            depth: d,
            material: "hardwood",
            area: area,
            cuYds: cuYds,
            bags2cu: bags
        });

        initPlannerTable();
        updatePlannerDonut();
        showToast("New garden bed added to project planner!");
    }

    function removePlannerZone(id) {
        plannerZones = plannerZones.filter(z => z.id !== id);
        initPlannerTable();
        updatePlannerDonut();
    }

    function updatePlannerDonut() {
        const ctx = document.getElementById('plannerDonutChart');
        if (!ctx) return;

        if (plannerDonut) {
            plannerDonut.destroy();
            plannerDonut = null;
        }

        if (plannerZones.length === 0) return;

        const labels = plannerZones.map(z => z.name);
        const data = plannerZones.map(z => Math.round(z.area));

        const colors = [
            '#10b981', '#3b82f6', '#f59e0b', '#8b5cf6', '#ec4899', '#06b6d4', '#14b8a6'
        ];

        plannerDonut = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: colors.slice(0, data.length),
                    borderWidth: 2,
                    borderColor: document.documentElement.classList.contains('dark') ? '#1e293b' : '#ffffff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                        labels: {
                            font: { family: 'Inter', size: 10 },
                            color: document.documentElement.classList.contains('dark') ? '#94a3b8' : '#64748b'
                        }
                    }
                }
            }
        });
    }

    // --- Tab 4: Print Report Synchronizer ---
    function updatePrintReport(c) {
        document.getElementById('reportTimestamp').textContent = new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
        document.getElementById('reportRefCode').textContent = `MC-${Math.floor(1000 + Math.random() * 9000)}`;

        document.getElementById('reportTotalArea').textContent = `${Math.round(c.areaSqFt)} sq ft`;
        document.getElementById('reportTotalYards').textContent = `${c.grossCuYds.toFixed(2)} yd³`;
        document.getElementById('reportBags2cu').textContent = `${c.bags2cuWhole} Bags`;
        document.getElementById('reportTotalWeight').textContent = `${Math.round(c.weightLbs).toLocaleString()} lbs (${c.weightTons.toFixed(2)} Tons)`;

        // Sync Itemized Table with Active Zones
        const tbody = document.getElementById('reportItemizedTableBody');
        if (tbody) {
            if (plannerZones.length > 0) {
                tbody.innerHTML = plannerZones.map(z => {
                    let dims = z.shape === 'rectangle' ? `${z.length}' x ${z.width}'` : (z.shape === 'circle' ? `Dia: ${z.outerDia}'` : `${z.area} sq ft`);
                    return `
                    <tr>
                        <td class="p-2 border-r border-slate-200 dark:border-slate-700 font-bold">${z.name}</td>
                        <td class="p-2 border-r border-slate-200 dark:border-slate-700">${dims}</td>
                        <td class="p-2 border-r border-slate-200 dark:border-slate-700">${z.depth.toFixed(1)}"</td>
                        <td class="p-2 border-r border-slate-200 dark:border-slate-700">${z.area.toFixed(1)}</td>
                        <td class="p-2 border-r border-slate-200 dark:border-slate-700 font-bold text-brand-600">${z.cuYds.toFixed(2)}</td>
                        <td class="p-2">${z.bags2cu}</td>
                    </tr>`;
                }).join('');
            } else {
                tbody.innerHTML = `
                <tr>
                    <td class="p-2 border-r border-slate-200 dark:border-slate-700 font-bold">Primary Landscape Bed</td>
                    <td class="p-2 border-r border-slate-200 dark:border-slate-700">${c.dimDesc}</td>
                    <td class="p-2 border-r border-slate-200 dark:border-slate-700">${c.depth.toFixed(1)}"</td>
                    <td class="p-2 border-r border-slate-200 dark:border-slate-700">${c.areaSqFt.toFixed(1)}</td>
                    <td class="p-2 border-r border-slate-200 dark:border-slate-700 font-bold text-brand-600">${c.grossCuYds.toFixed(2)}</td>
                    <td class="p-2">${c.bags2cuWhole}</td>
                </tr>`;
            }
        }
    }

    // --- Tab Navigation ---
    function switchTab(tabId) {
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.tab-btn').forEach(b => {
            b.classList.remove('active', 'border-brand-600', 'text-brand-600', 'dark:text-brand-400');
            b.classList.add('border-transparent', 'text-slate-500');
        });

        const activePanel = document.getElementById('tab-' + tabId);
        const activeBtn = document.getElementById('tabBtn_' + tabId);
        if (activePanel) activePanel.classList.add('active');
        if (activeBtn) {
            activeBtn.classList.add('active', 'border-brand-600', 'text-brand-600', 'dark:text-brand-400');
            activeBtn.classList.remove('border-transparent', 'text-slate-500');
        }

        if (tabId === 'planner') {
            setTimeout(() => {
                initPlannerTable();
                updatePlannerDonut();
            }, 50);
        }
    }

    // --- Presets Loader ---
    function loadPreset() {
        const p = document.getElementById('presetSelect').value;
        if (p === 'preset_front') {
            setBedShape('rectangle');
            document.getElementById('dim_length').value = 30;
            document.getElementById('dim_width').value = 10;
            setDepth(3.0);
            setContingency(5);
        } else if (p === 'preset_perimeter') {
            setBedShape('area');
            document.getElementById('dim_direct_area').value = 450;
            setDepth(3.0);
            setContingency(5);
        } else if (p === 'preset_trees') {
            setBedShape('donut');
            document.getElementById('dim_outer_dia').value = 8;
            document.getElementById('dim_inner_dia').value = 2;
            setDepth(2.5);
            setContingency(5);
        } else if (p === 'preset_garden') {
            setBedShape('rectangle');
            document.getElementById('dim_length').value = 20;
            document.getElementById('dim_width').value = 10;
            setDepth(2.0);
            setContingency(5);
        } else if (p === 'preset_playground') {
            setBedShape('rectangle');
            document.getElementById('dim_length').value = 25;
            document.getElementById('dim_width').value = 16;
            setDepth(6.0);
            setContingency(10);
        } else if (p === 'preset_refresh') {
            setBedShape('area');
            document.getElementById('dim_direct_area').value = 1200;
            setDepth(1.0);
            setContingency(5);
        }
    }

    // --- Reset Defaults ---
    function resetDefaults() {
        setBedShape('rectangle');
        document.getElementById('dim_length').value = 30;
        document.getElementById('dim_width').value = 10;
        setDepth(3.0);
        setContingency(5);
        document.getElementById('materialSelect').selectedIndex = 0;
        calculate();
        showToast("Calculators reset to standard defaults.");
    }

    function triggerCalculation() {
        calculate();
        const card = document.getElementById('resultsCard');
        card.classList.add('shimmer-active');
        setTimeout(() => card.classList.remove('shimmer-active'), 800);
        showToast("Volume calculations refreshed!");
    }

    // --- FAQ Accordion ---
    function toggleFaq(idx) {
        const ans = document.getElementById('faqAns_' + idx);
        const icon = document.getElementById('faqIcon_' + idx);
        if (!ans) return;
        if (ans.classList.contains('hidden')) {
            ans.classList.remove('hidden');
            if (icon) icon.style.transform = 'rotate(180deg)';
        } else {
            ans.classList.add('hidden');
            if (icon) icon.style.transform = 'rotate(0deg)';
        }
    }

    // --- URL State Management ---
    function updateShareUrl(c) {
        const params = new URLSearchParams();
        params.set('shape', c.shape);
        params.set('depth', c.depth);
        params.set('buffer', c.contingency);
        if (c.shape === 'rectangle') {
            params.set('l', document.getElementById('dim_length').value);
            params.set('w', document.getElementById('dim_width').value);
        } else if (c.shape === 'circle') {
            params.set('dia', document.getElementById('dim_diameter').value);
        } else if (c.shape === 'area') {
            params.set('sqft', document.getElementById('dim_direct_area').value);
        }
        const newUrl = window.location.pathname + '?' + params.toString();
        window.history.replaceState({}, '', newUrl);
    }

    function parseUrlParams() {
        const params = new URLSearchParams(window.location.search);
        if (!params.has('shape') && !params.has('depth')) return;

        const shape = params.get('shape');
        if (shape && ['rectangle', 'circle', 'donut', 'triangle', 'area'].includes(shape)) {
            setBedShape(shape);
        }

        const depth = parseFloat(params.get('depth'));
        if (!isNaN(depth)) setDepth(depth);

        const buffer = parseFloat(params.get('buffer'));
        if (!isNaN(buffer)) setContingency(buffer);

        if (shape === 'rectangle') {
            if (params.has('l')) document.getElementById('dim_length').value = params.get('l');
            if (params.has('w')) document.getElementById('dim_width').value = params.get('w');
        } else if (shape === 'circle') {
            if (params.has('dia')) document.getElementById('dim_diameter').value = params.get('dia');
        } else if (shape === 'area') {
            if (params.has('sqft')) document.getElementById('dim_direct_area').value = params.get('sqft');
        }
    }

    function copyShareUrl() {
        navigator.clipboard.writeText(window.location.href).then(() => {
            showToast("Deep-linked project URL copied to clipboard!");
        });
    }

    function copyFormattedSummary() {
        const c = lastCalc;
        const text = `CalcWorld Mulch Requisition Summary:\\n` +
            `Surface Area: ${c.areaSqFt.toFixed(1)} sq ft\\n` +
            `Target Depth: ${c.depth.toFixed(1)} inches (Buffer: ${c.contingency}%)\\n` +
            `Volume: ${c.grossCuYds.toFixed(2)} Cubic Yards (${c.grossCuFt.toFixed(2)} Cu Ft)\\n` +
            `2.0 Cu Ft Bags: ${c.bags2cuWhole} Bags\\n` +
            `3.0 Cu Ft Bags: ${c.bags3cuWhole} Bags\\n` +
            `Estimated Weight: ${Math.round(c.weightLbs).toLocaleString()} lbs (${c.weightTons.toFixed(2)} Tons)\\n` +
            `Bulk Delivered Cost: $${c.bulkCost.toFixed(2)}\\n` +
            `URL: ${window.location.href}`;

        navigator.clipboard.writeText(text).then(() => {
            showToast("Project summary copied to clipboard!");
        });
    }

    function copyPlannerSummary() {
        let text = "CalcWorld Multi-Bed Yard Project Plan:\\n";
        plannerZones.forEach(z => {
            text += `- ${z.name}: ${z.area.toFixed(1)} sq ft @ ${z.depth}" -> ${z.cuYds.toFixed(2)} cu yds (${z.bags2cu} bags)\\n`;
        });
        navigator.clipboard.writeText(text).then(() => {
            showToast("Multi-zone plan copied to clipboard!");
        });
    }

    function showToast(msg) {
        const toast = document.getElementById('toast');
        const toastMsg = document.getElementById('toastMsg');
        if (!toast) return;
        if (toastMsg) toastMsg.textContent = msg;
        toast.classList.remove('opacity-0', 'pointer-events-none');
        toast.classList.add('opacity-100');
        setTimeout(() => {
            toast.classList.remove('opacity-100');
            toast.classList.add('opacity-0', 'pointer-events-none');
        }, 2600);
    }

    function toggleTheme() {
        if (document.documentElement.classList.contains('dark')) {
            document.documentElement.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        } else {
            document.documentElement.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        }
        if (costChart) updateCostChart(lastCalc);
        if (plannerDonut) updatePlannerDonut();
    }

    function handleLeadSubmit(e) {
        e.preventDefault();
        const input = document.getElementById('leadEmailInput');
        const msg = document.getElementById('leadSuccessMsg');
        const btn = document.getElementById('leadSubmitBtn');
        if (input && input.value) {
            btn.disabled = true;
            btn.textContent = 'Preparing PDF...';
            setTimeout(() => {
                btn.classList.add('hidden');
                input.classList.add('hidden');
                msg.classList.remove('hidden');
            }, 800);
        }
    }
</script>

</body>
</html>
"""

print("Writing full single-file calculator...")
full_html = part1_head + guide_html + part3_faq_footer_script

# Verify banned words
clean_text = re.sub(r'<[^>]+>', ' ', full_html).lower()
found_banned = []
for bw in BANNED_WORDS:
    # search word boundary
    pattern = r'\b' + re.escape(bw) + r'\b'
    if re.search(pattern, clean_text):
        found_banned.append(bw)

if found_banned:
    print(f"ERROR: Found banned words in text: {found_banned}")
    sys.exit(1)
else:
    print("CHECK PASSED: ZERO banned words found!")

# Verify word count of guide
guide_plain = re.sub(r'<[^>]+>', ' ', guide_html)
words = [w for w in guide_plain.split() if w]
print(f"Educational guide word count: {len(words)} words (Target: 1200+)")
if len(words) < 1200:
    print("ERROR: Educational guide has less than 1200 words!")
    sys.exit(1)
else:
    print("CHECK PASSED: Educational guide exceeds 1200 words!")

# Verify AdSense slots
for slot_id in ["ad-slot-1", "ad-slot-2", "ad-slot-3", "ad-slot-4", "ad-slot-5"]:
    if f'id="{slot_id}"' not in full_html:
        print(f"ERROR: Missing AdSense slot: {slot_id}")
        sys.exit(1)
print("CHECK PASSED: All 5 AdSense slots verified!")

# Write to both paths
with open(target_path_onedrive, 'w', encoding='utf-8') as f:
    f.write(full_html)
print(f"SUCCESS: Written file to {target_path_onedrive}")

if os.path.exists(os.path.dirname(target_path_direct)):
    try:
        with open(target_path_direct, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"SUCCESS: Written file to {target_path_direct}")
    except Exception as e:
        print(f"Note: direct path already synced via OneDrive or error: {e}")

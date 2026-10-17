import glob
import os
import re
import sys
import datetime
import shutil

sys.stdout.reconfigure(encoding='utf-8')

ONEDRIVE_ROOT = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine'
DESKTOP_ROOT = r'C:\Users\Muham\Desktop\Calc\calcworld-engine'

ONEDRIVE_CALC_DIR = os.path.join(ONEDRIVE_ROOT, 'calculators')
DESKTOP_CALC_DIR = os.path.join(DESKTOP_ROOT, 'calculators')

BASE_URL = 'https://calcworld.net'
TODAY = datetime.date.today().isoformat()

# 1. Generate robots.txt
robots_content = f"""# CalcWorld Production Robots Directive
User-agent: *
Allow: /

# Sitemap Index
Sitemap: {BASE_URL}/sitemap.xml
"""

# 2. Collect all calculator filenames
calc_files = sorted(glob.glob(os.path.join(ONEDRIVE_CALC_DIR, '*.html')))

# 3. Generate sitemap.xml
sitemap_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    '  <!-- Homepage -->',
    '  <url>',
    f'    <loc>{BASE_URL}/</loc>',
    f'    <lastmod>{TODAY}</lastmod>',
    '    <changefreq>daily</changefreq>',
    '    <priority>1.0</priority>',
    '  </url>'
]

for f in calc_files:
    fname = os.path.basename(f)
    sitemap_lines.append('  <url>')
    sitemap_lines.append(f'    <loc>{BASE_URL}/calculators/{fname}</loc>')
    sitemap_lines.append(f'    <lastmod>{TODAY}</lastmod>')
    sitemap_lines.append('    <changefreq>weekly</changefreq>')
    sitemap_lines.append('    <priority>0.8</priority>')
    sitemap_lines.append('  </url>')

sitemap_lines.append('</urlset>')
sitemap_content = '\n'.join(sitemap_lines)

# Write robots.txt and sitemap.xml
with open(os.path.join(ONEDRIVE_ROOT, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)
with open(os.path.join(ONEDRIVE_ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

if os.path.exists(DESKTOP_ROOT):
    with open(os.path.join(DESKTOP_ROOT, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots_content)
    with open(os.path.join(DESKTOP_ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

print(f"Generated robots.txt and sitemap.xml with {len(calc_files) + 1} URLs!")

# 4. Process each calculator for Canonical & OG Tags
updated_canonical_count = 0
updated_og_count = 0

for f in calc_files:
    fname = os.path.basename(f)
    canonical_url = f"{BASE_URL}/calculators/{fname}"
    
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # Extract title and description
    title_match = re.search(r'<title>(.*?)</title>', c, re.I | re.DOTALL)
    title_text = title_match.group(1).strip() if title_match else f"{fname.replace('-', ' ').replace('.html', '').title()} | CalcWorld"
    
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', c, re.I)
    desc_text = desc_match.group(1).strip() if desc_match else f"Free, fast, and accurate {title_text}. Instant calculations, visual charts, and detailed explanations on CalcWorld."
    
    # 4a. Fix or inject Canonical
    canonical_tag = f'<link rel="canonical" href="{canonical_url}">'
    if re.search(r'<link\s+rel=["\']canonical["\']', c, re.I):
        c = re.sub(r'<link\s+rel=["\']canonical["\'][^>]*>', canonical_tag, c, flags=re.I)
    else:
        # insert after <head> or before </head>
        if '</head>' in c:
            c = c.replace('</head>', f'    {canonical_tag}\n</head>', 1)
    
    # Also clean up any example.com or calcworld.com in JSON-LD schemas
    c = c.replace('https://example.com/calculators/', f'{BASE_URL}/calculators/')
    c = c.replace('http://example.com/calculators/', f'{BASE_URL}/calculators/')
    c = c.replace('https://example.com/', f'{BASE_URL}/')
    c = c.replace('http://example.com/', f'{BASE_URL}/')
    c = c.replace('https://calcworld.example.com/', f'{BASE_URL}/')
    c = c.replace('https://calcworld.com/calculators/', f'{BASE_URL}/calculators/')
    c = c.replace('https://calcworld.com/', f'{BASE_URL}/')
    
    # 4b. Inject Open Graph and Twitter tags if missing
    if 'og:title' not in c:
        og_block = f"""
    <!-- Open Graph & Social SEO Meta Tags -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title_text}">
    <meta property="og:description" content="{desc_text}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:site_name" content="CalcWorld">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title_text}">
    <meta name="twitter:description" content="{desc_text}">
"""
        c = c.replace('</head>', f'{og_block}</head>', 1)
        updated_og_count += 1
        
    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(c)
        
    updated_canonical_count += 1

print(f"Updated Canonical on {updated_canonical_count} calculators.")
print(f"Injected Open Graph & Twitter meta tags on {updated_og_count} calculators.")

# 5. Mirror to Desktop
if os.path.exists(DESKTOP_CALC_DIR):
    for f in calc_files:
        dest = os.path.join(DESKTOP_CALC_DIR, os.path.basename(f))
        shutil.copy2(f, dest)
    print("Desktop mirror updated successfully!")

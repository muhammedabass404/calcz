import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

article_stats = []
seo_stats = {
    'canonical_domain_issues': set(),
    'missing_meta_desc': 0,
    'missing_schema_faq': 0,
    'missing_schema_webcalc': 0,
    'missing_og_tags': 0,
}
adsense_stats = {
    'ad_slots_count': {},
    'has_real_adsense_script': 0
}

for f in files:
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # 1. Article length
    m_art = re.search(r'<article[^>]*>(.*?)</article>', c, re.DOTALL | re.I)
    if m_art:
        art_text = re.sub(r'<[^>]+>', ' ', m_art.group(1))
        words = len(art_text.split())
        article_stats.append((name, words, True))
    else:
        # Check if there is a prose section or educational section outside <article>
        m_sec = re.search(r'<(?:section|div)[^>]*(?:class=["\'][^"\']*prose[^"\']*["\']|id=["\'][^"\']*guide[^"\']*["\'])(.*?)(?:</section>|</div>\s*<!--)', c, re.DOTALL | re.I)
        if m_sec:
            sec_text = re.sub(r'<[^>]+>', ' ', m_sec.group(1))
            words = len(sec_text.split())
            article_stats.append((name, words, False))
        else:
            article_stats.append((name, 0, False))

    # 2. Canonical
    m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', c, re.I)
    if m_canon:
        domain_match = re.search(r'https?://([^/]+)', m_canon.group(1))
        if domain_match:
            seo_stats['canonical_domain_issues'].add(domain_match.group(1))
    
    if not re.search(r'<meta\s+name=["\']description["\']', c, re.I):
        seo_stats['missing_meta_desc'] += 1
    if 'FAQPage' not in c:
        seo_stats['missing_schema_faq'] += 1
    if 'WebApplication' not in c:
        seo_stats['missing_schema_webcalc'] += 1
    if 'og:title' not in c:
        seo_stats['missing_og_tags'] += 1
        
    # 3. Ad slots
    ad_slots = re.findall(r'id=["\'](ad[-_]slot[-_]\d+)["\']', c, re.I)
    adsense_stats['ad_slots_count'][len(ad_slots)] = adsense_stats['ad_slots_count'].get(len(ad_slots), 0) + 1
    if 'pagead2.googlesyndication.com' in c:
        adsense_stats['has_real_adsense_script'] += 1

words_only = [w for _, w, _ in article_stats]
print(f"Total Calculators: {len(files)}")
print(f"Article Word Count Distribution:")
print(f"  Min words: {min(words_only)}")
print(f"  Max words: {max(words_only)}")
print(f"  Average words: {sum(words_only) // len(words_only)}")
print(f"  Under 500 words: {sum(1 for w in words_only if w < 500)}")
print(f"  500 - 1000 words: {sum(1 for w in words_only if 500 <= w < 1000)}")
print(f"  1000 - 1500 words: {sum(1 for w in words_only if 1000 <= w < 1500)}")
print(f"  1500+ words: {sum(1 for w in words_only if w >= 1500)}")

print("\nSEO Stats:")
print(f"  Canonical domains found: {seo_stats['canonical_domain_issues']}")
print(f"  Missing meta description: {seo_stats['missing_meta_desc']}")
print(f"  Missing Schema FAQPage: {seo_stats['missing_schema_faq']}")
print(f"  Missing Schema WebApplication: {seo_stats['missing_schema_webcalc']}")
print(f"  Missing OG tags: {seo_stats['missing_og_tags']}")

print("\nAdSense Stats:")
print(f"  Ad slots per page distribution: {adsense_stats['ad_slots_count']}")
print(f"  Has live AdSense script tag: {adsense_stats['has_real_adsense_script']}")

print("\nTop 10 shortest articles:")
sorted_by_words = sorted(article_stats, key=lambda x: x[1])
for name, w, has_art in sorted_by_words[:10]:
    print(f"  {name}: {w} words (has_article_tag={has_art})")

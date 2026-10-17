import glob
import os
import re

print("=== GOOGLE ADSENSE COMPLIANCE AUDIT ===")

# 1. Check Mandatory Trust Pages
required_pages = {
    "About Us": "calcworld-engine/about-us/index.html",
    "Privacy Policy": "calcworld-engine/privacy-policy/index.html",
    "Terms of Service": "calcworld-engine/terms-of-service/index.html",
    "Contact & Support": "calcworld-engine/contact/index.html",
    "404 Error Page": "calcworld-engine/404.html"
}

for name, path in required_pages.items():
    exists = os.path.isfile(path)
    size = os.path.getsize(path) if exists else 0
    print(f"[{'PASS' if exists else 'FAIL'}] {name}: {path} ({size} bytes)")

# 2. Check Privacy Policy clauses
with open("calcworld-engine/privacy-policy/index.html", "r", encoding="utf-8") as f:
    priv_text = f.read().lower()

clauses = {
    "Google AdSense Mention": "adsense" in priv_text or "google" in priv_text,
    "DoubleClick DART Cookie": "dart" in priv_text or "doubleclick" in priv_text,
    "Third-Party Advertising Cookies": "cookie" in priv_text and "third-party" in priv_text,
    "Opt-out Links (aboutads.info / Google Ads Settings)": "aboutads.info" in priv_text or "settings/ads" in priv_text,
    "GDPR Compliance Clause": "gdpr" in priv_text,
    "CCPA Compliance Clause": "ccpa" in priv_text,
    "Zero Server Telemetry / Client-side Privacy": "client-side" in priv_text
}

print("\n--- Privacy Policy Requirements ---")
for clause, status in clauses.items():
    print(f"[{'PASS' if status else 'FAIL'}] {clause}")

# 3. Check Thin Content / Article Length Across Calculators
calc_files = glob.glob("calcworld-engine/calculators/*.html")
word_counts = []
has_faq = 0
has_schema = 0

for cf in calc_files:
    with open(cf, "r", encoding="utf-8") as f:
        content = f.read()
    # strip HTML tags to estimate word count
    text = re.sub(r'<[^>]+>', ' ', content)
    words = len(re.findall(r'\b\w+\b', text))
    word_counts.append(words)
    if "FAQPage" in content or "faq" in content.lower():
        has_faq += 1
    if "application/ld+json" in content:
        has_schema += 1

avg_words = sum(word_counts) // len(word_counts) if word_counts else 0
min_words = min(word_counts) if word_counts else 0
max_words = max(word_counts) if word_counts else 0

print(f"\n--- Content Quality & EEAT Metrics (Total Calculators: {len(calc_files)}) ---")
print(f"Average Words per Calculator: {avg_words} words")
print(f"Minimum Words: {min_words} words | Maximum Words: {max_words} words")
print(f"Calculators with FAQ Schema: {has_faq} / {len(calc_files)}")
print(f"Calculators with JSON-LD Schema: {has_schema} / {len(calc_files)}")

# 4. Check Ad Placement Markup
ad_slot_types = set()
for cf in calc_files[:15]:
    with open(cf, "r", encoding="utf-8") as f:
        content = f.read()
    slots = re.findall(r'<div[^>]*class=["\'][^"\']*(?:ad-slot|ad-unit|adblock)[^"\']*["\'][^>]*>', content)
    for s in slots:
        ad_slot_types.add(s[:80])

print("\n--- Ad Slot Markup Sample ---")
for st in list(ad_slot_types)[:5]:
    print(" ", st)

# 5. Check ads.txt
ads_txt_path = "calcworld-engine/ads.txt"
print(f"\n--- ads.txt Status: {'Exists' if os.path.isfile(ads_txt_path) else 'Missing (Needs template)'} ---")

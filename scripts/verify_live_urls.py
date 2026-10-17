import urllib.request
import re

for url in [
    'http://localhost:8080/about-us/',
    'http://localhost:8080/privacy-policy/',
    'http://localhost:8080/terms-of-service/',
    'http://localhost:8080/contact/',
    'http://localhost:8080/404.html'
]:
    res = urllib.request.urlopen(url)
    print(f"URL: {url} -> Status {res.status}")
    html = res.read().decode('utf-8')
    links = re.findall(r'href=["\']([^"\']+)["\']', html)
    legal_links = [l for l in links if any(k in l for k in ['about', 'privacy', 'terms', 'contact'])]
    print("  Legal links found:", sorted(list(set(legal_links))))
    has_official_logo = 'CalcWorld Home' in html and 'Engine 2026' in html and 'svg' in html
    print(f"  Official Logo Present: {has_official_logo}")
    has_emerald_mismatch = 'emerald-600' in html
    print(f"  Has Emerald Color Mismatch: {has_emerald_mismatch}")
    print()

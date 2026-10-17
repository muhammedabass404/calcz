# -*- coding: utf-8 -*-
"""
1. Fix all 25 non-dark calculators so every calculator has class="dark scroll-smooth"
2. Ensure theme persistence script is in head
3. Unify all footer legal links to /legal-pages/*.html
4. Create root-level folders with index.html for:
   /about-us, /about, /terms-of-service, /terms, /privacy-policy, /privacy, /contact, /contact-us
5. Create Cloudflare Pages _redirects file
6. Mirror everything to Desktop directory
"""

import os
import re
import shutil

calc_dir = "calcworld-engine/calculators"
root_dir = "calcworld-engine"
desktop_dir = "C:/Users/Muham/Desktop/Calc/calcworld-engine"

def fix_calculator_themes_and_footers():
    theme_fixed = 0
    links_fixed = 0

    for f in sorted(os.listdir(calc_dir)):
        if f.endswith(".html"):
            fp = os.path.join(calc_dir, f)
            with open(fp, "r", encoding="utf-8", errors="ignore") as fl:
                c = fl.read()

            modified = False

            # 1. Fix html class to have "dark scroll-smooth"
            m_html = re.search(r'<html[^>]*class=["\']([^"\']*)["\']', c, re.I)
            if m_html:
                cls = m_html.group(1)
                classes = cls.split()
                if "dark" not in classes:
                    classes.append("dark")
                if "scroll-smooth" not in classes:
                    classes.append("scroll-smooth")
                new_cls = " ".join(classes)
                if new_cls != cls:
                    c = c[:m_html.start(1)] + new_cls + c[m_html.end(1):]
                    modified = True
                    theme_fixed += 1
            else:
                # No class on html tag
                c = re.sub(r'<html([^>]*)>', r'<html\1 class="dark scroll-smooth">', c, count=1, flags=re.I)
                modified = True
                theme_fixed += 1

            # 2. Ensure FOUC script is in head
            fouc_script = """<script>
    if (localStorage.getItem('theme') === 'light') {
        document.documentElement.classList.remove('dark');
    } else {
        document.documentElement.classList.add('dark');
    }
</script>"""
            if "localStorage.getItem('theme')" not in c:
                if "<head>" in c:
                    c = c.replace("<head>", f"<head>\n    {fouc_script}", 1)
                    modified = True

            # 3. Unify footer legal links
            # Replace various legal URLs with standard relative or absolute paths
            # In calculators (which are in /calculators/), relative path to legal-pages is ../legal-pages/
            c_new = re.sub(r'href=["\'](?:https?://calcworld\.net)?(?:/legal)?/(?:about-us|about)(?:\.html)?["\']', 'href="../legal-pages/about.html"', c, flags=re.I)
            c_new = re.sub(r'href=["\'](?:https?://calcworld\.net)?(?:/legal)?/(?:privacy-policy|privacy)(?:\.html)?["\']', 'href="../legal-pages/privacy.html"', c_new, flags=re.I)
            c_new = re.sub(r'href=["\'](?:https?://calcworld\.net)?(?:/legal)?/(?:terms-of-service|terms)(?:\.html)?["\']', 'href="../legal-pages/terms.html"', c_new, flags=re.I)
            c_new = re.sub(r'href=["\'](?:https?://calcworld\.net)?(?:/legal)?/(?:contact|contact-us)(?:\.html)?["\']', 'href="../legal-pages/contact.html"', c_new, flags=re.I)

            # Also fix bare /contact or /privacy
            c_new = c_new.replace('href="/contact"', 'href="../legal-pages/contact.html"')
            c_new = c_new.replace('href="/privacy"', 'href="../legal-pages/privacy.html"')
            c_new = c_new.replace('href="/terms"', 'href="../legal-pages/terms.html"')
            c_new = c_new.replace('href="/about-us"', 'href="../legal-pages/about.html"')

            if c_new != c:
                c = c_new
                modified = True
                links_fixed += 1

            if modified:
                with open(fp, "w", encoding="utf-8") as fl:
                    fl.write(c)

    print(f"Fixed dark theme in {theme_fixed} calculators!")
    print(f"Standardized footer links in {links_fixed} calculators!")

def create_root_legal_folders():
    lp_dir = os.path.join(root_dir, "legal-pages")
    about_content = open(os.path.join(lp_dir, "about.html"), "r", encoding="utf-8").read()
    privacy_content = open(os.path.join(lp_dir, "privacy.html"), "r", encoding="utf-8").read()
    terms_content = open(os.path.join(lp_dir, "terms.html"), "r", encoding="utf-8").read()
    contact_content = open(os.path.join(lp_dir, "contact.html"), "r", encoding="utf-8").read()

    # Map of folder -> content
    folder_map = {
        "about-us": about_content,
        "about": about_content,
        "privacy-policy": privacy_content,
        "privacy": privacy_content,
        "terms-of-service": terms_content,
        "terms": terms_content,
        "contact": contact_content,
        "contact-us": contact_content
    }

    for folder_name, content in folder_map.items():
        # Create in root
        f_path = os.path.join(root_dir, folder_name)
        os.makedirs(f_path, exist_ok=True)
        idx_file = os.path.join(f_path, "index.html")
        with open(idx_file, "w", encoding="utf-8") as f:
            f.write(content)

    print("Created all root-level legal folders and index.html files!")

def create_cloudflare_redirects():
    redirects_content = """/about-us /legal-pages/about.html 301
/about /legal-pages/about.html 301
/privacy-policy /legal-pages/privacy.html 301
/privacy /legal-pages/privacy.html 301
/terms-of-service /legal-pages/terms.html 301
/terms /legal-pages/terms.html 301
/contact /legal-pages/contact.html 301
/contact-us /legal-pages/contact.html 301
"""
    red_file = os.path.join(root_dir, "_redirects")
    with open(red_file, "w", encoding="utf-8") as f:
        f.write(redirects_content)
    print("Created _redirects file for Cloudflare Pages!")

def sync_to_desktop():
    if os.path.exists(desktop_dir):
        for root, dirs, files in os.walk(root_dir):
            rel = os.path.relpath(root, root_dir)
            dest = os.path.join(desktop_dir, rel)
            os.makedirs(dest, exist_ok=True)
            for file in files:
                sf = os.path.join(root, file)
                df = os.path.join(dest, file)
                if not os.path.exists(df) or os.path.getmtime(sf) > os.path.getmtime(df):
                    shutil.copy2(sf, df)
        print("Synchronized all changes to Desktop mirror directory!")

def main():
    fix_calculator_themes_and_footers()
    create_root_legal_folders()
    create_cloudflare_redirects()
    sync_to_desktop()
    print("All theme fixes and legal routing completed successfully!")

if __name__ == "__main__":
    main()

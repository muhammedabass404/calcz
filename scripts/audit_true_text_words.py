import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

calc_dir = r'C:\Users\Muham\OneDrive\Desktop\Calc\calcworld-engine\calculators'
files = sorted(glob.glob(os.path.join(calc_dir, '*.html')))

results = []

for f in files:
    fname = os.path.basename(f)
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    
    # Strip <head>, <script>, <style>, and forms/inputs to measure purely editorial/text content
    c_body = c
    if '<body' in c_body:
        c_body = c_body.split('<body', 1)[1]
    
    # Remove script tags
    c_clean = re.sub(r'<script[^>]*>.*?</script>', ' ', c_body, flags=re.DOTALL | re.I)
    c_clean = re.sub(r'<style[^>]*>.*?</style>', ' ', c_clean, flags=re.DOTALL | re.I)
    c_clean = re.sub(r'<svg[^>]*>.*?</svg>', ' ', c_clean, flags=re.DOTALL | re.I)
    
    # Extract only paragraphs, headings, list items, blockquotes, and table text
    text_blocks = re.findall(r'<(?:p|h1|h2|h3|h4|h5|li|blockquote|td|th)[^>]*>(.*?)</(?:p|h1|h2|h3|h4|h5|li|blockquote|td|th)>', c_clean, re.DOTALL | re.I)
    combined_text = ' '.join(re.sub(r'<[^>]+>', ' ', b) for b in text_blocks)
    words = len(combined_text.split())
    
    # Check if there is an <article> tag
    has_article_tag = '<article' in c
    
    results.append((fname, words, has_article_tag))

sorted_res = sorted(results, key=lambda x: x[1])

print(f"Total calculators: {len(results)}")
print(f"Distribution of true text content words:")
print(f"  < 500 words: {sum(1 for _, w, _ in results if w < 500)}")
print(f"  500 - 1000 words: {sum(1 for _, w, _ in results if 500 <= w < 1000)}")
print(f"  1000 - 1500 words: {sum(1 for _, w, _ in results if 1000 <= w < 1500)}")
print(f"  1500+ words: {sum(1 for _, w, _ in results if w >= 1500)}")

print("\nShortest 20 calculators by true text content:")
for name, w, has_art in sorted_res[:25]:
    print(f"  {name:40} : {w:4d} words (has_article={has_art})")

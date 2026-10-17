import glob
import os

calc_dir = r'C:\Users\Muham\Desktop\Calc\calcworld-engine\calculators'
files = glob.glob(os.path.join(calc_dir, '*.html'))

all_have_article = True
all_have_form = True
all_have_core = True

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    if 'article, [id*="seo-article"]' not in c:
        all_have_article = False
        print('Missing article suppression in:', os.path.basename(f))
    if 'form, [id*="calc-form"]' not in c:
        all_have_form = False
        print('Missing form suppression in:', os.path.basename(f))
    if 'id="calcworld-print-core"' not in c:
        all_have_core = False
        print('Missing print core in:', os.path.basename(f))

print(f"Desktop Total files checked: {len(files)}")
print(f"All 207 Desktop calculators hide article: {all_have_article}")
print(f"All 207 Desktop calculators hide form: {all_have_form}")
print(f"All 207 Desktop calculators have print core: {all_have_core}")

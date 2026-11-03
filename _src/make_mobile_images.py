"""Mobile-only carousel images, sliced from 2x exports of the Figma mobile frames."""
import json, os, sys, importlib.util
from PIL import Image
spec = importlib.util.spec_from_file_location("mi", "/home/claude/build/make_images.py")
OUT = sys.argv[1]
RAW = '/home/claude/build/raw2'
S = 2

# reuse clean_edges/save_webp without re-running the desktop script
src = open('/home/claude/build/make_images.py').read()
ns = {}
exec(src.split('manifest = {}')[0].replace('OUT = sys.argv[1]', 'OUT = None'), ns)
clean_edges, save_webp = ns['clean_edges'], ns['save_webp']

MROWS = {
  'onboarding': [
    ('13107', None, [(0,0,240,524,16),(256,0,240,524,16),(512,0,240,524,16),(768,0,240,524,16)]),
    ('13383', None, [(0,0,654,518,16)]),
    ('13418', '#fafafa', [(0,0,239.8,524,16),(256,0,239.8,524,16),(512,0,239.8,524,16),(767,0,240,524,16),(1023,0,558,524,14.21),(1597,0,558,524,14.21)]),
  ],
  'product-catalog': [
    ('3847', '#e6e6e6', [(0,0,358,782.1,16)]),
    ('4340', '#e6e6e6', [(0,0,554,524,16),(570,0,554,524,16),(1140,0,554,524,16)]),
    ('4362', '#fafafa', [(0,0,1103.5,592.1,0),(1119.5,0,284.3,592,16),(1419.8,0,800,590,16),(2235.8,0,800,590,16)]),
    ('14243', '#fafafa', [(0,0,358,592,15.27),(374,0,358,592,15.27),(748,0,800,590,16)]),
  ],
  'referral': [
    ('21721', '#fafafa', [(0,0,239.8,524,17.76),(261.1,0,239.8,524,17.76),(522.2,0,500.9,524,17.76)], 21.3),
    ('17634', '#fafafa', [(0,0,460,524,14.21),(476,0,460,524,14.21),(952,0,460,524,14.21),(1428,0,460,524,14.21)]),
    ('22766', '#fafafa', [(0,0,427,524,16),(443,0,270,525,0),(729,0,270,525,16),(1015,0,270,525,16),(1301,0,270,525,16),(1587,0,734,524,16)]),
    ('34858', '#fafafa', [(0,0,774,512,16)]),
  ],
}
manifest = {}
for page, rows in MROWS.items():
    manifest[page] = []
    for ri, (rid, band, items, *gap) in enumerate(rows):
        im = Image.open(f'{RAW}/m_{rid}.png').convert('RGB')
        bg = tuple(int(band[i:i+2], 16) for i in (1, 3, 5)) if band else (255, 255, 255)
        out = []
        for ii, (x, y, w, h, r) in enumerate(items):
            crop = im.crop((round(x*S), round(y*S), round((x+w)*S), round((y+h)*S)))
            crop = clean_edges(crop, r * S, bg)
            name = f'{page}/m-row{ri+1}-{ii+1}.webp'
            save_webp(crop, f'{OUT}/{name}')
            out.append({'src': f'/assets/img/{name}', 'w': round(w, 1), 'h': round(h, 1), 'r': r})
        manifest[page].append({'id': rid, 'band': band, 'items': out, **({'gap': gap[0]} if gap else {})})
json.dump(manifest, open('/home/claude/build/rows_m.json', 'w'), indent=1)
print('ok', {k: [len(r['items']) for r in v] for k, v in manifest.items()})

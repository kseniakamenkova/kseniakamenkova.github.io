"""Generate the static pages from content.py and rows.json.

Run from the repository root:  python3 _src/build.py
"""
import html, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_src"))
from content import HOME, CASES, LINKEDIN, CV, TELEGRAM, SKYENG  # noqa: E402

ROWS = json.load(open(os.path.join(ROOT, "_src", "rows.json")))
ROWS_M = json.load(open(os.path.join(ROOT, "_src", "rows_m.json")))  # phone-only carousels
SITE = "https://kseniakamenkova.github.io"


SHORT_WORDS = r"a|an|the|of|to|in|on|at|by|for|and|or|but|nor|with|from|as|is|it|be|we|i|my|our|no|so|up|per|via|vs|its|if|into|onto|than|that|this|both|each"
NBSP_RE = __import__("re").compile(r"(?<![\w’'])(" + SHORT_WORDS + r") (?=\S)", __import__("re").IGNORECASE)


def nbsp(s):
    """Glue short words to the next word with a non-breaking space so they never hang at a line end."""
    return NBSP_RE.sub(lambda m: m.group(1) + "\u00a0", s)


def esc(s):
    return html.escape(nbsp(s), quote=True).replace("&lt;b&gt;", "<b>").replace("&lt;/b&gt;", "</b>")


def ext(href, text, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{href}" target="_blank" rel="noopener">{esc(text)}</a>'


def asset_version(rel):
    """Short content hash so browsers fetch the new file right after an update."""
    import hashlib
    with open(os.path.join(ROOT, rel), "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:8]


def head(title, description, path):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}/assets/img/apple-touch-icon.png">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/Inter-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css?v={asset_version('assets/css/style.css')}">
</head>
"""


def header():
    return f"""<header class="site-header">
  <nav class="site-header__links" aria-label="Profiles">
    {ext(LINKEDIN, "LinkedIn")}
    {ext(CV, "CV")}
  </nav>
</header>
"""


def contact():
    return f"""<section class="contact" aria-label="Contact">
  <img class="contact__img" src="/assets/img/shiba.webp" alt="" width="140" height="177" loading="lazy">
  <div class="contact__text">
    <h2 class="contact__title">Thank you</h2>
    <p class="contact__line">Feel free to reach out via {ext(LINKEDIN, "LinkedIn", "u")}<br class="contact__br"> or telegram {ext(TELEGRAM, "@kskamenkova", "plain")}</p>
  </div>
</section>
"""


def page(title, description, path, body_cls, main):
    return head(title, description, path) + f"""<body class="{body_cls}">
{header()}<main>
{main}</main>
<script src="/assets/js/main.js?v={asset_version('assets/js/main.js')}" defer></script>
</body>
</html>
"""


# ---------- home ----------
def home():
    h = HOME
    cards = []
    for c in h["cards"]:
        bx, by, bw, bhh = c["crop"]["box"]
        iw, ih, il, it = c["crop"]["img"]
        mbx, mby, mbw, mbh = c["mcrop"]["box"]
        miw, mih, mil, mit = c["mcrop"]["img"]
        mk = lambda ms: "".join(f'<div class="metric"><p class="metric__value">{esc(v)}</p><p class="metric__label">{esc(l)}</p></div>' for v, l in ms)
        metrics = mk(c["metrics"])
        mmetrics = mk(c.get("mmetrics", c["metrics"]))
        crop_vars = f"--x:{bx}px;--y:{by}px;--w:{bw}px;--h:{bhh}px;--mx:{mbx}px;--my:{mby}px;--mw:{mbw}px;--mh:{mbh}px"
        img_vars = f"--iw:{iw};--ih:{ih};--il:{il};--it:{it};--miw:{miw};--mih:{mih};--mil:{mil};--mit:{mit}"
        cards.append(f"""      <article class="project">
        <a class="project__card" href="/{c['slug']}/" aria-label="Open case study: {esc(c['label'])}">
          <img class="project__mimg" src="/assets/img/home/m{c['img']}.webp" alt="" width="358" height="403" loading="lazy">
          <span class="project__year">{esc(c['year'])}</span>
          <span class="project__label">{esc(c['label'])}</span>
          <span class="project__btn" aria-hidden="true"><img src="/assets/img/arrow-card.svg" alt="" width="17" height="17"></span>
          <span class="project__media" aria-hidden="true">
            <span class="project__crop" style="{crop_vars}">
              <img src="/assets/img/home/{c['img']}.webp" alt="" style="{img_vars}" loading="lazy">
            </span>
          </span>
        </a>
        <div class="project__info">
          <p class="project__text">{html.escape(c['text'])}</p>
          <div class="project__line"></div>
          <div class="project__metrics">{metrics}</div>
          <div class="project__mmetrics">{mmetrics}</div>
        </div>
      </article>
""")
    intro = "".join(f'<p>{esc(p)}</p>' for p in h["intro"])
    main = f"""<div class="container home">
  <section class="hello">
    <div class="hello__avatar"><img src="/assets/img/home/avatar.webp" alt="Ksenia Kamenkova" width="288" height="383"></div>
    <div class="hello__text">
      <h1 class="hello__title">{esc(h['name'])}</h1>
      <div class="hello__intro">{intro}</div>
    </div>
  </section>
  <section class="projects" aria-labelledby="projects-title">
    <h2 id="projects-title" class="projects__title">Projects</h2>
    <div class="projects__grid">
{''.join(cards)}    </div>
  </section>
  {contact()}</div>
"""
    return page(h["title"], h["description"], "/", "page-home", main)


# ---------- case pages ----------
def text_block(t, cls):
    return f'<p class="{cls}">{esc(t)}</p>'


def body_item(item):
    kind = item[0]
    if kind == "p":
        return text_block(item[1], "body")
    if kind == "p_desktop":  # shown on desktop only
        return text_block(item[1], "body only-d")
    if kind == "callout":
        return f'<div class="callout"><p class="callout__label">{esc(item[1])}</p>{text_block(item[2], "body")}</div>'
    if kind == "points":
        lis = "".join(f"<li>{esc(t)}</li>" for t in item[1])
        return f'<ul class="points">{lis}</ul>'
    if kind == "metrics":
        ms = "".join(f'<div class="metric"><p class="metric__value">{esc(v)}</p><p class="metric__label">{esc(l)}</p></div>' for v, l in item[1])
        return f'<div class="metrics">{ms}</div>'
    if kind == "also":
        lis = "".join(f"<li>{esc(t)}</li>" for t in item[1])
        return f'<div class="also"><p class="also__title">also:</p><ul class="also__list">{lis}</ul></div>'
    if kind == "groups":
        out = []
        for g in item[1]:
            sub, txt = g[0], g[1]
            extra = ""
            if len(g) > 2:
                lis = "".join(f"<li>{esc(t)}</li>" for t in g[2])
                extra = f'<ul class="body-list">{lis}</ul>' + (text_block(g[3], "body") if g[3] else "")
            out.append(f'<div class="group"><h3 class="group__title">{esc(sub)}</h3>{text_block(txt, "body")}{extra}</div>')
        return f'<div class="groups">{"".join(out)}</div>'
    if kind == "review":
        _, name, role, photo, txt = item
        paras = "".join(f"<p>{esc(p).replace(chr(10), '<br>')}</p>" for p in txt.split("\n\n"))
        return f"""<figure class="review">
          <img class="review__quote" src="/assets/img/quote.svg" alt="" width="54" height="44">
          <figcaption class="review__who">
            <img class="review__photo" src="{photo}" alt="" width="54" height="54" loading="lazy">
            <span class="review__about"><span class="review__name">{esc(name)}</span><span class="review__role">{esc(role)}</span></span>
          </figcaption>
          <blockquote class="review__text">{paras}</blockquote>
        </figure>"""
    raise ValueError(kind)


def section(heading, body, hidden=False, mtitle=None):
    inner = "".join(body_item(b) for b in body)
    label = f'<span class="t-d">{esc(heading)}</span><span class="t-m">{esc(mtitle)}</span>' if mtitle else esc(heading)
    title = f'<div class="section__title" aria-hidden="true"></div>' if hidden else f'<h2 class="section__title">{label}</h2>'
    cls = "section section--untitled" if hidden else "section"
    return f"""<section class="{cls}">
      {title}
      <div class="section__body">{inner}</div>
    </section>
"""


def scaled_row(row, height):
    """A phone carousel made from a desktop row: same images, scaled to the phone screen height."""
    k = height / max(it["h"] for it in row["items"])
    return {"band": row["band"], "items": [
        {"src": it["src"], "w": round(it["w"] * k, 1), "h": round(it["h"] * k, 1), "r": round(it["r"] * k, 2)}
        for it in row["items"]]}


def image_row(slug, n, mobile=False, attrs=""):
    if mobile and slug not in ROWS_M:  # no phone frame in Figma yet: reuse the desktop screens
        row = scaled_row(ROWS[slug][n - 1], CASES[slug].get("mobile_row_height", 524))
    else:
        row = (ROWS_M if mobile else ROWS)[slug][n - 1]
    items = "".join(
        f'<img src="{it["src"]}" alt="" width="{round(it["w"])}" height="{round(it["h"])}" style="width:{it["w"]}px;height:{it["h"]}px;border-radius:{it["r"]}px" loading="lazy" draggable="false">'
        for it in row["items"])
    gap, column = (row.get("gap", 16), 358) if mobile else (24, 1152)
    gap_style = f' style="gap:{gap}px"' if mobile and "gap" in row else ""
    total = sum(it["w"] for it in row["items"]) + gap * (len(row["items"]) - 1)
    scrolls = total > column + 0.5
    cls = "rail" + (" rail--band" if row["band"] else "") + (" rail--scroll" if scrolls else "") + (" rail--m" if mobile else "")
    label = ' tabindex="0" role="region" aria-label="Screens (scroll sideways)"' if scrolls else ""
    if row["band"] and row["band"].lower() != "#fafafa":  # some phone bands use a different grey
        attrs += f' style="background:{row["band"]}"' if "style=" not in attrs else ""
        if "style=" in attrs and "background" not in attrs:
            attrs = attrs.replace('style="', f'style="background:{row["band"]};', 1)
    return f'<div class="{cls}"{attrs}><div class="rail__track"{label}><div class="rail__items"{gap_style}>{items}</div></div></div>\n'


def case(slug):
    c = CASES[slug]
    meta = []
    for i, m in enumerate(c["meta"]):
        if i:
            meta.append('<span aria-hidden="true">·</span>')
        meta.append(ext(SKYENG, m, "meta-link") if m == "skyeng" else f"<span>{esc(m)}</span>")
    # Every piece of the page gets a key; "mobile" in content.py lists the keys shown on phones, in order,
    # grouped (groups are 54px apart, items inside a group 24px). Pieces not listed are hidden on phones.
    pieces = []  # (key, html, wraps_in_container)
    for i, s_ in enumerate(c["intro"]):
        pieces.append((f"intro:{i}", section(s_[1], s_[2], mtitle=c.get("mobile_titles", {}).get(f"intro:{i}")), True))
    seen = set(s_[1] for s_ in c["intro"])
    for i, b in enumerate(c["blocks"]):
        key = f"block:{i}"
        if b[0] == "section":
            # Figma shows only the first of several "Process" headings
            pieces.append((key, section(b[1], b[2], hidden=b[1] in seen and b[1] == "Process",
                                        mtitle=c.get("mobile_titles", {}).get(key)), True))
            seen.add(b[1])
        elif b[0] == "row":
            pieces.append((key, ("row", b[1]), False))
        elif b[0] == "image":
            _, src, w, h, r, alt = b
            pieces.append((key, f'<img class="wide-img" src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" style="border-radius:{r}px" loading="lazy">', True))
    m_order, m_break = {}, set()
    mobile = c.get("mobile")
    if mobile:
        n = 0
        for gi, group in enumerate(mobile):
            for ii, key in enumerate(group):
                m_order[key] = n; n += 1
                if gi and not ii:
                    m_break.add(key)
        for key in m_order:
            if key.startswith("mrow:"):
                pieces.append((key, ("mrow", int(key[5:])), False))

    def attrs(key):
        if not mobile:
            return ""
        if key not in m_order:
            return ' data-m="hide"'
        return f' style="--mo:{m_order[key]}"' + (' data-m="break"' if key in m_break else "")

    intro_html, flow = [], []
    for key, body, wrap in pieces:
        if isinstance(body, tuple):
            html_part = image_row(slug, body[1], mobile=body[0] == "mrow", attrs=attrs(key))
        else:
            html_part = f'<div class="container"{attrs(key)}>{body}</div>\n'
        (intro_html if key.startswith("intro:") else flow).append(html_part)
    intro = "".join(intro_html)
    title_cls = "case-head__title case-head__title--wide" if c.get("wide_title") else "case-head__title"
    main = f"""<div class="container">
  <a class="back" href="/"><img src="/assets/img/back-arrow.svg" alt="" width="17" height="17"><span>back</span></a>
</div>
<div class="case{' case--mobile' if mobile else ''}">
  <div class="container case-head">
    <h1 class="{title_cls}">{html.escape(c['title']).replace(chr(10), ' <br>')}</h1>
    <p class="case-head__meta">{''.join(meta)}</p>
  </div>
  <div class="case-flow">
    <div class="case-intro">{intro}</div>
    {''.join(flow)}    <div class="container case-contact">{contact()}</div>
  </div>
</div>
"""
    return page(f"{c['title'].replace(chr(10), ' ')} — Ksenia Kamenkova", c["description"], f"/{slug}/", "page-case", main)


def relativize(text, depth, root_page=False):
    """Preview builds: make site-absolute links relative and point to index.html files."""
    import re
    pre = "../" * depth
    text = re.sub(r'(href|src)="/(?!/)([^"]*)"', lambda m: f'{m.group(1)}="{pre}{m.group(2) or "index.html"}"'
                  if not m.group(2).endswith("/") else f'{m.group(1)}="{pre}{m.group(2)}index.html"', text)
    if root_page:  # the preview host adds its own document wrapper to the root page
        text = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>", "", text)
        text = text.replace("</head>", "").replace("</body>\n</html>", "")
        text = re.sub(r'<body class="([^"]*)">', r'<div class="\1">', text)
        text = re.sub(r'<meta charset="utf-8">\s*<meta name="viewport"[^>]*>', '', text)
        text = text.rstrip() + "\n</div>\n<script>document.body.className=document.querySelector('.page-home')?'page-home':'';</script>\n"
    return text


OUT = ROOT
PREVIEW = "--preview" in sys.argv
if PREVIEW:
    OUT = sys.argv[sys.argv.index("--preview") + 1]


def write(path, text):
    if PREVIEW:
        depth = path.count("/")
        if path == "index.html":  # the preview host's own entry page, plus a normal copy for "back" links
            with open(os.path.join(OUT, "_root.html"), "w") as f:
                f.write(relativize(text, 0, root_page=True))
        text = relativize(text, depth)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(text)
    print("wrote", path)


write("index.html", home())
for slug in CASES:
    write(f"{slug}/index.html", case(slug))

"""Generate the static pages from content.py and rows.json.

Run from the repository root:  python3 _src/build.py
"""
import html, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "_src"))
from content import HOME, CASES, LINKEDIN, CV, TELEGRAM, SKYENG  # noqa: E402

ROWS = json.load(open(os.path.join(ROOT, "_src", "rows.json")))
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
    <p class="contact__line">Feel free to reach out via {ext(LINKEDIN, "LinkedIn", "u")} or telegram {ext(TELEGRAM, "@kskamenkova", "plain")}</p>
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
        metrics = "".join(f'<div class="metric"><p class="metric__value">{esc(v)}</p><p class="metric__label">{esc(l)}</p></div>' for v, l in c["metrics"])
        cards.append(f"""      <article class="project">
        <a class="project__card" href="/{c['slug']}/" aria-label="Open case study: {esc(c['label'])}">
          <span class="project__year">{esc(c['year'])}</span>
          <span class="project__label">{esc(c['label'])}</span>
          <span class="project__btn" aria-hidden="true"><img src="/assets/img/arrow-card.svg" alt="" width="17" height="17"></span>
          <span class="project__media" aria-hidden="true">
            <span class="project__crop" style="left:{bx}px;top:{by}px;width:{bw}px;height:{bhh}px">
              <img src="/assets/img/home/{c['img']}.webp" alt="" style="width:{iw};height:{ih};left:{il};top:{it}" loading="lazy">
            </span>
          </span>
        </a>
        <div class="project__info">
          <p class="project__text">{esc(c['text'])}</p>
          <div class="project__line"></div>
          <div class="project__metrics">{metrics}</div>
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
        paras = "".join(f"<p>{esc(p)}</p>" for p in txt.split("\n\n"))
        return f"""<figure class="review">
          <img class="review__quote" src="/assets/img/quote.svg" alt="" width="54" height="44">
          <figcaption class="review__who">
            <img class="review__photo" src="{photo}" alt="" width="54" height="54" loading="lazy">
            <span class="review__about"><span class="review__name">{esc(name)}</span><span class="review__role">{esc(role)}</span></span>
          </figcaption>
          <blockquote class="review__text">{paras}</blockquote>
        </figure>"""
    raise ValueError(kind)


def section(heading, body, hidden=False):
    inner = "".join(body_item(b) for b in body)
    title = f'<div class="section__title" aria-hidden="true"></div>' if hidden else f'<h2 class="section__title">{esc(heading)}</h2>'
    return f"""<section class="section">
      {title}
      <div class="section__body">{inner}</div>
    </section>
"""


def image_row(slug, n):
    row = ROWS[slug][n - 1]
    items = "".join(
        f'<img src="{it["src"]}" alt="" width="{round(it["w"])}" height="{round(it["h"])}" style="width:{it["w"]}px;height:{it["h"]}px;border-radius:{it["r"]}px" loading="lazy" draggable="false">'
        for it in row["items"])
    total = sum(it["w"] for it in row["items"]) + 24 * (len(row["items"]) - 1)
    scrolls = total > 1152.5
    cls = "rail" + (" rail--band" if row["band"] else "") + (" rail--scroll" if scrolls else "")
    label = ' tabindex="0" role="region" aria-label="Screens (scroll sideways)"' if scrolls else ""
    return f'<div class="{cls}"><div class="rail__track"{label}><div class="rail__items">{items}</div></div></div>\n'


def case(slug):
    c = CASES[slug]
    meta = []
    for i, m in enumerate(c["meta"]):
        if i:
            meta.append('<span aria-hidden="true">·</span>')
        meta.append(ext(SKYENG, m, "meta-link") if m == "skyeng" else f"<span>{esc(m)}</span>")
    blocks = []
    seen = set()
    for b in c["blocks"]:
        if b[0] == "section":
            # Figma shows only the first of several "Process" headings
            blocks.append(section(b[1], b[2], hidden=b[1] in seen and b[1] == "Process"))
            seen.add(b[1])
        elif b[0] == "row":
            blocks.append(image_row(slug, b[1]))
        elif b[0] == "image":
            _, src, w, h, r, alt = b
            blocks.append(f'<div class="container"><img class="wide-img" src="{src}" alt="{esc(alt)}" width="{w}" height="{h}" style="border-radius:{r}px" loading="lazy"></div>\n')
    # sections in the flow need the container wrapper; rows are full width
    flow = []
    for html_part, b in zip(blocks, c["blocks"]):
        flow.append(f'<div class="container">{html_part}</div>\n' if b[0] == "section" else html_part)
    intro = "".join(section(s[1], s[2]) for s in c["intro"])
    title_cls = "case-head__title case-head__title--wide" if c.get("wide_title") else "case-head__title"
    main = f"""<div class="container">
  <a class="back" href="/"><img src="/assets/img/back-arrow.svg" alt="" width="17" height="17"><span>back</span></a>
</div>
<div class="case">
  <div class="container case-head">
    <h1 class="{title_cls}">{esc(c['title']).replace(chr(10), '<br>')}</h1>
    <p class="case-head__meta">{''.join(meta)}</p>
  </div>
  <div class="case-flow">
    <div class="container case-intro">{intro}</div>
    {''.join(flow)}    <div class="container">{contact()}</div>
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

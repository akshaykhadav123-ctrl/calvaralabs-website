#!/usr/bin/env python3
"""Builds the Calvara Labs & Minerals static site.

  python3 build.py live     -> dist/     (clean URLs, for calvaralabs.com)
  python3 build.py preview  -> preview/  (links end in index.html, for file previews)

Content follows the Calvara Hydrated Lime Brochure (2026). Plant photos are optional:
drop them into src/photos/ with the names in PHOTOS and rebuild.
"""
import json, shutil, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "tools"))
from logo_parts import lockup, mark_svg

ROOT = Path(__file__).parent
SITE = "https://calvaralabs.com"
MODE = sys.argv[1] if len(sys.argv) > 1 else "live"
OUT = ROOT / ("dist" if MODE == "live" else "preview")

PHONE_DISPLAY = "+91 98927 27068"
PHONE_TEL = "+919892727068"
WHATSAPP = "https://wa.me/919892727068?text=Hello%20Calvara%2C%20I%20would%20like%20to%20ask%20about%20hydrated%20lime."
EMAIL = "sales@calvaralabs.com"
OFFICE = "54 Patrakar Colony, Section 7, New Power House Road, Jodhpur, Rajasthan 342001, India"
WORKS = "Ransigaon, Tehsil Bilara, District Jodhpur, Rajasthan, India"

# grade, label, Ca(OH)2 min, CaO eq, moisture max, acid insoluble max, passing 200 mesh min
GRADES = [
    ("95", "Premium", "95 %", "~72 %", "0.5 %", "0.8 %", "99.5 %"),
    ("94", "High purity", "94 %", "~71 %", "0.7 %", "0.9 %", "99.2 %"),
    ("93", "High purity", "93 %", "~70.5 %", "0.8 %", "1.0 %", "99 %"),
    ("92", "High purity", "92 %", "~69.5 %", "0.8 %", "1.06 %", "98.5 %"),
    ("90", "Standard", "90 %", "~68 %", "1.0 %", "3 %", "98 %"),
    ("85", "Standard", "85 %", "~64 %", "1.5 %", "5 %", "95 %"),
    ("80", "Bulk value", "80 %", "~60 %", "2.0 %", "8 %", "90 %"),
]
GRADE_USES = {
    "95": "Chemicals, ceramics and glass, drinking water, sugar refining",
    "94": "Chemicals, ceramics and glass, drinking water, sugar refining",
    "93": "Chemicals, ceramics and glass, drinking water, sugar refining",
    "92": "Chemicals, ceramics and glass, drinking water, sugar refining",
    "90": "Water and wastewater, sugar, flue gas, chemicals",
    "85": "Water and wastewater, sugar, flue gas, chemicals",
    "80": "Construction, steel, agriculture, paper, leather",
}
INDUSTRIES = [
    ("Water and wastewater", "pH correction, softening, heavy-metal and phosphate removal", ["92", "90", "85"]),
    ("Chemicals", "Calcium salts, bleaching powder, caustic soda production", ["95", "93", "90"]),
    ("Sugar industry", "Juice clarification and purification", ["90", "92", "85"]),
    ("Ceramics and glass", "Raw material and process additive", ["93", "95", "90"]),
    ("Flue gas treatment", "Scrubbing and neutralisation of SO<sub>2</sub> and HCl", ["85", "90"]),
    ("Construction", "Lime plaster, mortar, putty, soil stabilisation, AAC blocks", ["80", "85"]),
    ("Steel and metallurgy", "Flux, slag conditioning, acid neutralisation", ["80", "85"]),
    ("Paper, leather and textile", "Causticising, unhairing, dyeing and finishing", ["85", "80"]),
    ("Agriculture", "Soil pH correction, fertiliser preparation", ["80"]),
]
PLANT_STEPS = [
    ("kiln", "Kiln", "Limestone is burnt to quicklime (CaO) and drawn out onto the conveyor."),
    ("stock", "Raw material stock", "Quicklime from the kiln is stocked under cover and fed to the hydrators by conveyor."),
    ("hydrators", "Hydrators", "Quicklime is slaked with measured water into dry Ca(OH)<sub>2</sub> powder."),
    ("classifier", "Classifier", "Separates fine powder from grit to reach each grade's fineness."),
    ("smallbag", "Small bag packing", "Powder is fed from hoppers and filled in 25, 30, 35 or 40 kg bags."),
    ("jumbo", "Jumbo-bag packing", "900 kg bags filled under a bag-filter dust collector."),
]
PHOTOS = {  # key -> file in src/photos (optional)
    "kiln": "kiln.webp", "stock": "stock.webp", "hydrators": "hydrators.webp", "classifier": "classifier.webp",
    "smallbag": "smallbag.webp", "jumbo": "jumbo.webp", "jumbo-front": "jumbo-front.webp",
    "jumbo-vs-bags": "jumbo-vs-bags.webp", "warehouse": "warehouse.webp", "lab-titration": "lab-titration.webp",
    "lab-balance": "lab-balance.webp", "lab-hotplate": "lab-hotplate.webp", "akshay": "akshay.webp", "brochure-cover": "brochure-cover.webp", "hap-brochure-cover": "hap-brochure-cover.webp",
}


def photo(key):
    f = ROOT / "src" / "photos" / PHOTOS.get(key, "_none")
    return f"photos/{PHOTOS[key]}" if f.exists() else None


def href(root, page):
    if MODE == "live":
        return f"{root}{page + '/' if page else ''}" or "./"
    return f"{root}{page + '/' if page else ''}index.html"


# ---------- icons ----------
ICON = {
    "flame": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" aria-hidden="true"><path d="M12 3c1 4 5 5.5 5 10a5 5 0 0 1-10 0c0-2.5 1.5-3.5 2.5-5 .5 1.5 1.5 2 2.5 2-.5-2.5-.5-4.5 0-7z"/></svg>',
    "pile": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><path d="M2 19l6-9 4 4 3-5 7 10z"/><path d="M2 19h20"/></svg>',
    "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/></svg>',
    "sieve": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M3 8h18l-3 7H6z"/><path d="M8 18v1M12 18v2M16 18v1"/></svg>',
    "bag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><path d="M6 4h12l1 16H5z"/><path d="M8 4c0 2 1.5 3 4 3s4-1 4-3"/></svg>',
    "jumbo": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="7" width="16" height="13" rx="2"/><path d="M8 7V4M16 7V4"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" aria-hidden="true"><path d="M4 20l1.3-3.9A8 8 0 1 1 8 19z"/></svg>',
}
STEP_ICON = {"kiln": "flame", "stock": "pile", "hydrators": "drop", "classifier": "sieve", "smallbag": "bag", "jumbo": "jumbo"}


# ---------- shared pieces ----------
def brand(root, dark=False):
    svg = lockup(letters="#FFFFFF", v="#D9342D", outline="#D9342D", core="#FFFFFF", rule="#D9342D", sub="#E7EAEE", label="") if dark else lockup(label="")
    return f'<a class="brand" href="{href(root, "")}" aria-label="Calvara Labs &amp; Minerals, home">{svg}</a>'


NAV = [("hydrated-lime", "Hydrated lime"), ("export", "Prices &amp; export"), ("hydroxyapatite", "Hydroxyapatite"), ("about", "About &amp; quality"), ("contact", "Contact")]


# Announcement bar: edit this list to change the rotating messages (tag, text, link page, link label).
# link page: a site page key ('', 'export', 'hydroxyapatite', ...) optionally with #anchor, or a full https:// URL.
ANNOUNCEMENTS = [
    ("Free sample", "Get a free sample of any grade, with its Certificate of Analysis.", "export#quote", "Ask now"),
    ("Export", "CIF and CFR quotes to your port, palletised or non-palletised.", "export#quote", "Get a price"),
    ("Ready stock", "Seven grades, 80 to 95 % Ca(OH)₂, in 25, 30, 35 or 40 kg bags, palletised or non-palletised.", "hydrated-lime", "See grades"),
    ("New", "Hydroxyapatite micro grade: 250 g samples now open.", "hydroxyapatite#quote", "Request"),
]


def announce_bar(root):
    def link(target):
        if target.startswith("http"):
            return target
        pg, _, anchor = target.partition("#")
        return href(root, pg) + (f"#{anchor}" if anchor else "")
    items = "".join(
        f'<a class="announce-item{" is-on" if i == 0 else ""}" href="{link(t)}"><b>{tag}</b><span>{txt}</span><i>{lbl}</i></a>'
        for i, (tag, txt, t, lbl) in enumerate(ANNOUNCEMENTS))
    pause = '<svg viewBox="0 0 14 14" aria-hidden="true"><rect x="3" y="2" width="3" height="10" fill="currentColor"/><rect x="8" y="2" width="3" height="10" fill="currentColor"/></svg>'
    return f'''<div class="announce" role="region" aria-label="Announcements"><div class="wrap">
<div class="announce-track">{items}</div>
<button class="announce-btn" type="button" aria-label="Pause announcements" data-paused="false">{pause}</button>
</div></div>
<script>
(function(){{var it=document.querySelectorAll(".announce-item"),b=document.querySelector(".announce-btn");if(it.length<2){{if(b)b.hidden=true;return;}}
var i=0,t=null,reduce=window.matchMedia&&matchMedia("(prefers-reduced-motion: reduce)").matches;
var P='<svg viewBox="0 0 14 14" aria-hidden="true"><rect x="3" y="2" width="3" height="10" fill="currentColor"/><rect x="8" y="2" width="3" height="10" fill="currentColor"/></svg>',
    G='<svg viewBox="0 0 14 14" aria-hidden="true"><path d="M3 2l9 5-9 5z" fill="currentColor"/></svg>';
function show(n){{it[i].classList.remove("is-on");i=(n+it.length)%it.length;it[i].classList.add("is-on");}}
function play(){{stop();t=setInterval(function(){{show(i+1);}},5000);b.dataset.paused="false";b.setAttribute("aria-label","Pause announcements");b.innerHTML=P;}}
function stop(){{if(t)clearInterval(t);t=null;}}
function pause(){{stop();b.dataset.paused="true";b.setAttribute("aria-label","Play announcements");b.innerHTML=G;}}
b.addEventListener("click",function(){{b.dataset.paused==="true"?play():pause();}});
var r=document.querySelector(".announce");r.addEventListener("mouseenter",function(){{if(b.dataset.paused!=="true")stop();}});
r.addEventListener("mouseleave",function(){{if(b.dataset.paused!=="true")play();}});
r.addEventListener("focusin",function(){{if(b.dataset.paused!=="true")stop();}});
if(reduce)pause();else play();}})();
</script>'''


def header(root, current):
    cur = ' aria-current="page"'
    links = "".join(f'<a href="{href(root, p)}"{cur if p == current else ""}>{t}</a>' for p, t in NAV)
    burger = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M3 5h14M3 10h14M3 15h14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="site-top">
{announce_bar(root)}
<header class="site-head">
<div class="wrap head-row">
{brand(root)}
<nav class="nav" aria-label="Main">{links}<a class="btn btn-solid" href="{href(root, 'contact')}">Request a quote</a></nav>
<details class="menu"><summary aria-label="Open menu">{burger}Menu</summary><nav class="menu-panel" aria-label="Menu">
<a href="{href(root, '')}"{cur if current in ('', 'home') else ''}>Home</a>{links}<a href="{href(root, '')}#brochure">Brochures (PDF)</a>
<div class="menu-contact"><a class="btn btn-line" href="tel:{PHONE_TEL}">{ICON["phone"]}Call</a><a class="btn btn-wa" href="{WHATSAPP}">{ICON["wa"]}WhatsApp</a></div>
<a class="btn btn-solid" href="{href(root, 'contact')}">Request a quote</a></nav></details>
</div>
</header>
</div>'''


def footer(root):
    return f'''<footer class="site-foot">
<div class="wrap foot-grid">
<div>{brand(root, dark=True)}<p>Hydrated lime in seven grades, made at our own plant in Ransigaon, Jodhpur.</p></div>
<div><h2>Products</h2><ul><li><a href="{href(root, 'hydrated-lime')}">Hydrated lime grades</a></li><li><a href="{href(root, 'export')}">Prices &amp; export</a></li><li><a href="{brochure_href(root, 'lime')}" download>Hydrated lime brochure (PDF)</a></li><li><a href="{href(root, 'hydroxyapatite')}">Hydroxyapatite</a></li><li><a href="{brochure_href(root, 'hap')}" download>Hydroxyapatite brochure (PDF)</a></li></ul></div>
<div><h2>Company</h2><ul><li><a href="{href(root, 'about')}">About &amp; quality</a></li><li><a href="{href(root, 'contact')}">Request a quote</a></li><li>Office: {OFFICE}</li></ul></div>
<div><h2>Contact</h2><ul><li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li><li><a href="{WHATSAPP}">WhatsApp us</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
</div>
<div class="wrap foot-base">© 2026 Calvara Labs &amp; Minerals · HSN 2522 · CAS 1305-62-0</div>
</footer>'''


def cta_band(root, title="Ask for a sample of the grade you want", text="Tell us your use, monthly volume and the grade you have in mind. You hear back directly from our engineer, with a sample and its Certificate of Analysis."):
    return f'''<section class="cta-band"><div class="wrap cta-grid">
<div><h2>{title}</h2><p>{text}</p></div>
<div class="btn-row"><a class="btn btn-red" href="{href(root, 'contact')}">Request a quote</a><a class="btn btn-ghost-light" href="{WHATSAPP}">WhatsApp us</a></div>
</div></section>'''


ORG_LD = {
    "@context": "https://schema.org", "@type": "Organization", "name": "Calvara Labs & Minerals",
    "url": SITE + "/", "logo": SITE + "/assets/logo-512.png", "email": EMAIL, "telephone": PHONE_TEL,
    "address": {"@type": "PostalAddress", "streetAddress": "54 Patrakar Colony, Section 7, New Power House Road",
                "addressLocality": "Jodhpur", "addressRegion": "Rajasthan", "postalCode": "342001", "addressCountry": "IN"},
    "description": "Hydrated lime (calcium hydroxide) in seven grades, 80 to 95% Ca(OH)2, made at Ransigaon, Jodhpur, Rajasthan, India.",
}


def page(path, root, current, title, desc, body, extra_ld=None, noindex=False):
    canonical = SITE + "/" + (path + "/" if path and not path.endswith(".html") else "")
    ld = [ORG_LD] + ([extra_ld] if extra_ld else [])
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Calvara Labs &amp; Minerals">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#13202E">
<meta name="format-detection" content="telephone=yes">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{root}favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="preload" href="{root}assets/fonts/jost.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/site.css">
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else ld[0], ensure_ascii=False)}</script>
</head>
<body>
{header(root, current)}
<main id="main">
{body}
</main>
{footer(root)}
<button class="to-top" type="button" aria-label="Back to top" hidden><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 16V4M4.5 9.5 10 4l5.5 5.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Top</span></button>
<script>
(function(){{
  var top=document.querySelector('.site-top'), btn=document.querySelector('.to-top'), menu=document.querySelector('.menu');
  var smooth=!matchMedia('(prefers-reduced-motion: reduce)').matches;
  function pad(){{ if(top) document.documentElement.style.scrollPaddingTop=(top.offsetHeight+12)+'px'; }}
  pad(); addEventListener('resize',pad);
  btn.hidden=false;
  function onScroll(){{ btn.classList.toggle('is-on', scrollY>600); }}
  addEventListener('scroll',onScroll,{{passive:true}}); onScroll();
  btn.addEventListener('click',function(){{ scrollTo({{top:0,behavior:smooth?'smooth':'auto'}}); var s=document.querySelector('.skip'); }});
  if(menu){{
    menu.addEventListener('click',function(e){{ if(e.target.closest('.menu-panel a')) menu.open=false; }});
    document.addEventListener('click',function(e){{ if(menu.open && !menu.contains(e.target)) menu.open=false; }});
    document.addEventListener('keydown',function(e){{ if(e.key==='Escape' && menu.open){{ menu.open=false; menu.querySelector('summary').focus(); }} }});
  }}
}})();
</script>
</body>
</html>
'''
    if path.endswith(".html"):
        dest = OUT / path
    elif path:
        dest = OUT / path / "index.html"
    else:
        dest = OUT / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html.replace('src="photos/', f'src="{root}assets/photos/'), encoding="utf-8")


def crumbs(root, name):
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{href(root, "")}">Home</a> / <span aria-current="page">{name}</span></nav>'


# ---------- building blocks ----------
def ladder():
    rows = ""
    for g, label, ca, _, _, si, _ in GRADES:
        pct = (int(g) - 70) / 25 * 100
        rows += f'<li><span class="g">{g}</span><span class="bar" aria-hidden="true"><i style="width:{pct:.0f}%"></i></span><span class="si">silica ≤ {si}</span></li>'
    return f'''<div class="ladder" role="group" aria-label="Seven hydrated lime grades">
<div class="ladder-head">Seven grades<span>min. % Ca(OH)<sub>2</sub></span></div>
<ol>{rows}</ol>
<div class="ladder-foot">A higher grade means more active lime and less silica, so you dose less.</div>
</div>'''


def stats():
    return '''<div class="stats">
<div><b>7</b><span>purity grades, 80 to 95 %</span></div>
<div><b>95 %</b><span>top purity, Ca(OH)<sub>2</sub> min.</span></div>
<div><b>99.5 %</b><span>passes 200 mesh (95 grade)</span></div>
<div><b>25–40 kg</b><span>bags: 25, 30, 35 or 40 kg, palletised or non-palletised</span></div>
</div>'''


def engineer(root, short=False):
    img = photo("akshay")
    av = f'<img class="avatar" src="{img}" alt="Akshay Khadav" loading="lazy" width="84" height="84" style="padding:0">' if img else '<span class="avatar" aria-hidden="true">AK</span>'
    more = "" if short else "<p>I am a chemical engineer from IIT Bombay and I lead Calvara Labs &amp; Minerals. When you write to us, you speak directly with me about chemistry, grades and dispatch, not with a call centre.</p>"
    return f'''<div class="engineer">{av}<div>
<blockquote>“Tell me about your process. I'll suggest the grade that fits, and send you a sample to prove it.”</blockquote>
<p><b>Akshay Khadav</b>, B.Tech Chemical Engineering, IIT Bombay</p>
{more}
<div class="btn-row"><a class="btn btn-red" href="{WHATSAPP}">WhatsApp Akshay</a><a class="btn btn-ghost-light" href="tel:{PHONE_TEL}">Call {PHONE_DISPLAY}</a></div>
</div></div>'''


def plant_rail():
    items = ""
    for n, (key, title, text) in enumerate(PLANT_STEPS, 1):
        img = photo(key)
        media = f'<img src="{img}" alt="{title} at our Ransigaon plant" loading="lazy" width="452" height="460">' if img else ICON[STEP_ICON[key]]
        items += f'<li><div class="ph{"" if img else " ph-icon"}">{media}</div><h3><span class="n">{n}</span>{title}</h3><p>{text}</p></li>'
    return f'<ol class="rail">{items}</ol><p class="swipe-hint">Swipe to see all six steps.</p>'


def problems():
    rows = [
        ("Purity lower than promised", "You pay for 90 % and dose for 80 %, so consumption goes up.",
         "The grade is a guaranteed minimum", "The grade number is the minimum Ca(OH)<sub>2</sub> content, and every lot ships with a Certificate of Analysis."),
        ("Grit and silica", "Inert matter wears pumps and dosing lines and adds sludge.",
         "Silica capped for every grade", "Acid insoluble is held as low as 0.8 % in the 95 grade and 1.06 % in the 92 grade, and fineness is up to 99.5 % through 200 mesh."),
        ("Lumps and moisture", "Damp lime cakes, blocks feeders and loses strength.",
         "Dry powder, sealed bags", "Moisture is limited to 0.5 to 2.0 % by grade, and the packing date is printed on every lot."),
        ("Every truck is different", "One good lot, then the next one upsets your process.",
         "Supplied to your approved sample", "We agree the specification against the sample you approved, and every lot is traceable by lot number."),
        ("Nobody to call", "A trader can't answer technical questions or fix a problem.",
         "A chemical engineer on the phone", "Akshay Khadav (IIT Bombay) answers technical questions directly."),
    ]
    out = "".join(f'<div class="pf-row"><div class="bad"><h3>{a}</h3><p>{b}</p></div><div class="good"><h3>{c}</h3><p>{d}</p></div></div>' for a, b, c, d in rows)
    return f'''<div class="pf">{out}</div>
<div class="promise"><b>CoA</b><p>Our promise: what the certificate says is what you get. If a lot does not meet the agreed specification, tell us. We will test it, explain it and put it right.</p></div>'''


def ranges():
    return '''<div class="ranges">
<div><span class="nums">95 · 94 · 93 · 92</span><h3>High-purity range</h3><p>Chemicals, ceramics and glass, drinking water and sugar refining.</p></div>
<div><span class="nums">90 · 85</span><h3>Standard range</h3><p>Water and wastewater, sugar, flue gas and chemicals.</p></div>
<div><span class="nums">80</span><h3>Bulk value</h3><p>Construction, steel, agriculture, paper and leather.</p></div>
</div>'''


def industries():
    out = ""
    for name, use, gs in INDUSTRIES:
        chips = "".join(f'<li class="chip{" first" if i == 0 else ""}">{g}</li>' for i, g in enumerate(gs))
        out += f'<div><h3>{name}</h3><p>{use}</p><ul class="chips" aria-label="Suggested grades, first is the starting grade">{chips}</ul></div>'
    return f'<div class="inds">{out}</div>'


def spec_table():
    head = "".join(f'<th scope="col"><span class="gn">{g}</span>grade</th>' for g, *_ in GRADES)
    rows_def = [("Ca(OH)<sub>2</sub> content, min.", 2), ("Equivalent CaO (calculated)", 3), ("Moisture, max.", 4),
                ("Acid insoluble (silica), max.", 5), ("Passing 200 mesh (75 µm), min.", 6)]
    body = "".join(f'<tr><th scope="row">{label}</th>' + "".join(f'<td class="num">{g[i]}</td>' for g in GRADES) + "</tr>" for label, i in rows_def)
    table = f'<div class="table-box spec-table-wrap"><table class="spec-wide"><caption>Typical specification by grade</caption><thead><tr><th scope="col">Parameter</th>{head}</tr></thead><tbody>{body}</tbody></table></div>'
    cards = ""
    for g, label, ca, cao, moist, si, mesh in GRADES:
        cards += f'''<article class="gcard"><div class="gcard-top"><b>{g}</b><span>{label} grade</span></div>
<dl><div><dt>Ca(OH)<sub>2</sub>, min.</dt><dd>{ca}</dd></div><div><dt>Equivalent CaO</dt><dd>{cao}</dd></div><div><dt>Moisture, max.</dt><dd>{moist}</dd></div><div><dt>Silica (acid insoluble), max.</dt><dd>{si}</dd></div><div><dt>Passing 200 mesh, min.</dt><dd>{mesh}</dd></div></dl>
<p class="uses-line">{GRADE_USES[g]}</p></article>'''
    return table + f'<div class="grade-cards" aria-label="Grade specifications, swipe for more">{cards}</div><p class="swipe-hint">Swipe across to compare all seven grades.</p>'


def common_props():
    return '''<div class="table-box"><table style="min-width:0"><caption>Same across all grades</caption><tbody>
<tr><th scope="row">Appearance</th><td>White to off-white</td></tr>
<tr><th scope="row">Form</th><td>Free-flowing powder</td></tr>
<tr><th scope="row">Bulk density (loose)</th><td class="num">450 to 550 kg/m³</td></tr>
<tr><th scope="row">pH, saturated, 25 °C</th><td class="num">approx. 12.4</td></tr>
<tr><th scope="row">Solubility in water, 20 °C</th><td class="num">approx. 1.7 g/L</td></tr>
<tr><th scope="row">CAS / HSN</th><td class="num">1305-62-0 / 2522</td></tr>
</tbody></table></div>'''


def coa_sample():
    return '''<div class="coa"><div class="coa-head"><b>Certificate of Analysis, sample format</b><span>Calvara Labs &amp; Minerals · Hydrated lime · Grade 90 · Lot no. CLM/HL/____ · Packing date ____</span></div>
<div style="overflow-x:auto"><table><thead><tr><th scope="col">Parameter</th><th scope="col">Specification</th><th scope="col">Result</th></tr></thead><tbody>
<tr><th scope="row">Ca(OH)<sub>2</sub> content</th><td class="num">≥ 90 %</td><td>______</td></tr>
<tr><th scope="row">Moisture</th><td class="num">≤ 1.0 %</td><td>______</td></tr>
<tr><th scope="row">Acid insoluble</th><td class="num">≤ 3 %</td><td>______</td></tr>
<tr><th scope="row">Passing 200 mesh</th><td class="num">≥ 98 %</td><td>______</td></tr>
</tbody></table></div></div>'''


def bags():
    items = "".join(f'<li><b>{k} kg</b><span>Bag, liner, laminated</span></li>' for k in (25, 30, 35, 40))
    return f'<ul class="bags">{items}<li class="jumbo"><b>Pallets</b><span>Palletised or non-palletised</span></li></ul>'


def start_steps():
    return buy_steps([
        ("Tell us your use", "Share your application, monthly volume and the grade you have in mind."),
        ("Test a sample", "We send a sample and its CoA. You test it in your process or lab."),
        ("Approve and order", "We supply to the approved sample, with a CoA for every lot."),
    ])


def buy_steps(items):
    return f'<ol class="steps steps-{len(items)}">' + "".join(
        f'<li><span class="n">{n}</span><h3>{t}</h3><p>{p}</p></li>' for n, (t, p) in enumerate(items, 1)) + "</ol>"


def wide_photos():
    figs = [("jumbo-front", "900 kg jumbo bags in front of the processing plant"),
            ("jumbo-vs-bags", "Packed lots at the plant"),
            ("warehouse", "Covered warehouse with packed lots waiting for dispatch")]
    out = "".join(f'<figure><img src="{photo(k)}" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for k, c in figs if photo(k))
    return f'<div class="wide-photos">{out}</div>' if out else ""


def lab_photos():
    figs = [("lab-titration", "Titration: available Ca(OH)₂ content"), ("lab-balance", "Precision balance for the lime sugar test"),
            ("lab-hotplate", "Hot plate: sample digestion and drying")]
    out = "".join(f'<figure><img src="{photo(k)}" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for k, c in figs if photo(k))
    return f'<div class="wide-photos">{out}</div>' if out else ""


# Inserted into build.py: buyer-question components and the Prices & export page.
from urllib.parse import quote as _q

WA_NUM = "919892727068"


def wa(text):
    return f"https://wa.me/{WA_NUM}?text={_q(text)}"


def quote_builder(root, heading=True):
    grades = ["95", "94", "93", "92", "90", "85", "80", "Not sure"]
    def chips(name, opts, checked):
        return "".join(
            f'<label class="qchip"><input type="radio" name="{name}" value="{o}"{" checked" if o == checked else ""}><span>{o}</span></label>' for o in opts)
    head = '''<div class="section-head"><h2>Get a full quote in one message</h2><p class="lede">Tap your choices and send. Akshay replies with price, specification, container quantity, lead time and payment terms together.</p></div>''' if heading else ""
    return f'''{head}
<form class="qb" id="qb" onsubmit="return false">
<fieldset><legend>Grade</legend><div class="qchips">{chips("grade", grades, "90")}</div></fieldset>
<fieldset><legend>Packing</legend><div class="qchips">{chips("pack", ["25 kg bags", "30 kg bags", "35 kg bags", "40 kg bags"], "25 kg bags")}</div></fieldset>
<fieldset><legend>Pallets</legend><div class="qchips">{chips("pallet", ["Palletised", "Not palletised", "Not sure"], "Not sure")}</div></fieldset>
<fieldset><legend>Price basis</legend><div class="qchips">{chips("terms", ["CIF", "CFR", "FOB India", "Ex-works Jodhpur", "Delivered in India"], "CIF")}</div></fieldset>
<div class="qrow">
<div class="field"><label for="qb-port">Your port or city</label><input id="qb-port" type="text" placeholder="Durban, Port Louis, Mombasa"></div>
<div class="field"><label for="qb-qty">Quantity</label><input id="qb-qty" type="text" placeholder="1 x 20 ft a month"></div>
</div>
<div class="qactions">
<a class="btn btn-wa" id="qb-wa" href="{wa('Hello Akshay, please quote hydrated lime.')}">Send on WhatsApp</a>
<a class="btn btn-line" id="qb-mail" href="mailto:sales@calvaralabs.com?subject=Hydrated%20lime%20quote%20request">Send by email</a>
</div>
<p class="qprev" aria-live="polite"><span>Your message:</span> <span id="qb-text"></span></p>
</form>
<script>
(function(){{var f=document.getElementById("qb");if(!f)return;
function v(n){{var e=f.querySelector('input[name="'+n+'"]:checked');return e?e.value:"";}}
function build(){{var port=document.getElementById("qb-port").value.trim(),qty=document.getElementById("qb-qty").value.trim();
var g=v("grade"),t=v("terms");var lines=["Hello Akshay, please quote hydrated lime.",
"Grade: "+(g==="Not sure"?"please advise":g),"Packing: "+v("pack")+", "+v("pallet").toLowerCase(),
"Price basis: "+t+(port?" "+port:""),"Quantity: "+(qty||"to discuss"),
"Please include container quantity, lead time, payment terms and the spec sheet."];
var msg=lines.join("\\n");document.getElementById("qb-text").textContent=lines.slice(1,5).join(" · ");
document.getElementById("qb-wa").href="https://wa.me/{WA_NUM}?text="+encodeURIComponent(msg);
document.getElementById("qb-mail").href="mailto:sales@calvaralabs.com?subject="+encodeURIComponent("Hydrated lime quote: grade "+g+", "+t+(port?" "+port:""))+"&body="+encodeURIComponent(msg);}}
f.addEventListener("change",build);f.addEventListener("input",build);build();}})();
</script>'''


ASKS = [
    ("Prices on your terms",
     "CIF or CFR to your port, FOB an Indian port, ex-works Jodhpur, or delivered to your site in India. Price per tonne for each grade.",
     "Hello Akshay, please send your price per tonne for hydrated lime, CIF my port. Grade: ___ Port: ___"),
    ("Palletised or not",
     "Bags loaded palletised and stretch-wrapped, or loose (non-palletised) for more tonnes per container. Tell us which you need.",
     "Hello Akshay, please quote hydrated lime palletised and non-palletised so I can compare. Grade: ___ Port: ___"),
    ("Bag type and size",
     "25, 30, 35 or 40 kg laminated bags with liner, PP bags or bags printed with your brand, palletised or non-palletised.",
     "Hello Akshay, which bag options do you have for hydrated lime? I need ___ kg bags."),
    ("Container quantity",
     "How many tonnes fit in a 20 ft or 40 ft container for your packing, and whether part loads are possible.",
     "Hello Akshay, how many tonnes of hydrated lime fit in a 20 ft and a 40 ft container with ___ kg bags?"),
    ("MOQ, capacity and lead time",
     "Minimum order, monthly supply we can commit to, stock on hand, production and dispatch time, and quote validity.",
     "Hello Akshay, please share MOQ, monthly capacity and lead time for hydrated lime grade ___."),
    ("Payment terms",
     "Tell us the terms you work with, such as advance TT, LC at sight or credit, and Akshay will confirm what we can offer.",
     "Hello Akshay, what payment terms do you offer for hydrated lime exports? We usually work with ___."),
    ("Spec sheet, CoA and SDS",
     "Technical data sheet for every grade, a Certificate of Analysis with each lot, and a Safety Data Sheet (MSDS).",
     "Hello Akshay, please send the TDS, a sample CoA and the SDS for hydrated lime grade ___."),
    ("Export documents",
     "Commercial invoice, packing list, certificate of origin and bill of lading, plus loading photos and the container seal number.",
     "Hello Akshay, which export documents do you provide with a hydrated lime shipment to ___?"),
    ("Supplier registration",
     "Send us your vendor or supplier registration form and we fill it in with our company and export details.",
     "Hello Akshay, we need you to complete our supplier registration form. Where should I send it?"),
    ("Your standard or spec",
     "Testing to EN 459-1, JIS R 9001 or your own spec, an independent lab report, or a finer mesh such as 325 mesh.",
     "Hello Akshay, can you supply hydrated lime to this specification: ___"),
    ("Free sample",
     "A sample of the grade you want with its CoA, sent by courier, with tracking details and sample paperwork shared.",
     "Hello Akshay, please send a free sample of hydrated lime grade ___ to ___."),
    ("Plant visit or video call",
     "Visit our Ransigaon plant by appointment, or ask for a video call or recent photos of packing and loading.",
     "Hello Akshay, I would like a plant visit or video call to see your hydrated lime production."),
]


def asks_grid(limit=None):
    items = ASKS[:limit] if limit else ASKS
    cards = "".join(
        f'<article class="ask"><h3>{t}</h3><p>{d}</p><a class="ask-cta" href="{wa(m)}">Ask Akshay on WhatsApp</a></article>' for t, d, m in items)
    return f'<div class="asks">{cards}</div>'


def quote_builder_hap(root, heading=True):
    def chips(name, opts, checked, kind="radio"):
        return "".join(
            f'<label class="qchip"><input type="{kind}" name="{name}" value="{o}"{" checked" if (o in checked if isinstance(checked, list) else o == checked) else ""}><span>{o}</span></label>' for o in opts)
    head = '''<div class="section-head"><h2>Hydroxyapatite: request a sample or price</h2><p class="lede">Tap your choices and send. Akshay replies with price per kg, the TDS and sample CoA, and lead time.</p></div>''' if heading else ""
    return f'''{head}
<form class="qb" id="qbh" onsubmit="return false">
<fieldset><legend>Grade</legend><div class="qchips">{chips("hgrade", ["Micro, D50 3 to 8 µm", "Nano (in development)"], "Micro, D50 3 to 8 µm")}</div></fieldset>
<fieldset><legend>I want</legend><div class="qchips">{chips("hwant", ["250 g sample", "5 to 25 kg trial", "Regular supply", "Price only"], "250 g sample")}</div></fieldset>
<fieldset><legend>Use</legend><div class="qchips">{chips("huse", ["Toothpaste", "Tooth powder", "Tablets", "Cosmetics", "Lab / R&amp;D", "Other"], "Toothpaste")}</div></fieldset>
<fieldset><legend>Documents needed (tick any)</legend><div class="qchips">{chips("hdocs", ["TDS", "Sample CoA", "XRD", "Heavy metals", "Particle size"], ["TDS", "Sample CoA"], "checkbox")}</div></fieldset>
<div class="qrow">
<div class="field"><label for="qbh-where">City and country</label><input id="qbh-where" type="text" placeholder="Mumbai, India"></div>
<div class="field"><label for="qbh-qty">Quantity</label><input id="qbh-qty" type="text" placeholder="25 kg a month"></div>
</div>
<div class="qactions">
<a class="btn btn-wa" id="qbh-wa" href="{wa('Hello Akshay, I would like to ask about your hydroxyapatite.')}">Send on WhatsApp</a>
<a class="btn btn-line" id="qbh-mail" href="mailto:sales@calvaralabs.com?subject=Hydroxyapatite%20enquiry">Send by email</a>
</div>
<p class="qprev" aria-live="polite"><span>Your message:</span> <span id="qbh-text"></span></p>
</form>
<script>
(function(){{var f=document.getElementById("qbh");if(!f)return;
function v(n){{var e=f.querySelector('input[name="'+n+'"]:checked');return e?e.value:"";}}
function all(n){{return Array.prototype.map.call(f.querySelectorAll('input[name="'+n+'"]:checked'),function(e){{return e.value;}}).join(", ");}}
function build(){{var w=document.getElementById("qbh-where").value.trim(),q=document.getElementById("qbh-qty").value.trim();
var lines=["Hello Akshay, I would like to ask about your hydroxyapatite.","Grade: "+v("hgrade"),"Request: "+v("hwant"),"Use: "+v("huse").replace("&amp;","&"),
"Documents: "+(all("hdocs")||"none yet"),"Delivery: "+(w||"to discuss"),"Quantity: "+(q||"to discuss"),"Please include price per kg and lead time."];
var msg=lines.join("\\n");document.getElementById("qbh-text").textContent=lines.slice(1,4).join(" · ");
document.getElementById("qbh-wa").href="https://wa.me/{WA_NUM}?text="+encodeURIComponent(msg);
document.getElementById("qbh-mail").href="mailto:sales@calvaralabs.com?subject="+encodeURIComponent("Hydroxyapatite enquiry: "+v("hwant"))+"&body="+encodeURIComponent(msg);}}
f.addEventListener("change",build);f.addEventListener("input",build);build();}})();
</script>'''


HAP_ASKS = [
    ("Price per kg",
     "Prices for trial lots and regular supply, ex-works Jodhpur or delivered in India. Export prices on request.",
     "Hello Akshay, please send your hydroxyapatite price per kg for ___ kg (trial / regular)."),
    ("250 g sample",
     "A free 250 g sample of the micro grade with its Certificate of Analysis, sent by courier with tracking.",
     "Hello Akshay, please send a 250 g hydroxyapatite sample to ___. Our use: ___"),
    ("TDS and test reports",
     "Technical data sheet and sample CoA. Tell us which reports you need (XRD, Ca/P, heavy metals, particle size) and Akshay confirms what is available for your lot.",
     "Hello Akshay, please send the hydroxyapatite TDS and sample CoA. We also need: ___"),
    ("Packs and capacity",
     "1, 5 and 25 kg packs. We make small lots today and scale with demand; ask for monthly capacity and lead time.",
     "Hello Akshay, what monthly hydroxyapatite quantity can you supply, and what is the lead time?"),
    ("Nano grade",
     "Nano grade (20 to 100 nm) is in development. Ask Akshay for the expected timeline and to join the first sample list.",
     "Hello Akshay, please add us to the first sample list for nano hydroxyapatite. Our use: ___"),
    ("Regulatory documents",
     "Synthetic and animal-free. Tell us the documents your regulatory or QA team needs and Akshay confirms what we can provide.",
     "Hello Akshay, our QA team needs these documents for your hydroxyapatite: ___"),
]


def hap_asks_grid():
    cards = "".join(
        f'<article class="ask"><h3>{t}</h3><p>{d}</p><a class="ask-cta" href="{wa(m)}">Ask Akshay on WhatsApp</a></article>' for t, d, m in HAP_ASKS)
    return f'<div class="asks">{cards}</div>'


# Brochures shown at the top of the home page. Set "file" to a PDF in src/brochures/ to publish one;
# file None shows a "coming soon" card.
BROCHURES = {
    "lime": {"title": "Hydrated Lime Brochure 2026", "file": "Calvara-Hydrated-Lime-Brochure-2026.pdf",
             "meta": "10 pages · PDF · 1.3 MB", "what": "All 7 grades and specs, plant photos, packing, export loading and CoA format."},
    "hap": {"title": "Hydroxyapatite Brochure 2026", "file": "Calvara-Hydroxyapatite-Brochure-2026.pdf",
            "meta": "6 pages · PDF · 0.8 MB", "what": "Micro and nano grades, full specification, how we make it, and how to start with a 250 g sample."},
}


def brochure_href(root, key):
    f = BROCHURES[key]["file"]
    return f"{root}brochures/{f}" if f else None


def brochure_block(root):
    lime, hap = BROCHURES["lime"], BROCHURES["hap"]
    lh = brochure_href(root, "lime")
    hh = brochure_href(root, "hap")
    hap_btn = (f'<a class="btn btn-solid" href="{hh}" download>Download PDF</a><a class="btn btn-line" href="{hh}" target="_blank" rel="noopener">View online</a>' if hh else
               f'<a class="btn btn-line" href="{wa("Hello Akshay, please send the hydroxyapatite TDS and a sample CoA.")}">Ask on WhatsApp</a>')
    return f'''<div class="brochures" aria-label="Brochures">
<div class="broch broch-main">
<a class="broch-cover" href="{lh}" target="_blank" rel="noopener"><img src="photos/brochure-cover.webp" alt="Cover of the Calvara Hydrated Lime Brochure 2026" width="150" height="212"></a>
<div class="broch-body">
<p class="broch-kicker">Free download</p>
<h2 class="broch-title">{lime["title"]}</h2>
<p class="broch-what">{lime["what"]}</p>
<div class="btn-row"><a class="btn btn-red btn-big" href="{lh}" download>Download brochure (PDF)</a><a class="btn btn-line" href="{lh}" target="_blank" rel="noopener">View online</a></div>
<p class="broch-meta">{lime["meta"]}</p>
</div></div>
<div class="broch broch-hap{' broch-hap-live' if hh else ''}">
{f'<a class="broch-cover" href="{hh}" target="_blank" rel="noopener"><img src="photos/hap-brochure-cover.webp" alt="Cover of the Calvara Hydroxyapatite Brochure 2026" width="96" height="136"></a>' if hh else ''}
<div class="broch-body">
<p class="broch-kicker">{'Free download' if hh else hap["meta"]}</p>
<h2 class="broch-title broch-title-sm">{hap["title"]}</h2>
<p class="broch-what">{hap["what"]}</p>
<div class="btn-row">{hap_btn}</div>
{f'<p class="broch-meta">{hap["meta"]}</p>' if hh else ''}
</div></div>
</div>'''


# ---------- moving ticker and plant motion (home) ----------
TICKER = [
    "Hydrated lime 80–95 % Ca(OH)<sub>2</sub>", "Free sample with its CoA", "25, 30, 35 or 40 kg bags",
    "900 kg jumbo bags", "Palletised or non-palletised", "CIF and CFR export quotes",
    "Ready stock at Ransigaon, Jodhpur", "Hydroxyapatite: 250 g samples", "Talk directly to the engineer",
]


def ticker():
    items = "".join(f'<li>{t}</li>' for t in TICKER)
    return f'''<div class="ticker" aria-label="Calvara at a glance">
<div class="ticker-view"><div class="ticker-track"><ul>{items}</ul><ul aria-hidden="true">{items}</ul></div></div>
<button class="ticker-btn" type="button" aria-pressed="false" aria-label="Pause moving text"><svg viewBox="0 0 16 16" aria-hidden="true"><path class="i-pause" d="M4 3h3v10H4zM9 3h3v10H9z" fill="currentColor"/><path class="i-play" d="M5 3l8 5-8 5z" fill="currentColor"/></svg></button>
</div>'''


def motion_section(root):
    svg = (ROOT / "src" / "assets" / "media" / "process.svg").read_text()
    def vid(key, title, text):
        m = f"{root}assets/media/{key}"
        return f'''<figure class="reel">
<div class="reel-media"><video muted loop playsinline preload="none" poster="{m}-poster.jpg" aria-label="{title}"><source src="{m}.webm" type="video/webm"><source src="{m}.mp4" type="video/mp4"></video>
<button class="reel-btn" type="button" aria-label="Pause {title.lower()}"><svg viewBox="0 0 16 16" aria-hidden="true"><path class="i-pause" d="M4 3h3v10H4zM9 3h3v10H9z" fill="currentColor"/><path class="i-play" d="M5 3l8 5-8 5z" fill="currentColor"/></svg></button></div>
<figcaption><b>{title}</b>{text}</figcaption></figure>'''
    return f'''<section class="section motion"><div class="wrap">
<div class="section-head"><h2>See how your lime is made</h2><p class="lede">From quicklime to a sealed bag at our plant in Ransigaon, Jodhpur. Plant visits are welcome by appointment.</p></div>
<div class="reels">
<figure class="reel reel-svg"><div class="reel-media">{svg}
<button class="reel-btn" type="button" aria-label="Pause process animation"><svg viewBox="0 0 16 16" aria-hidden="true"><path class="i-pause" d="M4 3h3v10H4zM9 3h3v10H9z" fill="currentColor"/><path class="i-play" d="M5 3l8 5-8 5z" fill="currentColor"/></svg></button></div>
<figcaption><b>The process</b>Quicklime and measured water become dry hydrated lime.</figcaption></figure>
{vid("plant-tour", "Inside the plant", "Kiln, hydrators, classifier, packing and the plant lab.")}
{vid("packing-dispatch", "Packing and dispatch", "25 to 40 kg bags and 900 kg jumbo bags, ready stock.")}
</div>
<p class="swipe-hint">Swipe to see all three.</p>
</div></section>
<script>
(function(){{
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function setBtn(b, paused){{ b.classList.toggle('is-paused', paused); b.setAttribute('aria-label', (paused ? 'Play ' : 'Pause ') + b.getAttribute('aria-label').replace(/^(Play|Pause) /,'')); }}
  document.querySelectorAll('.reel').forEach(function(r){{
    var v = r.querySelector('video'), s = r.querySelector('.reel-media > svg'), b = r.querySelector('.reel-btn'), user = false;
    function play(){{ if(v){{ var p=v.play(); if(p&&p.catch)p.catch(function(){{}}); }} if(s) s.unpauseAnimations(); setBtn(b,false); }}
    function stop(){{ if(v) v.pause(); if(s) s.pauseAnimations(); setBtn(b,true); }}
    b.addEventListener('click', function(){{ user = true; if(b.classList.contains('is-paused')) play(); else stop(); }});
    if(reduce){{ stop(); return; }}
    if('IntersectionObserver' in window){{
      new IntersectionObserver(function(es){{ es.forEach(function(e){{ if(user) return; if(e.isIntersecting) play(); else stop(); }}); }}, {{threshold:.35}}).observe(r);
    }} else play();
  }});
  var t = document.querySelector('.ticker');
  if(t){{ var tb = t.querySelector('.ticker-btn');
    function tset(p){{ t.classList.toggle('is-paused', p); tb.classList.toggle('is-paused', p); tb.setAttribute('aria-pressed', p); tb.setAttribute('aria-label', p ? 'Play moving text' : 'Pause moving text'); }}
    tb.addEventListener('click', function(){{ tset(!t.classList.contains('is-paused')); }});
    if(reduce) tset(true);
  }}
}})();
</script>'''


# ---------- pages ----------
def home():
    root = ""
    body = f'''
<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow-plain">Hydrated lime · Jodhpur, Rajasthan</p>
<h1>Hydrated lime, made to the grade you need.</h1>
<p class="lede">Seven grades from 80 to 95 % Ca(OH)<sub>2</sub>, made at our own plant in Ransigaon, Jodhpur. Every lot is tested in our plant lab and ships with a Certificate of Analysis.</p>
<div class="btn-row"><a class="btn btn-solid" href="#quote">Get a price</a><a class="btn btn-red" href="{brochure_href(root, 'lime')}" download>Download brochure</a></div>
</div>
<div class="hero-ladder">{ladder()}</div>
</div></section>
{ticker()}

{motion_section(root)}

<section class="broch-band" id="brochure"><div class="wrap">
{brochure_block(root)}
</div></section>

<section><div class="wrap">{stats()}</div></section>

<section class="section section-tint" id="quote"><div class="wrap">
{quote_builder(root)}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Everything buyers ask us, ready to send</h2><p class="lede">Prices, packing, containers, documents and terms. Tap any card to ask Akshay directly; most replies come the same day.</p></div>
{asks_grid(6)}
<div class="btn-row" style="margin-top:22px"><a class="btn btn-line" href="{href(root, 'export')}">See all prices and export details</a><a class="btn btn-line" href="{href(root, 'export')}#hap">Buying hydroxyapatite? Request a sample</a></div>
</div></section>

<section class="section"><div class="wrap split">
<div class="prose">
<h2>Our own plant. Run by an engineer.</h2>
<p>Calvara Labs &amp; Minerals makes hydrated lime at its own plant in Ransigaon, in the limestone belt of Jodhpur. Limestone, kilns and lab testing are everyday work for us.</p>
<p>Each grade has a published specification. You test a sample first, and we supply to the sample you approve.</p>
<ul><li><b>Kiln know-how.</b> We know limestone, burning and calcium chemistry from running our own kiln.</li><li><b>Tested, not guessed.</b> Every lot is checked in our plant lab and ships with a CoA.</li><li><b>Sample first.</b> Try the grade in your own process before you place a regular order.</li></ul>
</div>
{engineer(root)}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>From stone to sack, step by step</h2><p class="lede">Every bag you buy goes through these six steps at our plant in Ransigaon, Jodhpur. Plant visits are welcome by appointment.</p></div>
{plant_rail()}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Bad lime costs you money. Here's how we prevent it.</h2><p class="lede">Most lime problems show up in your plant, not on the invoice. These are the five we hear about most often.</p></div>
{problems()}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Seven grades. Pick your purity.</h2><p class="lede">The grade number is the minimum Ca(OH)<sub>2</sub> content. A higher grade gives more active lime, less silica and a finer, whiter powder.</p></div>
{ranges()}
<p style="margin-top:24px"><a class="btn btn-solid" href="{href(root, 'hydrated-lime')}#spec">Compare all seven grades</a></p>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>One powder, nine industries</h2><p class="lede">Start with the grade in red. The right final grade depends on how much silica and inert matter your process can tolerate.</p></div>
{industries()}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Packed your way</h2><p class="lede">Sealed, laminated bags with liners, held in covered storage until loaded onto your truck. Part or full loads, ex-works or delivered.</p></div>
{bags()}
{wide_photos()}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>How to start</h2></div>
{start_steps()}
</div></section>

<section class="section section-tint"><div class="wrap split">
<div class="prose"><h2>Also from our calcium: hydroxyapatite</h2><p>We make synthetic, animal-free hydroxyapatite from purified calcium for toothpaste, tablets, cosmetics and labs. Micro grade samples are open now.</p><p><a href="{href(root, 'hydroxyapatite')}">Hydroxyapatite specification</a></p></div>
<div class="mini-tile"><span class="formula">Ca<sub>10</sub>(PO<sub>4</sub>)<sub>6</sub>(OH)<sub>2</sub></span><span class="meta">CAS 1306-06-5 · Ca/P 1.67 · D50 3 to 8 µm</span></div>
</div></section>

{cta_band(root)}
'''
    page("", root, "", "Hydrated Lime Manufacturer, Jodhpur | Grades 80–95 | Calvara Labs",
         "Hydrated lime in seven grades, 80 to 95% Ca(OH)2, made at Ransigaon, Jodhpur. Silica as low as 1.0%, 99.5% through 200 mesh, CoA with every lot. 25, 30, 35 or 40 kg bags, palletised or non-palletised.",
         body)


def lime():
    root = "../"
    faq = [
        ("Which grade do I need?", "Find your industry above and start with the grade shown in red. Then tell us your process: we will suggest a grade and send a sample with its Certificate of Analysis so you can test it."),
        ("Is the grade number a minimum or an average?", "A minimum. The grade number is the minimum Ca(OH)2 content, and every lot ships with a CoA showing the measured result."),
        ("What is the difference between quicklime and hydrated lime?", "Quicklime is calcium oxide (CaO). Hydrated lime is quicklime slaked with measured water to form dry calcium hydroxide, Ca(OH)2. It is safer to handle and easier to dose."),
        ("Do you export?", "Yes. We pack in sealed, laminated bags and load containers by a fixed, checked method with a moisture barrier and a numbered seal. Send your port and monthly volume with your enquiry."),
        ("How long can I store hydrated lime?", "Use it within 6 months. Lime slowly absorbs CO2 and moisture from the air, which lowers its effective grade. Keep it dry, in the sealed original bags, on pallets away from walls."),
        ("Can I visit the plant?", "Yes, plant visits at Ransigaon, Jodhpur are welcome by appointment. Call or WhatsApp +91 98927 27068."),
    ]
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    container = buy_steps([
        ("Container checked", "Clean, dry, with no holes or odour, before any bag goes in."),
        ("Moisture-lined", "A moisture barrier lines the floor and walls first."),
        ("Stacked tight", "Even rows with no gaps, so bags cannot shift or rub."),
        ("Braced and secured", "Gaps are filled and the load is secured against movement."),
        ("Loading photographed", "We photograph the loading for your records."),
        ("Sealed and numbered", "Closed with a numbered seal before it leaves our plant."),
    ])
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "Hydrated lime")}
<div class="page-head-grid">
<div class="prose" style="gap:18px">
<h1>Hydrated lime in seven grades</h1>
<p class="lede">Calcium hydroxide, Ca(OH)<sub>2</sub>. Fine, dry, high-purity powder from the lime belt of Jodhpur, Rajasthan. Every lot is tested and labelled, and made to the grade you need.</p>
<div class="btn-row"><a class="btn btn-red" href="{brochure_href(root, 'lime')}" download>Download brochure (PDF)</a><a class="btn btn-line" href="#spec">Compare grades</a></div>
</div>
<div class="mini-tile"><span class="formula">Ca(OH)<sub>2</sub></span><span class="meta">Calcium hydroxide · CAS 1305-62-0 · HSN 2522</span><span class="meta">Grades 95 · 94 · 93 · 92 · 90 · 85 · 80</span></div>
</div>
</div></section>

<section class="section" id="spec"><div class="wrap">
<div class="section-head"><h2>Typical specification by grade</h2><p class="lede">The grade number is the minimum Ca(OH)<sub>2</sub> content. Higher grades carry less silica and are finer.</p></div>
{spec_table()}
<p class="table-note">Typical, indicative values. Final specifications are confirmed against an agreed sample and the Certificate of Analysis for each lot.</p>
</div></section>

<section class="section section-tint" id="quote"><div class="wrap">
{quote_builder(root)}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Prices, packing and documents</h2><p class="lede">Tap a card to ask Akshay with the question already written.</p></div>
{asks_grid(6)}
<p style="margin-top:22px"><a class="btn btn-line" href="{href(root, 'export')}">All export details</a></p>
</div></section>

<section class="section section-tint"><div class="wrap split">
<div class="prose"><h2>Grade ranges and shared properties</h2><p>Which range suits which work, and the properties every grade shares.</p>{ranges().replace('class="ranges"', 'class="ranges" style="grid-template-columns:1fr;margin-top:8px"')}</div>
{common_props()}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Find your grade by industry</h2><p class="lede">Start with the grade in red.</p></div>
{industries()}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Packed your way, delivered as agreed</h2><p class="lede">Fully sealed, laminated bags and a fixed, checked container-loading method keep your lime dry all the way to your plant, including on board ship.</p></div>
{bags()}
<div class="facts" style="margin-top:24px">
<div><b>Completely sealed</b><p>Every bag is sealed at the mouth to keep out air and moisture.</p></div>
<div><b>Laminated packing</b><p>Laminated bags with liners keep the lime dry in handling and storage.</p></div>
<div><b>Palletised or non-palletised</b><p>Pallets for faster, cleaner unloading, or loose-loaded bags for more tonnes per container.</p></div>
<div><b>Your bag, your brand</b><p>Liner, laminated, company-branded or PP bags, with other layering on request.</p></div>
</div>
{wide_photos()}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>How we stuff your container</h2></div>
{container}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Storage and safe handling</h2></div>
<div class="facts facts-3">
<div><b>Keep it dry and sealed</b><p>Store in a cool, dry place in the sealed original bags. Stack on pallets, away from walls.</p></div>
<div><b>Use within 6 months</b><p>Lime slowly absorbs CO<sub>2</sub> and moisture from air, which lowers its effective grade.</p></div>
<div><b>Handle with care</b><p>Alkaline: irritates skin, eyes and lungs. Wear gloves, goggles and a dust mask. Rinse any contact with plenty of water.</p></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Questions buyers ask</h2></div>
<div class="faq">{faqs}</div>
</div></section>

{cta_band(root, "Get a hydrated lime quote", "Send the grade, monthly quantity and delivery city or port. You hear back directly from our engineer.")}
'''
    page("hydrated-lime", root, "hydrated-lime", "Hydrated Lime Grades 80–95% | Specifications | Calvara Labs, Jodhpur",
         "Compare seven hydrated lime grades: Ca(OH)2 80–95%, silica 0.8–8%, moisture 0.5–2.0%, 90–99.5% through 200 mesh. Bags of 25, 30, 35 or 40 kg, palletised or non-palletised, CoA with every lot.",
         body, faq_ld)


def hap():
    root = "../"
    spec = [("Hydroxyapatite content (XRD)", "95% min"), ("Free CaO", "None detected"), ("β-tricalcium phosphate", "3% max"),
            ("Ca/P molar ratio", "1.62 to 1.72"), ("Particle size, D50", "3 to 8 µm"), ("Loss on drying", "3% max"),
            ("pH (slurry)", "7 to 9.5"), ("Lead (Pb)", "2 mg/kg max"), ("Arsenic (As)", "3 mg/kg max"), ("Cadmium (Cd)", "1 mg/kg max"),
            ("Mercury (Hg)", "1 mg/kg max"), ("Fluoride (F)", "50 mg/kg max"), ("Total plate count", "100 cfu/g max"),
            ("Yeast and mould", "10 cfu/g max"), ("Pathogens", "Absent")]
    rows = "".join(f'<tr><th scope="row">{a}</th><td class="num">{b}</td></tr>' for a, b in spec)
    faq = [
        ("Is your hydroxyapatite animal-free?", "Yes. It is made synthetically from calcium hydroxide and food-grade phosphoric acid. No bone or fish is used."),
        ("What is the difference between micro and nano hydroxyapatite?", "Nano hydroxyapatite has particles under 100 nm. Our micro grade (D50 3 to 8 µm) is available for samples now. Nano grade (20 to 100 nm) is in development."),
        ("What does the Ca/P ratio tell me?", "Pure hydroxyapatite has a calcium to phosphorus molar ratio of 1.67. A ratio close to this shows the product is mostly hydroxyapatite."),
        ("Can I use it in a medical device or bone graft?", "No. Medical-grade hydroxyapatite needs a medical device licence, and we do not offer it."),
    ]
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "Hydroxyapatite")}
<div class="page-head-grid">
<div class="prose" style="gap:18px">
<h1>Hydroxyapatite powder, made in India</h1>
<p class="lede">Synthetic, animal-free hydroxyapatite made from our own purified calcium. Micro grade samples are available now for toothpaste, tooth powder, tablets, cosmetics and research.</p>
<div class="btn-row"><a class="btn btn-solid" href="#quote">Ask for a 250 g sample</a><a class="btn btn-red" href="{brochure_href(root, 'hap')}" download>Download brochure (PDF)</a><a class="btn btn-line" href="#spec">See the specification</a></div>
</div>
<div class="mini-tile"><span class="formula">Ca<sub>10</sub>(PO<sub>4</sub>)<sub>6</sub>(OH)<sub>2</sub></span><span class="meta">Hydroxyapatite (HAp) · CAS 1306-06-5</span><span class="meta">Molar mass 1004.6 g/mol · Ca/P 1.67</span></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Grades</h2></div>
<div class="table-box"><table style="min-width:0">
<thead><tr><th scope="col">Grade</th><th scope="col">Particle size</th><th scope="col">Status</th></tr></thead>
<tbody><tr><th scope="row">Micro</th><td class="num">D50 3 to 8 µm</td><td>Samples available now</td></tr>
<tr><th scope="row">Nano</th><td class="num">20 to 100 nm</td><td>In development</td></tr></tbody></table></div>
</div></section>

<section class="section section-tint" id="spec"><div class="wrap split">
<div class="prose"><h2>Micro grade specification</h2>
<p>These are the limits we make the micro grade to. Each lot ships with its own Certificate of Analysis showing the measured values.</p>
<p>Heavy metals and fluoride are controlled from the start: we test the incoming lime and use only food-grade phosphoric acid.</p><p>Need a TDS, sample CoA or a specific test report (XRD, Ca/P, heavy metals, particle size)? <a href="https://wa.me/919892727068?text=Hello%20Akshay%2C%20please%20send%20the%20TDS%20and%20sample%20CoA%20for%20your%20hydroxyapatite.%20We%20also%20need%3A%20___">Ask Akshay</a> and he will confirm what is available for your sample lot.</p></div>
<div class="table-box"><table style="min-width:0"><caption>Micro grade, target limits</caption><tbody>{rows}</tbody></table></div>
</div></section>

<section class="section"><div class="wrap split">
<div class="prose"><h2>How we make it</h2>
<ul><li>Our hydrated lime is purified to a clean calcium solution and filtered to 1 µm.</li>
<li>Food-grade phosphoric acid is added at pH 9 to 10, and hydroxyapatite precipitates.</li>
<li>The precipitate is aged and washed until the wash water is below 100 µS/cm.</li>
<li>It is dried at 105 °C, milled and sieved to size.</li></ul></div>
<div class="prose"><h2>The reaction</h2>
<p class="reaction">10 Ca(OH)<sub>2</sub> + 6 H<sub>3</sub>PO<sub>4</sub> → Ca<sub>10</sub>(PO<sub>4</sub>)<sub>6</sub>(OH)<sub>2</sub> + 18 H<sub>2</sub>O</p>
<p>Phase purity is confirmed by X-ray diffraction.</p></div>
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Applications</h2></div>
<div class="uses">
<div><span class="tag">Samples open</span><h3>Toothpaste</h3><p>Enamel-care and sensitivity toothpastes, often as a fluoride-free active.</p></div>
<div><span class="tag">Samples open</span><h3>Tooth powder</h3><p>Mild polishing and remineralising calcium in powder formats.</p></div>
<div><span class="tag">Samples open</span><h3>Tablets</h3><p>A calcium and phosphorus source in tablet formulations.</p></div>
<div><span class="tag">Samples open</span><h3>Cosmetics</h3><p>A mineral ingredient in skincare and personal care.</p></div>
<div><span class="tag">Samples open</span><h3>Laboratories</h3><p>Small packs for research and method development.</p></div>
<div><span class="tag">Planned</span><h3>Food supplements</h3><p>Planned once our food manufacturing licence is in place.</p></div>
</div>
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>How to start</h2><p class="lede">Packs of 1, 5 and 25 kg.</p></div>
{buy_steps([("Share your spec", "Particle size, purity and limits your formulation needs."), ("250 g sample", "Free sample with its Certificate of Analysis."), ("5 to 25 kg trial", "A trial lot to run in your process."), ("Regular supply", "Agreed specification, packing and schedule.")])}
</div></section>

<section class="section section-tint" id="quote"><div class="wrap">
{quote_builder_hap(root)}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>What we can send you</h2><p class="lede">Tap a card to ask Akshay on WhatsApp with the question already written.</p></div>
{hap_asks_grid()}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Questions buyers ask</h2></div>
<div class="faq">{faqs}</div>
</div></section>

{cta_band(root, "Request a hydroxyapatite sample", "Tell us your application, particle size and expected quantity. We send 250 g with a Certificate of Analysis.")}
'''
    page("hydroxyapatite", root, "hydroxyapatite", "Hydroxyapatite Powder Manufacturer India | Animal-Free | Calvara Labs",
         "Synthetic, animal-free hydroxyapatite (micro grade, D50 3–8 µm) for toothpaste, tablets, cosmetics and labs. HAp ≥95% by XRD, Ca/P 1.67. Free 250 g sample.",
         body, faq_ld)


def about():
    root = "../"
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "About &amp; quality")}
<div class="prose" style="gap:18px;max-width:760px">
<h1>Our own plant. Run by an engineer.</h1>
<p class="lede">Calvara Labs &amp; Minerals makes hydrated lime at its own plant in Ransigaon, in the limestone belt of Jodhpur. Limestone, kilns and lab testing are everyday work for us.</p>
</div>
</div></section>

<section class="section"><div class="wrap split">
<div class="prose">
<h2>Who we are</h2>
<p>Our hydrated lime comes in seven grades, from 80 to 95 % Ca(OH)<sub>2</sub>, each with a published specification. You test a sample first, and we supply to the sample you approve.</p>
<p>We also use our calcium to make finer chemicals, starting with <a href="{href(root, 'hydroxyapatite')}">hydroxyapatite</a>.</p>
<div class="addr"><b>Office</b><span class="muted">{OFFICE}</span></div>
<div class="addr"><b>Works</b><span class="muted">{WORKS}. Plant visits welcome by appointment.</span></div>
</div>
{engineer(root)}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Inside our plant</h2><p class="lede">From stone to sack in six steps.</p></div>
{plant_rail()}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Quality you can check</h2><p class="lede">Every lot is tested in our plant lab before dispatch. Here is what each test means for your process.</p></div>
<div class="facts">
<div><b>Ca(OH)<sub>2</sub> content</b><p>Active lime, measured by titration. Tells you how much you need to dose.</p></div>
<div><b>Moisture</b><p>Dry lime flows freely and does not cake in feeders.</p></div>
<div><b>Acid insoluble</b><p>Silica and grit that wear pumps and add sludge.</p></div>
<div><b>200-mesh fineness</b><p>Finer powder reacts faster and stays in suspension.</p></div>
</div>
{lab_photos()}
</div></section>

<section class="section section-tint"><div class="wrap split">
<div class="prose">
<h2>What arrives with your lime</h2>
<ul><li><b>CoA with every lot.</b> Results for the key parameters of your grade.</li>
<li><b>Full traceability.</b> Lot number, grade and packing date on each lot.</li>
<li><b>Approved-sample match.</b> Supplies are held to the sample you signed off.</li></ul>
</div>
{coa_sample()}
</div></section>

{cta_band(root, "Talk to us about your process")}
'''
    page("about", root, "about", "About Calvara Labs & Minerals | Lime Plant, Ransigaon, Jodhpur",
         "Calvara Labs & Minerals makes hydrated lime at its own plant in Ransigaon, Jodhpur. Plant lab tests every lot; CoA, lot traceability and approved-sample supply.",
         body)


def contact():
    root = "../"
    grade_opts = "".join(f"<option>Grade {g}</option>" for g, *_ in GRADES)
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "Contact")}
<div class="prose" style="gap:14px;max-width:760px">
<h1>Let's talk lime</h1>
<p class="lede">Ask for a sample, a specification sheet or a grade recommendation. You hear back directly from an engineer.</p>
<div class="btn-row"><a class="btn btn-wa" href="{WHATSAPP}">WhatsApp {PHONE_DISPLAY}</a><a class="btn btn-line" href="{href(root, 'export')}#quote">Quick price request</a></div>
</div>
</div></section>

<section class="section"><div class="wrap contact-grid">
<form class="form" action="https://formsubmit.co/{EMAIL}" method="POST">
<input type="hidden" name="_subject" value="New enquiry from calvaralabs.com">
<input type="hidden" name="_next" value="{SITE}/thanks/">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="f-company">Company</label><input id="f-company" name="company" type="text" autocomplete="organization" required></div>
<div class="field"><label for="f-phone">Phone or WhatsApp</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required></div>
<div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" inputmode="email" autocomplete="email"></div>
<div class="field"><label for="f-product">Product</label><select id="f-product" name="product"><option>Hydrated lime</option><option>Hydroxyapatite</option><option>Both</option></select></div>
<div class="field"><label for="f-grade">Grade</label><select id="f-grade" name="grade"><option>Not sure, please advise</option>{grade_opts}</select></div>
<div class="field"><label for="f-request">I would like</label><select id="f-request" name="request"><option>A sample</option><option>A price quote</option><option>A specification sheet</option><option>Grade advice</option></select></div>
<div class="field"><label for="f-qty">Monthly quantity</label><input id="f-qty" name="quantity" type="text" placeholder="20 tonnes a month"></div>
<div class="field full"><label for="f-use">Your application</label><input id="f-use" name="application" type="text" placeholder="Effluent treatment, AAC blocks"></div>
<div class="field full"><label for="f-where">Delivery city or port</label><input id="f-where" name="delivery" type="text" autocomplete="address-level2"></div>
<div class="field full"><label for="f-msg">Anything else (optional)</label><textarea id="f-msg" name="message" rows="3"></textarea></div>
<div class="actions"><button class="btn btn-red" type="submit">Send enquiry</button><p>We use your details only to answer this enquiry.</p></div>
</form>
<aside style="display:flex;flex-direction:column;gap:20px">
<div class="side-card dark">
<h2 style="font-size:22px">Your engineer</h2>
<p><b style="color:#fff">Akshay Khadav</b><br>B.Tech Chemical Engineering, IIT Bombay</p>
<div class="contact-line"><span>Call or WhatsApp</span><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div>
<div class="contact-line"><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
<div class="contact-line"><span>Office</span><p>{OFFICE}</p></div>
<div class="contact-line"><span>Works</span><p>{WORKS}</p></div>
</div>
<div class="side-card light">
<h2 style="font-size:20px">Ask us for</h2>
<ol><li>A sample of the grade you want to test</li><li>A specification sheet and Certificate of Analysis</li><li>Grade advice matched to your process</li></ol>
</div>
</aside>
</div></section>
<script>
(function(){{var q=new URLSearchParams(location.search);[["product","f-product"],["grade","f-grade"]].forEach(function(p){{var v=q.get(p[0]),s=document.getElementById(p[1]);if(!v||!s)return;for(var i=0;i<s.options.length;i++){{if(s.options[i].text.toLowerCase().indexOf(v.toLowerCase())>-1){{s.selectedIndex=i;break;}}}}}});}})();
</script>
'''
    page("contact", root, "contact", "Contact Calvara Labs & Minerals | Hydrated Lime Quote, Jodhpur",
         "Ask for a hydrated lime sample, specification sheet or grade advice. Call or WhatsApp +91 98927 27068. Office: Patrakar Colony, Jodhpur. Works: Ransigaon.",
         body)


def export():
    root = "../"
    faq = [
        ("What is the difference between FOB, CFR and CIF?", "FOB: we deliver the lime loaded on the ship at the Indian port; you pay sea freight and insurance. CFR: we also pay sea freight to your port. CIF: CFR plus marine insurance. Ex-works means you collect from our plant in Jodhpur."),
        ("Palletised or non-palletised: which should I choose?", "Palletised bags are faster and cleaner to unload with a forklift and suffer less handling damage. Non-palletised (loose-loaded) bags fit more tonnes in each container, so the freight cost per tonne is lower. Ask Akshay to quote both."),
        ("How quickly will I get a price?", "Usually the same day. Send your grade, packing, pallets, price basis, port and quantity, or use the quote form on this page."),
        ("Do you supply small trial orders?", "Yes. Start with a free sample, then a trial lot, then regular supply. Ask Akshay for the trial quantity that suits your process."),
        ("Can you match our specification?", "Send your specification or standard. We confirm the grade that meets it and send a sample with its CoA so you can test before ordering."),
    ]
    faqs = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "Prices &amp; export")}
<div class="prose" style="gap:16px;max-width:780px">
<h1>Prices, packing and export, answered</h1>
<p class="lede">Everything buyers usually ask before ordering hydrated lime or hydroxyapatite. Pick what you need below and Akshay sends it, usually the same day.</p>
<div class="btn-row"><a class="btn btn-solid" href="#quote">Hydrated lime quote</a><a class="btn btn-line" href="#hap">Hydroxyapatite sample or price</a></div>
</div>
</div></section>

<section class="section" id="quote"><div class="wrap">
{quote_builder(root)}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Hydrated lime: what we can send you</h2><p class="lede">Tap a card to ask Akshay on WhatsApp with the question already written.</p></div>
{asks_grid()}
</div></section>

<section class="section" id="hap"><div class="wrap">
{quote_builder_hap(root)}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Hydroxyapatite: what we can send you</h2><p class="lede">Tap a card to ask Akshay on WhatsApp with the question already written.</p></div>
{hap_asks_grid()}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>Hydrated lime packing options</h2></div>
{bags()}
{wide_photos()}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>Questions buyers ask</h2></div>
<div class="faq">{faqs}</div>
</div></section>

{cta_band(root, "Tell us your port and quantity", "Send the grade, packing and destination. You get price, container quantity, lead time and terms in one reply.")}
'''
    page("export", root, "export", "Prices & Export: Hydrated Lime CIF/CFR/FOB, Hydroxyapatite Samples | Calvara Labs",
         "Ask for hydrated lime prices CIF, CFR, FOB India or ex-works Jodhpur. 25, 30, 35 or 40 kg bags, palletised or non-palletised, 20 ft and 40 ft containers, TDS, CoA and SDS.",
         body, faq_ld)


def thanks():
    root = "../"
    body = f'''<div class="wrap notice">
<h1>Thank you, your enquiry is in</h1>
<p class="lede">Akshay will reply by phone or email, usually within one working day. For anything urgent, message us on WhatsApp.</p>
<div class="btn-row"><a class="btn btn-solid" href="{WHATSAPP}">WhatsApp us</a><a class="btn btn-line" href="{href(root, '')}">Back to home</a></div>
</div>'''
    page("thanks", root, "", "Thank you | Calvara Labs & Minerals", "Your enquiry has been sent to Calvara Labs & Minerals.", body, noindex=True)


def not_found():
    root = "/" if MODE == "live" else ""
    body = f'''<div class="wrap notice">
<h1>This page isn't here</h1>
<p class="lede">The link may be old or mistyped.</p>
<div class="btn-row"><a class="btn btn-solid" href="{href(root, 'hydrated-lime')}">Hydrated lime grades</a><a class="btn btn-line" href="{href(root, 'contact')}">Contact us</a></div>
</div>'''
    page("404.html", root, "", "Page not found | Calvara Labs & Minerals", "Page not found.", body, noindex=True)


def extras():
    shutil.copytree(ROOT / "src" / "assets", OUT / "assets", dirs_exist_ok=True)
    shutil.copytree(ROOT / "src" / "brochures", OUT / "brochures", dirs_exist_ok=True)
    if (ROOT / "src" / "photos").exists():
        shutil.copytree(ROOT / "src" / "photos", OUT / "assets" / "photos", dirs_exist_ok=True)
    (OUT / "assets" / "brand").mkdir(exist_ok=True)
    for f in ["logo.svg", "logo-horizontal.svg", "logo-horizontal-white.svg", "mark.svg", "calvara-logo-2000.png"]:
        shutil.copy(ROOT / "src" / "brand" / f, OUT / "assets" / "brand" / f)
    for f in ["favicon.svg", "favicon-32.png", "apple-touch-icon.png"]:
        shutil.copy(ROOT / "src" / f, OUT / f)
    (OUT / ".htaccess").write_text("ErrorDocument 404 /404.html\nDirectoryIndex index.html\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    urls = ["", "hydrated-lime/", "export/", "hydroxyapatite/", "about/", "contact/"]
    items = "".join(f"<url><loc>{SITE}/{u}</loc><lastmod>2026-11-10</lastmod></url>" for u in urls)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>\n')


if __name__ == "__main__":
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    home(); lime(); export(); hap(); about(); contact(); thanks(); not_found(); extras()
    print("built", OUT)

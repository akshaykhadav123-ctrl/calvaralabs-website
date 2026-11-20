"""Hindi pages for calvaralabs.com (/hi/). Called from build.py as hindi.build(module).

Written for Indian buyers: plain Hindi, keeping trade words people use every day
(ग्रेड, CoA, सिलिका, मेश, पैलेट, बैग). Facts match the English pages.
"""

UI = {"wa": "व्हाट्सऐप पर अक्षय से बात करें", "top": "ऊपर", "top_label": "पेज के ऊपर जाएँ"}

TICKER_HI = [
    ("मुफ़्त सैंपल", "किसी भी ग्रेड का सैंपल, उसके सर्टिफ़िकेट ऑफ़ एनालिसिस (CoA) के साथ।", "hi/contact", "अभी माँगें"),
    ("तैयार स्टॉक", "चार ग्रेड, 80 से 92 % Ca(OH)₂, 25, 30, 35 या 40 किलो के बैग में।", "hi/hydrated-lime", "ग्रेड देखें"),
    ("डिलीवरी", "जोधपुर प्लांट से या आपकी साइट तक, पैलेट पर या बिना पैलेट।", "hi/contact", "भाव पूछें"),
    ("नया", "हाइड्रॉक्सीएपेटाइट माइक्रो ग्रेड: 250 ग्राम के सैंपल उपलब्ध।", "hydroxyapatite", "जानें"),
]
TICKER_HI_EXTRA = ["900 किलो के जंबो बैग", "सीधे इंजीनियर से बात करें"]

NAV_HI = [("hi/hydrated-lime", "हाइड्रेटेड लाइम"), ("hydroxyapatite", "हाइड्रॉक्सीएपेटाइट"), ("documents", "दस्तावेज़"),
          ("export", "एक्सपोर्ट"), ("hi/contact", "संपर्क")]

IND_HI = {
    "Water and wastewater": ("पानी और अपशिष्ट जल", "pH सुधार, पानी को नरम करना, भारी धातु और फ़ॉस्फ़ेट हटाना"),
    "Chemicals": ("केमिकल", "कैल्शियम लवण, ब्लीचिंग पाउडर, कास्टिक सोडा उत्पादन"),
    "Sugar industry": ("चीनी उद्योग", "गन्ने के रस की सफ़ाई और शोधन"),
    "Ceramics and glass": ("सिरेमिक और काँच", "कच्चा माल और प्रोसेस एडिटिव"),
    "Flue gas treatment": ("फ़्लू गैस ट्रीटमेंट", "SO<sub>2</sub> और HCl की स्क्रबिंग और न्यूट्रलाइज़ेशन"),
    "Construction": ("निर्माण", "चूने का प्लास्टर, मसाला, पुट्टी, मिट्टी स्थिरीकरण, AAC ब्लॉक"),
    "Steel and metallurgy": ("स्टील और धातु उद्योग", "फ़्लक्स, स्लैग कंडीशनिंग, एसिड न्यूट्रलाइज़ेशन"),
    "Paper, leather and textile": ("कागज़, चमड़ा और कपड़ा", "कॉस्टिसाइज़िंग, चमड़े से बाल हटाना, रंगाई और फ़िनिशिंग"),
    "Agriculture": ("कृषि", "मिट्टी का pH सुधार, खाद तैयार करना"),
}

FAQ_HI = [
    ("मुझे कौन सा ग्रेड चाहिए?", "ऊपर अपना उद्योग देखें और लाल रंग में दिखाए ग्रेड से शुरू करें। फिर हमें अपनी प्रक्रिया बताइए: हम सही ग्रेड सुझाएँगे और उसका सैंपल CoA के साथ भेजेंगे, ताकि आप ख़ुद जाँच सकें।"),
    ("ग्रेड नंबर न्यूनतम है या औसत?", "न्यूनतम। ग्रेड नंबर Ca(OH)₂ की न्यूनतम मात्रा है, और हर लॉट के साथ CoA आता है जिसमें मापा गया परिणाम लिखा होता है।"),
    ("क्विकलाइम और हाइड्रेटेड लाइम में क्या अंतर है?", "क्विकलाइम कैल्शियम ऑक्साइड (CaO) है, जिसे कली चूना भी कहते हैं। हाइड्रेटेड लाइम उसी क्विकलाइम को नपे-तुले पानी से बुझाकर बना सूखा कैल्शियम हाइड्रॉक्साइड, Ca(OH)₂ है। इसे संभालना ज़्यादा सुरक्षित और डोज़ करना आसान है।"),
    ("क्या आप सैंपल भेजते हैं?", "हाँ। किसी भी ग्रेड का सैंपल उसके CoA के साथ भेजा जाता है। आप अपने प्लांट या लैब में जाँच लें, फिर उसी स्वीकृत सैंपल के अनुसार हम सप्लाई करते हैं।"),
    ("हाइड्रेटेड लाइम को कितने समय तक रख सकते हैं?", "सील बंद बैग में, सूखी और ठंडी जगह पर, छह महीने के भीतर इस्तेमाल करें। हवा की नमी और CO₂ से चूने का असरदार ग्रेड धीरे-धीरे घटता है।"),
]


def build(B):
    href, lic, wa, page = B.href, B.lic, B.wa, B.page

    def link(root, target):
        pg, _, anchor = target.partition("#")
        return href(root, pg) + (f"#{anchor}" if anchor else "")

    def ticker(root):
        items = "".join(f'<li><a href="{link(root, t)}"><b>{tag}</b> {txt} <span class="tk-go">{lbl}</span></a></li>' for tag, txt, t, lbl in TICKER_HI)
        items += "".join(f"<li>{t}</li>" for t in TICKER_HI_EXTRA)
        return f'''<div class="ticker ticker-top" role="region" aria-label="घोषणाएँ">
<div class="ticker-view"><div class="ticker-track"><ul>{items}</ul><ul aria-hidden="true" inert>{items}</ul></div></div>
<button class="ticker-btn" type="button" aria-pressed="false" aria-label="चलता टेक्स्ट रोकें">{lic("pause", "ic i-pause")}{lic("play", "ic i-play")}</button>
</div>'''

    def header(root, current, en_path):
        cur = ' aria-current="page"'
        links = "".join(f'<a href="{href(root, p)}"{cur if p == current else ""}{"" if p.startswith("hi/") else " hreflang=en"}>{t}</a>' for p, t in NAV_HI)
        en = f'{root}{en_path}' if en_path else root
        return f'''<a class="skip" href="#main">सीधे सामग्री पर जाएँ</a>
<div class="site-top">
{ticker(root)}
<header class="site-head">
<div class="wrap head-row">
{B.brand(root).replace('href="' + href(root, '') + '"', 'href="' + href(root, 'hi') + '"', 1)}
<nav class="nav" aria-label="मुख्य">{links}<a class="lang-switch" href="{en}" hreflang="en" lang="en">English</a><a class="btn btn-solid" href="{href(root, 'hi/contact')}">भाव पूछें</a></nav>
<a class="lang-switch lang-mob" href="{en}" hreflang="en" lang="en">English</a>
<details class="menu"><summary aria-label="मेन्यू खोलें">{lic("menu")}मेन्यू</summary><nav class="menu-panel" aria-label="मेन्यू">
<a href="{href(root, 'hi')}"{cur if current == 'hi' else ''}>होम</a>{links}<a href="{href(root, 'hi')}#brochure">ब्रोशर (PDF)</a>
<div class="menu-contact"><a class="btn btn-line" href="tel:{B.PHONE_TEL}">{lic("phone")}कॉल करें</a><a class="btn btn-wa" href="{B.WHATSAPP}">{lic("message-circle")}व्हाट्सऐप</a></div>
<a class="btn btn-solid" href="{href(root, 'hi/contact')}">भाव पूछें</a></nav></details>
</div>
</header>
</div>'''

    def footer(root):
        return f'''<footer class="site-foot">
<div class="wrap foot-grid">
<div>{B.brand(root, dark=True)}<p>हाइड्रेटेड लाइम के चार ग्रेड, जोधपुर के रणसीगांव में हमारे अपने प्लांट में बने।</p></div>
<div><h2>उत्पाद</h2><ul><li><a href="{href(root, 'hi/hydrated-lime')}">हाइड्रेटेड लाइम ग्रेड</a></li><li><a href="{B.brochure_href(root, 'lime')}" download>हाइड्रेटेड लाइम ब्रोशर (PDF, अंग्रेज़ी)</a></li><li><a href="{href(root, 'hydroxyapatite')}" hreflang="en">हाइड्रॉक्सीएपेटाइट</a></li><li><a href="{href(root, 'export')}" hreflang="en">एक्सपोर्ट और भाव</a></li></ul></div>
<div><h2>कंपनी</h2><ul><li><a href="{href(root, 'documents')}" hreflang="en">दस्तावेज़ (GST, IEC)</a></li><li><a href="{href(root, 'hi/contact')}">भाव पूछें</a></li><li>ऑफ़िस: {B.OFFICE}</li></ul></div>
<div><h2>संपर्क</h2><ul><li><a href="tel:{B.PHONE_TEL}">{B.PHONE_DISPLAY}</a></li><li><a href="{B.WHATSAPP}">व्हाट्सऐप करें</a></li><li><a href="mailto:{B.EMAIL}">{B.EMAIL}</a></li></ul></div>
</div>
<div class="wrap foot-base">© 2026 Calvara Labs &amp; Minerals · GSTIN {B.GSTIN} · HSN 2522 · CAS 1305-62-0</div>
</footer>'''

    def cta(root, title="जिस ग्रेड की ज़रूरत है, उसका सैंपल माँगें",
            text="अपना उपयोग, महीने की मात्रा और जो ग्रेड आप सोच रहे हैं, बताइए। जवाब सीधे हमारे इंजीनियर से आएगा, सैंपल और उसके CoA के साथ।"):
        return f'''<section class="cta-band"><div class="wrap cta-grid">
<div><h2>{title}</h2><p>{text}</p></div>
<div class="btn-row"><a class="btn btn-red" href="{href(root, 'hi/contact')}">भाव पूछें</a><a class="btn btn-ghost-light" href="{B.WHATSAPP}">व्हाट्सऐप करें</a></div>
</div></section>'''

    def hpage(path, root, current, en_path, title, desc, body, noindex=False):
        page(path, root, current, title, desc, body, lang="hi", alt=path + "/", noindex=noindex,
             head_html=header(root, current, en_path), foot_html=footer(root), ui=UI)

    def ladder():
        rows = ""
        for i, (g, _l, _ca, _c, _m, si, _mesh) in enumerate(B.GRADES):
            pct = (int(g) - 70) / 22 * 100
            rows += f'<li><span class="g">{g}</span><span class="bar" aria-hidden="true"><i style="width:{pct:.0f}%;--row:{i}"></i></span><span class="si">सिलिका ≤ {si}</span></li>'
        return f'''<div class="ladder" role="group" aria-label="हाइड्रेटेड लाइम के चार ग्रेड">
<div class="ladder-head">चार ग्रेड<span>न्यूनतम % Ca(OH)<sub>2</sub></span></div>
<ol>{rows}</ol>
<div class="ladder-foot">ऊँचे ग्रेड में सक्रिय चूना ज़्यादा और सिलिका कम होती है, इसलिए कम मात्रा में काम हो जाता है।</div>
</div>'''

    def stats():
        return '''<div class="stats">
<div><b>4</b><span>शुद्धता ग्रेड, 80 से 92 %</span></div>
<div><b>92 %</b><span>सबसे ऊँची शुद्धता, न्यूनतम Ca(OH)<sub>2</sub></span></div>
<div><b>98.5 %</b><span>200 मेश से पार (92 ग्रेड)</span></div>
<div><b>25–40</b><span>किलो के बैग: 25, 30, 35 या 40 किलो, पैलेट पर या बिना पैलेट</span></div>
</div>'''

    def industries():
        out = ""
        for name, _use, gs in B.INDUSTRIES:
            hn, hu = IND_HI[name]
            chips = "".join(f'<li class="chip{" first" if i == 0 else ""}">{g}</li>' for i, g in enumerate(gs))
            out += f'<div>{lic(B.IND_ICON.get(name, "factory"), "ic ind-ic")}<h3>{hn}</h3><p>{hu}</p><ul class="chips" aria-label="सुझाए गए ग्रेड, पहला ग्रेड शुरुआत के लिए">{chips}</ul></div>'
        return f'<div class="inds">{out}</div>'

    def faq():
        return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ_HI) + "</div>"

    def quote(root):
        s = B.quote_builder(root)
        for a, b in [
            ("<h2>Get a full quote in one message</h2>", "<h2>एक संदेश में पूरा भाव पाएँ</h2>"),
            ("Tap your choices and send. Akshay replies with price, specification, container quantity, lead time and payment terms together.",
             "अपने विकल्प चुनें और भेजें। अक्षय भाव, स्पेसिफ़िकेशन, डिलीवरी का समय और भुगतान की शर्तें एक साथ बताएँगे।"),
            ("<legend>Grade</legend>", "<legend>ग्रेड</legend>"), ("<legend>Packing</legend>", "<legend>पैकिंग</legend>"),
            ("<legend>Pallets</legend>", "<legend>पैलेट</legend>"), ("<legend>Price basis</legend>", "<legend>भाव का आधार</legend>"),
            ("kg bags", "किलो बैग"), ('"Not palletised"', '"बिना पैलेट"'), (">Not palletised<", ">बिना पैलेट<"),
            ('"Palletised"', '"पैलेट पर"'), (">Palletised<", ">पैलेट पर<"), ("Not sure", "पता नहीं"),
            ('value="CIF" checked', 'value="CIF"'), ('value="Delivered in India"', 'value="Delivered in India" checked'),
            ("Ex-works Jodhpur", "जोधपुर प्लांट से"), ("Delivered in India", "आपकी साइट तक"),
            (">Your port or city<", ">आपका शहर या पोर्ट<"), ('placeholder="Durban, Port Louis, Mombasa"', 'placeholder="जयपुर, अहमदाबाद, मुंद्रा पोर्ट"'),
            (">Quantity<", ">मात्रा<"), ('placeholder="1 x 20 ft a month"', 'placeholder="20 टन प्रति माह"'),
            (">Send on WhatsApp<", ">व्हाट्सऐप पर भेजें<"), (">Send by email<", ">ईमेल से भेजें<"),
            ("<span>Your message:</span>", "<span>आपका संदेश:</span>"),
            ("Hello Akshay, please quote hydrated lime.", "नमस्ते अक्षय जी, कृपया हाइड्रेटेड लाइम का भाव बताइए।"),
            ('"Grade: "', '"ग्रेड: "'), ('"please advise"', '"आप सुझाइए"'), ('"Packing: "', '"पैकिंग: "'),
            ('"Price basis: "', '"भाव का आधार: "'), ('"Quantity: "', '"मात्रा: "'), ('"to discuss"', '"बात करके तय करेंगे"'),
            ('"Please include container quantity, lead time, payment terms and the spec sheet."', '"कृपया डिलीवरी का समय, भुगतान की शर्तें और स्पेसिफ़िकेशन शीट भी भेजें।"'),
            ('"Hydrated lime quote: grade "', '"हाइड्रेटेड लाइम भाव: ग्रेड "'),
        ]:
            s = s.replace(a, b)
        return s

    def motion(root):
        s = B.motion_section(root)
        for a, b in [
            ("<h2>See how your lime is made</h2>", "<h2>देखिए आपका चूना कैसे बनता है</h2>"),
            ("From quicklime to a sealed bag at our plant in Ransigaon, Jodhpur. Plant visits are welcome by appointment.",
             "क्विकलाइम से सील बंद बैग तक, जोधपुर के रणसीगांव स्थित हमारे प्लांट में। समय लेकर प्लांट देखने ज़रूर आइए।"),
            ("<b>The process</b>Quicklime and measured water become dry hydrated lime.", "<b>प्रक्रिया</b>क्विकलाइम और नपा-तुला पानी मिलकर सूखा हाइड्रेटेड लाइम बनाते हैं।"),
            ("<b>Inside the plant</b>Kiln, hydrators, classifier, packing and the plant lab.", "<b>प्लांट के अंदर</b>भट्टी, हाइड्रेटर, क्लासिफ़ायर, पैकिंग और प्लांट लैब।"),
            ("<b>Packing and dispatch</b>25 to 40 kg bags and 900 kg jumbo bags, ready stock.", "<b>पैकिंग और डिस्पैच</b>25 से 40 किलो के बैग और 900 किलो के जंबो बैग, तैयार स्टॉक।"),
            ("Swipe to see all three.", "तीनों देखने के लिए स्वाइप करें।"),
            ('aria-label="Pause process animation"', 'aria-label="प्रक्रिया एनिमेशन रोकें"'),
            ('aria-label="Pause inside the plant"', 'aria-label="प्लांट वीडियो रोकें"'),
            ('aria-label="Pause packing and dispatch"', 'aria-label="पैकिंग वीडियो रोकें"'),
        ]:
            s = s.replace(a, b)
        return s

    def brochures(root):
        s = B.brochure_block(root)
        for a, b in [
            ("Free download", "मुफ़्त डाउनलोड"),
            (">Hydrated Lime Brochure 2026<", ">हाइड्रेटेड लाइम ब्रोशर 2026<"),
            (">Hydroxyapatite Brochure 2026<", ">हाइड्रॉक्सीएपेटाइट ब्रोशर 2026<"),
            ("All 4 grades and specs, plant photos, packing, export loading and CoA format.",
             "चारों ग्रेड और उनकी स्पेसिफ़िकेशन, प्लांट की तस्वीरें, पैकिंग, लोडिंग और CoA का फ़ॉर्मेट। ब्रोशर अंग्रेज़ी में है।"),
            ("Micro and nano grades, full specification, how we make it, and how to start with a 250 g sample.",
             "माइक्रो और नैनो ग्रेड, पूरी स्पेसिफ़िकेशन, बनाने का तरीका और 250 ग्राम के सैंपल से शुरुआत। ब्रोशर अंग्रेज़ी में है।"),
            ("Download brochure (PDF)", "ब्रोशर डाउनलोड करें (PDF)"), (">View online<", ">ऑनलाइन देखें<"),
            ("10 pages · PDF", "10 पेज · PDF"), ("6 pages · PDF", "6 पेज · PDF"),
            ('aria-label="View the Hydrated Lime Brochure online"', 'aria-label="हाइड्रेटेड लाइम ब्रोशर ऑनलाइन देखें"'),
            ('aria-label="View the Hydroxyapatite Brochure online"', 'aria-label="हाइड्रॉक्सीएपेटाइट ब्रोशर ऑनलाइन देखें"'),
            ('aria-label="Brochures"', 'aria-label="ब्रोशर"'),
        ]:
            s = s.replace(a, b)
        return s

    def engineer(root):
        img = B.photo("akshay")
        av = f'<img class="avatar" src="{img}" alt="Akshay Khadav" loading="lazy" width="84" height="84" style="padding:0">' if img else ""
        return f'''<div class="engineer">{av}<div>
<blockquote>“अपनी प्रक्रिया के बारे में बताइए। मैं सही ग्रेड सुझाऊँगा, और सैंपल भेजकर दिखाऊँगा कि वह काम करता है।”</blockquote>
<p><b>Akshay Khadav</b>, बी.टेक केमिकल इंजीनियरिंग, IIT बॉम्बे</p>
<p>आप हमें लिखते हैं तो सीधे मुझसे बात होती है: केमिस्ट्री, ग्रेड और डिस्पैच, किसी कॉल सेंटर से नहीं।</p>
<div class="btn-row"><a class="btn btn-red" href="{B.WHATSAPP}">अक्षय को व्हाट्सऐप करें</a><a class="btn btn-ghost-light" href="tel:{B.PHONE_TEL}">कॉल करें {B.PHONE_DISPLAY}</a></div>
</div></div>'''

    def crumbs(root, name):
        return f'<nav class="crumbs" aria-label="आप यहाँ हैं"><a href="{href(root, "hi")}">होम</a> / <span aria-current="page">{name}</span></nav>'

    # ---------- /hi/ home ----------
    root = "../"
    body = f'''
<section class="hero hero-video"><video class="hero-bg" muted loop playsinline preload="none" poster="{root}assets/media/hero-bg-poster.jpg" aria-hidden="true"><source src="{root}assets/media/hero-bg.webm" type="video/webm"><source src="{root}assets/media/hero-bg.mp4" type="video/mp4"></video><div class="wrap hero-grid">
<div class="hero-copy">
<p class="eyebrow-plain">हाइड्रेटेड लाइम · जोधपुर, राजस्थान</p>
<h1>आपकी ज़रूरत के ग्रेड का हाइड्रेटेड लाइम</h1>
<p class="lede">80 से 92 % Ca(OH)<sub>2</sub> तक चार ग्रेड, जोधपुर के रणसीगांव में हमारे अपने प्लांट में बने। हर लॉट की जाँच हमारी प्लांट लैब में होती है और उसके साथ सर्टिफ़िकेट ऑफ़ एनालिसिस (CoA) आता है।</p>
<div class="btn-row"><a class="btn btn-solid" href="#quote">भाव पूछें</a><a class="btn btn-red" href="{B.brochure_href(root, 'lime')}" download>{lic("download")}ब्रोशर डाउनलोड करें</a></div>
</div>
<div class="hero-ladder">{ladder()}</div>
</div></section>
{B.marquee(["चार ग्रेड", "80 से 92 % Ca(OH)<sub>2</sub>", "हर लॉट की जाँच", "हर डिस्पैच के साथ CoA", "जोधपुर, राजस्थान में निर्मित", "पहले सैंपल, फिर ऑर्डर"], "lg", speed=55)}

{motion(root)}

<section class="broch-band" id="brochure"><div class="wrap">
{brochures(root)}
</div></section>

<section><div class="wrap">{stats()}</div></section>

<section class="section section-tint" id="quote"><div class="wrap">
{quote(root)}
</div></section>

<section class="section"><div class="wrap split">
<div class="prose">
<h2>हमारा अपना प्लांट, एक इंजीनियर की देखरेख में</h2>
<p>Calvara Labs &amp; Minerals जोधपुर की चूना पट्टी में बसे रणसीगांव में अपने प्लांट पर हाइड्रेटेड लाइम बनाती है। चूना पत्थर, भट्टी और लैब जाँच हमारा रोज़ का काम है।</p>
<p>हर ग्रेड की स्पेसिफ़िकेशन तय है। पहले आप सैंपल जाँचते हैं, फिर हम उसी स्वीकृत सैंपल के अनुसार सप्लाई करते हैं।</p>
<ul><li><b>भट्टी का अनुभव।</b> अपनी भट्टी चलाने से हम चूना पत्थर, पकाई और कैल्शियम केमिस्ट्री को अच्छी तरह जानते हैं।</li><li><b>जाँच, अंदाज़ा नहीं।</b> हर लॉट प्लांट लैब में जाँचा जाता है और CoA के साथ भेजा जाता है।</li><li><b>पहले सैंपल।</b> नियमित ऑर्डर से पहले ग्रेड को अपनी प्रक्रिया में आज़माइए।</li></ul>
</div>
{engineer(root)}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>एक पाउडर, नौ उद्योग</h2><p class="lede">लाल रंग वाले ग्रेड से शुरुआत करें। सही ग्रेड इस पर निर्भर है कि आपकी प्रक्रिया कितनी सिलिका और अघुलनशील पदार्थ सह सकती है।</p></div>
{industries()}
</div></section>
{B.marquee([IND_HI[n][0] for n, _, _ in B.INDUSTRIES], "sm", reverse=True, speed=45)}

<section class="section"><div class="wrap">
<div class="section-head"><h2>ख़रीदारों के आम सवाल</h2></div>
{faq()}
</div></section>

{cta(root)}'''
    hpage("hi", root, "hi", "", "हाइड्रेटेड लाइम निर्माता, जोधपुर | ग्रेड 80–92 | Calvara Labs",
          "जोधपुर के अपने प्लांट में बना हाइड्रेटेड लाइम, चार ग्रेड: 80 से 92 % Ca(OH)2। सिलिका 1.06 % से, 98.5 % तक 200 मेश से पार, हर लॉट के साथ CoA।", body)

    # ---------- /hi/hydrated-lime/ ----------
    root = "../../"
    labels = [("Ca(OH)<sub>2</sub> मात्रा, न्यूनतम", 2), ("समतुल्य CaO (गणना से)", 3), ("नमी, अधिकतम", 4),
              ("एसिड अघुलनशील (सिलिका), अधिकतम", 5), ("200 मेश (75 µm) से पार, न्यूनतम", 6)]
    head = "".join(f'<th scope="col"><span class="gn">{g[0]}</span>ग्रेड</th>' for g in B.GRADES)
    rows = "".join(f'<tr><th scope="row">{lab}</th>' + "".join(f'<td class="num">{g[i]}</td>' for g in B.GRADES) + "</tr>" for lab, i in labels)
    table = f'<div class="table-box"><table class="spec-wide"><caption>ग्रेड के अनुसार सामान्य स्पेसिफ़िकेशन</caption><thead><tr><th scope="col">पैरामीटर</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
    bags = "".join(f'<li><b>{k} किलो</b><span>लाइनर वाला लैमिनेटेड बैग</span></li>' for k in (25, 30, 35, 40))
    bags = f'<ul class="bags">{bags}<li class="jumbo"><b>पैलेट</b><span>पैलेट पर या बिना पैलेट</span></li></ul>'
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "हाइड्रेटेड लाइम")}
<h1>हाइड्रेटेड लाइम के चार ग्रेड</h1>
<p class="lede">कैल्शियम हाइड्रॉक्साइड, Ca(OH)<sub>2</sub>। जोधपुर, राजस्थान की चूना पट्टी से बना महीन, सूखा और उच्च शुद्धता वाला पाउडर। हर लॉट की जाँच होती है, उस पर लेबल लगता है और ग्रेड आपकी ज़रूरत के अनुसार बनता है।</p>
<div class="btn-row"><a class="btn btn-red" href="{B.brochure_href(root, 'lime')}" download>{lic("download")}ब्रोशर डाउनलोड करें (PDF)</a><a class="btn btn-line" href="#spec">ग्रेड की तुलना करें</a></div>
</div></section>
{B.marquee([f"ग्रेड {g[0]}" for g in B.GRADES], "lg", speed=40)}

<section class="section" id="spec"><div class="wrap">
<div class="section-head"><h2>ग्रेड के अनुसार स्पेसिफ़िकेशन</h2><p class="lede">ग्रेड नंबर Ca(OH)<sub>2</sub> की न्यूनतम मात्रा है। ऊँचे ग्रेड में सिलिका कम और पाउडर ज़्यादा महीन होता है।</p></div>
{table}
<p class="swipe-hint">पूरी तालिका देखने के लिए स्वाइप करें।</p>
<p class="note" style="margin-top:14px;font-size:14px;color:var(--ink-soft)">ये सामान्य, संकेतात्मक मान हैं। अंतिम स्पेसिफ़िकेशन स्वीकृत सैंपल और हर लॉट के CoA से तय होती है।</p>
</div></section>

<section class="section section-tint" id="quote"><div class="wrap">
{quote(root)}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>उद्योग के अनुसार ग्रेड चुनें</h2><p class="lede">लाल रंग वाले ग्रेड से शुरुआत करें।</p></div>
{industries()}
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>पैकिंग आपकी पसंद की</h2><p class="lede">सील बंद, लैमिनेटेड बैग, अंदर लाइनर के साथ, ताकि आपके प्लांट तक चूना सूखा रहे।</p></div>
{bags}
</div></section>

<section class="section"><div class="wrap">
<div class="section-head"><h2>भंडारण और सुरक्षित इस्तेमाल</h2></div>
<div class="facts facts-3">
<div><b>सूखा और सील बंद रखें</b><p>ठंडी, सूखी जगह पर, मूल सील बंद बैग में रखें। दीवार से हटाकर पैलेट पर चट्टा लगाएँ।</p></div>
<div><b>छह महीने के भीतर इस्तेमाल करें</b><p>चूना हवा से धीरे-धीरे CO<sub>2</sub> और नमी सोखता है, जिससे असरदार ग्रेड घटता है।</p></div>
<div><b>सावधानी से संभालें</b><p>क्षारीय पदार्थ: त्वचा, आँख और साँस में जलन कर सकता है। दस्ताने, चश्मा और डस्ट मास्क पहनें। संपर्क होने पर खूब पानी से धोएँ।</p></div>
</div>
</div></section>

<section class="section section-tint"><div class="wrap">
<div class="section-head"><h2>ख़रीदारों के आम सवाल</h2></div>
{faq()}
</div></section>

{cta(root, "हाइड्रेटेड लाइम का भाव पाएँ", "ग्रेड, महीने की मात्रा और डिलीवरी का शहर बताइए। जवाब सीधे हमारे इंजीनियर से आएगा।")}'''
    hpage("hi/hydrated-lime", root, "hi/hydrated-lime", "hydrated-lime/", "हाइड्रेटेड लाइम ग्रेड 80–92 % | स्पेसिफ़िकेशन | Calvara Labs, जोधपुर",
          "हाइड्रेटेड लाइम के चार ग्रेड: Ca(OH)2 80–92 %, सिलिका 1.06–8 %, नमी 0.8–2.0 %, 90–98.5 % तक 200 मेश से पार। 25 से 40 किलो के बैग, हर लॉट के साथ CoA।", body)

    # ---------- /hi/contact/ ----------
    grade_opts = "".join(f"<option>ग्रेड {g[0]}</option>" for g in B.GRADES)
    auto = ("Calvara Labs & Minerals से संपर्क करने के लिए धन्यवाद। हमारे केमिकल इंजीनियर Akshay Khadav को आपकी पूछताछ मिल गई है "
            "और वे भाव, स्पेसिफ़िकेशन और डिलीवरी समय के साथ जल्द जवाब देंगे, अक्सर उसी दिन।\n\n"
            "तब तक हमारे ब्रोशर देखें (अंग्रेज़ी में):\n"
            "हाइड्रेटेड लाइम: https://calvaralabs.com/brochures/Calvara-Hydrated-Lime-Brochure-2026.pdf\n"
            "हाइड्रॉक्सीएपेटाइट: https://calvaralabs.com/brochures/Calvara-Hydroxyapatite-Brochure-2026.pdf\n\n"
            "जल्दी जवाब के लिए व्हाट्सऐप करें: +91 98927 27068\n\n"
            "Calvara Labs & Minerals, जोधपुर, राजस्थान · calvaralabs.com")
    body = f'''
<section class="page-head"><div class="wrap">
{crumbs(root, "संपर्क")}
<div class="prose" style="gap:14px;max-width:760px">
<h1>चूने की बात करें</h1>
<p class="lede">सैंपल, स्पेसिफ़िकेशन शीट या ग्रेड की सलाह माँगिए। जवाब सीधे एक इंजीनियर से मिलेगा।</p>
<div class="btn-row"><a class="btn btn-wa" href="{B.WHATSAPP}">व्हाट्सऐप {B.PHONE_DISPLAY}</a><a class="btn btn-line" href="{href(root, 'hi')}#quote">झटपट भाव</a></div>
</div>
</div></section>

<section class="section"><div class="wrap contact-grid">
<form class="form" action="https://formsubmit.co/{B.EMAIL}" method="POST">
<input type="hidden" name="_subject" value="नई पूछताछ (हिंदी पेज) calvaralabs.com">
<input type="hidden" name="_next" value="{B.SITE}/hi/thanks/">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_autoresponse" value="{auto}">
<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="field"><label for="f-name">आपका नाम</label><input id="f-name" name="name" type="text" autocomplete="name" required></div>
<div class="field"><label for="f-company">कंपनी</label><input id="f-company" name="company" type="text" autocomplete="organization" required></div>
<div class="field"><label for="f-phone">फ़ोन या व्हाट्सऐप</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required></div>
<div class="field"><label for="f-email">ईमेल</label><input id="f-email" name="email" type="email" inputmode="email" autocomplete="email"></div>
<div class="field"><label for="f-product">उत्पाद</label><select id="f-product" name="product"><option>हाइड्रेटेड लाइम</option><option>हाइड्रॉक्सीएपेटाइट</option><option>दोनों</option></select></div>
<div class="field"><label for="f-grade">ग्रेड</label><select id="f-grade" name="grade"><option>पता नहीं, आप सुझाइए</option>{grade_opts}</select></div>
<div class="field"><label for="f-request">मुझे चाहिए</label><select id="f-request" name="request"><option>सैंपल</option><option>भाव</option><option>स्पेसिफ़िकेशन शीट</option><option>ग्रेड की सलाह</option></select></div>
<div class="field"><label for="f-qty">महीने की मात्रा</label><input id="f-qty" name="quantity" type="text" placeholder="20 टन प्रति माह"></div>
<div class="field full"><label for="f-use">आपका उपयोग</label><input id="f-use" name="application" type="text" placeholder="पानी का ट्रीटमेंट, AAC ब्लॉक"></div>
<div class="field full"><label for="f-where">डिलीवरी का शहर</label><input id="f-where" name="delivery" type="text" autocomplete="address-level2"></div>
<div class="field full"><label for="f-msg">और कुछ (वैकल्पिक)</label><textarea id="f-msg" name="message" rows="3"></textarea></div>
<div class="actions"><button class="btn btn-red" type="submit">पूछताछ भेजें</button><p>आपकी जानकारी केवल इस पूछताछ का जवाब देने के लिए इस्तेमाल होती है।</p></div>
</form>
<aside style="display:flex;flex-direction:column;gap:20px">
<div class="side-card dark">
<h2 style="font-size:22px">आपके इंजीनियर</h2>
<p><b style="color:#fff">Akshay Khadav</b><br>बी.टेक केमिकल इंजीनियरिंग, IIT बॉम्बे</p>
<div class="contact-line"><span>कॉल या व्हाट्सऐप</span><a href="tel:{B.PHONE_TEL}">{B.PHONE_DISPLAY}</a></div>
<div class="contact-line"><span>ईमेल</span><a href="mailto:{B.EMAIL}">{B.EMAIL}</a></div>
<div class="contact-line"><span>ऑफ़िस</span><p>{B.OFFICE}</p></div>
<div class="contact-line"><span>प्लांट</span><p>{B.WORKS}</p></div>
</div>
<div class="side-card light">
<h2 style="font-size:20px">हमसे माँगें</h2>
<ol><li>जिस ग्रेड को आप जाँचना चाहते हैं, उसका सैंपल</li><li>स्पेसिफ़िकेशन शीट और सर्टिफ़िकेट ऑफ़ एनालिसिस</li><li>आपकी प्रक्रिया के अनुसार ग्रेड की सलाह</li></ol>
</div>
</aside>
</div></section>'''
    hpage("hi/contact", root, "hi/contact", "contact/", "संपर्क करें | हाइड्रेटेड लाइम का भाव, जोधपुर | Calvara Labs",
          "हाइड्रेटेड लाइम का सैंपल, भाव या स्पेसिफ़िकेशन माँगें। जोधपुर, राजस्थान। कॉल या व्हाट्सऐप +91 98927 27068।", body)

    # ---------- /hi/thanks/ ----------
    body = f'''
<section class="page-head"><div class="wrap">
<div class="prose" style="gap:14px;max-width:760px">
<h1>धन्यवाद, आपकी पूछताछ मिल गई है</h1>
<p class="lede">अक्षय जल्द ही जवाब देंगे, अक्सर उसी दिन। जल्दी बात करनी हो तो व्हाट्सऐप करें।</p>
<div class="btn-row"><a class="btn btn-wa" href="{B.WHATSAPP}">व्हाट्सऐप {B.PHONE_DISPLAY}</a><a class="btn btn-line" href="{href(root, 'hi')}">होम पर लौटें</a></div>
</div></div></section>'''
    hpage("hi/thanks", root, "", "thanks/", "धन्यवाद | Calvara Labs &amp; Minerals", "आपकी पूछताछ मिल गई है।", body, noindex=True)

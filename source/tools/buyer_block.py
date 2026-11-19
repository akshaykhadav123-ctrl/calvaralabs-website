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
<fieldset><legend>Packing</legend><div class="qchips">{chips("pack", ["25 kg bags", "50 kg bags", "900 kg jumbo bags", "Other bag size"], "25 kg bags")}</div></fieldset>
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
     "25, 30, 40, 45 or 50 kg laminated bags with liner, PP or paper bags, your brand printed, or 900 kg jumbo bags.",
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

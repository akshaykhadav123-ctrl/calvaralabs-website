

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

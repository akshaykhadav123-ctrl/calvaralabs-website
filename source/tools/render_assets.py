import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve()   # src folder
font = (src/"assets/fonts/space-grotesk.woff2").as_uri()
plex = (src/"assets/fonts/plex-sans-500.woff2").as_uri()
FACE = f"@font-face{{font-family:SG;src:url('{font}')}}@font-face{{font-family:PX;src:url('{plex}')}}"
def tile(px, rx, fs, bar=True):
    b = '<div style="position:absolute;left:14%;right:14%;bottom:13%;height:5%;background:#7FD6C2;border-radius:99px"></div>' if bar else ''
    return f'''<div style="width:{px}px;height:{px}px;display:grid;place-items:center;background:transparent">
<div style="position:relative;height:{px}px;width:{px*100/112}px;background:#1F2A5A;border-radius:{rx}px;display:grid;place-items:center;color:#fff;font:700 {fs}px SG;letter-spacing:-0.03em">
<span style="margin-top:-{px*0.06}px">Ca</span>{b}</div></div>'''
jobs = {
 "favicon-32.png": (32, tile(32, 5, 19, bar=False)),
 "apple-touch-icon.png": (180, f'<div style="width:180px;height:180px;background:#1F2A5A;display:grid;place-items:center;color:#fff;font:700 96px SG;letter-spacing:-0.03em"><span style="margin-top:-8px">Ca</span></div>'),
 "assets/logo-512.png": (512, tile(512, 64, 270)),
}
og = f'''<div style="width:1200px;height:630px;background:#F4F5FA;display:flex;align-items:center;gap:64px;padding:0 90px;box-sizing:border-box;font-family:SG;color:#1F2A5A">
<div style="position:relative;flex:none;width:300px;height:336px;background:#1F2A5A;border-radius:30px;color:#fff">
<span style="position:absolute;left:34px;top:26px;font:500 28px SG">20</span>
<span style="position:absolute;left:0;right:0;top:92px;text-align:center;font:700 150px SG;letter-spacing:-0.03em;line-height:1">Ca</span>
<span style="position:absolute;left:42px;right:42px;bottom:66px;height:11px;background:#7FD6C2;border-radius:99px"></span>
<span style="position:absolute;left:0;right:0;bottom:24px;text-align:center;font:500 22px SG;letter-spacing:.08em">40.08</span></div>
<div style="display:flex;flex-direction:column;gap:22px">
<div style="font:700 92px SG;letter-spacing:-0.025em;line-height:.95">Calvara</div>
<div style="font:500 20px SG;letter-spacing:.36em">LABS &amp; MINERALS</div>
<div style="font:500 30px PX;line-height:1.3;color:#4A5378;max-width:620px;margin-top:18px">Hydrated lime and hydroxyapatite from our own lime plant near Jodhpur, India</div>
</div></div>'''
jobs["assets/og.png"] = ((1200, 630), og)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, (size, html) in jobs.items():
        w, h = size if isinstance(size, tuple) else (size, size)
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.set_content(f"<html><head><style>{FACE}html,body{{margin:0;background:transparent}}</style></head><body>{html}</body></html>")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        out = src / name
        pg.screenshot(path=str(out), omit_background=not name.endswith("og.png") and name!="apple-touch-icon.png")
        print("wrote", out)
    b.close()

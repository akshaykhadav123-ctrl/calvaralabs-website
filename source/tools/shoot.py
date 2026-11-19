import sys, threading, functools, http.server, pathlib
from playwright.sync_api import sync_playwright
root = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]).resolve(); out.mkdir(parents=True, exist_ok=True)
pages = sys.argv[3].split(",")
H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 8765), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
with sync_playwright() as p:
    b = p.chromium.launch()
    for vw, tag in [(1440, "d"), (390, "m")]:
        pg = b.new_page(viewport={"width": vw, "height": 900})
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("requestfailed", lambda r: errs.append("FAIL " + r.url))
        for path in pages:
            pg.goto(f"http://127.0.0.1:8765/{path}", wait_until="networkidle"); pg.evaluate("async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}window.scrollTo(0,0)}"); pg.wait_for_timeout(500)
            name = (path.strip("/").replace("/", "_") or "home") + f"_{tag}.png"
            pg.screenshot(path=str(out / name), full_page=True)
            sw = pg.evaluate("document.documentElement.scrollWidth")
            print(name, "scrollWidth", sw, "errors", errs); errs.clear()
    b.close()
srv.shutdown()

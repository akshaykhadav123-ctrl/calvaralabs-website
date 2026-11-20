import sys, subprocess, pathlib
from playwright.sync_api import sync_playwright
H=pathlib.Path('/home/claude/plantreel'); F='/home/claude/calvaralabs-website/source/src/assets/fonts/'
svg=(H/'process.svg').read_text()
html=f"""<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:Jost;src:url(file://{F}jost.woff2);font-weight:100 900}}
@font-face{{font-family:'IBM Plex Sans';src:url(file://{F}plex-sans-400.woff2);font-weight:400}}
html,body{{margin:0}} svg{{display:block;width:720px;height:900px}}</style></head><body>{svg}</body></html>"""
(H/'proc.html').write_text(html)
mode=sys.argv[1] if len(sys.argv)>1 else 'still'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':720,'height':900}, device_scale_factor=1)
    pg.goto((H/'proc.html').as_uri()); pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(300)
    pg.evaluate("document.querySelector('svg').pauseAnimations()")
    if mode=='still':
        for t in [0.3,2.1,4.7]:
            pg.evaluate(f"document.querySelector('svg').setCurrentTime({t})")
            pg.screenshot(path=f'/tmp/claude-0/-home-claude/6bb12349-a274-5797-990c-1635e2b4aece/scratchpad/proc_{t}.png')
    else:
        fps=int(sys.argv[2]); out=sys.argv[3]; dur=6.0; n=int(dur*fps)
        d=H/'procframes'; d.mkdir(exist_ok=True)
        for i in range(n):
            pg.evaluate(f"document.querySelector('svg').setCurrentTime({i/fps})")
            pg.screenshot(path=str(d/f'{i:04d}.png'))
        subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(fps),'-i',str(d/'%04d.png'),'-vf',
          'scale=480:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64[p];[b][p]paletteuse=dither=none:diff_mode=rectangle',out],check=True)
    b.close()

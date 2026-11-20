"""Render Calvara plant photo reels (4:5) to MP4, WebM, poster and GIF."""
import subprocess, sys, math, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = pathlib.Path(__file__).parent
SRC = HERE / "src"
OUT = HERE / "out"; OUT.mkdir(exist_ok=True)
W, H, FPS = 720, 900, 24
SCENE, FADE = 2.8, 0.55
NAVY, RED, WHITE = (19, 32, 46), (217, 52, 45), (255, 255, 255)

def jost(size, wght=600):
    f = ImageFont.truetype(str(HERE / "fonts/jost.ttf"), size)
    f.set_variation_by_axes([wght]); return f
PLEX = lambda s: ImageFont.truetype(str(HERE / "fonts/plex-sans-400.ttf"), s)
PLEXB = lambda s: ImageFont.truetype(str(HERE / "fonts/plex-sans-600.ttf"), s)

LOGO = Image.open("/home/claude/calvaralabs-website/source/src/brand/calvara-logo-2000.png").convert("RGBA")
LOGO = LOGO.crop(LOGO.getbbox())

REELS = {
 "plant-tour": {
   "label": "Inside our plant · Ransigaon, Jodhpur",
   "scenes": [
     ("p3_x32.jpeg", "Kiln", "Limestone burnt to quicklime (CaO)", (0.30, 0.55)),
     ("p3_x33.jpeg", "Raw material stock", "Quicklime stocked under cover", (0.55, 0.45)),
     ("p3_x34.jpeg", "Hydrators", "Slaked with measured water to Ca(OH)₂", (0.45, 0.5)),
     ("p3_x35.jpeg", "Classifier", "Fine powder separated from grit", (0.40, 0.5)),
     ("p3_x36.jpeg", "Small bag packing", "25, 30, 35 or 40 kg bags", (0.5, 0.5)),
     ("p3_x37.jpeg", "Jumbo-bag packing", "900 kg bags under a dust collector", (0.5, 0.5)),
     ("p8_x62.jpeg", "Plant lab", "Every lot tested, CoA with every dispatch", (0.6, 0.6)),
   ],
   "end": ("Four grades, 80–92 % Ca(OH)₂", "Free sample with its CoA"),
 },
 "packing-dispatch": {
   "label": "Packing & dispatch · Ransigaon, Jodhpur",
   "scenes": [
     ("p3_x36.jpeg", "25 to 40 kg bags", "Filled from hoppers, sealed and stacked", (0.5, 0.5)),
     ("p3_x37.jpeg", "900 kg jumbo bags", "Filled under a bag-filter dust collector", (0.5, 0.5)),
     ("p4_x41.jpeg", "Jumbo bags in stock", "Ready to load", (0.5, 0.6)),
     ("p4_x42.jpeg", "Bagged ready stock", "Stored under cover at the plant", (0.5, 0.55)),
   ],
   "end": ("Palletised or non-palletised", "CIF and CFR export quotes"),
 },
}

def ease(t): return t * t * (3 - 2 * t)

def ken_burns(img, t, focus, idx):
    """Crop a 4:5 window from img that slowly zooms (alternating in/out) and drifts toward focus."""
    iw, ih = img.size
    base = min(iw / W, ih / H)          # largest 4:5 window
    z0, z1 = (1.0, 1.12) if idx % 2 == 0 else (1.12, 1.0)
    z = z0 + (z1 - z0) * ease(t)
    cw, ch = W * base / z, H * base / z
    fx, fy = focus
    # drift: start slightly off-focus, end on focus
    sx = fx - 0.06 * (1 - t) * (1 if idx % 2 else -1)
    cx = min(max(sx * iw, cw / 2), iw - cw / 2)
    cy = min(max(fy * ih, ch / 2), ih - ch / 2)
    box = (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2)
    return img.resize((W, H), Image.LANCZOS, box=box)

def gradient():
    g = Image.new("L", (1, H))
    for y in range(H):
        a = max(0, (y - H * 0.52) / (H * 0.48)); g.putpixel((0, y), int(235 * a ** 1.3))
    top = Image.new("L", (1, H))
    for y in range(H):
        a = max(0, 1 - y / 150); top.putpixel((0, y), int(120 * a))
    m = Image.eval(Image.merge("L", [g]), lambda v: v)
    full = Image.new("RGBA", (W, H), NAVY + (0,))
    full.putalpha(g.resize((W, H)))
    t = Image.new("RGBA", (W, H), (0, 0, 0, 0)); t.putalpha(top.resize((W, H)))
    return Image.alpha_composite(t, full)
GRAD = gradient()

def logo_pill():
    lw = 190; l = LOGO.resize((lw, round(LOGO.height * lw / LOGO.width)), Image.LANCZOS)
    p = Image.new("RGBA", (lw + 32, l.height + 22), (0, 0, 0, 0))
    d = ImageDraw.Draw(p); d.rounded_rectangle((0, 0, p.width - 1, p.height - 1), 12, fill=WHITE + (245,))
    p.alpha_composite(l, (16, 11)); return p
PILL = logo_pill()

def caption(frame, n, total, title, text, label, appear):
    """Overlay step chip, title and text; appear in 0..1 slides text up."""
    d = ImageDraw.Draw(frame)
    off = int((1 - ease(min(1, appear))) * 26); alpha = int(255 * ease(min(1, appear)))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    y = H - 210 + off
    chip = f"{n}"
    ld.rounded_rectangle((44, y, 44 + 52, y + 52), 12, fill=RED + (alpha,))
    f = jost(30, 600); bw = ld.textlength(chip, font=f)
    ld.text((44 + 26 - bw / 2, y + 7), chip, font=f, fill=WHITE + (alpha,))
    ld.text((44 + 52 + 16, y + 8), f"of {total}", font=PLEX(20), fill=(200, 208, 216, alpha))
    ld.text((44, y + 66), title, font=jost(52, 600), fill=WHITE + (alpha,))
    ld.text((44, y + 134), text, font=PLEX(24), fill=(214, 221, 228, alpha))
    frame.alpha_composite(layer)

def progress(frame, i, frac, total):
    d = ImageDraw.Draw(frame); gap = 6; x0, x1, y = 44, W - 44, 30
    seg = (x1 - x0 - gap * (total - 1)) / total
    for k in range(total):
        a = x0 + k * (seg + gap)
        d.rounded_rectangle((a, y, a + seg, y + 5), 3, fill=(255, 255, 255, 90))
        fill = 1 if k < i else (frac if k == i else 0)
        if fill > 0: d.rounded_rectangle((a, y, a + seg * fill, y + 5), 3, fill=WHITE + (255,))

def end_card(lines, t):
    f = Image.new("RGBA", (W, H), (244, 245, 246, 255)); d = ImageDraw.Draw(f)
    a = ease(min(1, t / 0.6)); alpha = int(255 * a); off = int((1 - a) * 20)
    lw = 330; l = LOGO.resize((lw, round(LOGO.height * lw / LOGO.width)), Image.LANCZOS)
    la = l.copy(); la.putalpha(Image.eval(l.getchannel("A"), lambda v: v * a))
    f.alpha_composite(la, ((W - lw) // 2, 150 + off))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    def ctr(txt, y, font, col):
        ld.text(((W - ld.textlength(txt, font=font)) / 2, y + off), txt, font=font, fill=col + (alpha,))
    ctr(lines[0], 470, jost(40, 600), NAVY)
    ctr(lines[1], 528, PLEX(26), (74, 87, 100))
    bx0, bx1, by = 120, W - 120, 640
    ld.rounded_rectangle((bx0, by + off, bx1, by + 84 + off), 14, fill=RED + (alpha,))
    ctr("WhatsApp +91 98927 27068", by + 22, PLEXB(30), WHITE)
    ctr("calvaralabs.com", 760, jost(34, 500), NAVY)
    f.alpha_composite(layer); return f

def render(key, still=False):
    R = REELS[key]; scenes = R["scenes"]; n = len(scenes)
    imgs = [Image.open(SRC / s[0]).convert("RGB") for s in scenes]
    sf = int(SCENE * FPS); ff = int((0.2 if still else FADE) * FPS); endf = int(2.6 * FPS)
    def scene_frame(i, k):
        t = k / (sf + ff)
        fr = ken_burns(imgs[i], 0.5 if still else t, scenes[i][3], 0 if still else i).convert("RGBA")
        fr.alpha_composite(GRAD)
        caption(fr, i + 1, n, scenes[i][1], scenes[i][2], R["label"], k / (0.45 * FPS))
        return fr
    frames_total = n * sf + endf
    END = end_card(R["end"], 1.0)
    mp4 = OUT / (f"{key}-still.mp4" if still else f"{key}.mp4")
    ff_cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
              "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "27", "-preset", "slow", "-movflags", "+faststart", "-an", str(mp4)]
    p = subprocess.Popen(ff_cmd, stdin=subprocess.PIPE)
    poster = None
    for g in range(frames_total):
        i, k = divmod(g, sf)
        if i < n:
            fr = scene_frame(i, k)
            nxt = i + 1
            if k >= sf - ff:  # crossfade into next scene / end card
                b = ((k - (sf - ff)) / ff)
                other = scene_frame(nxt, k - sf + ff) if nxt < n else END
                fr = Image.blend(fr, other, ease(b))
            # progress drawn on top (not part of blend)
            fr.alpha_composite(PILL, (W - PILL.width - 36, 56)) if False else None
            progress(fr, i, k / sf, n)
            if g == int(sf * 0.6): poster = fr.copy()
        else:
            fr = END.copy()
        p.stdin.write(fr.convert("RGB").tobytes())
    p.stdin.close(); p.wait()
    if not still:
        poster.convert("RGB").save(OUT / f"{key}-poster.jpg", quality=82)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp4), "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "38", "-row-mt", "1", "-an", str(OUT / f"{key}.webm")], check=True)
        print(key, "video done"); return
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp4), "-vf",
                    "fps=10,scale=432:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=192[p];[b][p]paletteuse=dither=sierra2_4a:diff_mode=rectangle",
                    str(OUT / f"Calvara-{key}.gif")], check=True)
    print(key, "done")

for k in REELS:
    render(k); render(k, still=True)

#!/usr/bin/env python3
"""Render per-page 1200x630 social cards (og-*.png) into src/assets/.

Matches the house og.png: white ground, Calvara lockup left, page title plus a
wrapped two-line subtitle on the right, red base bar. Run from the repo root:
    python3 source/tools/make_og_cards.py
Only the house assets are used (logo-2000.png, jost/plex woff2), so cards stay
on-brand without any network fetch.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
W, H = 1200, 630
INK = "#13202E"
SOFT = "#4A5562"
RED = "#D9342D"

JOSS = SRC / "assets/fonts/jost.woff2"
PLEX = SRC / "assets/fonts/plex-sans-400.woff2"

# name -> (title, [subtitle lines]). Lines wrap to the right-column width.
CARDS = {
    "og-lime.png": ("Hydrated lime", ["Grades 80 to 92 % Ca(OH)2, from our own plant in Ransigaon, Jodhpur", "Every lot tested in our lab, with a Certificate of Analysis"]),
    "og-hap.png": ("Hydroxyapatite", ["Synthetic and animal-free, micro grade D50 3 to 8 µm", "250 g samples open, each with its Certificate of Analysis"]),
    "og-export.png": ("Prices & export", ["CIF, CFR, FOB or ex-works Jodhpur, palletised or not", "Container quantity, lead time and terms in one same-day reply"]),
    "og-about.png": ("About & quality", ["Our own kilns, hydrators, plant lab and covered storage", "Run by a chemical engineer; every lot ships with a CoA"]),
    "og-contact.png": ("Request a quote", ["Tell us your grade, quantity and port; you hear back", "from the engineer, usually within one working day"]),
    "og-documents.png": ("Documents", ["GST, IEC and MSME registrations, plus independent lab reports", "Each certificate links to the portal where it can be verified"]),
}

COL_X = 520          # right text column left edge
COL_W = 600          # right text column max width
LOCK_W = 300


def lockup(width):
    im = Image.open(SRC / "brand/calvara-logo-2000.png")
    x0, y0, x1, y1 = im.getchannel("A").getbbox()
    crop = im.crop((x0, y0, x1, y1))
    h = int(crop.height * width / crop.width)
    return crop.resize((width, h), Image.LANCZOS)


def wrap(text, font, maxw, draw):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = cur + (" " if cur else "") + w
        if draw.textlength(trial, font=font) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    f_title = ImageFont.truetype(str(JOSS), 60)
    f_sub = ImageFont.truetype(str(PLEX), 25)
    f_web = ImageFont.truetype(str(JOSS), 22)
    for name, (title, subs) in CARDS.items():
        canvas = Image.new("RGB", (W, H), "#FFFFFF")
        d = ImageDraw.Draw(canvas)
        d.rectangle([0, H - 14, W, H], fill=RED)                 # red base bar
        lk = lockup(LOCK_W)                                       # lockup, left, centred
        canvas.paste(lk, (72, (H - lk.height) // 2 - 24), lk)

        d.text((COL_X, 166), title, font=f_title, fill=INK)       # title
        d.rectangle([COL_X, 246, COL_X + 120, 250], fill=RED)     # rule
        y = 290
        for sub in subs:                                           # wrapped subtitle
            for line in wrap(sub, f_sub, COL_W, d):
                d.text((COL_X, y), line, font=f_sub, fill=SOFT)
                y += 36
            y += 12
        d.text((COL_X, H - 74), "calvaralabs.com", font=f_web, fill=INK)
        out = SRC / "assets" / name
        canvas.save(out, "PNG", optimize=True)
        print("wrote", out.name, canvas.size, out.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()

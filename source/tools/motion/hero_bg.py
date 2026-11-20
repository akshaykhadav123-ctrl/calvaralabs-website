"""Captionless 16:9 background loop from plant photos (slow pan/zoom + crossfades)."""
import subprocess, pathlib
from PIL import Image, ImageEnhance

HERE = pathlib.Path(__file__).parent
SRC, OUT = HERE / "src", HERE / "out"
W, H, FPS = 1280, 720, 24
SCENE, FADE = 4.2, 1.1
SCENES = [("p3_x32.jpeg", (0.35, 0.5)), ("p3_x34.jpeg", (0.5, 0.45)), ("p4_x41.jpeg", (0.5, 0.6)),
          ("p3_x33.jpeg", (0.5, 0.5)), ("p3_x35.jpeg", (0.45, 0.45)), ("p4_x42.jpeg", (0.5, 0.5))]

def ease(t): return t * t * (3 - 2 * t)

def prep(f):
    im = Image.open(SRC / f).convert("RGB")
    im = ImageEnhance.Color(im).enhance(0.75)
    return im

def frame(im, t, focus, idx):
    iw, ih = im.size
    base = min(iw / W, ih / H)
    z0, z1 = (1.04, 1.14) if idx % 2 == 0 else (1.14, 1.04)
    z = z0 + (z1 - z0) * t
    cw, ch = W * base / z, H * base / z
    dx = (t - 0.5) * 0.08 * (1 if idx % 2 else -1)
    cx = min(max((focus[0] + dx) * iw, cw / 2 + 0.5), iw - cw / 2 - 0.5)
    cy = min(max(focus[1] * ih, ch / 2 + 0.5), ih - ch / 2 - 0.5)
    return im.resize((W, H), Image.LANCZOS, box=(cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2))

imgs = [prep(f) for f, _ in SCENES]
n = len(SCENES); sf = int(SCENE * FPS); ff = int(FADE * FPS)
total = n * sf  # loop: the last scene fades into the first
mp4 = OUT / "hero-bg.mp4"
p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "30", "-preset", "slow", "-movflags", "+faststart", "-an", str(mp4)], stdin=subprocess.PIPE)
span = sf + ff
for g in range(total):
    i, k = divmod(g, sf)
    # scene i is shown from its start; it began fading in during the previous scene's last ff frames
    fr = frame(imgs[i], (k + ff) / span, SCENES[i][1], i)
    if k >= sf - ff:
        j = (i + 1) % n
        nxt = frame(imgs[j], (k - (sf - ff)) / span, SCENES[j][1], j)
        fr = Image.blend(fr, nxt, ease((k - (sf - ff)) / ff))
    if g == 0:
        fr.save(OUT / "hero-bg-poster.jpg", quality=72)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait()
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp4), "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "42", "-row-mt", "1", "-an", str(OUT / "hero-bg.webm")], check=True)
print("done")

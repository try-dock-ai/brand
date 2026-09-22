"""Print-style portrait treatments from a transparent cutout.

usage: python3 halftone.py <cutout.png> <out.png> --mode halftone|engrave [--cell 9] [--ink 2337FD]
       [--contrast 1.4] [--brightness 1.1] [--width 1400] [--angle 22] [--bottom 1.0]
"""
import argparse, math
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageEnhance, ImageFilter

p = argparse.ArgumentParser()
p.add_argument('src'); p.add_argument('out')
p.add_argument('--mode', default='halftone')
p.add_argument('--cell', type=int, default=9)
p.add_argument('--ink', default='2337FD')
p.add_argument('--contrast', type=float, default=1.4)
p.add_argument('--brightness', type=float, default=1.1)
p.add_argument('--width', type=int, default=1400)
p.add_argument('--angle', type=float, default=22)
p.add_argument('--bottom', type=float, default=1.0, help='keep this fraction of height (crop torso)')
p.add_argument('--fade', type=float, default=0.0, help='fade out the bottom this fraction')
a = p.parse_args()
ink = tuple(int(a.ink[i:i+2], 16) for i in (0, 2, 4))

src = Image.open(a.src).convert('RGBA')
src = src.crop((0, 0, src.width, int(src.height * a.bottom)))
scale = (a.width * 2) / src.width
src = src.resize((int(src.width * scale), int(src.height * scale)), Image.LANCZOS)
alpha = src.split()[3]
if a.fade > 0:
    W, H = alpha.size
    grad = Image.linear_gradient('L').resize((W, int(H * a.fade))).transpose(Image.FLIP_TOP_BOTTOM)
    full = Image.new('L', (W, H), 255); full.paste(grad, (0, H - grad.height))
    alpha = Image.fromarray((np.asarray(alpha).astype(float) * np.asarray(full).astype(float) / 255).astype('uint8'))
gray = ImageOps.grayscale(src)
gray = ImageEnhance.Contrast(gray).enhance(a.contrast)
gray = ImageEnhance.Brightness(gray).enhance(a.brightness)
W, H = gray.size
g = np.asarray(gray).astype(float) / 255.0
al = np.asarray(alpha).astype(float) / 255.0
out = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(out)

if a.mode == 'halftone':
    cell = a.cell * 2
    ca, sa = math.cos(math.radians(a.angle)), math.sin(math.radians(a.angle))
    diag = int(math.hypot(W, H))
    n = diag // cell + 2
    for i in range(-n, n):
        for j in range(-n, n):
            x = i * cell * ca - j * cell * sa + W / 2
            y = i * cell * sa + j * cell * ca + H / 2
            if x < -cell or y < -cell or x > W + cell or y > H + cell:
                continue
            xi, yi = int(min(max(x, 0), W - 1)), int(min(max(y, 0), H - 1))
            cov = al[yi, xi]
            if cov < 0.15:
                continue
            dark = (1.0 - g[yi, xi]) * cov
            r = cell * 0.66 * math.sqrt(dark)
            if r < 1.0:
                continue
            d.ellipse((x - r, y - r, x + r, y + r), fill=ink + (255,))
elif a.mode == 'engrave':
    sp = a.cell * 2
    gb = np.asarray(gray.filter(ImageFilter.GaussianBlur(1.2))).astype(float) / 255.0
    for y0 in range(0, H, sp):
        top, bot = [], []
        for x in range(0, W, 3):
            yy = y0 + 2.2 * math.sin(x / 40.0) + 1.2 * math.sin(x / 9.0)
            yi = int(min(max(yy, 0), H - 1))
            cov = al[yi, x]
            if cov < 0.15:
                if len(top) > 2:
                    d.polygon(top + bot[::-1], fill=ink + (255,))
                top, bot = [], []
                continue
            t = (1.0 - gb[yi, x]) * cov * sp * 0.95
            top.append((x, yy - t / 2)); bot.append((x, yy + t / 2))
        if len(top) > 2:
            d.polygon(top + bot[::-1], fill=ink + (255,))
out = out.resize((W // 2, H // 2), Image.LANCZOS)
out.save(a.out)
print(a.out, out.size)

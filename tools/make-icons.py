"""Draws the app icons into ../icons. Run: python3 tools/make-icons.py (needs Pillow)."""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent.parent / "icons"
BG = (21, 19, 16)          # dark brown page background
ACCENT = (255, 148, 51)    # the apps' orange (dark-mode shade)
CREAM = (240, 235, 227)


def draw(size: int) -> Image.Image:
    s = 1024  # draw large, then shrink for smooth edges
    img = Image.new("RGB", (s, s), BG)
    d = ImageDraw.Draw(img)
    cx = s // 2
    # A microphone, kept inside the safe zone iOS/Android won't crop
    d.rounded_rectangle([cx - 105, 215, cx + 105, 590], radius=105, fill=ACCENT)
    d.arc([cx - 195, 300, cx + 195, 690], start=0, end=180, fill=CREAM, width=34)
    d.line([cx, 690, cx, 790], fill=CREAM, width=34)
    d.rounded_rectangle([cx - 130, 775, cx + 130, 809], radius=17, fill=CREAM)
    for x in (cx - 195 + 17, cx + 195 - 17):  # round the ends of the cradle
        d.ellipse([x - 17, 478, x + 17, 512], fill=CREAM)
    return img.resize((size, size), Image.LANCZOS)


OUT.mkdir(exist_ok=True)
for name, size in [("icon-192.png", 192), ("icon-512.png", 512), ("apple-touch-icon.png", 180)]:
    draw(size).save(OUT / name, optimize=True)
    print("wrote", OUT / name)

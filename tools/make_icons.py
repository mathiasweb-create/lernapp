# Erzeugt die App-Icons (blaues Quadrat mit weißem §). Aufruf: python3 -I make_icons.py <zielordner>
import sys, os
from PIL import Image, ImageDraw, ImageFont
out = sys.argv[1]
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
for size in (180, 192, 512):
    im = Image.new("RGB", (size, size), (29, 78, 216))
    d = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, int(size * 0.62))
    bb = d.textbbox((0, 0), "§", font=font)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((size - w) / 2 - bb[0], (size - h) / 2 - bb[1]), "§", font=font, fill=(255, 255, 255))
    im.save(os.path.join(out, "icon-%d.png" % size))
print("ok")

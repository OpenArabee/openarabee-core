import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import cairosvg

NAVY = "#0A2A45"; GOLD = "#C29A52"
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-SemiBold.otf"

def text_path(txt, font, size, x0, base):
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); upm = font["head"].unitsPerEm
    hmtx = font["hmtx"]; s = size/upm; x = x0; out = []
    for ch in txt:
        g = cmap[ord(ch)]
        pen = SVGPathPen(gs)
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, x, base)))
        out.append(pen.getCommands()); x += hmtx[g][0]*s
    return " ".join(out), x

# --- mark (100 x 100 design box) ---
MARK = f'''
  <path d="M14 88 L41 14 L54 49" fill="none" stroke="{NAVY}" stroke-width="11"
        stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="8"/>
  <path d="M22 64 C 40 69, 60 69, 72 60 C 60 56, 55 44, 63 37 C 70 31, 83 31, 86 41"
        fill="none" stroke="{GOLD}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M72 60 C 80 63, 88 63, 95 61" fill="none" stroke="{GOLD}" stroke-width="9" stroke-linecap="round"/>
'''

def svg(w, h, body): 
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>'

font = TTFont(FONT)
p1, x = text_path("Open", font, 64, 130, 74)
p2, x2 = text_path("Arabee", font, 64, x, 74)
W = int(x2 + 20)
full = svg(W, 110, f'<g transform="translate(6,5)">{MARK}</g><path d="{p1}" fill="{NAVY}"/><path d="{p2}" fill="{GOLD}"/>')
icon = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 108 108" width="108" height="108">{MARK}</svg>'
open("logo.svg","w").write(full); open("icon.svg","w").write(icon)
cairosvg.svg2png(bytestring=full.encode(), write_to="preview_logo.png", output_width=W*3, background_color="white")
cairosvg.svg2png(bytestring=icon.encode(), write_to="preview_icon.png", output_width=300, background_color="white")
print(W)

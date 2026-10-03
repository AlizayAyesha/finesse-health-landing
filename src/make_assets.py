import sys, os, io, json
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from shapely import affinity
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
import cairosvg
from PIL import Image
from build_mark import build, compose, geom_to_d, NAVY, SAGE
from wordmark import text_path

OUT = '/workspace/finesse-health/assets'
os.makedirs(OUT, exist_ok=True)
WHITE = '#FFFFFF'; PAPER = '#F4F0EA'

def clean(g, min_area=40):
    polys = [g] if isinstance(g, Polygon) else list(g.geoms)
    return unary_union([p for p in polys if p.area >= min_area])

layers = [(c, clean(g)) for c, g in compose(build())]
# mark bounds in card coords
mb = unary_union([g for _, g in layers]).bounds  # (772,213,1276,657)

def mark_paths(dx, dy, scale=1.0, colors=None):
    out = []
    for c, g in layers:
        g2 = affinity.affine_transform(g, [scale, 0, 0, scale, dx, dy])
        col = (colors or {}).get(c, c)
        out.append((col, geom_to_d(g2, prec=2, simp=0.12 * scale)))
    return out

def svg_doc(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" width="{w:g}" height="{h:g}" role="img" aria-labelledby="t">'
            f'<title id="t">{title.replace('&','&amp;')}</title>{body}</svg>\n')

def paths_xml(ps): return ''.join(f'<path fill="{c}" d="{d}"/>' for c, d in ps)

# ---------- logo-mark.svg (tight + 12px padding)
P = 12
mw, mh = mb[2] - mb[0] + 2 * P, mb[3] - mb[1] + 2 * P
variants = {'': None, '-reversed': {NAVY: WHITE}, '-white': {NAVY: WHITE, SAGE: WHITE}, '-navy': {SAGE: NAVY}}
for suf, cmap in variants.items():
    body = paths_xml(mark_paths(-mb[0] + P, -mb[1] + P, 1, cmap))
    open(f'{OUT}/logo-mark{suf}.svg', 'w').write(svg_doc(mw, mh, body, 'Finesse Health & Co. caduceus mark'))

# ---------- logo-full.svg (mark + outlined Montserrat wordmark), card layout
X0, Y0 = 743 - 20, 213 - 20
fw, fh = (1305 + 20) - X0, (824 + 22) - Y0
d1, b1, _ = text_path('FINESSE', 580, 81, 744 - X0, 678 - Y0, target_width=1305 - 744)
d2, b2, _ = text_path('HEALTH & CO.', 600, 39, 815 - X0, 785 - Y0, target_width=1234 - 815)
for suf, cmap in variants.items():
    tcol = (cmap or {}).get(NAVY, NAVY)
    body = paths_xml(mark_paths(-X0, -Y0, 1, cmap)) + f'<path fill="{tcol}" d="{d1}"/><path fill="{tcol}" d="{d2}"/>'
    open(f'{OUT}/logo-full{suf}.svg', 'w').write(svg_doc(fw, fh, body, 'Finesse Health & Co.'))

# ---------- horizontal lockup for site header (mark left, wordmark right)
s = 0.24  # mark scale
hm_w, hm_h = (mb[2]-mb[0])*s, (mb[3]-mb[1])*s
gap = 22
d3, b3, _ = text_path('FINESSE', 580, 42, hm_w + gap, 32, target_width=None, tracking_em=0.1)
d4, b4, _ = text_path('HEALTH & CO.', 600, 17, hm_w + gap + 1, 32+42+16, target_width=None, tracking_em=0.17)
hw_w = max(b3[2], b4[2]) + 2; hw_h = max(hm_h, 32+42+16+17+12)
oy = (hw_h - hm_h) / 2
for suf, cmap in variants.items():
    tcol = (cmap or {}).get(NAVY, NAVY)
    body = paths_xml(mark_paths(-mb[0]*s, -mb[1]*s + oy, s, cmap)) + f'<path fill="{tcol}" d="{d3}"/><path fill="{tcol}" d="{d4}"/>'
    open(f'{OUT}/logo-horizontal{suf}.svg', 'w').write(svg_doc(hw_w, hw_h, body, 'Finesse Health & Co.'))

# ---------- PNG exports
def png(svgfile, outfile, width=None, height=None):
    cairosvg.svg2png(url=svgfile, write_to=outfile, output_width=width, output_height=height)
png(f'{OUT}/logo-full.svg', f'{OUT}/logo-full.png', width=2000)
png(f'{OUT}/logo-full-reversed.svg', f'{OUT}/logo-full-reversed.png', width=2000)
png(f'{OUT}/logo-full-white.svg', f'{OUT}/logo-full-white.png', width=2000)
png(f'{OUT}/logo-mark-reversed.svg', f'{OUT}/logo-mark-reversed.png', width=1024)
png(f'{OUT}/logo-horizontal.svg', f'{OUT}/logo-horizontal.png', width=1200)
# logo-mark.png 1024 square canvas, mark centered
def square_svg(size, pad_frac, bg=None, cmap=None, radius=0):
    side = max(mb[2]-mb[0], mb[3]-mb[1]) / (1 - 2*pad_frac)
    sc = size / side
    dx = (size - (mb[2]-mb[0])*sc)/2 - mb[0]*sc
    dy = (size - (mb[3]-mb[1])*sc)/2 - mb[1]*sc
    bgx = f'<rect width="{size}" height="{size}" rx="{radius}" fill="{bg}"/>' if bg else ''
    return svg_doc(size, size, bgx + paths_xml(mark_paths(dx, dy, sc, cmap)), 'Finesse Health & Co.')
open(f'{OUT}/logo-mark-square.svg','w').write(square_svg(1024, 0.04))
cairosvg.svg2png(bytestring=square_svg(1024, 0.04).encode(), write_to=f'{OUT}/logo-mark.png')
# icons
cairosvg.svg2png(bytestring=square_svg(512, 0.12, PAPER).encode(), write_to=f'{OUT}/icon-512.png')
cairosvg.svg2png(bytestring=square_svg(180, 0.12, PAPER).encode(), write_to=f'{OUT}/apple-touch-icon.png')
cairosvg.svg2png(bytestring=square_svg(192, 0.12, PAPER).encode(), write_to=f'{OUT}/icon-192.png')
fav = square_svg(64, 0.02)
open(f'{OUT}/favicon.svg','w').write(fav)
for sz in (16, 32, 48):
    cairosvg.svg2png(bytestring=square_svg(sz*8, 0.0, cmap=({SAGE: '#4E6A55'} if sz==16 else None)).encode(), write_to=f'/tmp/fav{sz}.png')
    Image.open(f'/tmp/fav{sz}.png').resize((sz, sz), Image.LANCZOS).save(f'{OUT}/favicon-{sz}.png')
ims = [Image.open(f'{OUT}/favicon-{s}.png').convert('RGBA') for s in (16, 32, 48)]
ims[2].save(f'{OUT}/favicon.ico', format='ICO', sizes=[(16,16),(32,32),(48,48)], append_images=ims[:2])
print('done', mb)

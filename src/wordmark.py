"""Outline Montserrat text to SVG path data (fontTools instancer + SVGPathPen)."""
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
VF='/usr/share/fonts/truetype/sand-box/google/Montserrat/Montserrat-VariableFont_wght.ttf'
_cache={}
def font(w):
    if w not in _cache:
        _cache[w]=instancer.instantiateVariableFont(TTFont(VF),{'wght':w})
    return _cache[w]

def text_path(text,weight,cap_px,x_left,cap_top,target_width=None,tracking_em=0.0):
    """Return (d, bbox). Scales so cap height == cap_px; tracking chosen to hit target_width (ink width)."""
    f=font(weight); gs=f.getGlyphSet(); cmap=f.getBestCmap()
    upm=f['head'].unitsPerEm; cap=f['OS/2'].sCapHeight
    s=cap_px/cap
    names=[cmap[ord(c)] for c in text]
    def layout(track):
        x=0; items=[]
        for n in names:
            items.append((n,x)); x+=gs[n].width+track*upm
        return items
    def ink(items):
        xs=[]
        for n,x in items:
            bp=BoundsPen(gs); gs[n].draw(bp)
            if bp.bounds: xs+= [x+bp.bounds[0],x+bp.bounds[2]]
        return min(xs),max(xs)
    track=tracking_em
    if target_width:
        lo,hi=-0.2,1.0
        for _ in range(60):
            mid=(lo+hi)/2; a,b=ink(layout(mid))
            if (b-a)*s<target_width: lo=mid
            else: hi=mid
        track=(lo+hi)/2
    items=layout(track); a,b=ink(items)
    pen=SVGPathPen(gs, ntos=lambda v: ('%.2f'%v).rstrip('0').rstrip('.'))
    for n,x in items:
        # font units y-up -> svg y-down; baseline at cap_top+cap_px
        tp=TransformPen(pen,(s,0,0,-s,x_left+(x-a)*s,cap_top+cap_px))
        gs[n].draw(tp)
    return pen.getCommands(), (x_left,cap_top,x_left+(b-a)*s,cap_top+cap_px), track

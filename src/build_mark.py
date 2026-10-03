"""Build the Finesse Health caduceus mark as pure filled vector paths.
Geometry is authored in source-card pixel coordinates (2048x1118 mockup) so the
render can be overlaid on the original for comparison. Left half is authored and
mirrored about x = CX for perfect symmetry."""
import math, re, json, sys
import numpy as np
from shapely.geometry import Polygon, Point, LineString, MultiPolygon
from shapely.ops import unary_union
from shapely import affinity

CX = 1024.0
NAVY = "#253350"
SAGE = "#90A28B"
GAP = 5.5

def bez(p0,p1,p2,p3,n=40):
    t=np.linspace(0,1,n)[:,None]
    return ((1-t)**3)*p0+3*((1-t)**2)*t*p1+3*(1-t)*t*t*p2+t**3*p3

def path_poly(d):
    toks=re.findall(r'[MLCZ]|-?\d+\.?\d*',d)
    pts=[];i=0;cur=None;cmd=None
    while i<len(toks):
        tk=toks[i]
        if tk in 'MLCZ': cmd=tk;i+=1
        if cmd=='Z': i+=0; break
        if cmd=='M' or cmd=='L':
            cur=np.array([float(toks[i]),float(toks[i+1])]);i+=2;pts.append(cur)
            if cmd=='M': cmd='L'
        elif cmd=='C':
            c=[np.array([float(toks[i+2*k]),float(toks[i+2*k+1])]) for k in range(3)];i+=6
            seg=bez(cur,c[0],c[1],c[2]);pts.extend(seg[1:]);cur=c[2]
    return Polygon(pts).buffer(0)

def mirror(g): return affinity.scale(g,xfact=-1,yfact=1,origin=(CX,0))

def catmull(points,samples=24):
    P=np.array(points,float)
    P=np.vstack([2*P[0]-P[1],P,2*P[-1]-P[-2]])
    out=[]
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        # centripetal-ish via uniform with tension 0.5
        for t in np.linspace(0,1,samples,endpoint=False):
            t2,t3=t*t,t*t*t
            out.append(0.5*((2*p1)+(-p0+p2)*t+(2*p0-5*p1+4*p2-p3)*t2+(-p0+3*p1-3*p2+p3)*t3))
    out.append(P[-2])
    return np.array(out)

def tube(center,widths):
    """variable-width stroke: union of hulls of consecutive discs"""
    w=np.interp(np.linspace(0,1,len(center)),np.linspace(0,1,len(widths)),widths)
    parts=[]
    for i in range(len(center)-1):
        a=Point(center[i]).buffer(w[i]/2,32); b=Point(center[i+1]).buffer(w[i+1]/2,32)
        parts.append(unary_union([a,b]).convex_hull)
    return unary_union(parts)

def chain(*runs,samples=14):
    """smooth each run with Catmull-Rom; joins between runs are sharp corners"""
    pts=[]
    for r in runs:
        c=catmull(r,samples) if len(r)>2 else np.array(r,float)
        pts.extend(c if not pts else c[1:] if np.allclose(c[0],pts[-1]) else c)
    return Polygon(pts).buffer(0)

def build(params=None):
    # ---- ball + tapered staff (measured from the card)
    ball=Point(CX,241).buffer(28,128)
    ys=np.linspace(277,640,30); hw=np.interp(ys,[277,420,645],[12.8,11.0,4.6])
    left=[(CX-h,y) for y,h in zip(ys,hw)]; right=[(CX+h,y) for y,h in zip(ys[::-1],hw[::-1])]
    staff=Polygon(left+[(CX,657)]+right).buffer(1.2,join_style=1).buffer(-1.2,join_style=1)
    # ---- wings (left authored from measured edge points, mirrored)
    wing_navy=chain(
        [(772,296),(812,284),(850,272),(890,254),(917,242),(940,236),(961,241),(970,254),(972,275),(978,290),(990,298),(1001,302)],
        [(1001,302),(1001,345)],
        [(1001,345),(993,339),(983,333),(968,329),(953,332),(940,339),(924,350),(905,357),(882,357),(864,352)],
        [(864,352),(884,343),(904,332),(922,320),(936,314),(951,314)],
        [(951,314),(946,307),(937,297),(925,286),(912,279)],
        [(912,279),(891,284),(866,296),(840,306),(815,309),(794,306),(772,296)])
    wing_sage=chain(
        [(808,327),(831,320),(855,312),(881,301),(900,293),(913,289),(927,293),(940,304)],
        [(940,304),(926,309),(912,316),(898,323),(880,331),(852,336),(828,334),(808,327)])
    wing_navy=unary_union([wing_navy,mirror(wing_navy)])
    wing_sage=unary_union([wing_sage,mirror(wing_sage)])
    # ---- serpents: navy authored from measured centreline; sage = mirror image
    navy_pts=[(986,369),(965,367),(946,374),(939,390),(945,405),(963,413),(990,420),(1022,433),
        (1052,444),(1070,453),(1076,466),(1070,482),(1050,496),(1028,505),(1006,516),(992,528),(989,540),
        (994,555),(1010,566),(1031,576),(1046,590),(1051,606),(1046,619),(1039,628)]
    navy_w=[26,26,25,24,23,22,22,23,24,25,25,25,24,23,22,21,20,20,19,17,15,13,11,8]
    navy=tube(catmull(navy_pts,16),navy_w)
    sage=mirror(navy)
    def band(y0,y1): return Polygon([(700,y0),(1350,y0),(1350,y1),(700,y1)])
    win=[band(405,462),band(478,532),band(548,598)]
    front_at=['sage','navy','sage']
    return dict(ball=ball,staff=staff,wing_navy=wing_navy,wing_sage=wing_sage,navy=navy,sage=sage,win=win,front_at=front_at)

def compose(G):
    """returns list of (color, geometry) after knock-out gaps"""
    staff=G['staff']; ball=G['ball']
    navy=G['navy']; sage=G['sage']
    # who is on top where: within crossing windows, front serpent on top; elsewhere no overlap
    navy_front=unary_union([navy.intersection(w) for w,f in zip(G['win'],G['front_at']) if f=='navy'])
    sage_front=unary_union([sage.intersection(w) for w,f in zip(G['win'],G['front_at']) if f=='sage'])
    sage_final=sage.difference(navy_front.buffer(GAP))
    navy_final=navy.difference(sage_front.buffer(GAP))
    snakes=unary_union([navy_final,sage_final])
    staff_final=staff.difference(snakes.buffer(GAP))
    wn=G['wing_navy'].difference(snakes.buffer(GAP)); ws=G['wing_sage']
    return [(NAVY,unary_union([ball,staff_final,wn,navy_final])),(SAGE,unary_union([ws,sage_final]))]

def geom_to_d(g,prec=2,simp=0.15):
    g=g.simplify(simp,preserve_topology=True)
    polys=[g] if isinstance(g,Polygon) else list(getattr(g,'geoms',[]))
    d=[]
    f=lambda v: ('%.*f'%(prec,v)).rstrip('0').rstrip('.')
    for p in polys:
        if p.is_empty or p.area<2: continue
        for ring in [p.exterior,*p.interiors]:
            c=list(ring.coords)[:-1]
            d.append('M'+' L'.join(f'{f(x)} {f(y)}' for x,y in c)+'Z')
    return ''.join(d)

if __name__=='__main__':
    G=build(); layers=compose(G)
    allg=unary_union([g for _,g in layers]); print(allg.bounds)
    json.dump({'layers':[(c,geom_to_d(g)) for c,g in layers],'bounds':allg.bounds},open(sys.argv[1] if len(sys.argv)>1 else 'work/mark.json','w'))

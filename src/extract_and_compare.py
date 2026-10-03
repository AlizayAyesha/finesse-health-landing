import numpy as np, io, cairosvg
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy import ndimage
A='/workspace/finesse-health/assets'
src=np.array(Image.open('/workspace/finesse-health/source-card.png').convert('RGB')).astype(float)
X0,Y0,X1,Y1=723,193,1325,846
c=src[Y0:Y1,X0:X1]
# local paper estimate: median of bright pixels via heavy blur of masked image
lum=c.mean(-1)
ink=lum<215
bg=c.copy()
for k in range(3):
    m=~ndimage.binary_dilation(ink,iterations=4)
    w=ndimage.gaussian_filter(m.astype(float),25)+1e-6
    bg=np.stack([ndimage.gaussian_filter(c[...,i]*m,25)/w for i in range(3)],-1)
NAVY=np.array([0x25,0x33,0x50],float); SAGE=np.array([0x90,0xA2,0x8B],float)
def frac(col):
    v=col[None,None,:]-bg; p=c-bg
    t=(p*v).sum(-1)/(v*v).sum(-1)
    resid=np.linalg.norm(p-t[...,None]*v,axis=-1)
    return np.clip(t,0,1),resid
tn,rn=frac(NAVY); ts,rs=frac(SAGE)
use_s=(rs<rn)&(ts>tn*0.9)
# sage pixels also project partially on navy line; choose by residual
alpha=np.where(use_s,ts,tn)
alpha=np.clip((alpha-0.12)/(0.85-0.12),0,1)
# remove specks
lab,n=ndimage.label(alpha>0.3); sizes=ndimage.sum(np.ones_like(alpha),lab,range(1,n+1))
keep=np.isin(lab,np.where(sizes>=30)[0]+1)
keep=ndimage.binary_dilation(keep,iterations=2)
alpha=alpha*keep
rgb=np.where(use_s[...,None],SAGE,NAVY)
out=np.dstack([rgb,alpha*255]).astype(np.uint8)
im=Image.fromarray(out,'RGBA')
im=im.crop(im.getbbox())
W=im.width*2
im.resize((W,int(im.height*2)),Image.LANCZOS).save(f'{A}/logo-extracted.png')
print('extracted',im.size)

# ---------- comparison: original crop | vector recreation | overlay
orig=Image.open('/workspace/finesse-health/source-card.png').convert('RGB').crop((X0,Y0,X1,Y1))
S=2; w,h=orig.size
orig2=orig.resize((w*S,h*S),Image.LANCZOS)
svg=open(f'{A}/logo-full.svg').read()
mine=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=w*S))).convert('RGBA')
mine=mine.crop((0,0,w*S,h*S))
paper=Image.new('RGBA',(w*S,h*S),(235,231,226,255)); paper.alpha_composite(mine)
g=orig2.convert('L').convert('RGBA')
red=Image.new('RGBA',mine.size,(214,40,40,0)); red.putalpha(mine.split()[3].point(lambda v:int(v*0.5)))
g.alpha_composite(red)
ext=Image.open(f'{A}/logo-extracted.png').convert('RGBA')
ext=ext.resize((int(ext.width*(h*S)/ext.height*0.94),int(h*S*0.94)),Image.LANCZOS)
chk=Image.new('RGBA',(w*S,h*S),(255,255,255,255)); d=ImageDraw.Draw(chk)
for yy in range(0,h*S,24):
    for xx in range(0,w*S,24):
        if (xx//24+yy//24)%2: d.rectangle([xx,yy,xx+23,yy+23],fill=(225,225,225,255))
chk.alpha_composite(ext,((w*S-ext.width)//2,(h*S-ext.height)//2))
pad=30; lab_h=110
canvas=Image.new('RGB',(4*w*S+5*pad,h*S+lab_h+pad),(255,255,255))
try: f=ImageFont.truetype('/usr/share/fonts/truetype/sand-box/google/Montserrat/Montserrat-VariableFont_wght.ttf',64)
except: f=None
dd=ImageDraw.Draw(canvas)
for i,(img,lab) in enumerate([(orig2,'Original (card crop)'),(paper.convert('RGB'),'Vector SVG recreation'),(g.convert('RGB'),'Overlay (SVG red on original)'),(chk.convert('RGB'),'Extracted raster (transparent)')]):
    x=pad+i*(w*S+pad); canvas.paste(img,(x,lab_h)); dd.text((x,24),lab,fill=(37,51,80),font=f)
canvas.save(f'{A}/compare-logo.png'); print(canvas.size)

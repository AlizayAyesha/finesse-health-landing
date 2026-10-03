import json, sys, io, cairosvg
from PIL import Image, ImageChops, ImageOps
d=json.load(open('work/mark.json'))
VB=(740,195,570,480)
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB[0]} {VB[1]} {VB[2]} {VB[3]}" width="{VB[2]*2}" height="{VB[3]*2}">'+''.join(f'<path fill="{c}" d="{p}"/>' for c,p in d['layers'])+'</svg>'
png=cairosvg.svg2png(bytestring=svg.encode())
mine=Image.open(io.BytesIO(png)).convert('RGBA')
orig=Image.open('source-card.png').convert('RGB').crop((VB[0]*2-1024*0+0,0,0,0)) if False else Image.open('source-card.png').convert('RGB')
o=orig.crop((VB[0],VB[1],VB[0]+VB[2],VB[1]+VB[3])).resize(mine.size)
paper=Image.new('RGBA',mine.size,(240,237,232,255)); paper.alpha_composite(mine)
over=o.copy().convert('RGBA'); 
m=mine.copy(); a=m.split()[3].point(lambda v:int(v*0.55)); m.putalpha(a)
# overlay: original greyscale + mine tinted red
og=ImageOps.grayscale(o).convert('RGBA')
red=Image.new('RGBA',mine.size,(220,30,30,0)); red.putalpha(mine.split()[3].point(lambda v:int(v*0.5)))
og.alpha_composite(red)
W,H=mine.size
out=Image.new('RGB',(W*3,H),(255,255,255))
out.paste(o,(0,0)); out.paste(paper.convert('RGB'),(W,0)); out.paste(og.convert('RGB'),(W*2,0))
s=float(sys.argv[2]) if len(sys.argv)>2 else 0.5
out=out.resize((int(out.width*s),int(out.height*s)),Image.LANCZOS)
out.save(sys.argv[1])

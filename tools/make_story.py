import sys, os
from PIL import Image, ImageDraw, ImageFont
out, main1, main2, sub = sys.argv[1:5]
logo = sys.argv[5] if len(sys.argv)>5 else os.path.join(os.path.dirname(__file__),"logo_black.png")
W,H=1080,1920
BG=(239,230,212); FG=(17,16,14); DIM=(110,100,85)
im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
f=lambda w,s: ImageFont.truetype(f"/usr/share/fonts/opentype/noto/NotoSansCJK-{w}.ttc",s,index=1)
serif=lambda s: ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",s,index=1)
d.rectangle([50,50,W-50,H-50],outline=FG,width=2)
def c(y,t,font,fill):
    w=d.textlength(t,font=font); d.text(((W-w)/2,y),t,font=font,fill=fill)
lg=Image.open(logo).convert("RGBA"); lg.thumbnail((480,130))
im.paste(lg,((W-lg.width)//2,300),lg)
c(780,main1,serif(84),FG)
c(895,main2,serif(84),FG)
c(1060,sub,f("Regular",36),DIM)
d.line([470,1340,610,1340],fill=FG,width=2)
c(1390,"OPEN 18:00 – 02:00",f("Regular",36),FG)
c(1455,"뚝섬로36길 63 1층 · 뚝섬한강공원 앞",f("Regular",32),DIM)
c(1520,"@barbuto_seoul",f("Regular",32),DIM)
im.save(out,quality=92)

import sys, os
from PIL import Image, ImageDraw, ImageFont
out, main1, main2, sub = sys.argv[1:5]
logo = sys.argv[5] if len(sys.argv)>5 else None
W=H=1080
BLACK=(239,230,212); CREAM=(17,16,14); DIM=(110,100,85)
im=Image.new("RGB",(W,H),BLACK); d=ImageDraw.Draw(im)
f=lambda w,s: ImageFont.truetype(f"/usr/share/fonts/opentype/noto/NotoSansCJK-{w}.ttc",s,index=1)
serif=lambda w,s: ImageFont.truetype(f"/usr/share/fonts/opentype/noto/NotoSerifCJK-{w}.ttc",s,index=1)
d.rectangle([40,40,W-40,H-40],outline=CREAM,width=2)
def c(y,t,font,fill):
    w=d.textlength(t,font=font); d.text(((W-w)/2,y),t,font=font,fill=fill)
if logo and os.path.exists(logo):
    lg=Image.open(logo).convert("RGBA"); lg.thumbnail((440,120))
    im.paste(lg,((W-lg.width)//2,165-lg.height//2),lg)
else:
    c(120,"BARBUTO",f("Black",64),CREAM)
c(400,main1,serif("Bold",76),CREAM)
c(500,main2,serif("Bold",76),CREAM)
c(650,sub,serif("Bold",32) if False else f("Regular",34),DIM)
d.line([470,800,610,800],fill=CREAM,width=2)
c(845,"OPEN 18:00 – 02:00",f("Regular",30),CREAM)
c(900,"뚝섬로36길 63 1층 · 뚝섬한강공원 앞",f("Regular",28),DIM)
c(955,"@barbuto_seoul",f("Regular",28),DIM)
im.save(out,quality=95)

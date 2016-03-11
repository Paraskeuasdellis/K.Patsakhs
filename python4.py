



from PIL import Image, ImageDraw
import random
im = Image.new("RGB", (1024, 1024), "white")
circlesx = []
circlesy = []
circlesr = []
i = 0
while (i<20):
    i+=1
    x = random.randrange(1,1025)
    y = random.randrange(1,1025)
    r = random.randrange(10,501)
    circlesx.append(x)
    circlesy.append(y)
    circlesr.append(r)
    draw = ImageDraw.Draw(im)
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,0), outline ='red')
l = 0
for count in range(0,20):
    z = circlesx[count]
    w = circlesy[count]
    r1 = circlesr[count]
    for f in range(count,20):
        e = circlesx[f]
        k = circlesy[f]
        r2 = circlesr[f]
        a1 = (((z-e)**2)+((w-k)**2))**0.5
        if a1<=(r1+r2):
            l+=1
print l
im.show()


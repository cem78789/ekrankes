import autopy
import time
import win32api, win32con
import Image
import operator
import aggdraw
import Image, ImageFont
import ImageDraw
def cek(no):
    autopy.bitmap.capture_screen().save(no)
def tikla():
    win32api.SetCursorPos((1529,1016))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,1529,1016,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,1529,1016,0,0)
def crop(dadi):
    img = Image.open(dadi)
    cut = img.crop((564, 187, 990, 1200))
    cut.save(dadi)
def sonlandirici(dadi,dk):
    img = Image.open(dadi).convert('1')
    pix = img.load()
    x,y = img.size
    x1 = 0
    y1 = 0
    bose = 0
    boscnt = 0
    bos = []
    while y1 < y:
        x1 = 0
        cnt = 0
        while x1 < x:
            if pix[x1,y1] != 255:
                cnt = cnt + 1
            x1 = x1 + 1
        if cnt == 0:
            if y1 - 1 == bose:
                bos.append(y1)
                boscnt = boscnt + 1
            else:
                boscnt = 0
                bos[:] = []
            if boscnt == dk:
                bitispix = bos[0]
                break
            bose = y1
        y1= y1 + 1
    try:
        #print bitispix
        im = Image.open(dadi)
        if dk == 50:
            cut = im.crop((0, 0, 426, bitispix))
        elif dk == 300:
            cut = im.crop((0, 0, 1200, bitispix))
        cut.save(dadi)
    except:
        print "hata"
def sayfalastir(dler,s,k):
    topl = Image.new("RGB", (1200,2300), "white")
    draw = aggdraw.Draw(topl)
    x1 = 0
    y1 = 0
    #print "tamam"
    for dadi in dler:
        k = k + 1
        #print x1
        #print dadi
        img = Image.open(dadi)
        font = ImageFont.truetype("verdana.ttf", 16)
        draw = ImageDraw.Draw(img)
        draw.text((0, 0),str(k),(0,0,0),font=font)
        x,y = img.size
        if y1 + y + 300> 2400 or dadi == dler[-1]:
            if x1 >600 or dadi == dler[-1]:
                print str(s)+". sayfa tamamlandi"
                topl.save('topl'+str(s)+'.png','png')
                dler[:dler.index(dadi)+1] = []
                return dler,k-2,'topl'+str(s)+'.png'
            y1 = 0
            x1 = 1800-1100
        topl.paste(img, (x1,y1,x1 + x,y1 + y))
        y1 = y + y1 + 300
##ana dongu
a = 1
dler = []
x = int(raw_input('Soru Sayisi : '))
time.sleep(2)
while a <= x:
    dadi = 'lysmat6-'+str(a)+".png"
    cek(dadi)
    crop(dadi)
    tikla()
    a = a + 1
    time.sleep(0.3)
    dler.append(dadi)
for dadi in dler:
   sonlandirici(dadi,100)
s = 1
k = 0
sonlannalar = []
while 1:
    try:
        donut,k,t = sayfalastir(dler,s,k)
        print donut
        dler = donut
        if donut == None:
            break
        k = k + 1
        s = s + 1
        sonlannalar.append(t)
    except:
        break
    
for s in sonlannalar:
    sonlandirici(s,300)
    

print "Tamamlandi. Ismail Cem Yilmaz 1-5-2015 1:40"
    

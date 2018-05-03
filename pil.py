# from PIL import Image, ImageDraw, ImageFont
# x = Image.new(RGB, (500,500), color='red' )
# x = Image.new(RGB, (500,500), color='253.235.120' )
# x = Image.new('RGB', (500,500), color='#090217')
# x.save('/home/red/PycharmProjects/python_belhard/picture.jpg')

# x = Image.open('/home/red/PycharmProjects/python_belhard/picture.jpg')
# draw = ImageDraw.Draw(x)
# # draw.line((0,0,x.size[0],x.size[1]), fill='white', width=15)
# draw.text((50,50),'ttttt', fill='yellow' )
# #, font=ImageFont.truetype('DroidSans-Bold.ttf',13))
# draw.ellipse([30,30,200,200], outline='#B7D2DC',fill='#B7D2DC')
#
# x.save('/home/red/PycharmProjects/python_belhard/picture.jpg')

from PIL import Image, ImageDraw, ImageFont
from random import randint
def f(path,name):

    af = (randint(0,255),randint(0,255),randint(0,255))
    print(af)
    x = Image.new('RGB', (700, 700), color=af)
    a1 = randint(4,100)
    a2 = (randint(0,255),randint(0,255),randint(0,255))
    a3 = (randint(0, 255), randint(0, 255), randint(0, 255))
    l = []
    for i in range(a1):
        z = randint(0,700)
        y = randint(0,700)
        l.append(z)
        l.append(y)
    draw = ImageDraw.Draw(x)
    draw.polygon(l, fill=a2, outline=a3)

    a4 = (randint(0, 255), randint(0, 255), randint(0, 255))
    x2 = randint(0, 350)
    y2 = randint(0, 350)
    draw.text((x2, y2), 'my_sing', fill=a4, font=ImageFont.truetype('UbuntuMono-B.ttf',56))

    x.save(path + name)


# f('/home/red/PycharmProjects/python_belhard/', 'picture2.jpg')
from PIL import Image, ImageDraw, ImageFont
def f2(path):

    im = Image.open(path)
    color = im.convert('RGB')
    l = []
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            rgb = color.getpixel((i,j))
            l.append(rgb)
    s = set(l)
    litog = len(l)
    lc = []
    l2 = []
    for n in s:
        s1= l.count(n)
        lc.append(n)
        l2.append(round(s1/litog*100, 5))

        print("itog {} ; {} % ".format(n, round(s1/litog*100, 5)))

    l2_max = max(l2)
    l_in = l2.index(l2_max)
    print(lc[l_in])

    # print(len(l))
    # print(len(s))


f2('/home/red/PycharmProjects/python_belhard/123.jpg')

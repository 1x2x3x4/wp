from PIL import Image
import matplotlib.pyplot as plt
f = open('2.txt')
pp = []
while 1:
    c = f.readline()
    if c:
        s = eval(c.split('+')[1]+','+c.split('+')[2][:2])
        pp.append(s)
        print(s)
        # print(c)
    else:
        break

img = Image.new('RGB',(400,70),(255,255,255))
for i in pp:
    new = Image.new('RGB',(1,1),(0,0,0))
    img.paste(new,i)
plt.imshow(img)
plt.show()

# 第一阶段：读取偏移
with open('./misc47.png', 'rb') as f:
    bin_data = f.read()

point_list = []
for i in range(0, len(bin_data)):
    #print(hex(bin_data[i]))
    # union CTYPE type 中偏移固定位置在66 63 54 4C 后的 16 17 18 19 20 21 22 23 位
    # 先找到66 63 54 4C ，再根据固定的偏移找到uint32 x_offset 16 17 18 19 和uint32 y_offset 20 21 22 23
    if i+3<=len(bin_data) and hex(bin_data[i])=='0x66' and hex(bin_data[i+1])=='0x63' and hex(bin_data[i+2])=='0x54' and hex(bin_data[i+3])=='0x4c':
        # 两字节转为十进制，赌他不会用到三字节
        # 高位字节存在前，低位字节存在后，小端字节序
        l = int((bin_data[i+18] << 8) | bin_data[i+19])
        r = int((bin_data[i+22] << 8) | bin_data[i+23])
        point_list.append((l,r))

# 第二阶段：通过偏移画图
from PIL import Image
import matplotlib.pyplot as plt

img = Image.new('RGB',(400,70),(255,255,255))
for i in point_list:
    new = Image.new('RGB',(1,1),(0,0,0))
    img.paste(new,i)
plt.imshow(img)
plt.show()
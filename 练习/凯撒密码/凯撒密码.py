# python3
# -*- coding:utf-8 -*-

def Caesar_encode(plain,step):
    plain=str(plain)
    step=int(step)
    result=[]
    for i in range(len(plain)):
        result.append(chr(ord(plain[i])+step))
    return ''.join(result)

def Caesar_decode(cipher,step):
    cipher=str(cipher)
    step=int(step)
    result=[]
    for i in range(len(cipher)):
        result.append(chr(ord(cipher[i])-step))
    return ''.join(result)

cipher='bg[`sPejS>``gNBUQJ8N_F)FIVCS]'
print(len(cipher))
for i in range(1,26,1):
    print(i)
    print(Caesar_decode(cipher,i))










'''
cipher=Caesar_encode('abc',2)
print(cipher)

plain=Caesar_decode(cipher,2)
print(plain)
'''


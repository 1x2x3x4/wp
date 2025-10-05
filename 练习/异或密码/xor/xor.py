#As a freshman starting in 2024, you should know something about XOR, so this task is for you to sign in.

from pwn import xor
#The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths
from Crypto.Util.number import bytes_to_long

key = b'New_Star_CTF'
flag='flag{*******************}' #需要加密的明文模板

m1 = bytes_to_long(bytes(flag[:13], encoding='utf-8'))
m2 = flag[13:]

# 异或
c1 = m1 ^ bytes_to_long(key)
c2 = xor(key, m2)
print('c1=',c1)
print('c2=',c2)

'''
c1= 8091799978721254458294926060841
c2= b';:\x1c1<\x03>*\x10\x11u;'
'''

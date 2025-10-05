from Crypto.Util.number import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random

key = 208797759953288399620324890930572736628
key1 = long_to_bytes((key))
c = b'U\xcd\xf3\xb1 r\xa1\x8e\x88\x92Sf\x8a`Sk],\xa3(i\xcd\x11\xd0D\x1edd\x16[&\x92@^\xfc\xa9(\xee\xfd\xfb\x07\x7f:\x9b\x88\xfe{\xae'

my_aes=AES.new(key=key1,mode=AES.MODE_ECB)
print(my_aes.decrypt(pad(c, AES.block_size)))

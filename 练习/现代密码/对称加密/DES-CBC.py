from Crypto.Cipher import DES
import base64
# 不可用同一个对象进行加解密



key = b'gamelab@gamelab@'
iv = b'gamelab@gamelab@'
generator1 = DES.new(key,DES.MODE_CBC,iv)
result = generator1.encrypt(b'87650987')
print(result)
result_b64 = base64.b64encode(result)
print(result_b64)

de_generator1 = DES.new(key,DES.MODE_CBC,iv)
print(de_generator1.decrypt(base64.b64decode(result))) 



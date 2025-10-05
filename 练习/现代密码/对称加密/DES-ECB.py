from Crypto.Cipher import DES
import base64
# 可用同一个对象进行加解密

key=b'1234ABCD'
generator = DES.new(key,DES.MODE_ECB)

result_64 =  base64.b64encode(generator.encrypt(b'12345678'))
print(result_64) #打印输出

result =  generator.encrypt(b'12345678')
print(result) #打印输出


de_generator = DES.new(key,DES.MODE_ECB)

print(de_generator.decrypt(result))
print(de_generator.decrypt(base64.b64decode(result_64)))



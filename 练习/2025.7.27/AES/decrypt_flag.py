#AES-ECB模式需要
from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# 已知参数
key1 = 208797759953288399620324890930572736628
c = b'U\xcd\xf3\xb1 r\xa1\x8e\x88\x92Sf\x8a`Sk],\xa3(i\xcd\x11\xd0D\x1edd\x16[&\x92@^\xfc\xa9(\xee\xfd\xfb\x07\x7f:\x9b\x88\xfe{\xae'

# 1. 直接把整数转成 16 字节 key（无需 pad）
aes_key = long_to_bytes(key1)   # 16 字节

# 2. AES-ECB 解密
cipher = AES.new(aes_key, AES.MODE_ECB)
pt_padded = cipher.decrypt(c)

# 3. 去 PKCS#7 填充
pt = unpad(pt_padded, AES.block_size)

# 4. 打印结果
print(pt.decode())

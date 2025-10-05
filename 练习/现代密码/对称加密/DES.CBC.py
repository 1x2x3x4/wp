from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# 1. 填入题目给的 Key 和 IV（都是 16 字节）
key = b"gamelab@gamelab@"
iv  = b"gamelab@gamelab@"

# 2. 把题目里输出的那一串 Hex 密文完整复制到这里：
ct_hex = (
    "927fbe061d9a75737497f5a5215fe25e98c238cbb1d185d41432b76d681b9b735c5dc04f998b7acbefc275998a338616"
)

# 3. 解密并去掉填充
cipher = AES.new(key, AES.MODE_CBC, iv)
ct     = bytes.fromhex(ct_hex)
pt     = unpad(cipher.decrypt(ct), AES.block_size)

print(pt.decode("utf-8"))  # 打印出 flag



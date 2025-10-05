
from Crypto.Cipher import DES
import base64


# {"key": "BEL3iu2Gx7I=", "iv": "ygRMxA58vzs=", "ciphertext": "ZRYU/fFqtd891gdtDZjKw5d2G+VhVSi0i6EPB8810X4kWvhFa3/KpQ=="}
# DES+CBC

key = base64.b64decode("BEL3iu2Gx7I=")
print(key)
print(len(key))
iv = base64.b64decode("ygRMxA58vzs=")
print(iv)
print(len(iv))
ciphertext = base64.b64decode("ZRYU/fFqtd891gdtDZjKw5d2G+VhVSi0i6EPB8810X4kWvhFa3/KpQ==")
print(ciphertext)
print(len(ciphertext))
des = DES.new(key, DES.MODE_CBC, iv)
message = des.decrypt(ciphertext)
print(message)

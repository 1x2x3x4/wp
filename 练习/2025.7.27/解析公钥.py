from Crypto.PublicKey import RSA

pem = b"""-----BEGIN PUBLIC KEY-----
MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAMAzLFxkrkcYL2wch21CM2kQVFpY9+7+
/AvKr1rzQczdAgMBAAE=
-----END PUBLIC KEY-----"""

# 导入并解析
key = RSA.import_key(pem)

print("modulus (n) =", key.n) #n的结果为十进制（已自动转换）
print("public exponent (e) =", key.e) #十进制

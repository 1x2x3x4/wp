import itertools
from hashlib import sha256

# 已知条件
prefix = b'2100'
target_hash = '3a5137149f705e4da1bf6742e62c018e3f7a1784ceebcb0030656a2b42f50b6a'

def find_secret():
    # 后缀是 6 位数字，总共 10^6 种可能
    for suffix in itertools.product('0123456789', repeat=6):
        candidate = prefix + ''.join(suffix).encode()
        h = sha256(candidate).hexdigest()
        if h == target_hash:
            return candidate
    return None

if __name__ == '__main__':
    secret = find_secret()
    if secret:
        print(f"Found secrets: {secret!r}")
        print(f"Flag: moectf{{{secret.decode()}}}")
    else:
        print("No match found.")
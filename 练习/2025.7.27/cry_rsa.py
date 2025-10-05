from Crypto.Util.number import *
from gmpy2 import *
p=473398607161
q=4511491
e=19
phi = (p - 1) * (q - 1)
d   = inverse(e, phi)   
print(d+7)
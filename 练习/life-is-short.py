import base64
import hashlib

def abort(id):
    print('You failed test %d. Try again!' % id)
    exit(1)

print('Hello, Python!')
flag = input('Enter your flag: ')

if len(flag) != 38:
    abort(1)

if not flag.startswith('BaseCTF{'):
    abort(2)

if flag.find('Mp') != 10:
    abort(3)

if flag[-3:] * 8 != '3x}3x}3x}3x}3x}3x}3x}3x}':
    abort(4)

if ord(flag[-1]) != 125:
    abort(5)

if flag.count('_') // 2 != 2:
    abort(6)

if list(map(len, flag.split('_'))) != [14, 2, 6, 4, 8]:
    abort(7)

if flag[12:32:4] != 'lsT_n':
    abort(8)

if '😺'.join([c.upper() for c in flag[:9]]) != 'B😺A😺S😺E😺C😺T😺F😺{😺S':
    abort(9)

if not flag[-11].isnumeric() or int(flag[-11]) ** 5 != 1024:
    abort(10)

if base64.b64encode(flag[-7:-3].encode()) != b'MG1QbA==':
    abort(11)

if flag[::-7].encode().hex() != '7d4372733173':
    abort(12)

if set(flag[12::11]) != {'l', 'r'}:
    abort(13)

if flag[21:27].encode() != bytes([116, 51, 114, 95, 84, 104]):
    abort(14)

if sum(ord(c) * 2024_08_15 ** idx for idx, c in enumerate(flag[17:20])) != 41378751114180610:
    abort(15)

if not all([flag[0].isalpha(), flag[8].islower(), flag[13].isdigit()]):
    abort(16)

if '{whats} {up}'.format(whats=flag[13], up=flag[15]).replace('3', 'bro') != 'bro 1':
    abort(17)

if hashlib.sha1(flag.encode()).hexdigest() != 'e40075055f34f88993f47efb3429bd0e44a7f479':
    abort(18)

print('🎉 You are right!')
import this

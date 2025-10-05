from secrets import flag
flag='GCTF{xxxx}'

def xor_encrypto(m):
    c = []
    for i in range(len(flag) - 1):
        x = ord(flag[i]) ^ ord(flag[i + 1])
        c.append(x)
    return c

c=xor_encrypto(flag)

print('c={}'.format(c))

#c=[4, 23, 18, 61, 35, 55, 29, 45, 39, 55, 61, 45, 39, 23, 61, 13, 44, 67, 0, 0, 0, 0, 0, 111, 58, 37, 51, 10, 4]

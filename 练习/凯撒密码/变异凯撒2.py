# python3
# -*- coding:utf-8 -*-
str1 = 'ksjr{EcxvpdErSvcDgdgEzxqjql}'
str2 = ''
i = 5
for char in str1:
    if ord(char) >= 65 and ord(char) <= 90:
        if (ord(char)-i % 26) >= 65:
            temp = chr(ord(char)-i % 26)
        else:
            temp = chr(ord(char)-i % 26 - 65 + 90 +1)
    if ord(char) >= 97 and ord(char) <= 122:
        if (ord(char)-i % 26) >= 97:
            temp = chr(ord(char)-i % 26)
        else:
            temp = chr(ord(char)-i % 26 - 97 + 122 +1)
    if char == '{' or char == '}':
        temp = char
    str2 += temp
    i += 2

print(str2)

# -*- coding: utf-8 -*-
import hashlib

for a in range(32,127):
    for b in range(32,127):
        temp=chr(a)+chr(b)
        #print(temp)
        token = hashlib.md5(temp.encode("utf-8")).hexdigest()
        #print(token)
        if (token[1]>='0' and token[1]<='9'):
            if (token[14] >= '0' and token[14] <= '9'):
                if (token[17] >= '0' and token[17] <= '9'):
                    if (token[31] == '3'):
                        if (int(token[1]) == int(token[14]) and int(token[1]) == int(token[17])):
                            print(temp)
                            print(token)

import random
r = random.Random(372619038)   # 设置同样的种子
print(r.getrandbits(38))       # 相当于 mt_rand()

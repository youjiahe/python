#!/usr/bin/env python3
import hashlib
from sys import argv
import time
m=hashlib.md5()
with open(argv[1],'rb') as f:
    start = time.time()
    while True:
        data=f.read(4096)  #加上4096，会读得快一点
        if not data:
            end=time.time()
            break
        m.update(data)
print(m.hexdigest())
print(int(end-start))  #统计时间
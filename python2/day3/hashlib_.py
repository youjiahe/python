#!/usr/bin/env python3
import hashlib
# with open('/etc/passwd','rb') as f:
#     data=f.read()
# m=hashlib.md5(data)
# print(m.hexdigest())
m=hashlib.md5()
with open('/etc/passwd','rb') as f:
    while True:
        data=f.read(4096)
        if not data:
            break
        m.update(data)
print(m.hexdigest())
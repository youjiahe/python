#!/usr/bin/env python3
import hashlib
from sys import argv
def check_md5():
    m=hashlib.md5()
    with open(argv[1],'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()
if __name__ == '__main__':

    print(check_md5())
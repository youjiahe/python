#!/usr/bin/env python3
#string某块的ascii_letters函数:所有的大小写字母
#string某块的printable函数:所有的字符
from string import ascii_letters
from string import printable
from random import choice
import sys
def password(num=8):
    randp = ''
    for i in range(num):
        pass1=choice(printable)
        if pass1 in ['\n',' ','\r','\x0b','\x0c','\t']:
            continue
        randp = randp+pass1

    return randp

lo=int(sys.argv[1])
for i in range(10):
    print(password(lo))
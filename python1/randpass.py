#!/usr/bin/env python3
#string某块的ascii_letters函数:所有的大小写字母
#string某块的printable函数:所有的字符
#string某块的digits函数:所有的数字
from string import ascii_letters,digits
from string import printable
from random import choice
import sys

listp=ascii_letters+digits
def password(num=8):
    passwd=''
    for i in range(num):
        p0=choice(listp)
        passwd += p0
    return passwd
if sys.argv.__len__() ==2:
    for i in sys.argv[1]:
        if i not in digits:
            print('请输入一个数字')
            exit()
    else:
        lo = int(sys.argv[1])
        print(password(lo))
else:
    print(password())

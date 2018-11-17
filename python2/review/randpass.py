#!/usr/bin/env python3
from string import ascii_letters,digits
from random import random,choice,randint
from sys import argv
# def randpass1(num=8):
#     list=[choice(ascii_letters+digits) for i in range(num)]
#     pa=''
#     for i in list:
#         pa += i
#     return pa
def randpa(num=8):
    list=[choice(ascii_letters+digits) for i in range(num)]
    return ''.join(list)
if __name__ == '__main__':
    # print(randpass1())
    # print(randpass1(12))
    print(randpa())
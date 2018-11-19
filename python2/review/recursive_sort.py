#!/usr/bin/env python3
from random import randint,choice
def qsort(num):
    if len(num)<2:
        return num
    if type(num)=="<class 'list'>":
        middle=num[0]
        smaller=[l for l in num[1:] if l<=middle ]
        larger=[l for l in num[1:] if l>middle ]
    return qsort(smaller)+[middle]+qsort(larger)
if __name__ == '__main__':
    list=[randint(1,100) for i in range(10)]
    qsort(list)
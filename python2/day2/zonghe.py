#!/usr/bin/env python3
# from functools import partial
# def add(a,b,c,d,e):
#     return a+b+c+d+e
# newadd=partial(add,10,20,30,40)
# print(newadd(20))
#generator
import time
def num():
    a= 10 +20
    yield a
    yield 'hello world'
    b=20
    yield b
    c='he'+'llo'
    yield c
mg = num()
while True:
    try:
        o=mg.__next__()
        print(o,end='\r')
        time.sleep(0.4)
    except StopIteration:
        time.sleep(0.4)
        mg = num()
        continue




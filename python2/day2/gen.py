#!/usr/bin/env python3
def mygen():
    a= 10 + 20
    yield a
    yield 'hello world'
    b='ni'+' '+'hao'
    yield b
mg=mygen()
print(mg.__next__())
print(mg.__next__())
print(mg.__next__())
newmg=mygen()
for i in newmg:
    print(i)

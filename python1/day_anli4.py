#!/usr/bin/env python3
from day4_anli1 import get_context
def creen(st):
    print('+{}+'.format('*'*50))
    for i in st:
        print('+{:^50}+'.format(i))
    print('+{}+'.format('*'*50))

if __name__=='__main__':
    t=get_context()
    creen(t)
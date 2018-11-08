#!/usr/bin/env python3
nu = 1
while nu<=100:
    if nu<10:
        print(nu,end='  ')
    elif nu<100:
        print(nu,end=' ')
    else:
        print(nu)
    if nu%20==0:
        print('')
    nu += 1
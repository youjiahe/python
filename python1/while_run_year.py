#!/usr/bin/env python3
year = 1900
end = 2018
field = 1
while year <= end:
    if field%10==0:
        print('')
        field = 1
    if year%4==0 and year%100!=0:
        print(year,'年',sep='',end='')
        print('是闰年',end=',')
        field += 1
    elif year%400==0:
        print(year,'年',sep='',end='')
        print('是闰年',end=',')
        field += 1
    else:
        print('',end='')
    year += 1

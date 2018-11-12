#!/usr/bin/env python3
start = 9
end = 9
i = 1
j = 1
while i<=start:
    while j<=i:
        if i*j<10:
            print(i,'×',j,'=',i*j,sep='',end='  ')
            j += 1
        else:
            print(i, '×', j, '=', i * j, sep='', end=' ')
            j += 1
    print('')
    i += 1
    j=1
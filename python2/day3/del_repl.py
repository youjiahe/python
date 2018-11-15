#!/usr/bin/env python3
def del_re(list=[]):
    while list:
        for i in list:
            for j in list:
                if j==i:
                    list.pop(j)
li=list('hello')
lis=del_re(li)
print(lis)

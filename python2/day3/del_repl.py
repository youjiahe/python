#!/usr/bin/env python3
def del_re(list=[]):
    while list:
        for i in list:
            ind=list.index(i)
            for j in list[ind+1:-1]:
                if j==i:
                    list.pop(list.index(j))
li=list('hello')
lis=del_re(li)
print(lis)

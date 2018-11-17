#!/usr/bin/env python3
alist=[1,2,3,'you',[5,6,7],(1,2,3),'test',True]
print(alist[3])
#alist.pop(alist.index('test'))
alist.remove(True)
alist.extend([4,4,99])
alist.append([4,4,99])
#alist.sort() #报错
blist=list('google')
blist.sort()
print(alist)
blist.reverse()
blist.remove('o')
print(blist)


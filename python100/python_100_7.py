#!/usr/bin/env python3
alist=[10,20,30,'bob','alice',[1,2,3]]
alist[-1].append(4)
alist[-1].append(5)
alist[-1].append(6)
print(alist[-1])
print(11 not in alist)
print(alist[-1][2])
alist[-1].pop(-1)
print(alist[-1])
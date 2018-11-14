#!/usr/bin/env python3
import copy
a=[1,2,'you',['python','shell']]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
a.append('4')
a[3].append(3)
print(a,b,c,d,sep='\n')
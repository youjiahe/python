#!/usr/bin/env python3
from random import  randint,choice
list1=[randint(1,100) for i in range(10)]
print(list1)
print(list(filter(lambda x:x%2,list1)))
print(list(map(lambda x:x*100+31,list1)))
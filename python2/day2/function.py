#!/usr/bin/env python3
from random import  randint
# filter
nums=[randint(1,100) for i in range(10)]
print(nums)
print(list(filter(lambda x:x%2, nums)))
#map
print((list(map(lambda x:x*2+1,nums))))

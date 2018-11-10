#!/usr/bin/env python3
from random import randint
# l1=[]
# l2=[]
# ran_list=[ randint(1,1001) for i in range(20)]
# for i in ran_list:
#     if i>500:
#         l1.append(i)
#     elif i<=500:
#         l2.append(i)
# print(l1)
# print(len(l1))
# print(l2)
# print(len(l2))
num=[1,2,3,4,5,6,7,8,8]
length=len(num)
c=0
for i in range(9):
    for j in range(9):
        if num[i]!=num[j]:
            c += 1
            print(str(num[i])+str(num[j]),end=' ')
        else:
            continue
print('')
print(c)

#!/usr/bin/env python3
with open('test/1.txt') as s1:
    aset=set(s1)
with open('test/2.txt') as s2:
    bset=set(s2)
with open('test/1_2_diff.txt','w+') as s3:
    s3.writelines(aset-bset)
    cset=set(s3)

print('{:*^60}'.format('aset'))
print(aset)
print('{:*^60}'.format('bset'))
print(bset)
print('{:*^60}'.format('cset'))
with open('test/1_2_diff.txt') as s4:
    cset=set(s4)
print(cset)
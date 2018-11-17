#!/usr/bin/env python3
# 集合相当于是无值的字典，所以也用{}表示
myset = set('hello')
print("集合mysetd为: %s" % myset)
print("myset的长度是: %d " % len(myset))
print("myset的值有以下:",end=' ')
for i in myset:
    print(i,end=' ')
print(' ')
aset=set('abc')
bset=set('cde')
aset.add('d')
aset.update(['Z','z'])
bset.update(['a','Z'])
# a_a_b=aset & bset
# a_o_b=aset | bset
# a_s_b=aset - bset
a_a_b=aset.intersection(bset)
a_o_b=aset.union(bset)
a_s_b=aset.difference(bset)
print("aset： %s" % aset)
print("bset： %s" % bset)
print("aset 与 bset 的交集是 %s" % list(a_a_b) )
print("aset 与 bset 的并集是 %s" % a_o_b )
print("aset 与 bset 的差补是 %s" % a_s_b )
cset=set('abcde')
dset=set('abc')
print("cset是dset的超集吗？ %s " % cset.issuperset(dset))
print("dset是cset的子集吗？ %s " % dset.issubset(cset))


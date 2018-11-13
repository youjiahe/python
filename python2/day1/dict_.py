#!/usr/bin/env python3
# adict={'name':'bob','age':25}
# print('%(name)s,%(age)s' % adict)
# print(adict['name'])
# print(adict['age'])
# print('name' in adict)
# print('age' in adict)
# for i in adict:
# #    print('key:%s, value:%s' % (i,adict[i]) )
#     print('key:{}, value:{}'.format(i,adict[i]))
# adict['age']=26
# print(adict)

bdict={'name':'bbbbb','age':25,'email':'you@163.com'}
print(bdict.get('name'))
print(bdict.keys())
print(bdict.values())
print(bdict.items())
print(bdict.pop('email'))
print(bdict)
bdict.update({'name':'lisi'})
print(bdict)
bdict.update({'name':'zhangsan'})
print(bdict)
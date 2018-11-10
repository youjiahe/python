#！/usr/bin/env python3
strp='python'
slist=[1,2,3,[1,2,3],'python','thinkpad',True]
dict={'name':'you','age':24}

for strg in strp:
    print(strg,sep=' ',end=' ')
print('')
for l in slist:
    print(l,sep=' ',end=' ')
print('')

for k in dict:
    print(k)

for key in dict:
    print('%s:%s' % (key,dict[key]),sep=' ',end=' ')
print( '')
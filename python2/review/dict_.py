#!/usr/bin/env python3
dict1=dict(([1,"Adm+Eng+Serv"],[2,"Shell+Oper+Security"],[3,"DBA+NoSQL"],[4,"Cloud+Archetecture"],[5,"Python"]))
dict2=dict(([1,"牛犇"],[2,"丁明一"]))
dict3=dict(['1a'])
dict2[3]="评论家"
dict2[4]='李欣'
# dict2['pro']="王凯"
dict2.update({'pro':"王凯",'项目经理':"张威、紫琪"})
# tuple1=dict1.items()
tuple1=dict1.keys()
tuple2=dict1.values()
print(tuple1,list(tuple2)[0])
print(dict1)

for key in dict1:
    print('%s : %s' % (key,dict1[key]))

# print(dict1.get(2))
# print(dict2)
# print(dict3)
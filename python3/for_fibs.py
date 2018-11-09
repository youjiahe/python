#!/usr/bin/env python3
#斐波那契数列 ----- 最后一个数总是前两个书之和
#初始化列表 fibs=[0,1]
#fibs[0,1,1]
#fibs[0,1,1,2]
#fibs[0,1,1,2,3]
#使用append方法进行添加   列表名.append(列表值)

fibs=[0,1]
for i in range(10):  #追加10个元素
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)
#!/usr/bin/env python3
#斐波那契数列 ----- 最后一个数总是前两个书之和
#初始化列表 fibs=[0,1]
#fibs[0,1,1]
#fibs[0,1,1,2]
#fibs[0,1,1,2,3]
#使用append方法进行添加   列表名.append(列表值)
def fib(num=12):
    fibs=[0,1]
    for i in range(num-2):  #追加10个元素
        fibs.append(fibs[-2]+fibs[-1])
    print(fibs)
# if __name__=='__main__':
fib(4)
fib(15)
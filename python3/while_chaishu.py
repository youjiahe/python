#!/usr/bin/env python3
#导入随机数模块
import random
num=random.randint(1, 100)
guest = 0
count=1
while count<=5:
    guest=int(input('请输入一个数[1-100]：'))
    if guest==num:
        print('恭喜你猜对了,答案就是',num,sep='')
        break
    elif guest>num:
        print('猜大了',end=' ')
        print('还剩下',5-count,'次机会')
    elif guest<num:
        print('猜小了',end=' ')
        print('还剩下',5-count,'次机会')
    count += 1
else:
    print('你妹阿,五次机会都猜不对，可以回家了')
    print('彩票号码是',num)
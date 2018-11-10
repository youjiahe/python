#!/usr/bin/env python3
from random import randint
from string import digits
def intp(st):
    stat=0
    if st != '':
        for i in st:
            if i not in digits:
                stat=1
                break
            else:
                stat=0
    else:
        stat=2
    return stat

num=randint(1,100)
an=''
answer=-1
c=0
while answer!=num:
    while intp(an)!=0:
        an = input('请输入一个数字:')
    if intp(an)==0:
        answer=int(an)
        c += 1
    if answer==num:
        print('一共用了%d次机会' % (c))
        print('恭喜您喜提1分钱红包，2分钱流量券')
        break
    elif answer>num:
        print('猜大了')
    else:
        print('猜小了')
    an=''
else:
    print('五次机会用完，回去等通知')
#!/usr/bin/env python3
import random
quan = ['剪刀', '石头', '布']
com_win=[['剪刀','布'],['石头','剪刀'],['布','石头']]
you_win=[['剪刀','石头'],['石头','布'],['布','剪刀']]
c=0
y=0
you=-1
while c<2 and y<2:
    comput = random.randint(0, 2)
    while you not in [0,1,2]:
         you = input("请出拳[0：剪刀;1：石头;2：布]")
         if you not in ['0','1','2']:
             continue
         else:
             you=int(you)
    com_chu = quan[comput]
    you_chu = quan[you]
    zhan_ju = [com_chu, you_chu]

    if zhan_ju in com_win:
        c += 1
        print('总比分',c,':',y)
        print('电脑','你',sep='  ')
        print(com_chu,you_chu,sep='  ')
    elif zhan_ju in you_win:
        y += 1
        print('总比分',c,':',y)
        print('电脑','你',sep='  ')
        print(com_chu,you_chu,sep='  ')
    else:
        print('平局')
    you=-1

if c==2:
    print('-------------------------------')
    print('电脑硬了')
    print('总比分', c, ':', y)
    print('-------------------------------')
elif y==2:
    print('-------------------------------')
    print('你硬了')
    print('总比分', c, ':', y)
    print('-------------------------------')
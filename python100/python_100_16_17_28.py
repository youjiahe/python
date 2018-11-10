#!/usr/bin/env python3
import random
choice=['剪刀','石头','布']
com_win=[['石头','剪刀'],['剪刀','布'],['布','石头']]
player_win=[['石头','布'],['剪刀','石头'],['布','剪刀']]
c_counter=0;p_counter=0;you=-1;
nu=20
result=[]

while c_counter<2 and p_counter<2:
    com_choice=random.choice(choice)
    while you not in ['0','1','2']:
        you=input('请出拳【0：剪刀；1：石头；2：布】：')
    else:
        you_choice=choice[int(you)]
    result=[com_choice,you_choice]
    if result in com_win:
        c_counter += 1
        print('*'*nu)
        print('总比分# %d : %d' % (c_counter,p_counter))
        print('电脑:',com_choice,'玩家:',you_choice)
        print('*'*nu)
    elif result in player_win:
        p_counter += 1
        print('*'*nu)
        print('总比分# %d : %d' % (c_counter,p_counter))
        print('电脑:',com_choice,'玩家:',you_choice)
        print('*'*nu)
    else:
        print('*'*nu)
        print('平局')
        print('*'*nu)
    you=-1
if c_counter==2:
    print('*' * nu)
    print('电脑赢了')
    print('总比分# %d : %d' % (c_counter, p_counter))
elif p_counter==2:
    print('#' * nu)
    print('玩家赢了')
    print('总比分# %d : %d' % (c_counter, p_counter))
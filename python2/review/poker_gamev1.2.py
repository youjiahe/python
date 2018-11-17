#!/usr/bin/env python3
import os
from random import choice,randint
#A 2 3 4 5 6 7 8 9 10 J Q K
#♥ ♠ ♦ ♣
BT='♠'
RT='♥'
MH='♣'
FK='♦'
# print('\033[0m%s\033[0m' % BT,end=' ')
# print('\033[31m%s\033[0m' % RT,end=' ')
# print('\033[0m%s\033[0m' % MH,end=' ')
# print('\033[31m%s\033[0m' % FK)
# BT='\033[0m%s\033[0m' % BT
# RT='\033[31m%s\033[0m' % RT
# MH='\033[0m%s\033[0m' % MH
# FK='\033[31m%s\033[0m' % FK
# print(BT,RT,MH,FK)
# print("".join(pokerlist))


class Poker:
    def __init__(self,p_color=BT,p_brank='A'):
        self.p_color=p_color
        self.p_brank=p_brank

    def poker_produce(self):
        pok=''
        color_list = [BT, RT, MH, FK]
        brank_list = list('AKQJ98765432')
        brank_list.insert(4, '10')
        poker_dict={}
        n=52
        for i in range(13):
            for j in range(4):
                pokerlist =[color_list[j], brank_list[i]]
                poker = pok.join(pokerlist)
                poker_dict[n]=poker
                n -= 1
        return poker_dict

class PokerSend(Poker):
    def sendp(self,nums=3):
        n_old=0
        nu=0
        p_list=[]
        while True:
            poker_dict=self.poker_produce()
            n=randint(1,52)
            if n!=n_old:
                p=poker_dict[n]
                p_list.append(p)
                n_old=n
                nu +=1
            if nu>=nums:
                break
        return p_list

if __name__ == '__main__':
    poker=Poker()
    poker_nums=PokerSend()
    poker_dict=poker.poker_produce()
    print(poker_dict)
    players=['a','b','c','d']
    print(poker_dict.get(52))

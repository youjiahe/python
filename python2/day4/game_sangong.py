#!/usr/bin/env python3
import os
#A 2 3 4 5 6 7 8 9 10 J Q K
#♥ ♠ ♦ ♣
BT='♠'
RT='♥'
MH='♣'
FK='♦'
print('\033[0m%s\033[0m' % BT,end=' ')
print('\033[31m%s\033[0m' % RT,end=' ')
print('\033[0m%s\033[0m' % MH,end=' ')
print('\033[31m%s\033[0m' % FK)
BT='\033[0m%s\033[0m' % BT
RT='\033[31m%s\033[0m' % RT
MH='\033[0m%s\033[0m' % MH
FK='\033[31m%s\033[0m' % FK
print(BT,RT,MH,FK)

class Poker:
    def __init__(self,p_color=BT,p_brank='A'):
        self.p_color=p_color
        self.p_brank=p_brank

    @staticmethod
    def poker(self):
        pok=''
        pok.join(self.p_color,self.p_brank)
        return pok

if __name__ == '__main__':
    poker=Poker()
    print(poker.poker())
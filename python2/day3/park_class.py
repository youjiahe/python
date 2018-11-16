#!/usr/bin/env python3
import time
class Park:
    def __init__(self,man_num=1,child_num=1,free_price=100):
        self.man_num=man_num
        self.child_num=child_num
        self.free_price=free_price
    def calcl(self,h_ratio=1.2):
        if time.strftime('%a')=='Sat' or time.strftime('%a')=='Sun':
            return (self.man_num+0.5*self.child_num)*self.free_price*h_ratio
        else:
            return (self.man_num+0.5*self.child_num)*self.free_price
if __name__ == '__main__':
    famliy=Park(2,1)
    print(famliy.calcl())
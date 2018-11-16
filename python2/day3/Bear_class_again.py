#!/usr/bin/env python3
class Vendor:
    def __init__(self,em,ph):
        self.email=em
        self.phone=ph
class BearToy:
    def __init__(self,name,size,color,em,ph):
        self.name=name
        self.size=size
        self.color=color
        self.vendor=Vendor(em,ph)
    def sing(self):
        print('I am %s , my color is %s ' % (self.name,self.color))
class NewBear(BearToy):
    pass
if __name__ == '__main__':
    big=BearToy('BIGB','large','black','iiii@tedu.com','400500')
    print(big.color)
    big.sing()
    k=NewBear('mki','mi','pink','m@163.com','400600')
    print(k.color)
    print(big.vendor.email)
    print(big.vendor.phone)
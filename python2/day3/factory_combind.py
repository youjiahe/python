#!/usr/bin/env python3
class Vendor:
    def __init__(self,em,ph):
        self.email=em
        self.phone=ph
class BearToy:
    def __init__(self,name,size,color,em,ph):
        #实例初始化，自动调用
        self.name = name  #绑定属性到self，整个类中都可以用
        self.size = size
        self.color= color
        self.vendor=Vendor(em,ph)
    def sing(self):
        print('I am %s,my color is %s' % (self.name,self.color))
if __name__ == '__main__':
    big=BearToy('bearbig','Big','Black','cloud@tedu.com','4009876543')   #将会调用__init__方法
    print(big.vendor.email)
    print(big.vendor.email)
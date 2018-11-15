#!/usr/bin/env python3
class BearToy:
    def __init__(self,name,size,color):
        #实例初始化，自动调用
        self.name = name  #绑定属性到self，整个类中都可以用
        self.size = size
        self.color= color
    def sing(self):
        print('I am %s,my color is %s' % (self.name,self.color))
if __name__ == '__main__':
    big=BearToy('bearbig','Big','Black')   #将会调用__init__方法
    second=BearToy('bear2','Middle','Brown')
    print(big.size)
    print(big.color)
    big.sing()
    second.sing()
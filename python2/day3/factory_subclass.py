#!/usr/bin/env python3
class BearToy:
    def __init__(self,name,size,color):
        #实例初始化，自动调用
        self.name = name  #绑定属性到self，整个类中都可以用
        self.size = size
        self.color= color
    def sing(self):
        print('I am %s,my color is %s' % (self.name,self.color))

class NewBearToy(BearToy):
    def __init__(self,name,size,color,date):
        #BearToy.__init__(self,name,size,color)
        # self.name = name
        # self.size = size
        # self.color= color

        # 子类调用父类的__init__ 用super<Tab>;也可以用上面的繁琐方法
        super(NewBearToy, self).__init__(name,size,color)
        self.date=date

    def run(self):
        print('I can run!')

if __name__ == '__main__':
    big=NewBearToy('bearSmall','Small','Pink','2018-11-05')   #将会调用__init__方法
    big.sing() #子类继承父类的 sing 方法
    big.run()  #可以使用子类中的
    print(big.date)

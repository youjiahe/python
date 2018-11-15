#!/usr/bin/env python3
#多重继承
class A:
    def foo(self):
        print('你好！')
class B:
    def bar(self):
        print('How are you!')
class C(A,B):
    pass

if __name__ == '__main__':
    c=C()      #子类的实例继承了父类的属性
    c.foo()    #先从子类查找方法 foo() ，再到父类查找
    c.bar()    #如果foo()后面还有方法，则 从左往右，到本类，父类查找
#!/usr/bin/env python3
# a=10
# def foo():
#     print(a)
# def foobar():
#     a='hello'
#     print(a)
# def modify():
#     global a
#     a=999
#     print(a)
#
# print(a)
# foobar()
# print(a)
# modify()
# print(a)
x=10
def foo():
    print(x)
def bar():
    y=100
    print(y)
def foobar():
    x=999        # 局部变量将会遮盖住全局的x
    print(x)
def modify():
    global x     # 声明需要使用的 x 是全局变量
    x = 'hello'  # 将全局变量x重新赋值
# print(y)   # 错误，y是bar的局部变量，只能在bar函数中使用
print(x)
foo()
bar()
foobar()
print(x)
modify()
print(x)
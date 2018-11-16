#!/usr/bin/env python3
class SC:
    def hello(self):
        print('Hello World')

    @staticmethod
    def welcome():
        print('welcome back Rose!')

    @classmethod
    def greet(cls):
	    print('how are you!')


if __name__ == '__main__':
    SC.hello(11)  #需要实例，没有的话则报错
    SC.welcome()  #静态类，不需要
    SC.greet()    #类方法，不需要实例

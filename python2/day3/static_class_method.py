#!/usr/bin/env python3
class SC:
    def hello():
        print('Hello World')

    @staticmethod
    def welcome():
        print('welcome back Rose!')



if __name__ == '__main__':
    SC.hello()  #需要实例，没有的话则报错
    SC.welcome()  #静态类，不需要
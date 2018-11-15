#!/usr/bin/env python3
class SC:
    def hello(self):
        print('Hello World')

    @staticmethod
    def welcome(self):
        print('welcome back Rose!')



if __name__ == '__main__':
    SC.hello(15)  #需要实例，没有的话则报错
    SC.welcome()  #静态类，不需要
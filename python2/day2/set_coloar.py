#!/usr/bin/env python3
def set_color(func):
    def color():
        return "\033[31;1m%s\033[0m" % func()
    return color

def hello():
    return "Hello World!"

@set_color
def greet():
    return "How are you?"

if __name__ == '__main__':
    hh=set_color(hello)
    print(hh())
    print(greet)
    print(greet())

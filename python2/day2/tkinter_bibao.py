#!/usr/bin/env python3
import tkinter
from functools import partial

def hello(word):
    def say_hi():
        lb.config(text=word)
    return say_hi

root = tkinter.Tk()  #创建窗口
lb = tkinter.Label(root,text='Hello World!',font=['Arial',15])
mybutton=partial(tkinter.Button,root,fg='black',font=['Arial',12])
b1=mybutton(text='button1',command=hello('Hello Guangzhou'))
b2=mybutton(text='button2',command=hello('Hello Tedu'))
b3=mybutton(text='button3')
b4=mybutton(text='button4',command=quit)
for i in [lb,b1,b2,b3,b4]:
    i.pack()
root.mainloop()

#!/usr/bin/env python3
import tkinter
from functools import partial
root = tkinter.Tk()
lb = tkinter.Label(root,text='Hello World!')
mybutton=partial(tkinter.Button,root,fg='black')
b1=mybutton(text='button1')
b2=mybutton(text='button2')
b3=mybutton(text='button3')
b4=mybutton(text='button4')
for i in [lb,b1,b2,b3,b4]:
    i.pack()
root.mainloop()
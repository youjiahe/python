#!/usr/bin/env python3
import pickle as p
import os
import keyword
file='count.txt'
os.chdir('/root')
pwd=os.getcwd()
if not os.path.isfile(os.path.join(pwd,file)):
    alist = []
def mark():
    tup={}
    time='';pay='';comment='';c_type=''
    while not c_type:
        c_type=input('type:')
    while not time:
        time=input('time:')
    while not pay:
        pay=input('pay:')
    while not comment:
        comment=input('comment:')
    tup={'type':c_type,'time':time,'money':pay,'comment':comment}
    alist.append(tup)
    with open(file,'wb') as c1:
        p.dump(alist,c1)
def query():
    try :
        with open(file,'rb') as c2:
            marks=p.load(c2)
    except FileNotFoundError:
        print('No such file or directory:%s' % file )
    else:
        print(marks)
def show_menu():
    prompt='''[0] mark
[1] query
[2] quit
>'''
    cmds={'0':mark,'1':query}
    while True:
        choice = input(prompt)
        if choice not in '012':
            print('\033[31;1mInvalid commnad!\033[0m')
        elif not choice:
            continue
        elif choice=='2':
            exit()
        else:
            cmds[choice]()

if __name__=='__main__':
    show_menu()


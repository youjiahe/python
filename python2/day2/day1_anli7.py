#coding utf-8
#!/usr/bin/env python3
from datetime import datetime
import time
import pickle as p
import os
def save(fname):
    amount=int(input('acount:'))
    comment=input('comment:')
    ti=time.strftime('%F %R')
    with open(fname,'rb') as f:
        records=p.load(f)
        balance=records[-1][2] + amount
        save=[ti,0,amount,balance,comment]
        #['2018-11-14 15:20',0,1500,'salary']
        records.append(save)
    with open(fname,'wb') as f1:
        p.dump(records,f1)

def cost(fname):
    pay=int(input('pay:'))
    comment=input('comment:')
    ti=time.strftime('%F')
    with open(fname,'rb') as f:
        records=p.load(f)
        balance=records[-1][2] - pay
        save=[ti,pay,0,balance,comment]
        records.append(save)
    with open(fname,'wb') as f1:
        p.dump(records,f1)

def view(fname):
    with open(fname,'rb') as f:
        marks=p.load(f)
    print('%-16s%-8s%-8s%-12s%-30s' % ('date', 'cost', 'save', 'balance', 'comment'))
    for l in marks:
        print('%-16s%-8s%-8s%-12s%-30s' % tuple(l))
def show_menu():
    fname = 'fname.data'
    if not os.path.isfile(fname):
        init_data = [[datetime.now(), 0, 0, 10000, 'first count']]
        with open(fname, 'wb') as re:
            p.dump(init_data, re)
    cmds={'0': save,'1':cost,'2':view}
    prompt='''[0] save
[1] cost
[2] view
[3] quit
Please input your choice(0/1/2/3):'''
    while True:
        choice=input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid Input,Try again')
        if choice=='3':
            break
        cmds[choice](fname)

if __name__=='__main__':
    show_menu()
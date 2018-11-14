#!/usr/bin/env python3
import pickle as p
import time
import os
#账本
def save(fname):
    while True:
        try:
            acount=int(input('acount:'))
            comment=input('comment:')
        except :
            continue
        else:
            break
    ti=time.strftime('%F')

    with open(fname,'rb') as f:
        data_old=p.load(f)
    balance= data_old[-1][-2] + acount
    data=[ti,acount,0,balance,comment]
    data_old.append(data)

    with open(fname,'wb') as f:
        p.dump(data_old,f)

def cost(fname):
    while True:
        try:
            cos=int(input('cost:'))
            comment=input('comment:')
        except :
            continue
        else:
            break
    ti=time.strftime('%F')
    with open(fname,'rb') as f:
        data_old = p.load(f)
    balance = data_old[-1][-2] - cos
    data=[ti,0,cos,balance,comment]
    data_old.append(data)
    with open(fname,'wb') as f:
        p.dump(data_old,f)
def query(fname):
    with open(fname,'rb') as f:
        data=p.load(f)
    print('%-15s%-6s%-6s%-10s%-20s' % ('date','save','cost','balance','comment'))
    for i in data:
        print('%-15s%-6s%-6s%-10s%-20s' % tuple(i))
def show_menu():
    fname='record.data'
    if not os.path.isfile(fname):
        init_data=[]
        init_data.append(['2018-11-14',0,0,10000,'first comment'])
        with open(fname,'wb') as f:
            p.dump(init_data,f)
    cmds={'0':save,'1':cost,'2':query}
    prompt="""[0] save
[1] cost
[2] query
[3] quit
Please select your choice:"""
    while True:
        while True:
            try:
                command=input(prompt).strip()[0]
            except :
                continue
            else:
                break
        if command not in  '0123':
            print('Invalid input,Try again!')
            continue
        else:
            if command=='3':
                exit()
            else:
                cmds[command](fname)

if __name__ == '__main__':
    show_menu()
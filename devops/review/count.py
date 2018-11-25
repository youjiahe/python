#!/usr/bin/env python3
import getpass
import time
import os
import pickle as p
def init(fname):
    first_list=[['2018-11-12',0,0,10000,'first_comment']]
    if not os.path.isfile(fname):
        with open(fname,'wb') as  fobj:
            p.dump(first_list,fobj)
def save(fname):
    save = '' ; comment = ''
    while not save or not save.isdigit():
        try:
            save = input('save_money:').strip()
        except KeyboardInterrupt:
            print('bye')
            exit()
    while not comment:
        try:
            comment = input('comment:')
        except KeyboardInterrupt:
            print('bye')
            exit()
    ti=time.strftime('%F') 
    with open(fname,'rb') as fobj:
        data = p.load(fobj)
    with open(fname,'wb') as fobj:
        balance = data[-1][-2] + int(save)
        data.append([ti,save,0,balance,comment])
        p.dump(data,fobj)

def cost(fname):
    cost = '' ; comment = ''
    while not cost or not cost.isdigit():
        try : 
            cost = input('cost_money:').strip()
        except KeyboardInterrupt:
            print('bye')
            exit()
    while not comment:
        try : 
            comment = input('comment:')
        except KeyboardInterrupt:
            print('bye')
            exit()
    ti=time.strftime('%F') 
    with open(fname,'rb') as fobj:
        data = p.load(fobj)
    with open(fname,'wb') as fobj:
        balance = data[-1][-2] - int(cost)
        data.append([ti,0,cost,balance,comment])
        p.dump(data,fobj)

def query(fname):
    print('%-13s%-7s%-7s%-9s%-12s' % ('time','save','cost','balance','comment'))
    with open(fname,'rb') as fobj:
        data = p.load(fobj)
        for list in data:
            print('%-13s%-7s%-7s%-9s%-12s' % (list[0],list[1],list[2],list[3],list[4]))

def show_menu(fname):
    cmds={'1':save,'2':cost,'3':query}
    command=0
    prompt='''[1] save
[2] cost
[3] query
[4] quit
Please Input your request[1~4]:'''
    while True:
        while not command or command not in '1234':
            try:  
              command=input(prompt).strip()
            except KeyboardInterrupt:
                print('bye')
                exit()
        if command in ['4','quit']:
            print('Quit! bye')
            exit()
        else:
            cmds[command](fname)
        command = ''

if __name__ == '__main__':
    fname='count.txt'
    init(fname)
    show_menu(fname)

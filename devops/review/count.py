#!/usr/bin/env python3
import getpass
import time
def save(fname):
    count_list=[]
    save = '' ; content = ''
    while not save :
        save = input('save_money:')
    while not content:
        content = input('content:')
    ti=time.strftime('%F')
    balance =
    with open(fname,'wb') as fobj:


def cost(fname):
    pass
def show_menu(fname):
    cmds={'1':'save','2':'cost'}
    command=0
    prompt='''[1] save
[2] cost
[3] query
[4] quit
Please Input your request[1~4]:'''
    while not command or command not in '1234':
        command=input(prompt)
    if command=='4':
        print('Quit! bye')
        exit()
    else:
        cmds[command](fname)

if __name__ == '__main__':
    fname='count.txt'
    show_menu(fname)

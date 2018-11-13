#!/usr/bin/env python3
import getpass
dic={}
def login(dict={}):
    command=''
    name=input('username:')
    pasw=getpass.getpass()  #使用getpass模块，不会显示密码在终端

#    if name in dict.keys() and pasw==dict[name]:
    if dict.get(name)==pasw:
        print('\033[32;1mLogin Sucessfully!\033[0m')
    else:
        print('\033[31;1mLogin Failed!\033[0m UserName or PassWord invalid!')
def regit(dict={}):
    command=''
    name=input('username:')
    pasw=getpass.getpass()
    user_info={name:pasw}
    if name in dict.keys():
        print('User %s \033[31;1malready exists!\033[0m' % dict[name])
    else:
        while True:
            command=input('Please confirm {};[y/n]'.format(user_info))
            if command=='n':
                break
            elif command=='y':
                dict.update({name:pasw})
                break
def show_menu():
    choice='3'
    prompt="""[0] login
[1] regit
[2] quit\n"""
    while choice not in '012' or not choice:
        choice=input(prompt+'>')
        if choice=='2':
            exit()
        elif choice in '01':
            return choice
            break
        else:
            print('Invalid command!')
if __name__=='__main__':
    while True:
        choice=show_menu()
        cho={'0':login,'1':regit}
        if choice:
            cho[choice](dic)
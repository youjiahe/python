#!/usr/bin/env python3
import getpass
username=input('username: ')
password=getpass.getpass('password: ')
if username=='youjiahe' and password=='123456':
    print('Login\033[32;1m Sucessfully!\033[0m')
else:
    print('Login\033[31;1mIncorrect!!!\033[0m')

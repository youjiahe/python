#!/usr/bin/env python3
import randpass
import subprocess
from sys import argv
import os
import pickle as p
def useradd(username,password,fname):
    user_dict={}
    subprocess.call('useradd %s ' % username,shell=True)
    subprocess.call('echo %s | passwd --stdin %s' % (password,username),shell=True)

    if os.path.exists(fname):
        with open(fname,'rb') as fobj:
            user_dict=p.load(fobj)

    user_dict[username] = password

    with open(fname,'wb') as fobj:
        p.dump(user_dict,fobj)

def user_info_print(fname):
    with open(fname,'rb') as fobj:
        user_dict=p.load(fobj)
    print(user_dict)

if __name__ == '__main__':
    username=argv[1]
    password=randpass.randpa()
    fname='/opt/test/pass'
    useradd(username,password,fname)
    user_info_print(fname)
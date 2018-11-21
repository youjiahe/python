#!/usr/bin/env python3
import paramiko,paramiko.ssh_exception
import sys
import getpass
import os
import threading

def rcmd(host,username='root',password=None,cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,username=username,password=password)
    except paramiko.ssh_exception.AuthenticationException:
        print('\033[31mInvalid Password!\033[0m')
    stdin,stdout,stderr=ssh.exec_command(cmd)
    out=stdout.read()
    err=stderr.read()
    if out:
        print('[%s] \033[32;1mOK\033[0m:\n %s' % (host,out.decode()))
    if err:
        print('[%s] \033[31;1mERR\033[0m:\n %s' % (host,err.decode()))
    ssh.close()
if __name__ == '__main__':
    if len(sys.argv)!=3:
        print('Usage: %s ipfile "command"' % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file %s' % sys.argv[1])
        exit(2)
    ipfile=sys.argv[1]
    password=getpass.getpass('请输入密码：')
    cmd=sys.argv[2]
    with open(ipfile) as fobj:
        for line in fobj:
            host=line.rstrip()
            th=threading.Thread(target=rcmd,args=(host,'root',password,cmd))
            th.start()
    print(getpass.getuser())
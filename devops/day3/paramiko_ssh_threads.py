#!/usr/bin/env python3
import paramiko
import os
import threading
def rcmd(host,username='root',password=None,cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=username,password=password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    out=stdout.read()
    err=stderr.read()
    if out:
        print('[%s] \033[32;1mOK:\033[0m\n %s' % (host,out.decode()))
    if err:
        print('[%s] \033[31;1mERR:\033[0m\n %s' % (host,err.decode()))
    ssh.close()
if __name__ == '__main__':
    ips=['192.168.4.%s' % i for i in range(1,4)]
    password='123456'
    cmd='useradd yy'
    for ip in ips:
        th = threading.Thread(target=rcmd,args=(ip,'root',password,cmd))
        th.start()


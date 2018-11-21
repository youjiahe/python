#!/usr/bin/env python3
import paramiko
def rcmd(host,username='root',password=None,cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=username,password=password)
    stdin,stdout,stderr=ssh.exec_command(cmd)
    out=stdout.read()
    err=stderr.read()
    if out:
        print('[%s] OUT:\n %s' % (host,out))
    if err:
        print('[%s] ERR:\n %s' % (host,err))

if __name__ == '__main__':
    host='192.168.4.2'
    password='123456'
    cmd='id jia'
    rcmd(host,password=password,cmd=cmd)
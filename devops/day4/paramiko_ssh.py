#!/usr/bin/env python3
import paramiko
import threading
import getpass
def pssh(host,cmds,user,passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host,username=user,password=passwd)
    stdin,stdout,stderr=ssh.exec_command(cmds)
    out=stdout.read()
    err=stderr.read()
    if out:
        print('[%s] \033[32;1mOk\033[0m\n%s' % (host.rstrip(),out.decode()))
    if err:
        print('[%s] \033[31;1mNG\033[0m\n%s' % (host.rstrip(),err.decode()))

if __name__ == '__main__':
    fname='/root/host.txt'
    cmds='useradd you;id you'
    password=getpass.getpass()
    with open(fname) as fobj:
        for host in fobj:
            th=threading.Thread(target=pssh,args=(host,cmds,'root',password))
            th.start()


#!/usr/bin/env python3
import subprocess
import os
from time import sleep
import threading
n=0
def ping(ip):
    rc=subprocess.call('ping -i0.1 -c2 -W1.5 %s &>/dev/null' % ip,shell=True)
    if rc==0:
        print("%s......\033[32;1m[up]\033[0m" % ip)
    else:
if __name__ == '__main__':
    ips=["159.138.3.%s" % i for i in range(1,255)]
    for ip in ips:
        th=threading.Thread(target=ping,args=(ip,))
        th.start()  #相当于  target(args) => ping(ip)



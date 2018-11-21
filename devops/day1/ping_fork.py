#!/usr/bin/env python3
import subprocess
import os
from time import sleep
n=0
class Ping:
    def __init__(self,ip):
        self.ip=ip

    def ping(self):
        rc=subprocess.call('ping -i0.1 -c2 -W1 %s &>/dev/null' % self.ip,shell=True)
        if rc==0:
            return "%s......\033[32;1m[up]\033[0m" % self.ip
if __name__ == '__main__':
    for ip in range(1,254):
        pid=os.fork()
        if not pid:
            p=Ping("176.121.207.%s" % ip)
            rc=p.ping()
            if rc!=0:
                print(rc,n)
                exit()
            else:
                exit()




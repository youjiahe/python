#!/usr/bin/env python3
import subprocess
import os
import time
import threading
n=0
class Ping:
    def __init__(self,ip):
        self.ip=ip

    def __call__(self):
        rc=subprocess.call('ping -i0.1 -c2 -W1 %s &>/dev/null' % self.ip,shell=True)
        if rc==0:
            print("{:.<20}\033[32;1m[up]\033[0m".format(self.ip))

if __name__ == '__main__':
    ips = ["139.159.193.%s" % i for i in range(1, 255)]
    start=time.time()
    for ip in ips:
        th = threading.Thread(target=Ping(ip))
        th.start()
    end=time.time()
    print(end-start)

#!/usr/bin/env python3
import os
import subprocess
import time
def mping(ip):
    p = subprocess.call(
        'ping -c2 -i0.1 -W1 %s &>/dev/null' % ip,shell=True
    )
    if not p:
        print('{:.<20}\033[32;1m[up]\033[0m'.format(ip))
    else:
        print('{:.<20}\033[31;1m[down]\033[0m'.format(ip))
if __name__ == '__main__':
    ip_net='139.159.193.'
    ips=['%s%s' % (ip_net,host) for host in range(1,255)]
    start=time.time()
    for ip in ips:
        mping(ip)
    end=time.time()
    time.sleep(1)
    print(end-start)
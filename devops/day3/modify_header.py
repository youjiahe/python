#!/usr/bin/env python3
from urllib import request
from time import sleep
url='http://139.159.193.210'
url='https://www.jd.com'
#伪造头部信息
header={'User-Agent':'Mozilla/5.0 (X11; WIN10 x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
req=request.Request(url,headers=header)
#req=request.Request(url)
n=0
while True:
    html=request.urlopen(req)
    n += 1
    sleep(0.001)
    if n>=6000:
        break
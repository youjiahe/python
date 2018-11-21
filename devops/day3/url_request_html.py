#!/usr/bin/env python3
#request
from urllib import request
html = request.urlopen("https://www.163.com")
html1 = request.urlopen("https://www.baidu.com")
print(html.readlines(20))
with open("/opt/test/163.html",'wb') as fobj:
    while True:
        data = html.read(1024)
        if not data:
            break
        fobj.write(data)

with open("/opt/test/baidu.html",'wb') as fobj:
    while True:
        data = html1.read(1024)
        if not data:
            break
        fobj.write(data)

#[root@room9pc01 ~]# firefox /opt/test/163.html
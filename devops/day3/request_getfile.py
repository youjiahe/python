#!/usr/bin/env python3
from urllib import request
def get_file(url,dst):
    html = request.urlopen(url)
    with open(dst,'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)
if __name__ == '__main__':
    url="http://dingyue.nosdn.127.net/VbCNmHi2iC2SBXbuLOw9pkjAWEtZVxVIXrUIfnXE1oELL1539610935772.jpg"
    dst="/opt/test/kobe.img"
    get_file(url,dst)

#[root@room9pc01 ~]# eog /opt/test/kobe.img  #查看图片
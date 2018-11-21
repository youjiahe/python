#coding=utf8
#!/usr/bin/env python3
from urllib import request
import pickle as p
import re
import sys

def get_file(url, dst):
    try:
        html = request.urlopen(url)
    except :  #访问错误网页，错误处理
        print('%s 不存在或者访问超时' % url )
    else:
        with open(dst, 'wb') as fobj:
            while True:
                data = html.read(1024)
                if not data:
                    break
                fobj.write(data)
def get_urls(fname,patt):
    urls=[]
    with open(fname,'rb') as fobj:
        for line in fobj:
            url=re.search(patt,line.decode(errors="ignore"))

            if url:
                urls.append(url.group())
    return urls
if __name__ == '__main__':
#下载文件
    url="https://www.163.com"
    dst="/opt/test/163_com.html"
    get_file(url,dst)
    patt="(http|https)://[/.\w]+(jpg|jpeg|png|gif)"
    urls=get_urls(dst,patt)

    for url in urls:
        fname=url.split('/')[-1]
        dst="/opt/test/picture/%s"  % fname
        get_file(url,dst)

# [root@room9pc01 ~]# eog /opt/test/kobe.img  #查看图片
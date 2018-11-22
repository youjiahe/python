#!/usr/bin/env python3
from urllib import request,error
import re
import os
class GetFile:
    def __init__(self,url,patt,dir,fname):
        self.url=url
        self.patt=patt
        self.fname=fname

    def get_files(self):
        try:
            html=request.urlopen(self.url)
        except error.HTTPError:
            print('%s 不存在或访问超时' % self.url)
        else:
            with open(self.fname,'wb') as fobj:
                while True:
                    data=html.read(1024)
                    if not data:
                        break
                    fobj.write(data)

    def get_urls(self,charset='utf8'):
        urls = []
        c = re.compile(self.patt)
        with open(self.fname,'rb') as fobj:
            for ll in fobj:
                res=c.search(ll.decode(errors='ignore'))
                if res:
                    result=res.group()
                    urls.append(result)
        return urls
if __name__ == '__main__':
    url='https://www.163.com'
    patt='https*://[/.\w-]*\.(jpg|jpeg|png|gif)'
    dst='/opt/test/picture'
    fname='/opt/test/picture/url.txt'
    getf=GetFile(url,patt,dst,fname)
    getf.get_files()
    urls=getf.get_urls()
    print(urls)
    for u in urls:
        fn = u.split('/')[-1]
        fn = os.path.join(dst, fn)
        get = GetFile(u, patt, dst, fn)
        get.get_files()



#!/usr/bin/env python3
import os
import requests
import hashlib
def check_version(fname,ver_url):
    #如果版本文件不存在，则表示需要更新
    if not os.path.isfile(fname):
        return True

    #如果
    f=requests.get(ver_url)
    with open(fname) as fobj:
        local_ver=fobj.read()
    if f.text!=local_ver:
        return True
    return False

def download(url,fname):
    r = requests.get(url)
    with open(fname,'wb') as fobj:
        fobj.write(r.content)

def check_md5(url,fname):
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data=fobj.read(1024)
            if not data:
                break
            m.update(data)
    file_md5=m.hexdigest()

    r = requests.get(url)
    if r.text==file_md5.strip():
        return True   #文件未损坏，返回True
    return False      #文件损坏，返回False

def deploy(app_fname):
    os.chdir('/var/www/deploy',)


if __name__ == '__main__':
    ver_url='http://'
    fname=''
    new_version = check_version(ver_url,fname)
    if not new_version:
        print('没有新版本更新!')
        exit(1)
    download()
    md5 = check_md5()
    if not md5:
        print('文件有损坏')
        exit(2)
    deploy()
    download()
    print('新版本部署完成')
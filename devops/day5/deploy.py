#!/usr/bin/env python3
import os
import requests
import hashlib
import tarfile
def check_version(ver_url,fname):
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
    if r.text.strip()==file_md5:
        return True   #文件未损坏，返回True
    return False      #文件损坏，返回False

def deploy(deploy_dir,link,app_fname):
    os.chdir(deploy_dir)
    tar = tarfile.open(app_fname,'r:gz')
    tar.extractall()
    tar.close()

    if os.path.islink(link):
        os.unlink(link)

    src=app_fname.split('/')[-1].replace('.tar.gz','')
    src=os.path.join(deploy_dir,src)
    dst=link
    os.symlink(src,dst)

if __name__ == '__main__':
    deploy_dir = '/var/www/deploy'
    download_dir='/var/www/download'
    link = '/var/www/html/nsd1806'

    ver_url='http://192.168.4.3/deploy/live_version'
    fname='%s/live_version' % deploy_dir
    new_version = check_version(ver_url,fname)
    if not new_version:
        print('没有新版本更新!')
        exit(1)

    r = requests.get(ver_url)
    app_url='http://192.168.4.3/deploy/packages/web_pro%s.tar.gz' % r.text.strip()
    app_fname=app_url.split('/')[-1]
    app_fname=os.path.join(download_dir,app_fname)
    download(app_url,app_fname)

    md5_url='http://192.168.4.3/deploy/packages/web_pro%s.tar.gz.md5' % r.text.strip()
    md5 = check_md5(md5_url,app_fname)
    if not md5:
        print('文件有损坏')
        exit(2)

    deploy(deploy_dir,link,app_fname)

    #更新本地version文件
    download(ver_url,fname)
    print('新版本部署完成')
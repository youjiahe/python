#!/usr/bin/env python3
import requests
import os
import hashlib
import tarfile
import ding_Robot
def check_version(url,fname):
    if not os.path.isfile(fname):
        return  True
    r = requests.get(url)
    with open(fname) as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            if data != r.text:
                return True
    return False

def check_md5(url,fname):
    md5=hashlib.md5()
    r = requests.get(url)
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            md5.update(data)
    file_ok = md5.hexdigest()
    if r.text.strip() == file_ok:
        return True
    else:
        return False

def download(url,fname):
    r =requests.get(url)
    with open(fname,'wb') as fobj:
        fobj.write(r.content)

def deploy(deploy_dir,link,app_path):
    os.chdir(deploy_dir)
    tar = tarfile.open(app_path,'r:gz')

    tar.extractall()
    tar.close()

    if os.path.islink(link):
        os.unlink(link)

    dst = os.path.basename(app_path).replace('.tar.gz','')
    dst = os.path.join(deploy_dir,dst)
    os.symlink(dst,link)


if __name__ == '__main__':
    deploy_dir='/var/www/deploy/minth'
    download_dir='/var/www/download/minth'
    link='/var/www/html/minth'
    ver_url='http://192.168.4.51/deploy/live_version'
    ver_fname='/var/www/deploy/minth/live_version'
    new_version = check_version(ver_url,ver_fname)
    if not new_version:
        print('没有版本更新!')
        exit(1)

    version = requests.get(ver_url)
    app_url='http://192.168.4.51/deploy/packages/work_platform_%s.tar.gz' % version.text.strip()
    app_fname=app_url.split('/')[-1]
    app_fname=os.path.join(download_dir,app_fname)
    download(app_url,app_fname)

    md5_url='http://192.168.4.51/deploy/packages/work_platform_%s.tar.gz.md5' % version.text.strip()
    md5_ok=check_md5(md5_url,app_fname)
    if not md5_ok:
        print('文件有损坏')
        exit(2)

    deploy(deploy_dir,link,app_fname)
    #更新本地版本文件
    download(ver_url,ver_fname)

    msg = 'work_platform_%s 部署完成' % version.text.strip()
    reminders = ['']
    url = 'https://oapi.dingtalk.com/robot/send?access_token=47f4ae71f59ee1624cf30a4f6a4641fac15478aeec406c7f952556906096d790'
    ding_Robot.send_msg(url,reminders,msg)
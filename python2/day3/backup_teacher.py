#!/usr/bin/env python3
import time
import os
import tarfile
import hashlib
import pickle as p
def full_back(src_dir,dst_dir,md5_file):
    fname = os.path.basename(src_dir.rstrip())
    fname = "%s_full_%s.tar.gz" % (fname,time.strftime('%F'))
    fname = os.path.join(dst_dir,fname)

    tar = tarfile.open(fname,'w:gz')
    tar.add(src_dir)
    tar.close()

    #递归列出目录下的所有文件
    mydict={}
    for path,folders,files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path,file)
            value = check_md5(key)
            mydict[key]=value
    #把md5哈希写到文件中
    with open(md5_file,'wb') as m:
        p.dump(mydict,m)

def increate_back(src_dir,dst_dir,md5file):
    fname = os.path.basename(src_dir.rstrip())
    fname = "%s_full_%s.tar.gz" % (fname,time.strftime('%F'))
    fname = os.path.join(dst_dir,fname)

    tar = tarfile.open(fname,'w:gz')

    #递归列出目录下的所有文件
    mydict={}
    for path,folders,files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path,file)
            value = check_md5(key)
            mydict[key]=value
    #导出旧的md5哈希写到文件中

    with open(md5_file,'rb') as m:
        old_md5=p.load(m)

    #把新的哈希文件写到文件中
    with open(md5_file,'wb') as m:
        p.dump(mydict,m)

    #把md5值不相同的文件添加到增量备份文件中
    tar = tarfile.open(fname,'w:gz')
    for k in mydict:
        if old_md5.get(k)!=mydict[k]:   # 只需要判断新旧两个文件的键值
            tar.add(k)
    tar.close()

def check_md5(fname):
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)

if __name__=='__main__':
    src_dir = '/opt/test/project'
    dst_dir = '/opt/test/project_bak'
    md5_file = '/opt/test/project_bak/md5.data'
    if time.strftime('%a')=='Thu':
        full_back(src_dir,dst_dir,md5_file)
    else:
        increate_back(src_dir,dst_dir,md5_file)
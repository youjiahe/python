#!/usr/bin/env python3
import time
import pickle as p
import hashlib
import os
import tarfile
def check_md5(fname):
    md5=hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def full_bak(src_dir,dst_dir,md5_file):
    #全备份
    fname=os.path.basename(src_dir.rstrip('/'))
    fname='%s_full_%s.tar.gz' % (fname,time.strftime('%F'))
    fname=os.path.join(dst_dir,fname)
    tar=tarfile.open(fname,'w:gz')
    tar.add(src_dir)
    tar.close()

    #递归列出目录下所有文件
    md5_dict={}
    for path,folders,files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path,file)
            value = check_md5(key)
            md5_dict[key] = value

    with open(md5_file,'wb') as fobj:
        p.dump(md5_dict,fobj)

def incrt_bak(src_dir,dst_dir,md5_file):
    #增量备份
    fname=os.path.basename(src_dir.rstrip('/'))
    fname='%s_incrt_%s.tar.gz' % (fname,time.strftime('%F'))
    fname=os.path.join(dst_dir,fname)
    tar=tarfile.open(fname,'w:gz')
    #暂时不需要任何tar操作，等到md5值不一样是 tar.add()

    # 递归列出目录下所有文件
    md5_dict = {}
    for path, folders, files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path, file)
            value = check_md5(key)
            md5_dict[key] = value

    with open(md5_file,'rb') as fobj:
        old_md5=p.load(fobj)

    with open(md5_file, 'wb') as fobj:
        p.dump(md5_dict, fobj)

    for i in md5_dict:
        if old_md5.get(i)!=md5_dict[i]:
            tar.add(i)
        else:
            continue
    tar.close()

if __name__ == '__main__':
    src_dir='/opt/test/project'
    dst_dir='/opt/test/project_bak'
    md5_file='/opt/test/project_bak/md5.crt'
    if time.strftime('%a')=='Thu':
        full_bak(src_dir,dst_dir,md5_file)
    else:
        incrt_bak(src_dir,dst_dir,md5_file)
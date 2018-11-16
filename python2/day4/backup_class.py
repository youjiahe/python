#!/usr/bin/env python3
import tarfile
import hashlib
import time
import os
import pickle as p
class BackUp:
    def __init__(self,src_dir,dst_dir,md5_file):
        self.src_dir=src_dir
        self.dst_dir=dst_dir
        self.md5_file=md5_file

    def check_md5(self,fname):
        md5=hashlib.md5()
        with open(fname,'rb') as fobj:
            while True:
                data=fobj.read(4096)
                if not data:
                    break
                md5.update(data)
        return md5.hexdigest()

    def full_bak(self):
        #全备份
        fname=os.path.basename(self.src_dir)
        fname='%s_full_%s.tar.gz' % (fname,time.strftime('%F'))
        fname=os.path.join(self.dst_dir,fname)
        tar=tarfile.open(fname,'w:gz')
        tar.add(self.src_dir)
        tar.close()

        #保存md5校验值
        #递归列出所有的文件
        md5_dict={}
        for paths,folders,files in os.walk(self.src_dir):
            for file in files:
                key = os.path.join(paths,file)
                value = self.check_md5(key)
                md5_dict[key] = value

        with open(self.md5_file,'wb') as fobj:
            p.dump(md5_dict,fobj)

    def incrt_bak(self):
        #增量备份
        fname=os.path.basename(self.src_dir)
        fname='%s_incrt_%s.tar.gz' % (fname,time.strftime('%F'))
        fname=os.path.join(self.dst_dir,fname)
        tar=tarfile.open(fname,'w:gz')

        md5_dict={}
        for paths,folders,files in os.walk(self.src_dir):
            for file in files:
                key = os.path.join(paths,file)
                value = self.check_md5(key)
                md5_dict[key] = value
        with open(self.md5_file,'rb') as fobj:
            old_md5=p.load(fobj)

        with open(self.md5_file,'wb') as fobj:
            p.dump(md5_dict,fobj)

        for key in md5_dict:
            if old_md5.get(key)!=md5_dict[key]:
                tar.add(key)
        tar.close()

if __name__ == '__main__':
    src_dir = '/opt/test/project'
    dst_dir = '/opt/test/pro_bak'
    md5_file='/opt/test/md5.data'
    bk=BackUp(src_dir,dst_dir,md5_file)
    if time.strftime('%a')=='Fri':
        bk.full_bak()
    else:
        bk.incrt_bak()
























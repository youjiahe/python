#!/usr/bin/env python3
import time
import pickle as p
import hashlib
import os
import tarfile
class BackUp:
    def __init__(self,src_dir,dst_dir,md5_file):
        self.src_dir=src_dir
        self.dst_dir=dst_dir
        self.md5_file=md5_file
    def check_md5(self,fname):
        m=hashlib.md5()
        with open(fname,'rb') as fobj:
            while True:
                data=fobj.read(4096)
                if not data:
                    break
            m.update(data)
        return m.hexdigest()

    def full_bak(self):
        fname=os.path.basename(self.src_dir)
        fname='%s_full_%s.tar.gz' % (fname,time.strftime('%F'))
        fname=os.path.join(self.dst_dir,fname)
        tar=tarfile.open(fname,'w:gz')
        tar.add(self.src_dir)
        tar.close()

        md5={}
        for paths,folders,files in os.walk(self.src_dir):
            for file in files:
                key = str(os.path.join(paths,file))
                value = self.check_md5(key)
                md5[key]=value

        with open(md5_file,'wb') as fobj:
            p.dump(md5,fobj)

    def incrt_bak(self):
        fname = os.path.basename(self.src_dir)
        fname = '%s_incrt_%s.tar.gz' % (fname, time.strftime('%F'))
        fname = os.path.join(self.dst_dir, fname)
        tar = tarfile.open(fname, 'w:gz')

        md5 = {}
        for paths, folders, files in os.walk(self.src_dir):
            for file in files:
                key = str(os.path.join(paths, file))
                value = self.check_md5(key)
                md5[key] = value

        with open(md5_file, 'rb') as fobj:
            old_md5=p.load(fobj)

        with open(md5_file, 'wb') as fobj:
            p.dump(md5, fobj)

        for key in md5:
            if old_md5.get(key)!=md5[key]:
                tar.add(key)
        tar.close()

if __name__ == '__main__':
    src='/opt/test/project'
    dst='/opt/test/pro_bak'
    md5_file='/opt/test/pro_bak/md5.data'
    backup=BackUp(src,dst,md5_file)
    if time.strftime('%a')=='Sun':
        backup.full_bak()
    else:
        backup.incrt_bak()
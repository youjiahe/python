#！/usr/bin/env python3
import hashlib
import tarfile
import os
import time
import pickle as p
class BackUp:
    def __init__(self,src,dst,md5f):
        self.src_dir=src
        self.dst_dir=dst
        self.md5_file=md5f

    def check_md5(self,fname):
        md5=hashlib.md5()
        if os.path.exists(fname):
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
        fname=os.path.join(dst,fname)

        tar = tarfile.open(fname,'w:gz')
        tar.add(self.src_dir)
        tar.close()

        md5={}
        for paths,folders,files in os.walk(self.src_dir):
            for file in files:
                key=os.path.join(self.src_dir,file)
                value=self.check_md5(key)
                md5[key]=value

        with open(self.md5_file,'wb') as fobj:
            p.dump(md5,fobj)

    def incrt_bak(self):
        # 增量备份
        fname = os.path.basename(self.src_dir)
        fname = '%s_incrt_%s.tar.gz' % (fname, time.strftime('%F'))
        fname = os.path.join(dst, fname)

        tar = tarfile.open(fname, 'w:gz')

        md5 = {}
        for paths, folders, files in os.walk(self.src_dir):
            for file in files:
                key = os.path.join(self.src_dir, file)
                value = self.check_md5(key)
                md5[key] = value

        with open(self.md5_file,'rb') as fobj:
            old_md5=p.load(fobj)

        with open(self.md5_file, 'wb') as fobj:
            p.dump(md5, fobj)

        for key in md5:
            if old_md5.get(key)!=md5[key]:
                tar.add(key)
        tar.close()

if __name__ == '__main__':
    src='/opt/test/project'
    dst='/opt/test/pro_bak'
    md5f='/opt/test/pro_bak/md5.data'
    bk = BackUp(src,dst,md5f)
    if time.strftime('%a')=='MON':
        bk.full_bak()
    else:
        bk.incrt_bak()

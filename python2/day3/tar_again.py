#!/usr/bin/env python3
import tarfile
import os
import time
start=time.time()
os.chdir('/root')
tar=tarfile.open('etc.tar.gz','w:gz')
tar.add('/etc')
tar.close()
list=os.listdir('/root')
print('etc.tar.gz' in list)
end=time.time()
print('%ds' %  int(end-start) )
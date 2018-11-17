#!/usr/bin/env python3
import shutil
import os
#shutil.copyfileobj(open('/etc/passwd','rb'),open('/opt/test/pass','wb'))
#shutil.copyfile('/etc/shadow','/opt/test/sha')
#shutil.copystat('/etc/hostname','/opt/test/sha')
#shutil.copymode('/etc/hostname','/opt/test/sha')
#shutil.copytree('/etc/sysconfig/network-scripts/','/opt/nwtw')
#shutil.copy('/etc/sysconfig/network-scripts/ifcfg-enp1s0','/opt/test/enp1s0')
#shutil.copy2('/etc/sysconfig/network-scripts/ifcfg-enp1s0','/opt/test/enp1s1')
if not os.path.exists('/opt/test/project'):
    os.mkdir('/opt/test/project')
print(os.path.isdir('/opt/test/project'))
print(shutil.os.path.basename('/opt/test/project'))
#os.mknod('/opt/test/nod.txt')
if os.path.exists('/opt/test/nod.txt'):
    print('exits')
    print(os.path.isdir('/opt/test/nod.txt'))
    print(os.path.isfile('/opt/test/nod.txt'))
print(os.listdir('/opt/test'))
for  paths,folders,files in os.walk('/opt/'):
    print(paths)
for paths, folders, files in os.walk('/opt/'):
    print(folders)
for paths, folders, files in os.walk('/opt/'):
    print(files)
for paths,folders,files in os.walk('/opt'):
    for file in files:
        print(os.path.join(paths,file))
os.chmod('/opt/test/nod.txt',0o777)
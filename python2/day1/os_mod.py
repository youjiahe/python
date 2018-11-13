#!/usr/bin/env python3
import os
import datetime
import time
import pickle as p
import shutil

#shutil.copy2('/etc/passwd','/opt/test/')
#os.remove('/opt/test/passwd')
#print(os.getcwd())
#os.chdir('/root')

# os.chdir('/root/git/python/python2/day1')
#print(os.getcwd())
#print(os.listdir())
#print(os.listdir('/root'))
#os.mkdir('testtest')
#print(os.listdir())
#os.removedirs('testtest')
# try:
#     os.symlink('/etc/hosts','/opt/test/host')
# except FileExistsError:
#     print(os.listdir('/opt/test'))
#     print('file exists!')
# try:
#     os.mknod('testnod.py')
# except FileExistsError:
#     print(os.listdir())
#     print(os.listdir().index('testnod.py'))
# # finally:
# #     os.remove('testnod.py')
# print('testnod.py' in os.listdir())
# print(os.path.islink('/iso'))
# print(os.path.isfile('/etc/hosts'))
# print(os.path.exists('/tmp/1.txt'))
# print(os.path.isdir('/root/git'))
# print(os.path.split('/var/lib/libvirt/images/node.qcow2'))
# print(os.path.join('/var/lib/','node.qcow2'))
# tup=os.path.split('/etc/sysconfig/network-scripts/ifcfg-eth0')
# print(type(tup))
# hold=os.path.join('/root',tup[1])
# print(hold)
# os.makedirs('/opt/test/aaa/bbbb/ccc')
# os.chmod('/opt/test/aaa/',0o777)
# with open('/opt/test/1.txt','wb') as f:
#     p.dump({'name':'bob','age':25},f)
# with open('/opt/test/1.txt','rb') as f1:
#     info=p.load(f1)
# print(info)

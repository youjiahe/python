#!/usr/bin/env python3
import os
import datetime
import time
import pickle
import shutil

shutil.copy2('/etc/passwd','/opt/test/')
os.remove('/opt/test/passwd')
print(os.getcwd())
os.chdir('/root')
print(os.getcwd())
os.chdir('/root/git/python/python2/day1')
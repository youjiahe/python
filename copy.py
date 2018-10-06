from sys import argv
from os.path import exists

script, fn1, fn2=argv

open(fn2,"w").write(open(fn1).read())


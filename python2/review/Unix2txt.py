#!/usr/bin/env python3
from sys import argv
def unix2win(fname,dst):
    l=[]
    with open(fname,'r') as fobj:
        for line in fobj:
            newline=line.rstrip()+'\r\n'
            l.append(newline)
    print(l)
    with open(dst,'w') as fobj:
        fobj.writelines(l)

def read_file(fname):
    with open(fname,'r') as fobj:
        l=fobj.readlines()
    print(l)

if __name__ == '__main__':
    try:
        fname=argv[1]
        dst=argv[2]
    except IndexError:
        print('unix2txt.py <File path>')
    else:
        unix2win(fname,dst)
        read_file(dst)


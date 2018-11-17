#!/usr/bin/env python3
import os
def diff(fname1,fname2,output):
    f1=set()
    f2=set()
    if not os.path.isfile(fname1) or not os.path.isfile(fname2):
        print('Could be not file!')
        exit()
    with open(fname1) as fobj:
        for line in fobj:
            f1.add(line)

    with open(fname2) as fobj:
        for line in fobj:
            f2.add(line)

    diff = list( f1 - f2 )

    with open(output,'w') as fobj:
        fobj.writelines(diff)

if __name__ == '__main__':
    fname1='/var/ftp/share/test.txt'
    fname2 = '/var/ftp/share/test1.txt'
    out_file = 'test_out.txt'
    diff(fname1,fname2,out_file)
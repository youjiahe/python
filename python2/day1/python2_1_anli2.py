#!/usr/bin/env python3
from sys import argv
def unix2dos(fname,end='\r\n'):
    dst_fname=fname + '.txt'
    with open(fname) as src:
        with open(dst_fname,'w') as dst:
            for line in src:
                dst.write(line.rstrip()+end)

if __name__=="__main__":
    unix2dos(argv[1])
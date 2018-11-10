#!/usr/bin/env python3
import sys
def cp():
    src_file=open(sys.argv[1],'rb')
    dst_file=open(sys.argv[2],'wb')
    dst_file.write(src_file.read())
cp()

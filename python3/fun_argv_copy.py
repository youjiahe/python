#!/usr/bin/env python3
import  sys
def copy():
    print(sys.argv)
    src_obj = open(sys.argv[1],'rb')   #以二进制的方式打开文件，不会有编码问题
    dst_obj = open(sys.argv[2],'wb')

    while True:
        data=src_obj.read(4096)   #只读取4k数据
        if not data:
            break
        dst_obj.write(data)

    src_obj.close()
    dst_obj.close()

copy()

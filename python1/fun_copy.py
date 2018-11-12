#!/usr/bin/env python3
def copy(src,dst):
    src_obj = open(src,'rb')   #以二进制的方式打开文件，不会有编码问题
    dst_obj = open(dst,'wb')

    while True:
        data=src_obj.read(4096)   #只读取4k数据
        if not data:
            break
        dst_obj.write(data)

    src_obj.close()
    dst_obj.close()

copy('/bin/ls','/opt/ls1')
copy('/bin/ls','/opt/ls2')
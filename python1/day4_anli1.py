#os.path.exists()  用于判断某那个路径是否存在
#!/usr/bin/env python3
import os
import shutil
def get_path():
    while True:
        file_path=input('新建文件路径：')
        if not os.path.exists(file_path):
            return file_path
            break
        else:
            print('%s already exists!' % file_path)
            exit()
def get_context():
    context=[]
    text=''
    print('请输入文件内容:')
    while True:
        text=(input('>'))
        if text=='quit':
            break
        context.append(text)
    return context

def write_file(files,t1):
    t1 = ['%s\n' % l for l in t1]
    path=open(files,'w')
    path.writelines(t1)
    path.close()

if __name__=='__main__':
    path=get_path()
    t=get_context()
    write_file(path,t)
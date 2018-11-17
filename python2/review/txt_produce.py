#!/usr/bin/env python3
import os
def get_path():
    path=''
    while True:
        try:
            path=input('Input your file path:')
        except (TypeError,ValueError):
            print('Invalid input')
            continue
        except (KeyboardInterrupt,EOFError):
            print('Bye')
            break
        else:
            if os.path.exists(path):
                print('This path %s is exists!' % path)
                continue
            elif not path:
                continue
            else:
                return path

def get_context():
    print('Input your context:')
    text_list=[]
    while True:
        context=input('>')
        if context=='quit':
            break
        else:
            text_list.append(context+'\n')
    return text_list

def write_file(path,context):
    with open(path,'w') as fobj:
        fobj.writelines(context)

if __name__ == '__main__':
    path=get_path()
    text=get_context()
    write_file(path,text)
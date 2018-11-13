#!/usr/bin/env python3
def into_shed(_list,_elements=''):
    if _elements:
        _list.append(_elements)
        return _list
    else:
        print('_elements invalid!')
def out_shed(_list):
    _list.pop()
    return _list
def query_elements(_list,_num):
    _num=int(_num)
    return _list[_num]
def query_index(_list,_elements=''):
    if _elements!='':
        if not _list:
            print('Empty shed')
        else:
            return _list.index(_elements)
    elif _elements=='':
        return _list
if __name__=='__main__':
    command=''
    list=[]
    comm=[]
    while True:
        if command==r'quit' or command==r'exit':
            break
        while True:
            if len(comm)!=0:
                break
            command=input('{1:into; 2:out; 3:query [option] [elements];}>').strip()
            comm=command.split()
        if comm[0]=='1':
            for i in range(len(comm)-1):
                list=into_shed(list,comm[i+1])
        elif comm[0]=='2':
            list=out_shed(list)
        if comm[0]=='3':
            if len(comm)==3:
                if comm[1]=='-e' and comm[2].isdigit():
                    print(query_elements(list,comm[2]))
                elif comm[1]=='-i'  and comm[2].isalnum():
                    print(query_index(list,comm[2]))
            elif len(comm)==1:
                print(query_index(list))
        comm=[]
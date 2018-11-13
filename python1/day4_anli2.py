#!/usr/bin/env python3
from string import digits,ascii_letters
def var_j(st=''):
    var_ok_str=digits+ascii_letters+'_'
    first_ok=ascii_letters+'_'
    locat=[]
    c=0
    for i,j in enumerate(st):
        index=i+1
        if j not in var_ok_str:
            print('%s 第%d个字符非法' % (j,index))
            c += 1
        elif i==0 and j not in first_ok:
            print('\033[31m首字符不正确！\033[0m')
            break
    else:
        if c==0:
            print('\033[32m变量合法\033[0m')


if __name__=='__main__':
    data = input('输入一个变量名')
    var_j(data)
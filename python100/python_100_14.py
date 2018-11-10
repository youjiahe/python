#!/usr/bin/env python3
from random import randint
from string import digits
def intp(st):
    stat=0
    if st != '':
        for i in st:
            if i not in digits:
                stat=1
                break
            else:
                stat=0
    else:
        stat=2
    return stat
def pingji(score):
    if not isinstance(score,int):
        return 1
    else:
        if score>=90:
            return '优秀'
        elif score>=80:
            return '良好'
        elif score>=70:
            return '中'
        elif score>=60:
            return '及格'
        else:
            return '不及格'

ch='';ma='';en=''

while intp(ch)!=0:
    ch=input('语文成绩:')
else:
    chinese=int(ch)
    chpj=pingji(chinese)

while intp(ma)!=0:
    ma=input('数学成绩:')
else:
    math=int(ma)
    mapj = pingji(math)

while intp(en)!=0:
    en=input('英语成绩:')
else:
    english=int(en)
    enpj=pingji(english)
print('''语文：%s 
数学：%s  
英语：%s''''' % (chpj,mapj,enpj))
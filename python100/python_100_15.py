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
        if score>=60 and score<70:
            return '\033[33m及格\033[0m'
        elif score>=70 and score <80:
            return '\033[34m中等\033[0m'
        elif score>=80 and score<90:
            return '\033[35m良好\033[0m'
        elif score>=90:
            return '\033[32m优秀\033[0m'
        else:
            return '\033[31m不及格\033[0m'
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
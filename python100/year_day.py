#!/usr/bin/env python3\
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
def leap_judge(year=1000):
    stat=-1
    if year%4==0 and year%100!=0:
        stat=0
    elif year%400==0:
        stat=0
    return stat

leap=[31,29,31,30,31,30,31,31,30,31,30,31]
common=[31,28,31,30,31,30,31,31,30,31,30,31]
sum_days=0

y_input='';m_input='';d_input=''

while intp(y_input)!=0:
    y_input=input('年：')
while intp(m_input) != 0:
    m_input=input('月：')
while intp(d_input) != 0:
    d_input=input('日：')

y=int(y_input)
m=int(m_input)
d=int(d_input)
if y > 2999 or y<1000:
    print('%d年不在范围1000-2999内' % (y))
    exit()
if m > 12 or m <1:
    print('%d月不在范围1-12内' % (m))
    exit()
if leap_judge(y)==0:
    if d > leap[m-1] or d < 1:
        print('%d日不在范围1-%d内' % (m,leap[m-1]))
        exit()
else:
    if d > common[m-1] or d < 1:
        print('%d日不在范围1-%d内' % (d,common[m-1]))
        exit()


if leap_judge(y)==0:
    for i in range(m-1):
        sum_days = sum_days + leap[i] + d
else:
    for j in range(m-1):
        sum_days = sum_days + common[j] + d
print(sum_days)
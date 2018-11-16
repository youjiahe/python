#!/usr/bin/env python3
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    @classmethod   #可以给类传递参数，相当于在类里面定义实例
    def create_date(cls,str_data):
        y,m,d=map(int,str_data.split('-'))
        return  cls(y,m,d)

    @staticmethod  #类中的一个内建函数
    def is_valid_date(str_data):
        y,m,d=map(int,str_data.split('-'))
        return 0 < y < 4000 and 1 <= m <=12 and 1 <= d <=31

if __name__ == '__main__':
    d1=Date(2018,12,6)
    print(d1.year)
    d2=Date.create_date('2018-11-15')
    print(d2.year)
    print(Date.is_valid_date('2018-11-15'))

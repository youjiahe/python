#!/usr/bin/env python3
import time_method
from datetime import datetime,timedelta
print(time_method.time_method())
print(time_method.strftime('%Y-%m-%d %H:%M:%S'))
time_method.sleep(1)
print(time_method.localtime(0))
print(time_method.ctime())
print(time_method.ctime(150000000000))  #从1970-1-1起始的秒数时间
print(time_method.asctime())
print(datetime.now())  #微秒级
t=datetime.today()
print(t.year,t.month,t.day,t.hour,t.microsecond)
days = timedelta(days=82,hours=72)  #常用
dt=t+days
print(dt.year,dt.month,dt.day,dt.hour)

#!/usr/bin/env python3
import time_method
start=time_method.time_method()
sum=0
for i in range(50000000):
    sum += i
end=time_method.time_method()
time_use=end-start
print('use time : %.2fs' % time_use )

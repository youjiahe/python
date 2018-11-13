#!/usr/bin/env python3
import time
n = 0
while True:
    print('{}{}\r'.format('#'*n,'@'+'#'*(19-n)),end='')
    time.sleep(0.2)
    n +=1
    if n==20:
        n=0
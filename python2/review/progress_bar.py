#!/usr/bin/env python3
import time_method
def bar(num=20):
    print('%s\r' % '#'*num,end='')
    n=0
    while True:
        try:
            print('%s%s\r'% ('#'*(n),'@'+'#'*(num-n)),end='')
            n += 1
            time_method.sleep(0.3)
            if n>num:
                n=0

        except KeyboardInterrupt:
            print(' ')
            print('bye')
            break
if __name__ == '__main__':
    bar()

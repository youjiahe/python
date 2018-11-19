import os
import time
def add(num=1000):
    sum=0
    for i in range(1,num+1):
        sum += i
    print(sum)

if __name__ == '__main__':
    start=time.time()

    for i in [100000000,50000000,20000000,225]:
        pid = os.fork()
        if not pid:
            add(i)
            exit()
    for i in range(4):
        os.waitpid(-1,0)

    end = time.time()
    print(end - start)




#!/usr/bin/env python3
import threading
import time
def ma():
    def pr(i):
        print('python great！')
        time.sleep(7*i)
    def thr():
        threads=[]
        for i in range(1,2):
            th = threading.Thread(target=pr,args=(i,))
            time.sleep(1)
            threads.append(th)
        start=time.time()
        # print(threads)
        # time.sleep(12)
        for i in range(2):
            threads[i].start()
        for i in range(2):
            threads[i].join()
        end=time.time()
        print('all are done waste %.2f' % (end-start))
    thr()
if __name__ == '__main__':
    ma()




import os
import time
pid=os.fork()
if not pid:
    print("in child1...")
    time.sleep(10)
    print("child1 done")
    exit()
pid=os.fork()
if not pid:
    print("in child2...")
    time.sleep(15)
    print("child2 done")
    exit()

time.sleep(20)
os.waitpid(-1,1)  #一个waitpid()处理一个zombie进程
os.waitpid(-1,1)
time.sleep(10)
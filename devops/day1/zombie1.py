#!/usr/bin/env python3
import os
import time
start=time.time()
pid = os.fork()
if pid :
    print("父进程.....pid:%s" % pid)
    print(os.waitpid(-1,0))
    time.sleep(20)
else:
    print("子进程.....pid:%s" % pid)
    time.sleep(6)
end=time.time()
print("用时：%.2fs" % (end-start))
#watch -n 1 ps a  查看
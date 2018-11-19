import os
import time
start=time.time()
print('start......')
pid=os.fork()
if pid:
    print('父进程......')
    rc=os.waitpid(-1,0)
    time.sleep(20)
else:
    print('子进程')
    time.sleep(10)
end=time.time()
print("用时：%.2fs" % (end-start))

#运行
#start......
# 父进程......
# 子进程
# 用时：10.01s
# 用时：20.01s

# 25366 pts/4    S+     0:00 watch -n 1 ps a
# 25402 pts/3    S+     0:00 python3 zombie.py
# 25403 pts/3    Z+     0:00 [python3] <defunct>

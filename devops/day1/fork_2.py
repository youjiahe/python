import os
print('hello')
pid=os.fork()
if pid:
    print('父进程 ......')
else:
    print('子进程......')
print('又来了')
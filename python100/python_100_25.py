#！/usr/bin/env python3
def fib(num=10):
    fibs=[0,1]
    for i in range(num-2):
        fibs.append(fibs[-2]+fibs[-1])
    return fibs[-1]
print(fib(100))    #计算第100个斐波那契数列
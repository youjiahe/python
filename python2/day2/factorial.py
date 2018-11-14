#!/usr/bin/env python3
#计算阶乘
# def func(num):
#     i=num
#     while True:
#         i=i*(num-1)
#         num -= 1
#         if num==1:
#             return i
#             break
# if __name__ == '__main__':
#     print(func(6))
def func(num):
    if num==1:
        return 1
    return num*func(num-1)
            # 4*func(3)
            # 4*3*func(2)
            # 4*3*2*func(1)
            # 4*3*2*1
if __name__ == '__main__':
    print(func(6))

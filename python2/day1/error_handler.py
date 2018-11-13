#!/usr/bin/env python3
# 异常处理，把有可能发生异常的语句放到try中执行，发生异常跳转到异常处理
# 把不生生异常才执行的语句放到else中；
# 不管是否异常与否，都执行的放到finally中
try:
    num = int(input('number:'))
    result = 100/num
except (ValueError,ZeroDivisionError):
    print('Input invalid!')
except (KeyboardInterrupt,EOFError):
    print('bye-bye')
else:
    print(result)
finally:
    print(r'Done')

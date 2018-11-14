#!/usr/bin/env python3
def set_info(name,age):
    print('%s years old is %d' % (name,age))
#
# set_info('bob',25)
# set_info('25',23)
# set_info(age=23,name='bo')
# set_info('bb',age=27)
# set_info(age=23,'ii')  #报错
alist=['bobo',25]
#set_info(alist)   #报错，因为age没有给值
set_info(*alist)   #成功，加一个'*'号

# def mytest(*args):  #*表示元组
#     print(args)
# mytest('uuu','ooo')
# mytest(10)
# mytest(('yy','qq'))

# def mydict(**dit):
#     print(dit)
# mydict()
# mydict(name='bob',age=25)
an=(input('>'))

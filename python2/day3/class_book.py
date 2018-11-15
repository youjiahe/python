#！/usr/bin/env python3
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def __str__(self):
        return'《%s》' % self.title

    def __call__(self):
        print('《%s》的作者是%s' %  (self.title,self.author))

if __name__ == '__main__':
    b=book('Python核心编程','wesly')
    print(b)  #调用__str__()
    b()       #调用__call__()
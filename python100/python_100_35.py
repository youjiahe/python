#/usr/bin/env python3
def multi_table(num=9):
    end=num
    for i in range(1,end+1):
        for j in range(1,i+1):
            if i*j<10:
                print('%d×%d=%d' % (j,i,i*j),end='  ')
    #            print(j, '×', i, '=', i * j, sep='', end='  ')
            else:
                print('%d×%d=%d' % (j,i,i*j),end=' ')
    #            print(j,'×',i,'=',i*j,sep='',end=' ')
        print('')
multi_table(4)
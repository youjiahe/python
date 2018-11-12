#/usr/bin/env python3
end=9
for i in range(1,end+1):
    for j in range(1,i+1):
        print('{:<7}'.format('%d×%d=%d' % (j, i, i * j)), end='')
    print('')
#!/usr/bin/env python3
from random import randint
def exam():
    x=-65534;y=-65534
    while x==y:
        x=randint(1,101)
        y=randint(1,101)
    method=randint(0,1)
    mx=max(x,y);mn=min(x,y)
    if method==0:
        print('{}+{}=?'.format(x,y))
        result=x+y
        return result
    else:
        print('{}-{}=?'.format(mx,mn))
        result=x-y
        return result
def main():
    c=0;will='';willing=''
    result = exam()
    while True:
        prompt='Input your answer：'
        try:
            answer=int(input(prompt))
        except ValueError:
            print('\033[31mInvalid Input!\033[0m')
            continue
        else:
            if answer==result:
                print('\033[32;1mGreat!\033[0m')
                willing=input('Again?[y/n]')
                if willing=='y':
                    result = exam()
                    c = 0
                    continue
                else:
                    exit()
            else:
                c += 1
                if c<3:
                    print('\033[31mAnswer error!\033[0m')
                    continue
                else:
                    print('You have no oppotuniy! Correct answer is %d' % result)
                    will=input('Again?[y/n]')
                    if will=='y':
                        result = exam()
                        c=0
                        continue
                    else:
                        break
if __name__ == '__main__':
    main()
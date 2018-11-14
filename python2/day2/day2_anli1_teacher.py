#!/usr/bin/env python3
from random import randint,choice
def exam():
    c=0
    # def add(x,y):
    #     return x+y
    # def sub(x,y):
    #     return x-y
    nums=[randint(1,101) for i in range(2)]
    op=choice('+-')
    cmds={'+':lambda x, y:x+y,'-':lambda x, y:x-y}
    #cmds={'+':add,'-':sub}
    nums.sort(reverse=True)
    # if op=='+':
    #     result=nums[0]+nums[1]
    # else:
    #     result=nums[0]-nums[1]
    result=cmds[op](*nums)
    while True:
        try:
            answer=int(input('%d %s %d = ' % (nums[0],op,nums[1])))
        except ValueError:
            continue
        except (KeyboardInterrupt,EOFError):
            print('bye-bye')
            exit()
        else:
            if answer==result:
                print('\033[32;1mGreat!\033[0m')
                break
            else:
                c+=1
                if c<3:
                    print('\033[31mWrong answer\033[0m')
                else:
                    print('\033[31mYour haven\'t chances.\033[0m Correct answer is %d' % result)
                    break
def main():
    while True:
        exam()
        while True:
            try :
                will=input('Again?[y/n]:').strip()[0]
            except ValueError:
                continue
            except (KeyboardInterrupt, EOFError):
                print('bye-bye')
                exit()
            else:
                if will=='y':
                    break
                else:
                    exit()

if __name__ == '__main__':
    main()
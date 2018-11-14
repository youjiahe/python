#!/usr/bin/env python3
from random import randint,choice
def exam():
    nums=[randint(1,101) for i in range(2)]
    nums.sort(reverse=True)
    oper=choice('+-')
    cmds={'+':lambda x,y:x+y,'-':lambda x,y:x-y}
    result=cmds[oper](*nums)
    c=0
    while True:
        try :
            answer=int(input('%d %s %d = ' % (nums[0],oper,nums[1])))
        except (EOFError,KeyboardInterrupt):
            print('bye-bye')
            exit()
        except:
            continue
        else:
            if answer==result:
                print('\033[32;1mGreat\033[0m')
                break
            else:
                print('\033[31;1mWrong\33[0m')
                c+=1
                if c<3:
                    continue
                else:
                    print('You have no chances! Correct answer is %d' % result)
                    break

def main():
    exam()
    while True:
        while True:
            try :
                choose=input('Again?[y/n]:').strip()[0]
            except (EOFError,KeyboardInterrupt):
                print('bye-bye')
                exit()
            except:
                continue
            else:
                if choose=='y':
                    exam()
                else:
                    exit()
if __name__ == '__main__':
    main()
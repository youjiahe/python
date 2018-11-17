#!/usr/bin/env python3
from string import digits,ascii_letters
import keyword
iden = digits + ascii_letters + '_'
def identifier_ok(word=''):
    if keyword.iskeyword(word):
        print('"%s" is Keyword' % word)
        exit()

    elif word[0] not in iden:
        print('"%s" first character is illegal' % word)
        exit()
    ind=0
    for w in word:
        if w not in iden:
            ind=word.index(w)+1
            print('第%d个字符非法' % ind)

    if not ind:
        print('标示符 "%s" 合法' % word)

if __name__ == '__main__':
    while True:
        try:
            var=input('>')
        except (KeyboardInterrupt,EOFError):
            print('byr')
            break
        except :
            continue
        else:
            if var=='quit':
                exit()
            elif var:
                identifier_ok(var)
            else:
                continue

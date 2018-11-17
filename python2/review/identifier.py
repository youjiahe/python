#!/usr/bin/env python3
from string import digits,ascii_letters
import keyword
def identifier_ok(word=''):
    iden = digits + ascii_letters + '_'
    if keyword.iskeyword(word):
        print('%s is Keyword' % word)
        exit()

    elif word[0] not in iden:
        print('%s first character is illegal' % word)
        exit()

    while True:
        li=list(word)
        ind=0
        for w in li:
            if w not in iden:
                ind=li.index(w)
                print('第%d个字符非法' % ind)
            break
        if not ind:
            print('标示符 %s 合法' % word)
            break
if __name__ == '__main__':
    var='_fhaoi'
    identifier_ok(var)

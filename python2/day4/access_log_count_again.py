#!/usr/bin/env python3
from collections import Counter
import re
class CountAccess:
    def __init__(self,fname,patt):
        self.fname=fname
        self.patt=patt

    def __call__(self):
        c=Counter()
        cpatt=compile(self.patt)
        with open(fname) as fobj:
            for line in fobj:
                m = cpatt.search(self.patt, line)
                if m:
                    c.update(m.group())
                
    def most(self,num):


if __name__ == '__main__':
    fname='access.log'
    ip='(\d{1,3}\.){3}\d{3}'
    br='Chrome|Firefox|MISE'
    print(CountAccess(fname,ip))
    print(CountAccess(fname,br))
    print(CountAccess(fname, ip).most(2))
    print(CountAccess(fname, br).most(2))
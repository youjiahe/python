#!/usr/bin/env python3
from collections import Counter
import re
class CountAccess:
    def __init__(self,fname,patt):
        self.fname=fname
        self.patt=patt

    def __call__(self):
        pass

if __name__ == '__main__':
    fname='access.log'
    ip='(\d{1,3}\.){3}\d{3}'
    br='Chrome|Firefox|MISE'
    print(CountAccess(fname,ip))
    print()

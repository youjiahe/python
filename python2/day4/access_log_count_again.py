#!/usr/bin/env python3
from collections import Counter
import re
class CountAccess:
    def __init__(self,fname,patt):
        self.fname=fname
        self.patt=patt

    def __call__(self):
        c=Counter()
        cpatt=re.compile(self.patt)
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    c.update([m.group()])
        return c

if __name__ == '__main__':
    fname='access_log'
    ip='(\d{1,3}\.){3}\d{3}'
    br='Chrome|Firefox|MISE'
    ip_c=CountAccess(fname,ip)
    br_c=CountAccess(fname,br)
    print(ip_c().most_common(3))
    print(br_c().most_common(3))

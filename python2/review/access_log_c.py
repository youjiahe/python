#!/usr/bin/env python3
import pickle as p
from collections import Counter
import re
class CountIpBr:
    def __init__(self,fname,patt):
        self.fname=fname
        self.patt=patt
    def count(self):
        c=Counter()
        cpatt=re.compile(self.patt)
        with open(self.fname) as fobj:
            for line in fobj:
                l=cpatt.search(line)
                if l:
                    c.update([l.group()])
        return c

if __name__ == '__main__':
    ip='(\d{1,3}.){3}\d{1,3}'
    br='Chrome|Firefox|MISE'
    fname='access_log'
    c_ip=CountIpBr(fname,ip)
    c_br=CountIpBr(fname,br)
    print(c_ip.count().most_common(3))
    print(c_br.count())
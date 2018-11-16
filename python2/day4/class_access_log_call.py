#!/usr/bin/env python3
import re
class AccessLogCount:
    def __init__(self,fname,patt):
        self.fname=fname
        self.patt=patt

    def __call__(self):
        patt_dict={}
        cpatt=re.compile(self.patt)
        with open(self.fname) as  f:
            for line in f:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key,0) +1
        return patt_dict

if __name__ == '__main__':
    fname='access_log'
    ip = '(\d{1,3}\.){3}\d{1,3}'
    br = 'Chrome|Firefox|MSIE'
    ai_c=AccessLogCount(fname,ip)
    ab_c=AccessLogCount(fname,br)
    print(ai_c())
    print(ab_c())
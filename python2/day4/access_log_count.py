#!/usr/bin/env python3
import re
def count_patt(fname,patt):
    patt_dict={}
    cpatt=re.compile(patt)
    with open(fname) as f:
        for line in f:
            m = cpatt.search(line)
            if m:
                k=m.group()
                patt_dict[k] = patt_dict.get(k,0) +1
    return patt_dict

if __name__ == '__main__':
    fname='access_log'
    ip='(\d{1,3}\.){3}\d{1,3}'
    print(count_patt(fname,ip))
    br='Chrome|Firefox|MSIE'
    print(count_patt(fname,br))
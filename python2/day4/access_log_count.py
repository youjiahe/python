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

    #运行结果：
    # {'172.40.58.150': 10, '172.40.58.124': 6, '172.40.58.101': 10, '127.0.0.1': 121, '192.168.4.254': 103,
    #  '192.168.2.254': 110, '201.1.1.254': 173, '201.1.2.254': 119, '172.40.0.54': 391, '172.40.50.116': 244}
    # {'Chrome': 24, 'Firefox': 870, 'MSIE': 391}
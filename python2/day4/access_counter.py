#!/usr/bin/env python3
import re
from collections import Counter
class AccessLogCount:
    def __init__(self,fname,patt):
        self.fname=fname
        self.patt=patt

    def __call__(self):
        patt_dict={}
        cpatt=re.compile(self.patt)
        result = Counter()
        with open(self.fname) as  f:
            for line in f:
                m = cpatt.search(line)
                if m:
                    result.update([m.group()])
        return result


if __name__ == '__main__':
    fname='access_log'
    ip = '(\d{1,3}\.){3}\d{1,3}'
    br = 'Chrome|Firefox|MSIE'
    ai_c=AccessLogCount(fname,ip)
    ab_c=AccessLogCount(fname,br)
    print(ab_c())
    print(ai_c().most_common(3))  #返回最大的三个


#运行结果：   结果有排序
#Counter({'Firefox': 870, 'MSIE': 391, 'Chrome': 24})
#Counter({'172.40.0.54': 391, '172.40.50.116': 244, '201.1.1.254': 173, '127.0.0.1': 121, '127.0.0.1': 121})
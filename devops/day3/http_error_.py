#!/usr/bin/env python3
from urllib import request,error

url1='http://139.159.193.210/abc'  #不存在abc
url2='http://139.159.193.210/zz'  #权限700

try:
    request.urlopen(url1)
except error.HTTPError as e:
    print('错误:',e)

try:
    request.urlopen(url2)
except error.HTTPError as e:
    print('err:',e)

# 运行结果：
# 错误: HTTP Error 404: Not Found
# err: HTTP Error 403: Forbidden

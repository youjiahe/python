#!/usr/bin/env python3
from urllib import request
import json

citycode='101280101'  #广州城市代码
url_sk='http://www.weather.com.cn/data/sk/%s.html' % citycode
url_zs='http://www.weather.com.cn/data/zs/%s.html' % citycode
url_info='http://www.weather.com.cn/data/cityinfo/%s.html' % citycode

sk=request.urlopen(url_sk)
result=sk.read()
w = json.loads(result)
for keys in w['weatherinfo']:
    print('%s : %s' % (keys,w['weatherinfo'].get(keys)) )

#!/usr/bin/env python3
import re
date=re.sub('-','_','2018-11-19')
print(date)
da=re.split('-|\.','2018-1-8-9,hello.world')
print(da)
ip=re.search('(\d{1,3}\.){3}\d{1,3}','172.40.50.116 - - [03/Dec/2017:15:29:37 +0800] "GET /noindex/css/fonts/Light/OpenSans-Light.woff HTTP/1.1" 404 241 "http://172.40.50.116/noindex/css/open-sans.css" "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"')
print('ip:',ip.group())
url=re.search('\"(http.+?)\"','172.40.50.116 - - [03/Dec/2017:15:29:37 +0800] "GET /noindex/css/fonts/Light/OpenSans-Light.woff HTTP/1.1" 404 241 "http://172.40.50.116/noindex/css/open-sans.css" "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"')
print('url:',url.group())
ip=re.match('(\d{1,3}\.){3}\d{1,3}','172.40.50.116 - - [03/Dec/2017:15:29:37 +0800] "GET /noindex/css/fonts/Light/OpenSans-Light.woff HTTP/1.1" 404 241 "http://172.40.50.116/noindex/css/open-sans.css" "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"')
print(ip.group())
ip=re.findall('\d','172.40.50.116 - - [03/Dec/2017:15:29:37 +0800] "GET /noindex/css/fonts/Light/OpenSans-Light.woff HTTP/1.1" 404 241 "http://172.40.50.116/noindex/css/open-sans.css" "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"')
print(ip)
ip=re.finditer('\d','172.40.50.116 - - [03/Dec/2017:15:29:37 +0800] "GET /noindex/css/fonts/Light/OpenSans-Light.woff HTTP/1.1" 404 241 "http://172.40.50.116/noindex/css/open-sans.css" "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0"')
for i in ip:
    print(i.group(),sep='',end='')
print()
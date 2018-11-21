#!/usr/bin/env python3
#使用默认浏览器访问百度，并且搜索'你好'
from urllib import request
import webbrowser
quote=request.quote('你好')
url='https://www.baidu.com/s?wd=' + quote
webbrowser.open_new_tab(url)
# coding=utf-8
# 添加头信息

import urllib2
import random

url = "http://www.itcast.cn"
url_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
]

user_agent = random.choice(url_list)

request = urllib2.Request(url)

request.add_header('User-Agent', user_agent)

request.get_header('User-Agent')

response = urllib2.urlopen(request)

html = response.read()

print html
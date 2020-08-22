# coding=utf-8
# 向爬虫请求信息添加一个特定的头信息
import urllib2

url = "http://www.itcast.cn"
# IE的User-Agent
user_agent = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"} 
request = urllib2.Request(url, headers = user_agent)
# 通过调用Request.add_header()添加或修改一个特定的header
'''
request.add_header("Connection", "keep-alive")
'''

response = urllib2.urlopen(request)
html = response.read()
print html
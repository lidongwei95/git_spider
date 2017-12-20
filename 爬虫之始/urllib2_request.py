import urllib2

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
html = response.read()
print html
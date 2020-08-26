# coding=utf-8
# 编写一个小程序爬取当下lol贴吧整体内容
# http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=0
import urllib
import urllib2


def loadPage(url, filename):
	"""
	根据url发送请求,获取服务器相应文件
	"""
	print "loading" + filename
	headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
	request = urllib2.Request(url = url, headers = headers)
	response = urllib2.urlopen(request)
	html = response.read()
	return html

def writePage(html, filename):
	"""
	将爬去到的文件html保存到本地
	"""
	print "downloding" + filename
	with open(filename, "w") as f:
		f.write(html)
	print "-" * 44


def tiebaSpider(url, beginpage, endpage):
	"""
	处理ｕｒｌ，分配每个ｕｒｌ去发送请求
	"""
	for page in range(beginpage, endpage+1):
		pn = (page-1)*50

		filename = "第" + str(page) + "页.html"	
		# 组合成完整的url并且每次pn值50递增
		fullurl = url + "&pn=" + str(page)
		# 调用函数发送请求获取HTML页面
		html = loadPage(fullurl, filename)
		# 将获取到的HTML页面写入本地磁盘中
		writePage(html, filename)



if __name__ == '__main__':
	#　输入爬取信息相关
	kw = raw_input("请输入要爬去的贴吧名：")
	beginpage = int(raw_input("请输入起始页"))
	endpage = int(raw_input("请输入终止页"))
	url = "http://tieba.baidu.com/f?"
	key = urllib.urlencode({'kw':kw})
	url = url + key

	tiebaSpider(url, beginpage, endpage)

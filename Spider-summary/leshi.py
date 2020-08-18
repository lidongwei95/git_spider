# -*- coding: utf-8 -*-

import urllib
import requests
import json
from lxml import etree
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')


class Leshi(object):
	def __init__(self):
		self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
		self.num = 0
		self.items = []

	def send_request(self):
		keyword = {"c":"1",
			"d":"1",
			"md":"",
			"o":"2",
			"p":self.num,
			"s":"1"
			}
		key_str = urllib.urlencode(keyword)
		link = 'http://list.le.com/apin/chandata.json?' + key_str
		print "*"*44
		response = requests.get(link, headers=self.headers)
		html = json.loads(response.text)
		return html

	def parse_page(self,html):
		movie_list = html['album_list']
		for movie in movie_list:
			item = {}
			item['name'] = movie['name']
			item['playCount'] = movie['playCount']
			item['rate'] = movie['rating']
			item['commant'] = movie['subname']
			# item['zhuyan'] = ','.join([ actor for actor in movie['starring'].values()])  # 加上后转换csv格式会出错
			self.items.append(item)

			with open("movie.json", "a") as f:
				content = json.dumps(dict(item), ensure_ascii=False) + ".\n"
				f.write(content)

	def start_work(self,):
		while self.num < pagenum:
			html = self.send_request()
			self.parse_page(html)
			self.num += 1

if __name__ == '__main__':
	leshi = Leshi()
	pagenum = int(raw_input("输入要爬取的页数："))
	leshi.start_work()
	

# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem

# https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw=python&p=1&isadv=0

# http://sou.zhaopin.com/jobs/
# searchresult.ashx?jl=%e9%80%89%e6%8b%a9%e5%9c%b0%e5%8c%ba&kw=python&isadv=1&sg=18e7dad7022649868108978516ae2d70&p=7

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%80%89%E6%8B%A9%E5%9C%B0%E5%8C%BA&kw=python&isadv=1&sg=18e7dad7022649868108978516ae2d70&p=1']

    def parse(self, response):
        itemlist = response.xpath('//div[@class="newlist_main"]//table[@class="newlist"]')[1:]
        for each in itemlist:
            item = MyspiderItem()
            item['salary'] = each.xpath('./tr/td[@class="zwyx"]/text()').extract_first()
            item['area'] = each.xpath('./tr/td[@class="gzdd"]/text()').extract_first()

            print 'loading...'
            yield item

        if response.xpath('//li[@class="pagesDown-pos"]/a').extract_first():
            url = response.xpath('//li[@class="pagesDown-pos"]/a/@href').extract_first()
            yield scrapy.Request(url, callback=self.parse)


            



# //div[@class="newlist_main"]//ul/li/a[@class="next-page"] 下一页


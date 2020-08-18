# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from mySpider.items import MyspiderItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MyspiderPipeline(object):
    # 写入职位列表数据
    def open_spider(self, spider):
        self.filename = open("zhilian.json", "w")

    def process_item(self, item, spider):        
        # 以中文存储到json文件
        content=json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(content)
        return item

    def close_item(self, spider):
        self.filename.close()

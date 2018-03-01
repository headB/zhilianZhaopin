# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import json

class ZhaopinPipeline(object):

	def __init__(self):
		self.content = []

	def process_item(self, item, spider):
		self.content.append(dict(item))
		return item

	def close_spider(self,spider):
		with open('jobs1.json','w') as file2:
			file2.write(json.dumps(self.content,indent=4))
		print('hello world!')


class ExamplePipeline(object):
	def process_item(self, item, spider):
		#utcnow() 是获取UTC时间
		item["crawled"] = datetime.utcnow()
		# 爬虫名
		item["spider"] = spider.name
		return item
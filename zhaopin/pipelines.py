# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import json

class ZhaopinPipeline(object):
    def process_item(self, item, spider):

        with open('jobs.json','a') as file1:
            content = json.dumps(dict(item),) + "\n"
            file1.write(content)
        #print(type(item))

        return item

class ExamplePipeline(object):
    def process_item(self, item, spider):
        #utcnow() 是获取UTC时间
        item["crawled"] = datetime.utcnow()
        # 爬虫名
        item["spider"] = spider.name
        return item
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from  scrapy import Item,Field


class ZhaopinItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    title = Field()
    url = Field()
    jobName = Field()
    company = Field()
    salary = Field()
    crawled = Field()
    spider = Field()
    #salary = Field()


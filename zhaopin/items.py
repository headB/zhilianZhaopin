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
    #1职位要求
    jobName = Field()
    #2公司名
    company = Field()
    #3工作地点
    location = Field()
    #4学历要求
    backGroup = Field()
    #5薪资
    salary = Field()
    #6公司规模
    scale = Field()
    #7任职要求
    require = Field()
    #8任职经验
    experience = Field()
    #9企业性质
    enterprise = Field()

    #10关于这个职位的详情页.!!
    detail = Field()

    linkUrl = Field()

    crawled = Field()
    spider = Field()
    #salary = Field()


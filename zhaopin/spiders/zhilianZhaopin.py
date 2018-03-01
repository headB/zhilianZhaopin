# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from zhaopin.items import ZhaopinItem

##添加去重!!
from scrapy.dupefilters import RFPDupeFilter

class ZhilianzhaopinSpider(CrawlSpider):
	name = "zhilianZhaopin"
	allowed_domains = ["zhaopin.com"]
	start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E4%B8%9C&kw=java&sm=0&p=1']
	rules = (Rule(LinkExtractor(),callback='afterProcess',),)


	def afterProcess(self,response):
		#print("hello world!!")
		title = response.xpath("//title/text()").extract()[0]
		items = ZhaopinItem()
		items['title'] = title

		yield items
	#def parse(self, response):
		#pass

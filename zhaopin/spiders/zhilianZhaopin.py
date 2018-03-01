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
	rules = (
		Rule(LinkExtractor(),callback='afterProcess',),
		Rule(LinkExtractor(),callback='processingThisPage',),

			 )

	def processingThisPage(self):
		pass

	def afterProcess(self,response):
		title = response.xpath("//title/text()").extract()[0]
		items = ZhaopinItem()
		items['title'] = title
		items['url'] = response.url

		items['title'] = title
		# 1职位要求
		items['jobName'] = title
		# 2公司名
		items['company'] = title
		# 3工作地点
		items['location'] = title
		# 4学历要求
		items['backGroup'] = title
		# 5薪资
		items['salary'] = title
		# 6公司规模
		items['scale'] = title
		# 7任职要求
		items['require'] = title
		# 8任职经验
		items['experience'] = title
		# 9企业性质
		items['enterprise'] = title

		yield items
	#def parse(self, response):
		#pass
	def getJobName(self):
		pass


	def getCompany(self):
		pass


	def getLocation(self):
		pass

	def getBackGroup(self):
		pass


	def getSalary(self):
		pass


	def getScale(self):
		pass

	def getRequire(self):
		pass


	def getExperience(self):
		pass


	def getEnterprise(self):
		pass


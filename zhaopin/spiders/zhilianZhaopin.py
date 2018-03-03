# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from zhaopin.items import ZhaopinItem
from scrapy_redis.spiders import CrawlSpider
#from scrapy_redis.spiders import RedisCrawlSpider

##添加去重!!
from scrapy.dupefilters import RFPDupeFilter


##尝试一下直接改装.!!redisCrawlSpider
##不不,是尝试一下用scrapy_redis的普通crawlSpider,据说有分布式功能.!!
class ZhilianzhaopinSpider(CrawlSpider):
	name = "zhilianZhaopin"
	allowed_domains = ["zhaopin.com"]
	start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E4%B8%9C&kw=java&sm=0&p=1']
	rules = (
		Rule(LinkExtractor(allow=('kw=java&sm=0&p=1')),callback='processingThisPage',),
		#Rule(LinkExtractor(allow=('https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E4%B8%9C&kw=java&sm=0&p=1')),callback='processingThisPage',follow=True),

			 )

	def processingThisPage(self,response):
		print(response.url)
		print(response.xpath("//title/text()"))
		tables = response.xpath('//div[@id="newlist_list_content_table"]/table')
		#table1 = response.xpath('//div[@id="newlist_list_content_table"]')


		#for x in tables:
		#	print(x.xpath("string(.)"))
		item = []
		#return True
		for x in tables:
			items = ZhaopinItem()
			x1 = x.xpath(".//tr[1]/td[1]/div/a[1]//text()").extract()
			items['jobName'] = ''.join(x1)

			x1 = x.xpath(".//tr[1]/td[3]//text()").extract()
			items['company'] = ''.join(x1)

			x1 = x.xpath(".//tr[1]/td[4]//text()").extract()
			items['salary'] = ''.join(x1)

			yield items


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
	def getJobName(self,response):
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


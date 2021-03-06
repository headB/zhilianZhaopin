# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from zhaopin.items import ZhaopinItem
from scrapy_redis.spiders import CrawlSpider
from scrapy_redis.spiders import RedisCrawlSpider
import requests
from lxml import etree

#from scrapy_redis.spiders import RedisCrawlSpider

##添加去重!!
from scrapy.dupefilters import RFPDupeFilter


##尝试一下直接改装.!!redisCrawlSpider
##不不,是尝试一下用scrapy_redis的普通crawlSpider,据说有分布式功能.!!
class ZhilianzhaopinSpider(CrawlSpider):


	name = "zhilianZhaopin"
	allowed_domains = ["zhaopin.com"]

	start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%B9%BF%E4%B8%9C&kw=java&sm=0&p=1']
	#redis_key = 'zhaopin:start_urls'

	rules = (
		#处理本页面可以用其他的方式提取的,下面展示另外一种方式
		Rule(LinkExtractor(restrict_xpaths=(r'//div/table//tr/td/div/a[1]')),callback='processJobDetail',follow=True),
		##下面这个匹配所有的下一页或者具体的数字页面
		Rule(LinkExtractor(allow=(r'ashx\?jl=%e5%b9%bf%e4%b8%9c&kw=java&sm=0&sg=.+&p=\d+')),follow=True),
	)




		##首先上面匹配到入口网址或者下一页之后,回调下面这个函数
	def detectJobDetail(self,response):
		print(response.xpath("//title"))
		tables = response.xpath('//div[@id="newlist_list_content_table"]/table')
		print(len(tables))
		tables = tables[1:]
		print(len(tables))
		for x in tables:
			detailUrl = x.xpath(".//tr[1]/td[1]/div/a[1]/@href").extract()
			if detailUrl:
				print(detailUrl[0])
				yield scrapy.Request(detailUrl[0],callback=self.processJobDetail)



	##这个函数就用于解析获取到每一页里面所有的职位详情的URL(每一页估计都有60个职位)
	def processJobDetail(self,response):
		items = ZhaopinItem()
		x = response.xpath("/html/body/div[6]/div[1]")
		# 职位名称
		x1 = x.xpath("/html/body/div[5]/div[1]/div[1]/h1//text()").extract()
		items['jobName'] = ''.join(x1)
		# 公司名字
		x1 = x.xpath("/html/body/div[5]/div[1]/div[1]/h2//text()").extract()
		items['company'] = ''.join(x1)
		# 工资待遇
		x1 = x.xpath("ul/li[1]//text()").extract()
		items['salary'] = ''.join(x1)
		# 工作地点
		x1 = x.xpath("ul/li[2]//text()").extract()
		items['location'] = ''.join(x1)
		# 企业性质
		x1 = x.xpath("/html/body/div[6]/div[2]/div[1]/ul/li[2]//text()").extract()
		items['enterprise'] = ''.join(x1)
		# 公司规模
		x1 = x.xpath("/html/body/div[6]/div[2]/div[1]/ul/li[1]//text()").extract()
		items['scale'] = ''.join(x1)
		# 需要的工作经验
		x1 = x.xpath("ul/li[5]//text()").extract()
		items['experience'] = ''.join(x1)
		# 学历需求
		x1 = x.xpath("ul/li[6]//text()").extract()
		items['backGroup'] = ''.join(x1)
		# 具体职业要求
		#x1 = x.xpath("ul/li[1]//text()").extract()
		#items['require'] = ''.join(x1)

		x1 = x.xpath("/html/body/div[6]/div[1]/div[1]/div/div[1]//text()").extract()
		x2 = ''.join(x1)
		x2 = x2.replace(' ','')
		x2 = x2.replace('\r\n','')
		items['detail'] = x2

		##该页具体的原始url地址
		items['linkUrl'] = response.url

		yield items


	def processingThisPage(self,response):
		print(response.url)
		print(response.xpath("//title/text()"))
		tables = response.xpath('//div[@id="newlist_list_content_table"]/table')

		##看看能不能设置一个优先设置,去删除某些元素.看看.!!

		for x in tables:
			items = ZhaopinItem()

			#职位名称
			x1 = x.xpath(".//tr[1]/td[1]/div/a[1]//text()").extract()
			items['jobName'] = ''.join(x1)
			#公司名字
			x1 = x.xpath(".//tr[1]/td[3]//text()").extract()
			items['company'] = ''.join(x1)
			#工资待遇
			x1 = x.xpath(".//tr[1]/td[4]//text()").extract()
			items['salary'] = ''.join(x1)
			#工作地点
			x1 = x.xpath(".//tr[1]/td[5]//text()").extract()
			items['location'] = ''.join(x1)
			#企业性质
			x1 = x.xpath(".//tr[2]/td/div/div/ul/li[1]/span[2]//text()").extract()
			items['enterprise'] = ''.join(x1)
			#公司规模
			x1 = x.xpath(".//tr[2]/td/div/div/ul/li[1]/span[3]//text()").extract()
			items['scale'] = ''.join(x1)
			#需要的工作经验
			x1 = x.xpath(".//tr[2]/td/div/div/ul/li[1]/span[4]//text()").extract()
			items['experience'] = ''.join(x1)
			#学历需求
			x1 = x.xpath(".//tr[2]/td/div/div/ul/li[1]/span[5]//text()").extract()
			items['backGroup'] = ''.join(x1)
			#具体职业要求
			x1 = x.xpath(".//tr[2]/td/div/div/ul/li[2]//text()").extract()
			items['require'] = ''.join(x1)


			#相信这里还需要一个函数来处理收集详细的职业要求和公司工作环境需求.!!#公司介绍

			##测试一下scrapy的request先.
			detailUrl = x.xpath(".//tr[1]/td[1]/div/a[1]/@href").extract()

			if not detailUrl:
				continue

			yield  scrapy.Request(detailUrl[0],callback=self.loadDetailPage)
			#items['detail'] = self.manualGetHtml(detailUrl[0])


			#print(self.tracer)
			yield items



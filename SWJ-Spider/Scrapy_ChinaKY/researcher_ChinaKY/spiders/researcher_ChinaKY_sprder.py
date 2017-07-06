# -*- coding: utf-8 -*-
import scrapy
from researcher_ChinaKY.items import ResearcherChinakyItem

#base_url = 'http://www.chinakaoyan.com'


class ResearcherChinakySprderSpider(scrapy.Spider):
    name = "researcher_ChinaKY_sprder"

    # allowed_domains = ["http://www.chinakaoyan.com/graduate/InfoList/class/ds/schoolID/82.shtml"]
    # start_urls = ['http://http://www.chinakaoyan.com/graduate/InfoList/class/ds/schoolID/82.shtml/']

    def parse(self, response):


        #中国考研网
        #researcher_lists = response.xpath('//div[@class="w500 fl ml20"]//div[@class="list"]//a//@href').extract()
       # researcher_nextpaper_url = response.xpath(
        #    u'//div[@class="w500 fl ml20"]//div[@class="list"]//div[@class="page font16"]//a[@title="后一页"]//@href')

        #考研帮
        researcher_lists = response.xpath('//div[@class="waper"]//div[@class="main"]//ul[@class="subList"]//a//@href').extract()

        researcher_nextpaper_url = response.xpath(
            u'//div[@class="waper"]//div[@class="main"]//div[@class="tPage"]//a[contains(text(),"下一页")]//@href')

        for nextpaper_url in researcher_nextpaper_url.extract():
            # 中国考研网
            #yield scrapy.Request(base_url+nextpaper_url)
            # 考研帮
            yield scrapy.Request(nextpaper_url)

        for researcher in researcher_lists:
            # 中国考研网
            #yield scrapy.Request(base_url + researcher, callback=self.get_researcher)
            # 考研帮
            yield scrapy.Request(researcher, callback=self.get_researcher)




    def get_researcher(self, response):
        # 中国考研网
        #researcher_url_name = response.xpath('//div[@class="w660 fl"]/h3/text()').extract()[0]
        #researcher_url_masseges = response.xpath('//div[@class="arc-body font14"]/p//text()').extract()
        # 考研帮
        researcher_url_name = response.xpath('//div[@class="waper"]//div[@class="article"]/h1[@class="articleTitle"]/text()').extract()
        researcher_url_masseges = response.xpath('//div[@class="waper"]//div[@class="articleCon"]/p//text()').extract()

        item=ResearcherChinakyItem()

        item['research_name'] = researcher_url_name
        item['university'] = self.university
        item['research_messages'] = researcher_url_masseges

        return item



    def __init__(self, start_url='', domain='', university='', **kwargs):
        super(ResearcherChinakySprderSpider, self).__init__(**kwargs)
        self.start_urls = [start_url]
        self.allowed_domains = [domain]
        self.university = university

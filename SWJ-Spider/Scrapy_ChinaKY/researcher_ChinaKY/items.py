# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ResearcherChinakyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    university = scrapy.Field()  # 学校
    research_name = scrapy.Field()  # 学者姓名
    research_messages = scrapy.Field()  # 学者信息


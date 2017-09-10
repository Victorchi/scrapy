# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JournalItem(scrapy.Item):
    '''
    期刊种子item
    '''
    url = scrapy.Field()
    title = scrapy.Field()
    vendor = scrapy.Field()
    id = scrapy.Field()


class ContentItem(scrapy.Item):
    '''
    文章item
    '''
    url = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    vendor = scrapy.Field()
    id = scrapy.Field()
    year = scrapy.Field()
    issue = scrapy.Field()


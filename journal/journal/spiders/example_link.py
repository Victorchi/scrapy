# -*- coding: utf-8 -*-
import scrapy
from journal.items import JournalItem
import re
from scrapy.linkextractors import LinkExtractor
from  scrapy.spiders import CrawlSpider, Rule
from journal.dbtuils import MySQLHelper


class ExampleLinkSpider(CrawlSpider):
    name = 'example_link'
    custom_settings = {
        'ITEM_PIPELINES': {
            'journal.pipelines.JournalPipeline': 299,
        }
    }
    start_urls = [
        'http://www.cqvip.com/data/main/search.aspx?action=so&tid=7&k=&w=&o=&mn=&issn=&cnno=&rid=0&c=&gch=&cnt=&curpage=%s&perpage=0' % p
        for p in range(1, 946)]

    def parse(self, response):
        item = JournalItem()
        movies = response.xpath('//ul/li')
        for movie in movies:
            item['title'] = movie.xpath(
                'table/tr[2]/th/a/text()').extract()
            item['vendor'] = 'cqvip'
            url = movie.xpath('table/tr[2]/th/a/@href').extract()[0]
            url = str(re.sub('\\"','',url).replace('\\',''))
            if self.checkURL(url):
                continue
            item['url'] = url
            item['id'] = 1
            yield item

    def checkURL(self, url):
        '''
        校验是否保存该页面的link
        :param url:
        :return:
        '''

        sql = 'select searchcode from journals WHERE url="%s"' % url
        result = MySQLHelper().find_all(sql)
        if result is None or len(result) < 1:
            return False
        else:
            return True

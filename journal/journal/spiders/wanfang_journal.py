# -*- coding: utf-8 -*-
import scrapy
from journal.items import JournalItem
import re
from scrapy.linkextractors import LinkExtractor
from  scrapy.spiders import CrawlSpider, Rule
from journal.dbtuils import MySQLHelper


class WanfangJouranlSpider(CrawlSpider):
    name = 'wanfang_journal'
    custom_settings = {
        'ITEM_PIPELINES': {
            'journal.pipelines.JournalPipeline': 299,
        }
    }
    _list1 = ['A', 'B',]
    start_urls = ['http://c.wanfangdata.com.cn/PeriodicalLetter.aspx?NodeId={p1}&PageNo='
                  '{p2}'.format(p1=n, p2=p) for n in _list1 for p in range(1, 5)]

    def parse(self, response):
        item = JournalItem()
        movies = response.xpath('//div[@class="list"]/span')
        print 'movies:',movies,type(movies)
        for movie in movies:
            item['title'] = movie.xpath(
                'a[@class="link"]/text()').extract()
            item['vendor'] = 'wanfang'
            url = movie.xpath('a[@class="link"]/@href').extract()[0]
            url = 'http://c.wanfangdata.com.cn/'+str(url)
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

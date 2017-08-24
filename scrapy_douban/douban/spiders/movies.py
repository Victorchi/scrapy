# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from douban.items import DoubanItem


class MoviesSpider(scrapy.Spider):
    name = 'notes'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }


    def start_requests(self):
        urls = ['https://book.douban.com/tag/%E5%A4%96%E5%9B%BD%E6%96%87%E5%AD%A6',
               'https://book.douban.com/tag/%E5%A4%96%E5%9B%BD%E6%96%87%E5%AD%A6']
        for url in urls:
            yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath(".//*[@id='subject_list']/ul/li")
        for movie in movies:
            item['title'] = movie.xpath(
                "div[2]/h2/a/text()").extract()
            item['article'] = movie.xpath(
                "div[2]/div[1]/text()").extract()
            item['quote'] = movie.xpath("div[2]/p/text()").extract()
            item['star'] = movie.xpath(
                "div[2]/div[2]/span[2]/text()").extract()
            item['num'] = movie.xpath("div[2]/div[2]/span[3]/text()").extract()
            item['link'] = movie.xpath("div[2]/h2/a/@href").extract()
            yield item

        next_url1 = response.xpath(".//*[@id='subject_list']/div[2]/span[4]/a/@href").extract()
        next_url2 = response.xpath(".//*[@id='subject_list']/div[2]/span[5]/a/@href").extract()

        for next_url in [next_url1, next_url2]:
            if next_url:
                next_url = 'https://book.douban.com' + next_url[0]
                print "this is:", next_url, '-------------------------------------------------'
                yield Request(next_url, headers=self.headers)

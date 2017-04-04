
# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from douban.items import DoubanItem


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }


    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url,headers=self.headers)

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//div[@class="info"]')
        for movie in movies:
            item['title'] = movie.xpath(
                'div[@class="hd"]/a/span[1]/text()').extract()
            item['movieInfo'] = movie.xpath(
                'div[@class="bd"]/p/text()').extract()
            item['quote'] = movie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            item['star'] = movie.xpath(
                'div[@class="bd"]/div[@class="star"]/span[2]/text()').extract()
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            print "this is:",next_url
            yield Request(next_url,headers=self.headers)
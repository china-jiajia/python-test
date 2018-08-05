# -*- coding: utf-8 -*-
import scrapy


class JiajiaSpider(scrapy.Spider):
    name = 'jiajia'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass

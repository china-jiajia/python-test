#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


import scrapy
from first.items import FirstItem

class jiajiaSpider(scrapy.Field):
    name= "jiajia"
    allowed_domains = ["baidu.com"]
    start_urls = ('http://www.baidu.com/',)

    def parse(self,response):
        item=FirstItem()
        item["content"]=response.xpath("/html/head/title/text()").extract()
        yield item
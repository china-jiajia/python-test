#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

from scrapy.spider import Spider

class FirstSpider(Spider):
    name="first"
    allowed_domains=["baidu.com"]
    start_urls=["http://www.baidu.com"]
    def parse(self,response):
        pass
    
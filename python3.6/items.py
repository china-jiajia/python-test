#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

import scrapy

# class FirstItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()


class FirstItem(scrapy.Item):
    content=scrapy.Field()
    link=scrapy.Field()
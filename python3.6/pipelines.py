#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


class FirstPipeline(object):
    def process_item(self,item,spider):
        print(item["contennt"])
        return item
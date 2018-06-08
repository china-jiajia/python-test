#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
import jinja2


links = [{'title': u'杭州地铁三期规划真是获批 3 号线即将上马','href':'http://zzhz.zjol.com.cn/system/2016/12/21/021404496.shtml'},
         {'title': u'涉及房地产的四个关键点','href':'http://zzhz.zjol.com.cn/system/2016/12/19/021402558.shtml'},
         {'title': u'潮鸣项目定名"凤起潮鸣",绿城说的"杭州生活样本"将如何呈现','href':'http://zzhz.zjol.com.cn/system/2016/12/19/021402558.shtml'}]


content = render('hzfc.html',items=links)
print(content)

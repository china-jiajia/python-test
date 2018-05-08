#!/usr/bin/env python 
# -*- coding: utf-8 -*-


tpl = 'percent %.2f %%' % 99.976234444444
print(tpl)

tpl1 = "i am %(name)s sex:%(sex)s age:%(age)d" % {"name":"laowang","sex":"male","age":68}
print(tpl1)


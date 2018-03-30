#!/usr/bin/env python
# -*- coding utf8 -*-

# 字典当中可以包含列表，包含字典或者更多的元素，字典当中的元素是无序存在的
# a_list = [1,2,3,4,5,4]
# d = {'apple':1,'pear':2,'orange':3}
# d2 = {1:'a','c':'b'}
#
# # 打印字典和列表
# print(d['apple'])
# print(a_list[0])
#
# # 删除字典里面的元素
# del d['pear']
# print(d)
#
# # 添加元素
# d['b'] = 30
# print(d)


a_list = [1,2,3,4,5,4]
d = {'apple':[1,2,3],'pear':{1:3,3:'a'},'orange':3}

print(d)
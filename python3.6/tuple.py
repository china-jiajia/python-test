#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao



#元祖(元素不可被修改,不能增加或者删除)
# tu = (11,22,33,44)
# 一般写元祖的时候,最后面添加一个逗号','

# 1.书写格式
# 2.索引
# 3.切片
# 4.可以被for循环,可迭代
# 5.可以被转换
# 6.元祖是有序的
# 7.元祖的一级元素不可修改、删除、增加

#索引
# v = tu[0]
# print(v)

# #切片
# v = tu[0:2]
# print(v)


#可以被for循环;可迭代对象
# for item in tu:
#     print(item)



#字符串、列表、元祖转换
# str
# list
# tuple

# s = "adageg2"
# li = ["wetvda","jp[i23fjej"]
# tu = ("2yehi2","vjcahjkls")

# v = tuple(s)
# print(v)

# v = tuple(li)
# print(v)

# v = list(tu)
# print(v)

# v = "_".join(tu)
# print(v)

# li = ["asdf","asdfasdf"]
# li.extend((11,22,33,))
# print(li)

#元祖的一级元素不可修改、删除、增加
# tu = (111,"alex",(11,22),[(33,44)],True,33,44)
# # #元祖,有序
# # v = tu[3][0][0]
# # print(v)
#
# tu[3][0] = 567
# print(tu)


#tu.count(22) 获取指定元素在在元祖中出现的次数

#tu.index(22) 获取元祖中指定元素的位置


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


#字典
# 1.字典结构(key:value)
# 2.字典的value可以是任何值
# 3.列表、字典不能作为字典的key
# 4.字典是无序的
# 5.字典是支持for循环
# 6.字典支持删除
# 7.通过索引的方式找到字典元素
# 8.key重复的话只能保留一个(布尔值可以为key)
# 9.keys() values() items() get update

# info = {"k1":"v1","k2":"v2"}


#字典的vlue可以是任何值
# info = {
#     "k1":18,
#     "k2":True,
#     "k3":[
#         11,
#         22,
#         33,
#         {
#             "kk1":"vv1",
#             "kk2":"vv2",
#             "kk3":(11,22),
#         }
#     ],
#     "k4":(11,22,33,44)
# }
#
# print(info)


#布尔值、列表、字典不能作为字典的key
# info = {
#     1:'asdf',
#     "k1":'asfd',
#     True:"123",
#     # [11,22]:123,
#     (11,22):123,
#     # {'k1':'v1'}:123
# }
#
# print(info)


#字典是无序
info = {
    "k1":18,
    "k2":True,
    "k3":[
        11,
        22,
        33,
        {
            "kk1":"vv1",
            "kk2":"vv2",
            "kk3":(11,22),
        }
    ],
    "k4":(11,22,33,44)
}

# print(info)

# v = info['k1']
# print(v)

# 通过索引的方式找到指定元素
# v = info['k3'][3]['kk3'][0]
# print(v)

#支持del 删除
# del  info['k3'][3]['kk3']
# print(info)


#for循环(默认for循环只能拿到key)
# for item in info:
#     print(item)

# for item in info.keys():
#     print(item)
#
#
# for vale in info.values():
#     print(vale)

#key 和value同时输出
# for k,v in  info.items():
#     print(k,v)

# clear
# copy
# fromkeys
# items
# keys
# values



#formkeys 会在内部进行循环;根据序列来创建字典,并制定统一的值
# v = dict.fromkeys(["k1",123,"999"],123)
# print(v)


# 根据key获取值,key不存在时可以指定默认值(None)
# dic = {
#     "k1":"v1"
# }
#
# # v = dic['k1']
# # print(v)
#
# v = dic.get('k11',11111)
# print(v)


#删除并获取值
# dic = {
#     "k1":"v1",
#     "k2":"v2"
# }

##指定某一个key删除
# v = dic.pop('k1',)
# print(dic,v)

# v = dic.pop('k11',90)   #指定默认值
# print(dic,v)

##随机删除
# v = dic.popitem()
# print(dic,v)


#设置值,已存在不设置,获取当前key对应的值,不存在设置,获取当前对应key的值
# dic = {
#     "k1":"v1",
#     "k2":"v2"
# }
#
# v = dic.setdefault('k1111','123')
# print(dic,v)



#更新
# dic = {
#     "k1":"v1",
#     "k2":"v2"
# }
#
# # dic.update({'k1':'11111','k3':123})
# dic.update(k1=123,k3=456,k5="adfda")  #**kwargs
# print(dic)




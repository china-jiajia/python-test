#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


# li = [1,12,9,"age",["石振文",["9",10],"庞麦郎"],"alex",True]

# 1.列表格式
# 2.列表可以嵌套任何类型
# 3.可以通过索引取值
# 4.可以进行切片取值
# 5.可以for循环
# 6.可以被修改和删除
#     索引
#     切片
# 7.支持 in 操作
# 8.列表是有序的,元素可以被修改


# 获取:
#     索引
#     切片
#     for 循环
#
# 修改:
# 索引方式
# li[1]=120
# print(li)
# li[1]=[11,22,33,44]
# print(li)

#切片
# li[1:3]= [120,90]
# print(li)


#删除:
# #索引方式
# del li[1]
# print(li)
#
# #切片方式
# del li[2:6]
# print(li)

#in 操作
# v = 12 in li
# v1 = 120 in li
# print(v,v1)


#字符串转换列表,内部使用for循环
# s = 'dafewg2fwejlksdifjw'
#
# new_li = list(s)
# print(new_li)
#
# for i in s:
#     print(i)



#列表转换成字符串
#需要自己写for新年换呢一个一个处理;既有数字又有字符串
# li = [11,22,33,"123","alex"]

# r = str(li)
# print(r)

# s = ""
# for i in li:
#     s = s + str(i)
# print(s)


#直接使用字符串join方法: 列表中的元素只有字符串
# li = ["123","alex"]
# v = "".join(li)
# print(v)



# list：是一个类
# li是list中的一个对象,他所具备的功能
# list类中提供的方法


#li对象调用append方法#
# li = [11,22,33,44]
#原来值最后追加
# ll = li.append(5)
# print(ll)   #字符串不能直接进行修改
# li.append("alex")
# li.append([123,567])
# print(li)


#清空列表
# li.clear()
# print(li)

#浅拷贝
# v = li.copy()
# print(v)

#计算元素出现的次数
# v = li.count(22)
# print(v)

#列表扩展
# li = [11,22,33,44]
# # li.extend([9898,"不得了"])
# # print(li)
# li.extend("不得了")
# print(li)

#获取当前值索引位置(最左优先)
# li = [11,22,33,22,44]
# v = li.index(22)
# print(v)

#在指定索引位置插入元素
# li = [11,22,33,22,44]
# li.insert(0,99)
# print(li)


#删除某个值,并获取被删除的值(如果没有指定索引位置默认是最后一个)
# li = [11,22,33,22,44]
# v = li.pop()
# print(li)
# print(v)
#
# li = [11,22,33,22,44]
# v = li.pop(3)
# print(li)
# print(v)


#删除列表中的指定值,左边优先
# li = [11,22,33,22,44]
# li.remove(22)
# print(li)

#PS: pop remove del li[0]  del[7:9] clear

#将当前列表进行翻转
# li = [11,22,33,22,44]
# li.reverse()
# print(li)

#列表排序
# li = [11,22,44,33,22]
# li.sort()     #正序排序
# print(li)

# li.sort(reverse=True)     #倒序排序
# print(li)

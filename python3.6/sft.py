#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


# expandtabs,断句20
# test = "username\temail\tpassword\tjiajiatao\t526453770@qq.com\ttemail\tpassword\tjiajiatao\t526453770@qq.com"

# v = test.expandtabs(20)
# print(v)


#判断当前输入是否是数字
# test = "123"
# test = "②"    #1 ,②
# test = "二"
# v1 = test.isdecimal()
# v2 = test.isdigit()
# v3 = test.isnumeric()
# print(v1,v2,v3)


#字母，数字，下划线:标识符 def class
# a = "def"
# v = a.isidentifier()
# print(v)

#是否存在不可显示的字符
# test = "hiopget2ohshtio"
# test = "hiopget\n2ohshtio"
# v = test.isprintable()
# print(v)


#判断是否全部是空格
# test= " "
# v = test.isspace()
# print(v)


#判断是否是标题
# test = "Rcturn True if all cased characters is S are uppercase and there is"
# v1 = test.istitle()
# print(v1)
# v2 = test.title()
# print(v2)
# v3 = v2.istitle()
# print(v3)


#将字符串中的每一个元素按照指定分隔符进行拼接
# test = "你是风儿我是沙"
# print(test)
# t = ' '
# v1 = t.join(test)
# v ="_".join(test)
# print(v1,v)


#设置宽度,并将内容居中
# test = "alex"
# v1 = test.center(20,"中")
# v2 = test.ljust(20,"*")
# v3 = test.rjust(20,"*")
# print(v1,v2,v3)
# v = test.zfill(20)      #默认不能指定字符来填充只能使用"0"
# print(v)

#判断全部是否是大小写,转换为大小写
# test = "Alex"
# v1 = test.islower()
# v2 = test.lower()
# print(v1,v2)
#
# v3 = test.isupper()
# v4 = test.upper()
# print(v3,v4)


# test = " alex "
# test = "\nalex "
# #去除左右空白(能够去除\t \n)
# v1 = test.lstrip()
# v2 = test.rsplit()
# v3 = test.strip()
# print(v1,v2,v3)

#去除指定内容
# test = " alex "
# v1 = test.lstrip("al")
# v2 = test.rsplit("al")
# v3 = test.strip("al")
# print(v1,v2,v3)

#对应字符替换
# v = "asidufasd;fiuadkf;adfkjalsdjf"
# m = str.maketrans("aeiou","12345")
# new_v = v.translate(m)
# print(new_v)


#字符串分割
# test = "testtasdddfg"
# v = test.partition('s')         #只分割一次动作,可以拿到指定分割的字符
# print(v)
# v1 = test.rpartition('s')       #只做中间一次分割,可以拿到指定分割的字符
# print(v1)
# v2 = test.split('s',2)          #可以分割多次,拿不到指定分割的字符
# print(v2)
# v3 = test.rsplit('s',2)
# print(v3)

#分割，只能根据true，false:是否保留换行
# test = "asdfadfasdf\nasdfasdf\nadfasdf"
# v = test.splitlines(False)
# print(v)

#以xxx开头,以xxx结尾
# test = "backend 1.1.1.1"
# v = test.startswith('a')
# print(v)
# v1 = test.endswith("1")
# print(v1)

#大小写转换
# test = "alex"
# v = test.swapcase()
# print(v)


# test = "alexalexalex"
# # v = test.replace("ex",'bbb')
# v = test.replace("ex",'bbb',2)      #替换前两个ex
# print(v)


# test = "妹子有种冲我来"
#
# # index = 0
# # while index < len(test):
# #     p = test[index]
# #     print(p)
# #
# #     index +=1
# # print("==========")
#
# for item in test:
#     print(item)



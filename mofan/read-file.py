#!/usr/bin/env python
# -*- coding utf8 -*-

# 打印出文件的所有内容
# file = open('my file.txt','r')
#
# content = file.read()
#
# print(content)


# 逐行打印出文件内容，这个要定义多次读
file = open('my file.txt','r')

content = file.readline()
second_read_time = file.readline()
print(content,second_read_time)

# readlines 打印出所有文件的内容 内容都会输出到一个list列表中
# file = open('my file.txt','r')
# content = file.readlines()
# print(content)
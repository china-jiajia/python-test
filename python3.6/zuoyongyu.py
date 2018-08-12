#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/12'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


# def test1():
#     print("in the test1")
#
# def test():
#     print("in the test")
#     return test1
#
# res=test()
# print(res())

#http://www.cnblogs.com/linhaifeng/articles/6113086.html#_labe8

# 函数调用位置和函数内置变量没有关系

name = 'alex'

def foo():
    name='linhaifeng'
    def bar():
        name='wupeiqi'
        print(name)
    return bar

a=foo()
print(a)
a()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/27'
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

# 参考博客地址:
    # http://www.cnblogs.com/yuanchenqi/articles/5732581.html

import  os

# print(os.getcwd())
# os.chdir("test1")
# os.chdir("..")
# print(os.getcwd())

# os.makedirs("dirname1/dirname2")
# print(os.listdir())
# print(os.stat('os-code.py'))

# print(os.path.split(r'/Users/jiajia/python-test/python3.6/22-day/os-code.py'))

a="/Users/jiajia/python-test/python3.6"
b="22-day/os-code.py"

print(os.path.join(a,b))    #路径拼接


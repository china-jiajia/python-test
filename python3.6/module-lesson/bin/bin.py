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

import sys,os
# sys.path.append(r'/Users/jiajia/python-test/python3.6/module-lesson')     #不允许

BASE_DIR = os.path.dirname(os.path.dirname(__file__))       #这样写跑到终端上就不行了
sys.path.append(BASE_DIR)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      #这样写是取绝对文件绝对路径
sys.path.append(BASE_DIR)

from my_module import  main


def looger():
    pass

if __name__ == '__main__':
    main.run()
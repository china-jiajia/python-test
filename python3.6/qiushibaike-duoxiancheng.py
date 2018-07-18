#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


'''
多线程爬取糗事百科 段子
'''


import threading
import urllib.request
import re
import urllib.error

'''
多线程实例代码段
'''

# class A(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(0,10):
#             print("我是线程A")
#
# class B(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         for i in range(0,10):
#             print("我是线程B")
#
#
# thr1=A()        #实例化
# thr1.start()
# thr2=B()        #实例化
# thr2.start()

headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(1,36,2):
            url="https://www.qiushibaike.com/8hr/page/"+str(i)
            pagedata=urllib.request.urlopen(url).read().decode('utf-8','ignore')
            pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datalist=re.compile(pat,re.S).findall(pagedata)
            for j in range(0,len(datalist)):
                print("第"+str(i)+"页第"+str(j)+"个段子的内容是:")
            try:
                print(datalist[j])
            except urllib.error.HTTPError as e:
                if hasattr(e,"code"):
                    print(e.conde)
                if hasattr(e,"reason"):
                    print(e.reason)
class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(0,36,2):
            url="https://www.qiushibaike.com/8hr/page/"+str(i)
            pagedata=urllib.request.urlopen(url).read().decode('utf-8','ignore')
            pat='<div class="content">.*?<span>(.*?)</span>.*?</div>'
            datalist=re.compile(pat,re.S).findall(pagedata)
            for j in range(0,len(datalist)):
                print("第"+str(i)+"页第"+str(j)+"个段子的内容是:")
            try:
                print(datalist[j])
            except urllib.error.HTTPError as e:
                if hasattr(e,"code"):
                    print(e.conde)
                if hasattr(e,"reason"):
                    print(e.reason)

one=One()       #实例化
one.start()
two=Two()       #实例化
two.start()


'''
urllib.error.HTTPError: HTTP Error 503: Service Temporarily Unavailable
服务不可用,对方服务器问题
'''
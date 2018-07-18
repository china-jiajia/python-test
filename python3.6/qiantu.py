#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

'''
千图网抓图脚本,这里并没有成功
'''

import urllib.request
import re
import urllib.error


for i in range(1,10):
    pageurl="http://www.58.pic.com/haibaomoban/0/id-"+str(i)+".html"
    data=urllib.request.urlopen(pageurl).read().decode("utf-8","ignore")
    pat='<a class="thumb-box".*?src="(.*?).jpg!'
    imglist=re.compile(pat).findall(data)
    for j in range(0,len(imglist)):
        try:
            thisimg=imglist[i]
            thisimgurl=thisimg+"_1024.jpg"
            file="/User/jiajia/qiantu/"+str(i)+str(j)+".jpg"
            urllib.request.urlretrieve(thisimgurl,filename=file)
            print("第"+str(i)+"页第"+str(j)+"个图片爬取成功")
        except urllib.error.HTTPError as e:
            if hasattr(e,"code"):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)
        except Exception as e:
            print(e)

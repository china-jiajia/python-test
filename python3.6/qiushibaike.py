#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

import urllib.request
import re
import urllib.error


headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)

for i in range(1,10):
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


'''
#urllib.error.HTTPError: HTTP Error 503: Service Temporarily Unavailable
这个是被抓住了
'''
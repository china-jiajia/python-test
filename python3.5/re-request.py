#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import re
import requests
import time

url = 'https://news.ycombinator.com/'
data = requests.get(url)

#print(data)
#print(data.text)  #这里.text等同于read()

code = data.encoding
print(code)
page_status = data.status_code
print(page_status)

rdata = re.findall('"(https?://.*?)"',data.text)
print(rdata)
print(len(rdata))
print('\n')
print('\n')
time.sleep(5)
for htm in range(len(rdata)):
    print(rdata[htm])


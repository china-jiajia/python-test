#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


class mzitu():
    def __init__(self):
    	self.headers = {
    		"User-Agent": "Mozilla/5.0 (Windows NT 6.2;WOW64) AppleWebKit/535.24 (KHTML,like Gecko) Chrome/19.0.1055.1 Safari/535.24"}

    def all_url(self,url):
    	html = self.request(url)
    	all_a = BeautifulSoup(html.text,'lxml').find('div',class_='all').find_all('a')
    	for a in all_a:
    		title = a.get_text()
    		print(u'开始保存:',title)
    		path = str(title).replace("?",'_')
    		self.mkdir(path)
    		href = a['href']
    		self.html(href)

    def html(self,href):
    	html = self.request(href)
    	self.headers['referer'] = href
    	# max_span = BeautifulSoup(html.text,'lxml').find('div',class_='mainnav').find_all('span')[-2].get_text()
    	max_span = BeautifulSoup(html.text,'lxml').find('div',class_='mainnav').find_all('span')[-2].get_text()
    	for page in range(1,int(max_span) + 1):
    		page_url = href + '/' + str(page)
    		self.img(page_url)

    def img(self,page_url):
    	img_html = self.request(page_url)
    	img_url = BeautifulSoup(img_html.text,'lxml').find('div',class_='main-image').find('img')['src']
    	self.save(img_url)

    def save(self,img_url):
    	name = img_url[-9:-4]
    	img = self.request(img_url)
    	f = open(name + '.jpg','ab')
    	f.write(img.content)
    	f.close()

    def mkdir(self,path):
    	path = path.strip()
    	isExists = os.path.exists(os.path.join("~/Desktop/mzitu",path))
    	if not isExists:
    		print(u'建了一个名字叫做',path,u'的文件夹!')
    		os.makedirs(os.path.join("~/Desktop/mzitu",path))
    		os.chdir(os.path.join("~/Desktop/mzitu",path))
    		return True
    	else:
    		print(u'名字叫做',path,u'的文件夹已经存在了!')
    		return False

    def request(self,url):
    	content = requests.get(url,headers=self.headers)
    	return content

Mzitu = mzitu()
Mzitu.all_url('http://www.mzitu.com/all')

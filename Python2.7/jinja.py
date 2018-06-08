#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import os
from jinja2 import Environment,PackageLoader



def test_simple():
	title = "Title H "
	items = [{'href':'a.com','caption':'ACaption'},{'href':'b.com','caption':'Bcaption'}]
	content="This is content"
	result = render('simple.html',**locals())
	print(result)

if __name__ == '__main__':
	test_simple()

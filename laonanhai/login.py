#!/usr/bin/env python
# -*- coding: utf-8 -*-

user = input('请输入用户名:',)
pwd = input('请输入密码:',)

count = 0

while count < 3:
    if user == 'root' and pwd == 'AbC123':
        print('欢迎进入系统,请操作')
        break
    else:
        print('用户名或密码错误,请重新输入')
        break
    count +=1
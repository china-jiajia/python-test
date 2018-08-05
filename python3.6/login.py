#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


count = 0

while count < 3:
    user = input('请输入用户名: ')
    pwd = input('请输入密码: ')
    if user == 'root' and pwd == 'abc!123':
        print('---------登录成功----------')
        break
    else:
        print('--------信息输入错误--------')
    count +=1


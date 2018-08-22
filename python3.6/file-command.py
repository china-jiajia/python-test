#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/13'
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

# www.cnblogs.com/linhaifeng/articles/5984922.html#_lable4
#r w a

#r

# f=open('test.txt','r',encoding='utf-8')
# data=f.read()
# print(data)
# f.close()


# print(f.readable())
# print(f.readline())         #一次读一行
# print(f.readline())         #一次读一行
# print(f.readline())         #一次读一行
# print(f.readline())         #一次读一行

# data=f.readlines()          #读取行不换行
# print(data)
# f.close()


#w
# f=open('test.txt','w',encoding='utf-8')
# # f.read()
# f.write('111111111111111\n')
# f.write('222222222222222\n')
# f.write('333333333333333\n')
# f.writelines(['444444\n','555555555\n'])        #写一个列表行
# f.close()



#a 追加到最后
# f=open('test.txt','a',encoding='utf-8')
# f.write('写到文件最后')
# f.close()



#r+  内容覆盖
# f=open('test.txt','r+',encoding='utf-8')
# f.write('写到文件最后')
# f.close()

# 1
# src_file=open('test.txt','r',encoding='utf-8')
# data=src_file.read()
# src_file.close()
#
# dst_f=open('test1.txt','w',encoding='utf-8')
# dst_f.write(data)
# dst_f.close()


# # 2
# src_file=open('test.txt','r',encoding='utf-8')
# data=src_file.readlines()
# src_file.close()
#
# print(data)
# dst_f=open('test1.txt','w',encoding='utf-8')
# # dst_f.writelines(data)
# dst_f.write(data[0])
# dst_f.close()



with open('test.txt','w') as f:
    f.write('1111111\n')


with open('test1.txt','r',encoding='utf-8') as src_f,\
        open('test.txt','w',encoding='utf-8') as dst_f:
    data=src_f.read()
    dst_f.write(data)
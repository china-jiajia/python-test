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




# l=[1,2,3,4,5]
# print(list(map(str,l)))


# from functools import reduce
# l=[1,2,3,4,5]
# print(reduce(lambda x,y:x+y,l,3))

# name=['alex_sb','linhaifeng']
# res=filter(lambda x:not x.endswith('sb'),name)
# print(res)
# print(list(res))



#rb 模式
# f=open('test.txt','rb',encoding='utf-8') #b的方式不能指定编码
# f=open('test.txt','rb')
# data=f.read()
# #'字符串'-----encode------>bytes
# #bytes--------decode----------->'字符串'
# print(data)
# print(data.decode('utf-8'))



# f=open('test1.txt','wb')
# f.write(bytes('11111111\n',encoding='utf-8'))
# f.write('niubi'.encode('utf-8'))


# f=open('test1.txt','ab')        #ab当中的a不仅仅是以为文件最后一行结尾的,而是文件内容最后一个光标结尾的
# f.write('niubi1'.encode('utf-8'))





#文件操作的其他方法
# f=open('test.txt','r+',encoding='utf-8',newline='')
# f=open('test.txt','r+',encoding='utf-8',newline='')     #读取文件中真正的换行符
# print(f.close())
# print(f.encoding )
# f.flush()

# print(f.tell())
# f.readline()
# print(f.tell())

# print(f.readlines())


# f.seek(3)   #用来控制光标的移动
# print(f.tell())
# print(f.read())

# data=f.read(4)
# print(data)


# f.truncate(10)    #文件截断"从最开始到,10个字符开始截取"





# 高级玩法
# f=open('test.txt','b',encoding='utf-8')
# print(f.tell())
# f.seek(10)
# print(f.tell())
# f.seek(3)
# print(f.tell())


# f=open('test.txt','b',encoding='utf-8')
# print(f.tell())
# f.seek(10,0)
# print(f.tell())
# f.seek(3,0)
# print(f.tell())


#seek相对位置(seek是以字节去操作)
# f=open('test.txt','rb')
# print(f.tell())
# f.seek(10,1)
# print(f.tell())
# f.seek(3,1)
# print(f.tell())

#从文件末尾开始seek
# f=open('test.txt','rb')
# print(f.tell())
# f.seek(-5,2)
# print(f.tell())
# f.seek(3,2)
# print(f.tell())


# f=open('test.txt','rb')
# data=f.readlines()
# print(data[-1].decode('utf-8'))


f=open('test.txt','rb')

#循环读取文件
# for i in f:
#     print(i.decode('utf-8'))


for i in f:
    offs=-10
    f.seek(-3,2)
    while True:
        f.seek(offs,2)
        data=f.readlines()
        if len(data) > 1:
            print('文件的最后的一行是%s' %(data[-1].decode('utf-8')))
            break
        offs*=2

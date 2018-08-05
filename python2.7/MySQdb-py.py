#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao

import MySQLdb

'''
打开数据库连接
'''

db = MySQLdb.connect("localhost","root","tJJ199005","test")


'''
使用cursor()方法获取操作游标
'''
cursor = db.cursor()


'''
使用execut方法执行SQL语句
'''

cursor.execute("select version()")


'''
使用fetchone()方法获取一条数据
'''
data = cursor.fetchone()

print"Database version : %s " % data


'''
关闭数据库
'''
db.close()

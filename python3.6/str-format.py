#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao


# 字符串格式常用方法:
#     百分号
#     format


#百分号字符串格式化
# msg='i am %s  my hobby is %s' % ('lhf',1)
# msg1='i am %s  my hobby is %s' % ('lhf',[1,2])
# msg2='i am %s  my hobby is %d' % ('lhf',1)
# print(msg,msg1,msg2)

#打印浮点数(百分比)
# tpl = "percent %.2f" % 99.976232532
# tpl1 = "percent %.4s" % 99.976232532    #字符串截取位数
# print(tpl,tpl1)

# tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
# print(tpl)

# msg='i am \033[43;1m%(name)-60s\033[0m my hobby is alex' % {"name":'lhf'}
# print(msg)
#
# print('root','x','0','0',sep=':')



#format字符串格式化
# tpl = "i am {},age {},".format("seven",18,'alex')
# tpl = "i am {0},age {1},{2}".format("seven",18,'alex')
# print(tpl)


# tpl = "i am {name},age {age}, really {name}".format(name="seven",age=18)
# print(tpl)

# tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
# print(tpl)


# tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
# print(tpl)


# tpl = "i am {:s}, age {:d}".format(*["seven", 18])
# tpl = "i am {:s}, age {:d}".format("seven", 18)     #["seven",18]
# tpl = "i am {}, age {}".format("seven", 18)     #["seven",18]
# tpl = "i am {0}, age {1}".format("seven", 18)     #["seven",18]
# # print(tpl)

# tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
# print(tpl)

# tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%},{}".format(15, 15, 15, 15, 15, 15.87623, 2)     #b:二进制 o:八进制 d:整型 x:十六进制(小写abcd) X:十六进制(大写ABCD)
# print(tpl)
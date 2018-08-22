#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'jiajia'
__mtime__ = '2018/8/23'
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

"""
参考博客:
www.cnblogs.com/linhaifeng/articles/6140395.html

"""

"""
user_dic={'username':None,'login':False}


def auth_func(func):
    def wrapper(*args,**kwargs):
        if user_dic['username'] and user_dic['login']:
            res=func(*args,**kwargs)
            return res
        username=input('用户名: ').strip()
        passwd=input('密码: ').strip()
        if username == 'sb'  and passwd == '123':
            user_dic['username']=username
            user_dic['login']=True
            res=func(*args,**kwargs)
            return res
        else:
            print('用户名或密码错误')
    return wrapper

@auth_func
def index():
    print('欢迎来到京东主页')

@auth_func
def home(name):
    print('欢迎回家%s' % name)

@auth_func
def shopping_cat(name):
    print('%s购物车里有 [%s,%s,%s]' %(name,'奶茶','妹妹','娃娃'))

index()
home('产品经理')
shopping_cat('产品经理')
"""



"""
user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]


current_dic={'username':None,'login':False}


def auth_func(func):
    def wrapper(*args,**kwargs):
        if current_dic['username'] and current_dic['login']:
            res=func(*args,**kwargs)
            return res
        username=input('用户名: ').strip()
        passwd=input('密码: ').strip()
        for user_dic in user_list:
            if username == user_dic['name'] and passwd == user_dic['passwd']:
                current_dic['username']=username
                current_dic['login']=True
                res = func(*args,**kwargs)
                return res
        else:
            print('用户名或者密码错误')

    return wrapper

@auth_func
def index():
    print('欢迎来到京东主页')

@auth_func
def home(name):
    print('欢迎回家%s' % name)

@auth_func
def shopping_cat(name):
    print('%s购物车里有 [%s,%s,%s]' %(name,'奶茶','妹妹','娃娃'))


print('before---->',current_dic)
index()
print('after---->',current_dic)
home('产品经理')
shopping_cat('产品经理')
"""



"""
带参数装饰器

user_list=[
    {'name':'alex','passwd':'123'},
    {'name':'linhaifeng','passwd':'123'},
    {'name':'wupeiqi','passwd':'123'},
    {'name':'yuanhao','passwd':'123'},
]


current_dic={'username':None,'login':False}

def auth(auth_type='filedb'):
    def auth_func(func):
        def wrapper(*args,**kwargs):
            print('认证类型是',auth_type)
            if auth_type == 'filedb':
                if current_dic['username'] and current_dic['login']:
                    res=func(*args,**kwargs)
                    return res
                username=input('用户名: ').strip()
                passwd=input('密码: ').strip()
                for user_dic in user_list:
                    if username == user_dic['name'] and passwd == user_dic['passwd']:
                        current_dic['username']=username
                        current_dic['login']=True
                        res = func(*args,**kwargs)
                        return res
                else:
                    print('用户名或者密码错误')
            elif auth_type == 'ldap':
                print('鬼才这么玩呢')
                res = func(*args, **kwargs)
                return res
            else:
                print('鬼才知道你用的什么认证方式')
                res = func(*args, **kwargs)
                return res

        return wrapper
    return auth_func

@auth(auth_type='filedb')   #auth_func=auth=(auth_type='filedb')----->@auth_func 附加了一个  ---->index=auth_func(index)
def index():
    print('欢迎来到京东主页')

@auth(auth_type='ldap')
def home(name):
    print('欢迎回家%s' % name)

@auth(auth_type='sssss')
def shopping_cat(name):
    print('%s购物车里有 [%s,%s,%s]' %(name,'奶茶','妹妹','娃娃'))


print('before---->',current_dic)
index()
print('after---->',current_dic)
home('产品经理')
shopping_cat('产品经理')
"""
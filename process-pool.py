#!/usr/bin/env python
# -*-  coding utf8 -*-

# 线程池
# Pool默认会实用所有的线程，需要手动指定线程数


import multiprocessing as mp

def job(x):
    return x*x


def multicore():
#    pool = mp.Pool()               #默认使用所有核心数
    pool = mp.Pool(processes=3)     #指定使用核心数
    res = pool.map(job,range(10000))
    print(res)
    res = pool.apply_async(job,(2,))    #apply_async() 一次只能做一个数据计算
    print(res.get())

    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])


if __name__=='__main__':
    multicore()

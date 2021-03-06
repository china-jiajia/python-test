#!/usr/bin/env python
# -*- coding utf8 -*-

# 存储进程输出 Queue

import  multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000):
        res += i+i**2+i**3
    q.put(res)

if __name__=='__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)

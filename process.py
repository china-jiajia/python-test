#!/usr/bin/env python
# -*- coding utf8 -*-

import multiprocessing as mp
# import  threading as td

def  job(a,d):
    print('aaaa')

# t1 = td.Thread(target=job,args=(1,2))
# t1.start()
# t1.join()

if __name__=='__main__':
    p1 = mp.Process(target=job,args=(1,2))
    p1.start()
    p1.join()

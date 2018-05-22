#!/usr/bin/env python 
# -*- coding: utf-8 -*-


msg = '1'


def while_true():
    i=0
    while True:
        if msg != '':
            i+=1
            if i==2:
                print(i)
                print(msg)
                break;
print("while ture exit!")
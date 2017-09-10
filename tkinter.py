#!/usr/bin/env python
# -*- coding utf8 -*-

#注释这个得在python 自带的IDE下运行 pycharm其它工具会报错提示没有该模块



import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')

var = tk.StringVar()

l = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)

l.pack()

on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(window,text='hit me',width=15,height=2,command=hit_me)

b.pack()

window.mainloop()


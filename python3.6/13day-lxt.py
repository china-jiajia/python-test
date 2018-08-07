#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Mrtao



dic = {
    "植物":
        {"草本植物":
             ["牵牛花", "瓜叶菊", "葫芦", "翠菊", "冬小麦", "甜菜"],
         "木本植物":
             ["乔木", "灌木", "半灌木", "如松", "杉", "樟"],
         "水生植物":
             ["荷花", "千屈菜", "菖蒲", "黄菖蒲", "水葱", "再力花", "梭鱼草"]},
    "动物":
        {"两栖动物":
             ["山龟", "山鳖", "石蛙", "娃娃鱼", "蟾蜍", "龟", "鳄鱼", "蜥蜴", "蛇"],
         "禽类":
             ["雏鸡", "原鸡", "长鸣鸡", "昌国鸡", "斗鸡", "长尾鸡", "乌骨鸡"],
         "哺乳动物":
             ["虎", "狼", "鼠", "鹿", "貂", "猴", "貘", "树懒", "白马", "狗"]}}


# li = []
# while True:
#     for i,v in enumerate(dic,1):
#         print(i,v)
#         li.append(v)
#     u_c = input('>>>')
#     u_c = int(u_c)
#     li1 = []
#     while True:
#         for i,v in enumerate(dic[li[u_c-1]],1):
#             print(i,v)
#             li1.append(v)
#         u_c1 = input('>>>>')
#         u_c1 = int(u_c1)
#         while True:
#             for i in dic[li[u_c-1]][li1[u_c1-1]]:
#                 print(i)


db = {
    "广州":{},
    "上海":{
        "宝山":{},
    },
    "北京":{
        "昌平":{
            "沙河":{},
            "回龙观":{},
        },
        "朝阳":{},
        "海定":{},
    }

}

path = []
while True:
    temp = db
    for item in path:
        temp = temp[item]
    print("当前可选的所有子节点: ",list(temp.keys()))

    choice = input('1:添加节点 2:查看节点(Q/B); \n >>>')
    if choice == "1":
        name = input('请输入要查看的节点名称: ')
        temp[name] = {}
    elif choice == "2":
        name = input('请输入要查看的节点名称: ')
        path.append(name)
    elif choice.lower() == 'b':
        if path:
            path.pop()
    elif choice.lower() == 'q':
        break
    else:
        print("输入错误,请重新输入！！！")

    # #当前节点下都有哪些子节点
    # print("当前可选的所有子节点： ",list(db.keys()))
    # v = input(">>>")
    # db[v] = {}
    # print(db)
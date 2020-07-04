#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""code_info
@Time    : 2020 2020/6/29 2:58 下午
@Author  : keyoung
@File    : Narcissus.py
"""
count = 0  # 初始化
for i in range(100, 1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i - a * 100 - b * 10
    # a = i//100
    # b = (i%100)//10
    # c = i%10
    if a ** 3 + b ** 3 + c ** 3 == i:
        #   print(i)
        count = count + 1
    else:
        continue
print("1000以内的水仙花数有: ", count, " 个")

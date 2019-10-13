#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename : if ... elif ... else
# author by : hare
# time : 2019.10.13

# 用户输入数字

num = float(input("输入一个数字: "))
if num > 0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")


# 还有一种嵌套的方法：
# num = float(input("输入一个数字: "))
# if num >= 0:
#    if num == 0:
#        print("零")
#    else:
#        print("正数")
# else:
#    print("负数")


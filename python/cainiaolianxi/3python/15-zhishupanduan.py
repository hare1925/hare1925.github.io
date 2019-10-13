#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename : 质数判断
# author by : hare
# time : 2019.10.13

# python程序用于检测用户输入的数字是否为质数

# 一个大于1的自然是，除了1和它本身外，不能被其他自然数整除，换句话说就是该数除了1和它本身不在有其他的因数。

# 用户输入
num = int(input("请输入一个数字： "))

# 质数大于 1
if num > 1:
    #查看因子
    for i in range(2, num): # 这里的 i 代表的是遍历从 2 到 num-1 的所有数
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘以", num // i, "是", num)
            break   # 这里可以确保，当得到第一个可以整除的数时结束循环，因为用户输入的数字可能会很大，但是我们的目的是判断是否是质数，而不是输出次数所有的因数。
    else:
        print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")


















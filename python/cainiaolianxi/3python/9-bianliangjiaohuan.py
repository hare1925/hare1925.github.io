#!/usr/bin/bash
# -*- coding: UTF-8 -*-

# fliename : 变量交换
# author by : hare
# tiem : 2019.10.13

# 用户输入

x = input('输入 x 的值： ')
y = input('输入 y 的值： ')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后 x 的值为：{}'.format(x))
print('交换后 y 的值为：{}'.format(y))







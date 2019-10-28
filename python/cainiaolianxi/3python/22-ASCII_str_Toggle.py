#!/usr/bin/python
# -*- coding: UTF-8 -*-

# FileName : ASCII<=>str_Toggle
# Author by : hare
# Time : 2019.10.22

# 用户输入字符、ASCII码
c = input("请输入一个字符: ")
a = int(input("请输入一个ASCII码: "))

print( c + " 的ASCII码为", ord(c))
print( a + " 对应的字符为", chr(a))


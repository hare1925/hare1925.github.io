#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Failname : ascii码和str互换
# author by : hare
# time : 2019.10.22

#用户输入自负
c = input("请输入一个字符")

#用户输入ascii码，并转换为整型
a = int(input("请输入ascii码："))

print( c + " 的ASCII码为", ord(c))
print( a , " 对应的字符为", chr(a))


#!/usr/bin/python
# -*- coding: UTF-8 -*-

# FileName : 21-shuzhi_2_8_10_16.py
# Description :二进制、八尽职、十进制、十六进制转换
# Last Change : 2019.10.22
# Maintainer : hare <hare1925@163.com>
# Licence : None
# Version : 0.0.1

# 获取用户输入十进制数
dec = int(input("输入数字："))

print("十进制数为：", dec)
print("转换为二进制数为：", bin(dec))
print("转换为八进制数为：", oct(dec))
print("转换为十六进制数为：", hex(dec))


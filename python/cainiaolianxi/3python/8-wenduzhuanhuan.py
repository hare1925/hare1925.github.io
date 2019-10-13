#!/usr/bin/bash
# -*- coding: UTF-8 -*-

# filename : 温度转换
# author by : hare
# time : 2019.10.13

# 用户输入摄氏温度
celsius = float(input('输入摄氏温度: '))

# 计算华氏温度
fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转换为华氏温度为 %0.1f ' %(celsius,fahrenheit))





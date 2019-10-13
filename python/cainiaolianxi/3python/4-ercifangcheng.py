#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename : 计算二次方程
# author by : hare
# 2019.10.12

# 二次方程式 ax**2 + bx + c = 0
# a, b, c 用户提供，为实数， a != 0

# 导入 cmath(复杂数学运算）模块

import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))

# 计算
d = (b ** 2) - (4 * a * c)

# 两种求解方式
sal1 = (-b-cmath.sqrt(d)) / (2 * a)
sal2 = (-b+cmath.sqrt(d)) / (2 * a)

print('结果为 {0} 和 {1}'.format(sal1, sal2))
















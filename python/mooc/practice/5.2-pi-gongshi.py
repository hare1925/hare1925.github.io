#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Filename : 圆周率的计算
# Author by : hare
# Time : 2019.10.22

pi = 0
N = 100
for k in range(N):
    pi += 1 / pow(16, k) * ( \
        4 / (8 * k + 1) - 2 / (8 * k + 4) - \
        1 / (8 * k + 5) - 1 / (8 * k + 6))
print("圆周率值是：{}".format(pi))



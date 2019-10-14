#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename : 99乘法表
# author by : hare
# time : 2019.10.14

# 九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(j, i, i * j), end='')
    print()


























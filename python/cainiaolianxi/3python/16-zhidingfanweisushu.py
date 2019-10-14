#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename : 输出指定范围内的素数
# author by : hare
# time : 2019.10.14

# 素数(prime number)又称质数，有无限个。除了 1 和 它本身 以外不再被其他的除数整除。

# 输出指定范围的素数

# take input from the user

lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper+1):
    # 素数大于1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break

        else:
            print(num)


























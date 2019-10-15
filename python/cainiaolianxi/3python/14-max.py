#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename : max()
# author by : hare
# time : 2019.10.13

# 最简单的
print(max(1, 2))
print(max('a', 'b'))

# 也可以对列表和元组使用
print(max([1, 2]))
print(max((1, 2)))

# 更多实例
print("80, 100, 1000 最大值为：", max(80, 100, 1000))
print("-20, 100, 400 最大值为：", max(-20, 100, 400))
print("-80, -20, -10 最大值为：", max(-80, -20, -10))
print("0, 100, -400 最大值为：", max(0, 100, -400))


#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename: 数字求和
# author by :hare
# 2019.10.12

# 用户输入名称
num1 = input("输入第一个数字：")
num2 = input("输入第二个数字：")


# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为：{2}'.format(num1, num2, sum))


# input()内置函数获取输入，input()返回一个字符串，所以需要用float()方法将字符串转换为数字。

#等同于
# print('两数之和为 %.1f' %(float(input('输入第一个数字：')) + float(input('输入第二个数字：'))))

# 直接在print里面就不需要槽了













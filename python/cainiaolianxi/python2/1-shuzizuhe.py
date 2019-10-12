#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 菜鸟练习1
# 有 1 2 3 4 四个数字能组成多少个不相同且无重复的三位数？各是多少？
# 分析：可填写百位、十位、各位都是数字 1 2 3 4.组成所有的排列后在去掉不满足条件的排列。

# 2019.10.12
# by hare

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k ) and ( k != j ) and ( j != i):
                print(i,j,k)

# 错误纠正：
# 1、print需要加（），因为这个是python3
# 2、if 语句后面只能这样用and连接，如果是c语言可以用 && 连接。

# 温习：
# 1、range（）这里是小括号，语法为：range（star，stop，步长）









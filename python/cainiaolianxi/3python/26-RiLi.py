#!/usr/bin/python
# -*- coding: UTF-8 -*-

# FileName : 生成日历
# Author by : hare
# Time :2019.10.30

# 引入日历模块
import calendar as rili


# 输入指定年月
yy = int(input("输入年份："))
mm = int(input("输入月份："))

# 显示日历

print(rili.month(yy, mm))



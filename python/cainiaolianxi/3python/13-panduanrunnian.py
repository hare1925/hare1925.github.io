#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filename : 判断闰年
# author by : hare
# time : 2019.10.13

year = int(input("输入一个年份: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{} 是闰年".format(year))
        else:
            print("{} 不是闰年".format(year))
    else:
        print("{} 是闰年".format(year))
else:
    print("{} 不是闰年".format(year))

# 整百年能被400整除的是闰年
# 非整百年能被4整除的是闰年







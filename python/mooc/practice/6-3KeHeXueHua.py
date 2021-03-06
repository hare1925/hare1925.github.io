#!/usr/bin/python
# -*- coding:UTF-8 -*-

# FileName : 科赫雪花
# Author by : hare
# Time : 2019.10.27

#kochDrawV1.py
import turtle as tt
def koch(size, n):
    if n == 0:
        tt.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            tt.left(angle)
            koch(size/3, n-1)
def main():
    tt.setup(800, 400)
    tt.penup()
    tt.goto(-300, -50)
    tt.pendown()
    tt.pensize(2)
    koch(600, 3)    # 3阶科赫曲线，阶数
    tt.hideturtle()
main()


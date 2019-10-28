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
    tt.setup(600, 600)
    tt.penup()
    tt.goto(-200, 100)
    tt.pendown()
    tt.pensize(2)
    tt.pencolor("red")
    level = 3   #3阶科赫曲线，阶数
    koch(400, level)    # 3阶科赫曲线，阶数
    tt.right(120)
    koch(400, level)
    tt.right(120)
    koch(400, level)
    tt.hideturtle()
    tt.done()
main()


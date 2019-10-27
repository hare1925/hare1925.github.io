#!/usr/bin/python
# -*- coding: UTF-8 -*-

# FileName : 7段数码管
# Author by : hare
# Time : 2019.10.27

import turtle as tt
def drawLine(draw):     #绘制单段数码管
    tt.pendown() if draw else tt.penup()
    tt.fd(40)
    tt.right(90)
def drawDigit(digit):   # 根据数字绘制7段数码管
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    tt.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    tt.left(180)
    tt.penup()  # 为绘制后续数字确定位置
    tt.fd(20)   # 为绘制后续数字确定位置
def drawDate(date):     #获得要输出的数字
    for i in date:
        drawDigit(eval(i)) # 通过eval()函数将数字变为整数
def main():     #用主函数main调用前面定义的函数，完成程序
    tt.setup(800, 350, 200, 200)
    tt.penup()
    tt.fd(-300)
    tt.pensize(5)
    drawDate('20191027')
    tt.htdeturtle()
    tt.done()
main()


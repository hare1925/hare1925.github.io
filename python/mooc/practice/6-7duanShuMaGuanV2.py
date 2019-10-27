#!/usr/bin/python
# -*- coding: UTF-8 -*-

# FileName : 7段数码管
# Author by : hare
# Time : 2019.10.27

import turtle as tt
import time
def drawGap():  # 绘制数码管间隔
    tt.penup()
    tt.fd(5)
def drawLine(draw):     #绘制单段数码管
    drawGap()
    tt.pendown() if draw else tt.penup()
    tt.fd(40)
    drawGap()
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
def drawDate(date):     #获得要输出的数字, data为日期，格式为‘%Y-%m=%d+’，这里相当于 - = + 相当于 年 月 日，这里可以用循环判断
    tt.pencolor("red")
    for i in date:
        if i == '-':
            tt.write('年', font=("Arial", 18, "normal"))
            tt.pencolor("green")
            tt.fd(40)
        elif i == '=':
            tt.write('月', font=("Arial", 18, "normal"))
            tt.pencolor("blue")
            tt.fd(40)
        elif i == '+':
            tt.write('日', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i)) # 通过eval()函数将数字变为整数
def main():     #用主函数main调用前面定义的函数，完成程序
    tt.setup(800, 350, 200, 200)
    tt.penup()
    tt.fd(-300)
    tt.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+', time.gmtime()))
    tt.hideturtle()
    tt.done()
main()


#pythondraw.py

import turtle #引入turtle库
turtle.setup(650, 350, 200, 200)    #setup设置长提大小及位置，与屏幕的相对位置（长、宽、默认屏幕位置x轴、默认屏幕位置y轴）
turtle.penup()      #抬起画笔（因为正中心的坐标是海龟的0,0坐标） 别名turtle.pu
turtle.fd(-250)     #forWard 向前-250 像素，就是向后喽，显示就是在左边喽（这里用的是海龟的相对坐标体系）fd向前，bk向后，circle以海龟左方为圆心画圆形）
turtle.pendown()    #别名turtle.pd 它与penup是成对出现的
turtle.pensize(25)
turtle.pencolor("purple")   #这里可以使用RGB色彩体系，turtle库默认使用小数值，turtle.colormode(mode),turtle.colormode(255)这个是使用255数值。RGB的小数值： turtle.pencolor(0.63,0.13,0.94) ；RGB的元组值： turtle.pencolor((0.63,0.13,0.94))
turtle.seth(-40)        #setheading的缩写，改变绝对角度（x轴右边为0/360度，y轴上面为90/-270度）；还可以使用turtle.left和turtle.right让海龟向左右转向（这个是海龟的相对角度）
for i in range(4):
    turtle.circle(40, 80)   #第一个参数是海龟左侧半径的像素，第二个时绘制的弧度是80度
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()   #有这一句，程序运行后不会退出，否则会自动退出。













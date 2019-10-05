#TemoConvert.py

TempStr = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
### 这个程序有个bug，例如输入的值为sdf，最后一个字符为f或c的时候，程序还是会执行，当执行到eval的时候就会报错了。


# tempstr是一个
# TempStr = input("请输入带有符号的温度值：")
# if TempStr[-1] in ['F', 'f']:
    # C = (eval(TempStr[0:-1]) - 32) / 1.8
    # print("转换后的温度是{:.2f}C".format(C))
# elif TempStr[-1] in ['C', 'c']:
    # F = 1.8 * eval(TempStr[0:-1]) + 32
    # print("转换后的温度是{:.2f}F".format(F))
# else:
    # print("输入格式错误")


















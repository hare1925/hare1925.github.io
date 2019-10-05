#温度转换实例

wendu = input("请输入带有符号的温度值：")

if wendu[-1] in ['F', 'f']:
    C = (eval(wendu[:-1]) -32) / 1.8
    print("转换后的温度为：{:.2f}C".format(C))
elif wendu[-1] in ['c', 'C']:
    F = eval(wendu[:-1]) * 1.8 + 32
    print("转换后的温度为：{:.2f}F".format(F))
else:
    print("你输入的温度值有误")









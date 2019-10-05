# 计算千分之五和百分之一的力量

a = input("你向知道每天进步百分之几的力量？")

dayfactor = float(a) / 100

dayup = pow(1 + dayfactor, 365)
daydown = pow(1 - dayfactor, 365)

print("每天进步百分之{}的力量是{:.2f}".format(a, dayup))
print("每天退步百分之{}的力量是{:.2f}".format(a, daydown))


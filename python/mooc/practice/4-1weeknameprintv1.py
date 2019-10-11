#Weeknameprintv1
# 根据1-7数字输出相应星期
# 2019.10.11
# by hare


weekStr = "星期一星期二星期三星期四星期五星期六星期日"

weekId = eval(input("请输入星期数字（1-7）："))

pos = (weekId -1) * 3

print(weekStr[pos: pos+3])













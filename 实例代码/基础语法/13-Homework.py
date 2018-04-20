# 1、彩票中奖  从控制台输入一个数字，判断是否和随机出来的数字(0-100)一致，
# 一致提示中奖，不一致，提示好可惜，只差一点点
import random
# 获取一个随机数
res = random.choice(range(101))
# print(res)
numStr = input("请输入您喜欢的数字：")  # str
# 将str转为int
num = int(numStr)
# 判断两个数是否相等
if res == num:
    print("恭喜，中奖500万，请去梦里领取")
else:
    print("很抱歉，再来一次")


# 2、从控制台输入一个三位数，判断当前数字是否为水仙花数
# 153   1^3 + 5^3 + 3^3 = 153
# 222

num = 153
# 个位
a = num % 10
# 百位
b = num // 100
# 十位
c = (num // 10) % 10

if (a**3 + b**3 + c**3) == num:
    print("Yes")
else:
    print("No")



# 3、判断平闰年
# 闰年的条件：1、能被4整除，不能被100整除   2、能被400整除
# 3、只要满足前面两个中任意一个条件就是闰年
year = 1000

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("闰年")
else:
    print("平年")


'''
if elif else  
if 嵌套
string
while 循环
List
for in
'''
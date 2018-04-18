import random
# 1、彩票中奖  从控制台输入一个数字，判断是否个我随机出来的数字(0-100)是否一致，
# 一致提示中奖，不一致，提示好可惜，只差一点点

def lottery():
    while True:
        num = int(random.randrange(100))
        bingo = int(random.randrange(100))
        if num == bingo:
            print("你的数字为 ：",num)
            print("你中奖了！\n")
            break
        else:
            print("你的数字为 ：", num)
            print("好可惜，只差了一点点！")


#a()
# 2、从控制台输入一个三位数，判断当前数字是否为水仙花数
# 153   1^3 + 5^3 + 3^3 = 153
#

def number():
        num = int(input("请输入一个三位数："))
        a = num % 10
        b = num // 10 % 10
        c = num // 100

        if a**3 + b**3 + c**3 == num:
            print("是水仙花数")
        else:
            print("不是水仙花数")


# 3、判断平闰年
# 闰年的条件：1、能被4整除，不能被100整除   2、能被400整除
# 3、只要满足前面两个中任意一个条件就是闰年

def  yearT():
    year = int(input("请输入一个年份："))
    if year == 1900:
        print(year,"不是闰年")
    elif year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
        print(year,"是闰年")
    else:
        print(year,"不是闰年")

lottery()
#number()
#yearT()
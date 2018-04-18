# if 语句
"""
语法：
if 表达式：
    语句
# if else

if 表达式：
    语句
else：
    语句

# if elif

if 表达式：
    语句
elif 表达式：
    语句
else:
    语句

"""

num1 = 20
num2 = 20
print(num1 == num2)

if num1 == num2:
    print("-----------")
    print("sssdasddada")

print("下雨了")

if num1 == num2:
    print("+++++++")
else:
    print("---------")

print("======")


# num5 = int(input("______:"))
# if num5 % 2 == 0:
#     print("偶数")
# else:
#     print("奇数")

age = 21

if  age > 120:
    print("长寿")
elif (age < 101)  and (age > 81) :
    print("高寿")
elif (age <  81) and (age > 61)  :
    print("耄耋")
elif (age < 80) and (age > 61 ):
    print("老人")
elif age < 61:
    print("普通")
elif age < 0:
    print("未出世")
else:
    print("正常")


# 我

hope = 60
face = 72
rep = 12

if face<hope:
    print("呵呵")
elif face>hope:
    print("可以交个朋友")
    if face>120:
        print("可以深交")
    elif (face>hope) and (rep > hope):
        print("可以交友")
    else:
        print("呵呵")


# if-elif-else
# age   120 长寿   101-120 高寿   81-100  耄耋   61-80   普通
#   60  老年人     0 未出生
# if
# if - else
age = 123
if age >= 120:
    print("长寿")
if age > 100 and age < 120:
    print("高寿")
if age > 80 and age <= 100:
    print("耄耋")
if age > 60 and age <= 80:
    print("正常")


# if-elif-else
'''
语法格式：
if 条件一:
    语句一
[elif 条件二:
    语句二
elif 条件三:
    语句三
elif 条件n:
    语句n]
[else:
    语句n+1]
'''
# 逻辑：当程序执行到if语句时，判断条件一是否成立，成立执行语句一，
# 并结束该条件语句，如果条件一不成立，判断条件二是否成立，
# 成立执行语句二，并结束该条件语句，不成立判断条件三....
# 当所有的elif后面的条件都不成立时，执行语句n+1,并结束if语句

# age   120 长寿   101-120 高寿   81-100  耄耋   61-80   普通
#  1- 60  老年人     <=0 未出生
# 控制台输入一个数字
#
age = int(input("请输入您的年龄："))
if age > 120:
    print("长寿")
elif age > 100 and age <= 120:
    print("高寿")
elif age > 80 and age <= 100:
    print("耄耋")
elif age > 60 and age <= 80:
    print("普通")
elif age >= 1 and age <= 60:
    print("老年人")
elif age <= 0:
    print("您居然还未出生")





if age > 120:
    print("长寿")
elif age > 100:
    print("高寿")
elif age > 80:
    print("耄耋")
elif age > 60:
    print("普通")
elif age >= 1:
    print("老年人")
elif age <= 0:
    print("您居然还未出生")





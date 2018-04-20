# TypeError: '>' not supported between instances of 'str' and 'int'
# 比较运算符在使用时要求前后两个对象的类型一致

# if语句
'''
语法格式：
if 表达式:
    语句
'''
# 逻辑：当程序执行到if语句时，首先进行表达式的判断，如果表达式为真，则
# 执行if下面的语句，否则不执行if下面的语句，继续执行if后面的语句
# 何为真，何为假
# 假： 0  0.0  ""  ''  None  False
# 真： 除了假就是真
num1 = 20
num2 = 20
print(num1 == num2)  # True
if num1 == num2:
    print("我到底能不能输出，就看你了")
    print("啦啦啦")

print("下雨了")

# if-else语句
'''
语法格式：
if 表达式:
    语句一
else:
    语句二
'''
# 逻辑：当程序执行到if-else语句时，首先进行表达式的判断，
# 如果表达式为真，则执行if下面的语句一，否则执行else下面的语句二
# 当执行完语句一或语句二时，继续执行else后面语句

# 从控制台输入一个数，判断奇偶数，偶数输出good，奇数输出well
numStr = input("请输入一个数字:")
# print(type(num))  # str
# 数据类型转换
num = int(numStr)
if num % 2 == 0:
    print("good")
else:
    print("well")


# ****************************************
num1 = 200
if num1 == 200:
    print("1")
if num1 > 100:
    print("么么发   2")
else:
    print("再见   3")
print("好人啊   4")
if num1 < 100:
    print("冷   5")


if 1:
    print("呵呵")
    print("123456")
else:
    print("pppppppp")








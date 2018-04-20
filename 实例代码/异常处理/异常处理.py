# 异常处理
# 文件操作
# os  date

# 错误   异常
'''
在程序运行期间，总会遇到各种各样的错误，有些错误是程序编写有问题造成的，这种错误
我们叫bug，bug是必须修复的。
有些错误是用户输入有问题造成的，这种错误可以通过检测用户输入的内容来做相应的处理。
还有一些错误是无法在程序运行过程中预测的，比如从网络抓取数据，网络突然中断，这类
错误称之为异常，异常在程序运行期间也是必须处理的，否则，程序也会因为这些问题
而终止。
'''

# print("hello wordl")  # 代码编写错误，语法没有错误， 需要更改

# name 'num' is not defined
# print(num)  # 代码编写错误，语法有错误， 需要更改

# ZeroDivisionError: division by zero
# print(10 / 0)  # 代码编写错误，编写时语法没有错误， 运行时语法有错误，需要更改

# print("1234567889000")

# 需求：当程序运行时出现错误，但不会让程序终止，可以跳过该错误继续向下执行。
# 异常处理
'''
try ... except ... else
语法格式：
try:
    语句(预测可能会出现问题的语句)
except 错误码1 as e:
    语句1(错误处理语句)
[except 错误码2 as e:
    语句2(错误处理语句)
...
except 错误码n as e:
    语句n(错误处理语句)
]
[else:
    语句n+1
]
注：else：可有可无
作用：用来检测try语句中的代码块是否有错误，如果有，让except语句捕获错误
信息并处理。

逻辑：当程序执行到try...except...else语句时：
1、如果try后面的语句在执行时出现异常，python就跳回try语句并执行第一个匹配到
该异常的except语句，异常处理完毕后，程序会通过整个try语句(除非在处理异常时
又产生新的异常)
2、如果try后面的语句在执行时出现异常，但是并没有匹配到except语句，异常将会被
提交到最上层的try语句，或者程序的最上层(程序会被终止，并打印错误信息)。
3、如果try后面的语句在执行时没有出现异常，python会执行else后面的语句(如果
else语句存在的话),然后程序会通过整个try语句向下继续执行。
'''
# print(10 / 0)
# print("123")
try:
    # print(10 / 0)
    # print(num)
    print("123")
except ZeroDivisionError as e:
    print("您的除数为0了，请修改")
    print(e)
except NameError as e:
    print("某一个变量未定义")
else:
    print("恭喜你，代码居然没错")

print("*****************************")
'''
try:
    print(10 / 0)
except NameError as e:
    print("变量未定义")

print("~~~~~~~~~~~~~")
'''
# 使用except但是不匹配任何类型错误，当try语句出现异常时，就执行except语句
try:
    print(10 / 0)
except:
    print("嘿嘿嘿")
print("--------------")

# else语句可有可无
try:
    print(10 / 1)
except:
    print("嘿嘿嘿")
else:
    print("啪啪啪")
print("--------------")

# 使用except语句匹配多种异常
try:
    print(num)
    print(10 / 0)
except (NameError, ZeroDivisionError, IndexError):
    print("您可能出现了NameError/ZeroDivisionError/IndexError的错误")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


# 特殊应用
# 1、错误其实是class(类),所有的错误都继承于BaseException，如果在捕获异常时，
# 如果遇到BaseException这个异常，会将子类全部忽略。
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("除数不能为0")
except BaseException as e:
    print("BaseException")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$")

# 如果try语句出现错误，先匹配到BaseException，那么其他的错误就不能被捕获(匹配)到了。
try:
    print(10/0)
except BaseException as e:
    print("BaseException")
except ZeroDivisionError as e:
    print("除数不能为0")
print("===========================")

# 2、可以跨越多层捕获的，fun3调用fun2,fun2调用fun1，实际上是fun1有问题，
# 但只要是try能够捕获到，就能够处理
def fun1():
    print(10 / 0)
def fun2():
    fun1()
def fun3():
    fun2()

try:
    fun3()
except ZeroDivisionError as e:
    print("我也许会出现")

'''
try ... except ... finally
语法格式：
try:
    语句(预测可能会出现问题的语句)
except 错误码1 as e:
    语句1(错误处理语句)
[except 错误码2 as e:
    语句2(错误处理语句)
...
except 错误码n as e:
    语句n(错误处理语句)
]
[finally:
    语句n+1
]
注：finally：可有可无
finally： 无论有没有异常，都会执行(如果又finally语句的话)
'''
try:
    print(10 / 1)
except BaseException as e:
    print("嘿嘿")
finally:
    print("怕怕")



# assert  断言
def func(num, divnum):
    # 断言：第一个参数为判断条件，当条件成立时，代码继续向下执行；
    # 当条件不成立时，程序直接结束在assert语句，提出AssertionError；
    # 第二个参数：为错误提示语
    assert (divnum != 0), "第二个参数不能为0"
    return num / divnum

print(func(10, 1))


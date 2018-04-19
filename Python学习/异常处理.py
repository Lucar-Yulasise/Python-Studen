# 异常处理

# 错误 异常

"""
在程序运行期间，总会遇到各种各样的错误，有些错误是程序编写有问题造成的我们
叫BUG，BUG是必须修复的
有些错误是用户输入有问题造成的，这种错误可以通过检测用户输入的内容来做相应的处理
还有些错误是无法在程序运行过程中预测的，比如从网络突然中断，这类错误称之异常。异常
在程序运行期间也是必须处理的，否则，程序也会因为这些问题而终止

"""

#print("hello wordl")#代码编写错误，语法没有错误，需要修改
#print(num) # 语法错误，变量未定义
#print(10/0) # 代码编写错误，编写时语法没有错误，运行时语法有错误。

# 需求：当程序运行时出现错误，当不会让程序终止，可以跳过该错误

"""
try ····· except····· else

语法：
try:
    语句
except 错误码:
    语句
    
[    
finally:
    语句
]

逻辑： 当程序执行到try except else语句时：
1、如果try后面的语句在执行时出现异常，Python就跳回try语句执行第一个匹配到
该异常的except语句，异常处理完毕后，程序会通过整个try语句（除非在处理异常时有产生新的异常）

2. 如果try后面的语句在执行时出现异常，但是并没有匹配到except语句，异常将会被提交到最上层的try语句
，或者程序


"""
try:
    print(10/0)
except ZeroDivisionError as e:
    print("除数不能为0，除数自动设置为1",10/1)
    print(e)
except NameError as e:
    print("某一个变量为定义")
else:
    print("代码通过编译")

print("*****************************************")


try:
    print(10/0)
except(NameError,ZeroDivisionError,IndexError):
    print("你可能出现了NameError/ZeroDivisionError/IndexError")
print("!!!!!!!!!!!!!!!!!!!!!!")

# 特殊应用
# 1.错误其实是class类，所有的错误都继承于BaseException，在捕获异常时如果遇见了BaseException这异常
# 会将字类全部忽略
try:
    print(10/0)
except ZeroDivisionError as e:
    print("除数不能为0——————")
except BaseException as e:
    print("BaseException")
print("***************%%$$")

try:
    print(10/0)
except BaseException as e:
    print("BaseException")
except ZeroDivisionError as e:
    print("除数不能为0")


print("***************")


def fun1():
    print(10/0)
def fun2():
    fun1()
def fun3():
    fun2()
try:
    fun3()
except ZeroDivisionError as e:
    print("除数不能为0")

try:
    print(10/0)
except BaseException as e:
    print("HH")
finally:
    print("PP")


def func(num,divnum):
    # 断言：第一个参数为判断条件，当条件成立时，代码继续向下执行
    # 当条件不成立，程序直接结束找assert语句，提出AssertionError；
    # 第二个参数：为错误提示语
    assert (divnum !=0),"第二个参数不能为0"
    return num /divnum
print(func(10,5))
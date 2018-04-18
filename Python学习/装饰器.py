def fun1():
    print(123)
def fun2():
    # 函数内部是可以调用其他函数的，但必须保证这个函数在之前声明过
    fun1()
#fun2() 在函数可以定义另一个函数
def fun3():
    def fun4():
        print(4,5,6)
    fun4()
#fun3()
# 装饰器
"""
概念：本身就是一个闭包
什么是闭包：把一个函数作为参数，返回一个代替版的函数。
本质：就是一个返回函数的函数
"""
# 最简单的闭包的写法
def closer():
    def inner():
        print("我是内部的函数")
    return inner
res = closer()
closer()()

# 1、简单的装饰器
# 定义一个函数
def myPrint():
    print("Hello")

# 定义一个函数，该函数有一个函数类型的参数，返回值为该函数的内部函数

def outer(paraFun):
    def inner():
        paraFun()
    return inner
# 调用outer 函数
# 将myPrint函数当作参数传递给outer函数
f = outer(myPrint)
f()

# 2.复杂一点的装饰器
# 定义一个函数，该函数有一个参数
def getAge(age):
    print("我的年龄是 %d "%age)
def outer(paraFun):
    # 内部函数有形参
    def inner(num):
        if num < 0:
            num = 12
        paraFun(num)
    return inner
f1 = outer(getAge)
f1(-45)

"""
通过装饰器的方式，会使我们的代码变得更加简洁：将检测条件的逻辑放到一个相对独立的方法中，
通过装饰器的包装应用到我们需要的地方。
如果我们将检测条件放到原本的函数中，也可以达到相同的目的，但不可置否的是，使用装饰器的方式会使我们以最少的代码达到目的
"""
def getDiv(a,b):
        print(a/b)
def outer(func):
    def inner(num1,num2):
        if num1 < 0:
            num1 = 1
        if num2 <= 0:
            num2 = 1
        func(num1,num2)
    return inner
f3 = outer(getDiv)
f3(12,0)

# 3 使用@符号将装饰器用到函数中
#
def outer(func):
    def inner(num):
        if num < 0:
            num = 0
        print("我使inner")
        func(num)
    return inner
@outer
def getAge(age):
    print(age)
getAge(12)
getAge(-90)

# 4 通用装饰器

def outer(func):
    def inner(*args,**kwargs):
        if len(args) == 0:
            print("请输入内容")
        elif args[0] < 0:
            print("过小")
        print(args)
        print(kwargs)
        func(*args,**kwargs)
    return inner
@outer
def age():
    print("1234343343")
age()

@outer
def hh(l,k):
    print(l,k)
hh(-99,2)

@outer
def AA(l,k):
    print(l,k)
AA(l =99,k = 2)
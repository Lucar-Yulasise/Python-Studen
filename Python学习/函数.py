"""
手机：电池 屏幕 主板 摄像头 外壳
手机：一个完整的项目
电池：功能模块（函数/方法）
屏幕：碎了，换屏幕

认识函数/方法/行为：在于个完整的项目中，某些功能可能会重复使用，那么将这个功能封装成函数，
当我们想要使用这些功能时，直接调用该函数即可。

本质：函数就是对功能模块的封装
优点：1.简化代码结构，增加代码的复用度
      2.如果想修改某些功能或者调试某些功能，只需要修改或调试相应函数即可。

函数的定义：
格式：
def 函数名(参数列表)：
    语句
    return 表达式

1、def:定义函数的关键字：函数的代码块是以def开始的
2、函数名：当前函数的名称，命名规则遵循标识符名规则。
3、（）：参数列表的开始与结束
4、参数列表：格式：（参数1，参数2，参数3、、、、、参数n）：任何传入函数的参数用逗号隔开，参数必须在括号中，参数类似变量名称
5、：冒号：函数的内容以冒号开始，并开始四位缩进
6、语句：函数封装的功能模块
7、retuen;一般用于当前函数的结束，并将信息返回给函数的调用者
8、表达式：即将返回函数调用者的信息
注：函数最后的return 表达式 可以不写，默认返回一个None
注：函数仅仅定义时不会执行，如果函数只定义时，只能说明该函数有这个功能，但是没有被使用


函数的调用：
格式： 函数名(参数列表)
1.函数名：要调用的功能的函数名称
2.():参数列表的开始与结束
3、参数列表：函数调用者传给函数的信息，参数类似于常量
注：即使没有参数，小括号依旧不能省略

函数调用的本质：将实参传递给形参赋值的过程

注：在Python只能先声明再调用。

"""

def myPrint():
    print("Hello world")
    print("你好，世界")
    print("FFFFFFFFFF")

myPrint()
"""
只要见到XXX()就代表了执行了一个函数
"""


"""
型参（形式参数）：定义函数时，小括号中的变量。本质：就是变量
"""
def myPrint1(str1):
    print(str1)
"""
实参（实际参数）：函数调用时传递给函数的数据，本质就是值
"""
myPrint1("Hello")

# 需求：定义一个函数，该函数有name及age两个参数：分行输出
# 注：1参数目前函数定义时的个数于函数调用时的函数，必须一致
#     2目前参数时从左向右以次给形参赋值的
# 定义函数时，如果时多个单词的组合，遵循驼峰原则

def myPrint2(name,age):
    print("-----------------------")
    print(name)
    print(age)
myPrint2("Mick",21)
myPrint2(12,"Mick")


def mySum(num1,num2):
    # return 表达式，可以是任意类型的数据或计算表达式或任意类型其他类型的数据
    # return :将表达式的内容返回给函数的调用者，表达式为什么类型的数据
    # 目前该函数就可以认为是什么类型
    # 当我们的返回值为None时，可以省略。系统会默认添加
    return num1 + num2
res = mySum(1,2)
print(res)

def seShi():
    print("12323")
    return "abc"
res2 = seShi()
print(seShi())
print(res2)


# 关键字参数
# 允许函数调用时，传入参数顺序与声明时的顺序不一致，当赋值不会错乱
def getNameAndAge(nmae,age):
    print("%s   %s"%(nmae,age))
# getNameAndAge("Mick",12)
# getNameAndAge(12,"Mick")

#关键字参数：就是在函数调用时写出形参并等号赋值
#建议：以后尽量在函数调用时使用关键字参数
#但是用关键字参数时，实参的传入循序就任意了
getNameAndAge(nmae="MM",age=18)
getNameAndAge(age=21,nmae="QQ")

#默认参数 概念：在函数定义shi，将某些形参直接赋予初始值。如果函数调用没有传入参数，默认使用初始值。
#注意：如果函数使用了默认值格式，那么将默认参数放到没有默认参数的后面
# 如果使用默认值，函数调用时可以不传该型参，默认使用定义时的初始值。

def myPrint4(name,age=36):
    print(name,age)
myPrint4("MMMM")


# 参数传递

"""
值传递：传递的一个值，传递的时不可变的数据类型；传递的是一个常量

"""
def funnl(num):
    print(num)
funnl(100)
temp = 20
funnl(temp)


#引用传递:传递的是可变数据类型,传递的是变量的内存地址
# list dict set是可变的

def fun2(li):
    li[0] = 100
    print(li)
list1 = [1,2,3]
print(list1)
fun2(list1)
print(list1)



# 函数内部变量与函数外部变量
def fun3(num):
    #函数内部的变量与函数形参名一致了，再内部使用，看变量定义的先后顺序
    #在变量定义之后使用，则会默认取变量的值；在变量定义之前使用，则会默认取形参的值
    num = 33
    print("Num==",num)
    num = 200
    print('Num==',num)
tmp = 20
fun3(tmp)

# 不定长参数（元组）
# 概念：能够处理比形参个数多的实参

# def sum1(a,b):
#     print(a+b)
# def sum2(a,b,c):
#     print(a+b+c)
# sum1(1,3)

# 加了星号（*）的变量可以存放为定义的变量参数，如何函数在调用时，没有指定参数，那么他就是一个空元组
# 如果函数调用时，传入了参数，那么吧这些参数按顺序放到一个元组中。
# 加了星号的变量数据类型就是元组类型
# def fun(*args):
#     num = 0
#     for i in range(args):
#         num += i
#     print(num)
# fun(12,12)


def fun3(*args,num):
    print(args,num)
fun3(12,12,num=1)

#不定长参数（字典）
# 加了两星号（**），可以存放未定义的变量参数:代表键值对的参数列表，数据类型就是字典类型

def myTest(**kwargs):
    print(kwargs)

# 传入参数格式
myTest(a=1)
myTest(QQ=22,wx=200)


def test2(num ,**kwargs):
    print(num)
    print(kwargs)
    print(kwargs.get("a"))
test2(100,a=100)
test2(num=200,a=222)


# 定义一个通用函数
def fun(*args,**kwargs):
    print(args)
    print(kwargs)
fun()
fun(1,2,3,4)
fun(a=1,b=2,c=3)

# 定义函数

def getStudent(id,name,sex,**kwargs):
    pass # 代表一条空语句，本身没有任何意义，只是一条占位语句
getStudent(111,"aa",1)
getStudent(100,"bb",1,age=12,height=150,weight=100)


# 匿名函数
"""
概念：不使用def这个关键字定于函数，用lambda关键字来创建匿名函数

特点：
1、lambda 只是一个表达式，函数体比def简单得多
2、lambda 本质只是表达式，而不是代码块，仅仅只能封装简单的逻辑。
3、lambda 函数有自己的命名空间，并且不能访问自由的参数列表

格式：lambda 参数1，参数2...参数n：表达式
表达式，只是一体条简单的语句，不能包含循环，不能有return,yiled,但运行简单的if语句，如果表达式为元组，用小括号阔起来
"""
res = lambda num1,num2,num3,num4:num1+num2+num3+num4
print(res(1,2,3,4))

# 偏函数
# int() 函数可以字符串转为整型，默认是十进制转化，可以设置进制格式（base = 2）
print(int("10101"))
print(int("1011",base=8))

def myInt(str):
    return int(str,base=2)
print(myInt("101110"))

# functools 模块
import functools
# functools.partial 可以创建偏函数，可以不再使用函数的方式创建
# 偏函数：把函数的某个参数固定（默认值），返回一个新的函数，使用偏函数后再调函数会简单点
#
newInt = functools.partial(int,base=2)
print(newInt("1011"))

def newDiv(a,b):
    return b/a
print(newDiv(2,10))
print(newDiv(15,2))

div_2 = functools.partial(newDiv,2)
print(div_2(10))

# 函数当作数据类型使用
def sum1(a,b):
    return a + b
f = sum1
print(type(f))
f2 = sum1(1,2)
print(type(f2))
# 1、函数可以作为一种数据类型 function
# 2 、函数的返回值可以作为一种数据
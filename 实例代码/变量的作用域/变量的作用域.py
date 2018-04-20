# 变量的作用域
# 异常处理   文件处理   os  date
# B G E L
'''
作用域：变量的可以使用的范围
程序中的变量并不是在当前文件下任意位置均可使用，访问的权限决定于变量定义的
位置。

变量的作用域：
B(bulit-in)   内建作用域
G(Global)    全局作用域
E(Enclosing)  闭包函数外面的函数中
L(Local)  局部作用域

变量的查找规则：L -> E -> G -> B, 先从局部找，找到直接使用；找不到去闭包
作用域查找，找到直接使用；找不到去全局作用域中查找，找到直接使用；
找不到去内建作用域中查找，找到直接使用；找不到直接报错。

在python中，只有模块(module)、类(class)、函数(def, lambda)才会引入新的作用域。
其他的代码块(例如if、for、try)是不会引入新的作用域的，也就是说，在这些语句中
定义的变量，在其他位置也可以使用。
'''
# 验证
if 1:
    a = 10
    print(a)
print(a)

# num = 1
# print(num)  # NameError: name 'num' is not defined

# 函数会产生新的作用域
def func():
    b = 200
    print(b)
func()
# print(b)  # 报错 NameError: name 'b' is not defined

# L -> E -> G -> B
'''
# dir()  为python的内建函数 ： 作用域范围为内建作用域  内建函数/内建变量
dir = 1  # Global 全局作用域  全局变量
def outer():
    dir = 2  # Enclosing  闭包作用域  闭包内部变量 
    def inner():
        dir = 3  # Local  局部作用域  局部变量
    return inner
'''

print("*************脚麻吗**************")
num = 100 # 定义一个名为num的全局变量
print('1====', num)   # 100

def func():
    # num = 200  # 相当于在局部范围def内重新定义了一个名为num的局部变量
    global num  # global 变量名  ： 先声明当前变量为全局变量，方便在
                # 局部范围内直接使用或修改全局变量
    # 如果使用global关键字时，需要放在函数的开始位置
    num = 200
    # 在函数内部可以直接使用全局变量，但如果该变量没有global修饰词时，是不能
    # 修改全局变量的。
    print("2====", num)  #
func()
print("3====", num)  #

print("--------------------------------")

i = 666
def outer():
    i = 555   # 局部变量
    def inner():
        nonlocal i  # nonlocal 非局部的
        i = 444   #
        print("inner ==", i)
    inner()
    print("outer ==", i)

outer()
print("i ==", i)


a = 200
def outer():
    a = 300
    def inner():
        nonlocal a
        a = 400
        def litter():
            nonlocal a
            a = 500
            print(a)
        litter()
        print(a)
    inner()
    print(a)

outer()























# 变量的作用域

# B G E L
"""
作用域：变量的可以使用范围
程序中的变量并不是找当前文件下任意位置均可使用的，访问的权限决定于变量的位置

变量的作用域：
B(bulit-in) 内建作用域
G(Global) 全局作用域
E(Enclosing) 闭包函数外面的函数
L(Local) 局部作用域

变量的查找规则：L -> E -> G -> B,先从局部找，找到直接使用，找不到再去

再Python中，只有模块（module）、类（class）函数（def，lambda）才会引入新的作用域
其他的代码块（例如if for try）是不会引入新的作用域，也就是说，在这些语句中定义的变量，在其他位置也可以使用

"""

if 1:
    a = 10
    print(a)
print(a)

# 函数会产生新的作用域
def func():
    b = 200;
    print(b)
func()

"""
# dir() 为Python的内建函数：作用域范围为内建作用域 内建函数/内建变量
dir = 1 # Clobal 全局作用域 全局变量
"""

num = 100
print("1====",num)

def func():
    num = 200
    print("2===",num)
func()
print("3=====",num)


def func():
    global num
    # 如果使用global关键字时，需要放在函数的开始位置

    num = 200
    print("2=====",num)

func()

print("------------------------------------------------")

i = 666
def outer():
    i = 555 # 局部变量
    def inner():
        nonlocal i # 非局部变量
        i = 444
        print("inner == ",i)
    inner()
    print("outer == ",i)
outer()
print(i)


a = 200
def outer():
    a = 300
    def inner():
        a = 400
        print(a)                                                 
    inner()
    print(a)
outer()

#闭包
"""
闭包
概念：在函数体内定义的内部函数，并且该内部函数使用的外部数的变量，外部函数将内部函数作为返回值返回，该函数就叫闭包


"""
one = 100
def F():
    two = 200
    def N():
        three = 300
        return three
    return N

f = F()
a = f()
print(a)

one = 300
def D():
    global one
    one = 44
    return  one
print(one)

def A():
    num = 666
    def B():
        nonlocal num
        num += 1
        print(num)
    return B
f1 = A()
f1()
f1()
f1()

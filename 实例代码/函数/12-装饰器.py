# 装饰器
def fun1():
    print(123)
def fun2():
    # 函数内部是可以调用其他函数的，但必须保证这个函数在调用之前声明过
    fun1()
# fun2()

# 在函数内部可以定义另一个函数
def fun3():
    def fun4():
        print(456)
    fun4()
# fun3()

# 装饰器
'''
概念：本身就是一个闭包
什么是闭包：把一个函数作为参数，返回一个代替版的函数。
本质：就是一个返回函数的函数
'''
# 最简单的闭包的写法
def closer():
    def inner():
        print("我是内部的函数")
    # 执行inner函数
    # inner()
    return inner

res = closer()   # res ===== inner   inner函数
# print(type(res))  # function函数类型
res()   # inner()
# print(res)

# 整合写法
closer()()










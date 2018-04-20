# 闭包
'''
闭包：
概念：在函数体内定义的内部函数，并且该内部函数使用的外部函数的变量，外部函
数将内部函数作为返回值返回，该内部函数就叫做闭包。

优点：避免变量污染全局环境，我们可以在全局范围内间接使用局部变量。
缺点：数据会长期驻留在内存中，造成内存浪费，在IE浏览器中，极易崩溃，所以
请慎重使用。
'''
one = 100  # 全局
def F():
    two = 200  # Enclosing
    def N():
        three = 300  # 局部
        return three
    return N

f = F()   # f === N
a = f()   # f() === N()
print(a)


def A():
    num = 666
    def B():
        nonlocal num
        num += 1
        print(num)
    return B
f1 = A()   # f1 === B
f1()   # 667
f1()   # 668
f1()   # 669

f2 = A()
f2()  # 667




"""
生成器： generator : 使用yield的函数被称为时是生成器函数
使用yield的函数于普通函数的区别：生成器函数是一个返回迭代器的函数，只能用于迭代器
"""

def go1():
    print(1)
    print(2)
    print(3)

def go2():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30
print(type(go2))
print(type(go2()))
a = go2()
next(a)
next(a)
next(a)

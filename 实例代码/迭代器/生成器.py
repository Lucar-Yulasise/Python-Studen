'''
生成器：generator：使用yield的函数被称为是生成器函数。
使用yield的函数与普通函数的区别：生成器函数是一个返回迭代器的函数，只能用于迭代操作
可以认为生成器就是一个迭代器
'''
def go1():
    print(1)
    print(2)
    print(3)
# print(type(go1))  # function
# print(type(go1()))  # NoneType

# yield 命令
def go2():
    print(1)
    yield 111111
    print(2)
    yield 20
    print(3)
    yield 30

print(type(go2))  # function
print(type(go2()))  # generator

a = go2()
# next(a)
# next(a)
# next(a)
# next(a)  # StopIteration
print(next(a))
print(next(a))
print(next(a))
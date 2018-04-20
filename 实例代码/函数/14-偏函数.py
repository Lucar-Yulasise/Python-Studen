# 偏函数
# int()  函数可以将字符串转为整型，默认是十进制转换，可以设置进制格式
# （base=2 8 10 16）
print(int("1010"))
print(int("1011", base=2))

# 仿写偏函数功能
def myInt(str):
    return int(str, base=2)

# myInt("1011") == int("1011", base=2)
print(myInt("1011"))

# functools 模块
import functools

# functools.partial  可以创建偏函数，可以不再使用函数的方式创建
# 偏函数：把函数的某些参数固定(默认值)，返回一个新的函数，使用偏函数后
# 再调用函数会简单点

# functools.partial(即将更改的函数, 原函数的各个参数)
# 第一个参数为函数名
# 从第二个参数开始：为即将固定的参数， 从左向右依次给原函数的参数赋值
# 如果在偏函数中原函数的参数未全部赋值，后期调用函数时，从没有值的参数开始赋值

newInt = functools.partial(int, base=2)
print(newInt("1011"))

def newDiv(a,b):
    return b / a
print(newDiv(2, 10))
print(newDiv(15, 2))

div_2 = functools.partial(newDiv, 2)
print(div_2(10))




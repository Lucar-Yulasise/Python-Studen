# 不定长参数
# 概念:能够处理比形参个数多的实参
def sum1(a,b):
    print(a+b)
def sum2(a,b,c):
    print(a+b+c)

# print(max(1,2,6,9,0,8,7,6,4))

# 加了星号(*)的变量，可以存放未定义的变量参数。
# 如果函数在调用时没有传入参数，那么他就是一个空元组，
# 如果函数调用时传入参数，那么把这些参数按照顺序放到元组中。
# 加了星号(*)的变量的数据类型就是元组类型。

# 计算所有传入的实参的和
def fun(*args):
    print(args)
    num = 0
    for i in args:
        num += i
    print(num)
fun()
fun(1)
fun(1,2,3)
fun(6,8,9,6,5,4,3)


def fun2(num1, num2, *args):
    print(num1)
    print(num2)
    print(args)
# fun2(1)  # error

fun2(1,2)
fun2(1,2,3)
fun2(1,2,3,4,5,6,7)

def fun3(*args, num):
    print(args)
    print(num)
print("-----------------")
fun3(1,2,3,4, num=5)








# def setName():

# 匿名函数
'''
概念：不使用def这个关键字定义函数，用lambda关键字来创建匿名函数

特点：
1、lambda 只是一个表达式，函数体比def简单的多
2、lambda本质是表达式，而不是代码块，仅仅只能封装最简单的逻辑
3、lambda函数有自己的命名空间，并且不能修改除自己的参数列表以外的参数或全局命名
空间的参数

格式： lambda 参数1,参数2...参数n : 表达式
表达式:只是一条简单的语句，不能包含循环，也不能有return，也不能有yield，
但允许有简单的if语句。如果表达式为元组，用小括号括起来。
'''
def sum1(num1,num2,num3,num4):
    if num1 > 100:
        num1 = 1
        num2 = 2
    return num1 + num2 + num3 + num4
# print(sum1(1,2,3,4))
# 函数的定义
res = lambda num1,num2,num3,num4 : num1+num2+num3+num4
# 函数的调用
print(res(1,2,3,4))

# if-else可以写在lambda中，格式为：
# 结论1 if 判断表达式 else 结论2
# 当判断表达式为真时，取结论1；当判断表达式为假时，取结论2
add1 = lambda num:"True" if num==1 else "False"
print(add1(1))
print(add1(2))

pow1 = lambda num1, num2 : num1 * num2
print(pow1(1,2))

a = 30
def add3(num1):
    return a+num1
print(add3(1))

b = 200
res5 = lambda num : b
print(res5(1))





# 编写一个函数，功能：将传入的参数相加，返回两个参数的和

# 函数的定义
def mySum(num1, num2):
    # return 表达式  表达式可以是任意类型的数据或计算式或任意其他类型的数据
    # return：将表达式的内容返回给函数的调用者，表达式为什么类型的数据，
    # 目前该函数就可以认为是什么类型
    return num1 + num2

# 函数的调用
mySum(1, 2)
# 输出：值
res = mySum(2,3)
print(res)
print(type(res))


def ceShi():
    print("123456")
    # 当函数执行到return语句时，代表该函数执行结束，return后面的代码不再执行
    return "abc"
    # print("2468000000000")
ceShi()

res2 = ceShi()
print(res2)


# 默认返回值  None
def testReturn():
    print("我是测试")
    # return None:当我们的函数的返回值为None,可以省略，
    # 系统默认会自动添加这行代码
    return None

testReturn()

# res3 = testReturn()
# print(res3)


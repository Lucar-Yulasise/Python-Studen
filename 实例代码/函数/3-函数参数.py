
# 需求：编写一个函数，在函数调用时出入函数一个字符串，函数的功能是打印改字符串

# 定义一个只有一个参数的函数
# 形参(形式参数):定义函数时，小括号中的变量。本质：就是变量
# 在函数中，是可以正常使用形参的
def myPrint(name):
    print("***************")
    print(name)

# 函数的调用
# 实参(实际参数):函数调用时传递给函数的数据，本质是值
# 注：如果函数在声明时有形参，那么函数调用时就必须传入实参
myPrint("abcdeghj")
# TypeError: myPrint() missing 1 required positional argument: 'name'
# 错误：调用函数时，缺少必须的参数
# myPrint()

# 需求：定义一个函数，该函数有name及age两个参数，功能：将这个形参分行输出
# 建议：定义函数时，如果是多个单词的组合，遵循驼峰原则，单词的首字母大写
def getNameAndAge(name, age):
    print("----------------")
    print(name)
    print(age)

# 调用函数
# getNameAndAge("MM",18)
getNameAndAge(28, "GG")
# getNameAndAge("WW")

# 注：参数：目前函数定义时的个数与函数调用时的个数必须一致；
# 目前实参是从左向右依次给形参赋值的



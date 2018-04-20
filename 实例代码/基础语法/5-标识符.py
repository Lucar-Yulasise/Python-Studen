# 什么叫标识符：就是一个字符串（但字符串不一定是标识符）
# 标识符的作用：给变量、常量、函数、类、对象等命名的
# 标识符的命名规则：1、只能包含数字、字母及下划线
#                    2、不能以数字开头
#                    3、不能是python的关键字
#                    4、区分大小写
#                    5、具有一定的实际意义

# python3以后支持汉字，但以后不建议使用

a = 30
A = 40
print(a)
print(A)

A12 = 40
# qw*er = 60  # 错误
# 1qw = 77   # 错误
a_b = 56
_c = 99

# def = 88  # 错误  关键字

# 仅作娱乐
中国 = "china"
print(中国)

# 获取python中所有的关键字
import keyword
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert',
# 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
# 'not', 'or', 'pass', 'raise', 'return', 'try',
# 'while', 'with', 'yield']   33个




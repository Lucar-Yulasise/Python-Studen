# from...import语句
# 作用：从一个模块中引入部分功能
# 格式： from module import name1[, name2...namen]

# import module1,modele2
# module1.myPrint()  # 1
# module1.eat()  # eat
# modele2.myPrint()  # 2
# modele2.run()  # run

from module1 import eat,myPrint
from modele2 import myPrint
# 后写的函数或变量或类会把之前相同的函数或变量或类替换掉
# 遵循就近原则
# def myPrint():
#     print("嘿嘿")
# def myPrint():
#     print("呵呵")

# 使用模块中的功能,直接调用
eat()
myPrint()


# os  date   面向对象

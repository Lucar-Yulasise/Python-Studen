#from ....import 语句
# 从一个模块中引入部分功能
# 格式： from module import name
from module1 import eat,myPrint

# *:通配符，代表所有
# 作业：把一个模块中所有的内容全部引入当前模块下
# 该格式不要过多的使用
from module1 import *
eat()
myPrint()

def myPrint():
    print("嘿嘿")
myPrint()
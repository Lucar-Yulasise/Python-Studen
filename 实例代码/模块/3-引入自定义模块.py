# 自定义模块： 自己创建的.py文件

# 引入自定义模块, 引入模块时不要加.py后缀
import module1
import modele2

# import module1, modele2

# 使用自定义模块中的内容
# 格式： 模块名.函数名/变量名
print(module1.newPI)
module1.myPrint()
modele2.myPrint()

def myPrint():
    print("123")
myPrint()


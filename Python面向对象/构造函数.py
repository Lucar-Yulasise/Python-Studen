# 构造函数

'''
构造函数：__init__(参数列表)：在使用类创建对象时自动调用
'''
class Person():
    # 定义属性（定义变量）
    # 注意：类里面的方法目前必须意self为初是常数
    # self:代表当前类的实例对象
    name = ""
    age = 0
    def eat(self):
        print("person---eat")
    def run(self):
        print("person---run")
    def sleep(self,hours):
        print("我睡了%d小时"%hours)

    def __init__(self,name,age,weight=30):
        self.name = name
        self.age = age
        self.weight = weight
        print("我显示的是init函数")

per1 = Person("Mick",21)
print(per1.name)
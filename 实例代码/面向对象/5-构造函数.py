# 构造函数
'''
构造函数：__init__(参数列表)  ：在使用类创建对象时自动调用。
注意：如果自己不写构造函数，系统默认也会加上一个空的构造函数。
'''
class Person():
    # 类属性
    # name = ""
    # age = 0

    # 默认的构造函数
    # __init__函数没有返回值，不能写return
    # def __init__(self):
    #     pass

    # 自己重新写构造函数时，只能更改参数列表及函数体，不能写return这条语句
    # def __init__(self):
    #     print("我显示的是init函数")

    def __init__(self, name, age, weight=30.0):
        print("小兔子乖乖")
        # 对象属性(定义在构造函数中的属性为对象属性)
        self.name = name
        self.age = age
        self.weight = weight
    # 建议：一个类中最好只有一个init函数，如果写了多个，程序不会报错，
    # 但是只会执行最后一个写的init函数

    def eat(self):
        print("person--eat")
    def sleep(self, hours):
        print("我睡了%d小时" % hours)


# 建议使用关键字
per1 = Person(name="Lily", age=30, weight=50.0)
per1.name = "TT"
print(per1.name, per1.age)   # "" 0
print(per1.weight)
print(per1)

per2 = Person("Tom", 45)


# Person()

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


"""
实例化对象：
格式：对象名 = 类名（参数列表）
注意：就算没有参数，也不能省略小括号
"""

f1 = Person() # 执行了一个构造方法
print(f1)
print(id(f1))
print(type(f1))
f2 = Person()
print(f2)
print(id(f2))
print(type(f2))

list1 = [1,2,3]
list2 = [1,2,3]
print(id(list1))
print(id(list2))

per1 = Person()

per1.age = 18
per1.name = "lili"
print(per1.name,per1.age)
print("----------------------------------------")
per1.sleep(10)

per2 = Person()
per2.eat()
print(per2)

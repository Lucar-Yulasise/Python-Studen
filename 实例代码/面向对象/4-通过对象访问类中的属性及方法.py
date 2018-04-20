class Person():
    name = ""
    age = 0
    def eat(self):
        print("person--eat")
        # self：代表当前类的实例对象
        print(self)

    def run(self):
        print("person--run")
    def sleep(self, hours):
        print("我睡了%d小时" % hours)

# 通过Peson类实例化一个对象per1
per1 = Person()
'''
访问类中的属性:
格式：对象名.属性名
修改类中的属性:
格式： 对象名.属性名 = 新值
'''
print(per1.age)
per1.age = 18
print(per1.age)
per1.name = "Lily"
print(per1.name)

'''
访问类中的方法/函数/行为
格式：对象名.函数名(参数列表)
# 类中的函数，默认第一个参数为self，在对象调用时，默认会把当前对象
传给self这个形参，我们真正在调用时是不用管这个形参的。
'''
per1.eat()  # self
print(per1)  #
per1.sleep(12)

print("--------------------")
per2 = Person()
per2.eat()
print(per2)












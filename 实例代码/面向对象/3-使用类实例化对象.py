class Person():
    name = ""
    age = 0
    def eat(self):
        print("person--eat")
    def run(self):
        print("person--run")
    def sleep(self, hours):
        print("我睡了%d小时" % hours)

'''
实例化对象：
格式：对象名(变量名) = 类名(参数列表)
注意：就算没有参数，小括号也不能省略
'''
# 实例化对象
per1 = Person()
print(per1)
print(type(per1))
print(id(per1))

per2 = Person()
print(per2)
print(type(per2))
print(id(per2))

# Person() 执行了一个叫构造函数的方法
per3 = Person()





# list
# list1 = [1,2,3]
# list2 = [1,2,3]
# print(id(list1))
# print(id(list2))
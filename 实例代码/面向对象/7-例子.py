class Person():
    def __init__(self,name):
        self.name = name
        self.age = 200

class Student():
    def __init__(self, Person):
        # per属性是Person类型的变量
        self.per = Person

per1 = Person("Lily")
stu = Student(per1)

print(stu.per)
print(per1)

print(stu.per.name)
print(stu.per.age)
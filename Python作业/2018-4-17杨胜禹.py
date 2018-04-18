'''
学生信息管理：
用一个列表存储所有学员信息：学员信息如下：姓名name、年龄age、年级grade、
成绩score(成绩默认60)

1、打印所有学员信息
2、新增学员信息
3、计算所有学员年龄的和
4、将所有学员的年龄及年级加1
5、将所有学员成绩置为0，并打印所有学员信息
6、通过年龄对学员排序，可以设置升序或降序，并打印所有学员信息  (选作)
(选择排序   冒泡排序  快速排序   插入排序)
'''
'''
学员信息用什么保存  
'''
student = [{"name":"lily","age":12,"grade":3,"score":60},
           {"name":"李雷","age":19,"grade":4,"score":89}]

def show_all():
    for stu in student:
        print("name:%s  age:%d  grade:%d  score:%2d"%(stu["name"],stu["age"],stu["grade"],stu["score"]))
    print("****信息完成*******")

def addAge():
    for stu in student:
        num = stu["age"]
        sum = num+num
        print(num)
    print("年龄的总和为：%d"%sum)

def insert_student(name,age,grade,score=60):
    student.append({"name":name,"age":age,"grade":grade,"score":score})


insert_student("Mick",age=12,grade=4,score=99)
insert_student("Fake",age=15,grade=4)
insert_student("张三",age=21,grade=5,score=87)
addAge()
show_all()
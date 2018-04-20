'''
设计类：
类名：见名知意，类名的首字母大写，其他遵循命名规则。
属性：见名知意，其他遵循命名规则。
行为（方法，功能，函数）：见名知意，其他遵循命名规则。
'''
'''
创建类：
格式：
class 类名(父类列表):
    属性(个数不定)
    行为(个数不定)
    
类：一种数据类型,不占内存，学过的类：String，List，Tuple等。
用类创建出来的实例对象（变量）是占内存的。
'''
# 创建一个Person类
class Person():
    # 定义属性(定义变量)
    name = ""
    age = 0
    # 行为：定义方法(函数)
    # 注意：类里面的方法/函数目前必须以self为第一个参数
    # self：代表当前类的实例对象
    def eat(self):
        print("person--eat")
    def run(self):
        print("person--run")
    def sleep(self, hours):
        print("我睡了%d小时" % hours)

'''
类名为：Wife
属性：age  sex   height
行为：购物   做头发hours   旅游num

类名为：Husband
属性：age  weight  faceValue
行为：擦地  做饭  挣钱money

类名为：Car
属性：color  type
行为：跑
'''

class Wife():
    age = 0
    sex = 1
    height = 30.0
    def shopping(self):
        print("我们喜欢购物")
    def makeHair(self, hours):
        print("做头发花了%d个小时" % hours)
    def play(self, num):
        print("去玩了%d个地方" % num)

class Husband():
    age = 18
    weight = 60.0
    faceValue = 100
    def clearFloor(self):
        print("擦地")
    def cook(self):
        print("做饭")
    def work(self, money):
        print("今天的工资为%d" % money)











"""
设计类：
类名：见面思意，类名的首字母大写
属性：见名知意，其他遵循命名规则
行为：同上

"""

'''
创建类：
格式：
class 类名(父类列表):
    属性
    行为
'''

class Person():
    # 定义属性（定义变量）
    # 注意：类里面的方法目前必须意self为初是常数
    # self:代表当前类的实例对象
    name = ""
    age = 0
    def myPrint(self):
        print("person---eat")
    def run(self):
        print("person---run")
    def sleep(self,hours):
        print("我睡了%d小时"%hours)

    """
    l
    """

class Wife():
    age = 0
    sex = 0
    height = 0
    def gouwu(self):
        print("我们喜欢购物")
    def ztf(self,hours):
        print("HHHdasu %d"%hours)
    def lv(self,num):
        print("旅行了%d个地方"%num)

class Husband():
    age = 0
    weight = 0
    faceValue = 0
    def cadi(self):
        pass
    def zf(self):
        pass
    def zq(self,money):
        pass
class Car():
    color = 0
    type = 0
    def run(self):
        pass


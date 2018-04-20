# 不定长参数
# 加了星号(*)的变量，可以存放未定义的变量参数。
# 如果函数在调用时没有传入参数，那么他就是一个空元组，
# 如果函数调用时传入参数，那么把这些参数按照顺序放到元组中。
# 加了星号(*)的变量的数据类型就是元组类型。

# 加了两个星号(**)的变量，可以存放未定义的变量参数。
# 加了两个星号(**)的变量:代表键值对的参数列表，数据类型就是字典类型。

# 定义一个函数
def myTest(**kwargs):
    print(kwargs)

# 函数的调用
myTest()
# 传入参数格式 : key=value
myTest(a=1)
myTest(qq=100, wx=200, mm=300)

#
def test2(num, **kwargs):
    print(num)
    print(kwargs)
    print(kwargs.get("a"))
    # print(kwargs["a"])

test2(100)
test2(200,a=100)
test2(num=300,a=222)


# 定义一个通用的函数
def fun(*args, **kwargs):
    print(args)
    print(kwargs)
fun()
fun(1,2,3,4)
fun(a=1, b=2, c=3)
fun(1,2,3,d=4,f=5)

# 定义一个获取学生信息函数：
# 必须传入：id，name，sex  可选：height，age，weight
def getStudent(id,name,sex, **kwargs):
    pass

getStudent(111,"aa",0)
getStudent(100,"bb",1,age=12, height=150)
getStudent(100,"bb",1,age=12, height=150, weight=100)



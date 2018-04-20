# 如果想要使用math里面的内容，需要导入math库
# 库：本质就是一个.py文件
# 导入库的格式   import math
import math
# 当导入math库文件时，我们可以调用math里面所有的内容
print(math.pi)
# 1、向上取整
print(math.ceil(1.03))

# 2、向下取整
print(math.floor(1.99))

# 3、返回小数部分与整数部分, 返回的数据都是浮点型
# (小数部份，整数部分)
print(math.modf(3.22))

# 4、开方  返回浮点数
print(math.sqrt(9))   # 3

# 5、返回绝对值  返回浮点数
print(math.fabs(10))   # 10.0

# 6、求e的x次幂   math.exp(x)
print(math.exp(2))

# 7、log()   指数  返回浮点数
print(math.log(100, 10))   # 2

# 8、log10()    返回浮点数
print(math.log10(100))  # 2

# ************三角函数(了解)***************
# acos(x)  返回x的反余弦弧度值， x的取值范围  -1  -  1 之间
print(math.acos(0.34))
# math.asin(x)  x的取值范围  -1  -  1 之间
# math.atan(x)  x为任意一个数
# math.sin(x)  x为任意一个数
# math.cos(x)  x为任意一个数
# math.tan(x)  x为任意一个数

# 将角度转为弧度
print(math.radians(180.0))
# 将弧度转为角度
print(math.degrees(math.pi))


# ************随机数（重点）***********
# 想要获取随机数，需要导入random库
import random

# 1、从一个序列中随机挑选一个元素
print(random.choice([1, 2, 3, 4, 5, 6]))
# 2、range(x)
print(random.choice(range(6)))  # range(6)  === [0,1,2,3,4,5]
# 3、从字符串中随机选一个字母
print(random.choice("meakelra"))

# 4、从指定范围内，按指定的递增奇数获取随机数
# 语法格式：random.randrange([start,] stop [, step])
# start: 指定开始的值，这个值包含在取值范围内，如果不写该参数，默认从0开始
# stop:指定结束的值，但这个值不包含在取值范围内
# step:指定的递增基数，默认值为1

# 从0-99之间随机选一个数
print(random.randrange(100))
print(random.randrange(20, 55))
print(random.randrange(0, 10, 4))   # 0 4 8

# 4位
# random.randrange(1000,10000)

# 5、随机产生一个0-1之间的浮点数
print(random.random())

# 取整   0-10 之间的整数
print(int(random.random() * 10))










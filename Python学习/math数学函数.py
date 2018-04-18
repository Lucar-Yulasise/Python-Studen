import math
import random

print(math.pi)

#向上取整
print(math.ceil(1.03))

#向下取整
print(math.floor(1.99))

#返回小数部分与整数部分，返回的数据全都是浮点数
print(math.modf(3.22))

#开方
print(math.sqrt(9))

# 返回绝对值，浮点数
print(math.fabs(10))

#求 e 的 x 次幂
print(math.exp(2))

#指数
print(math.log(100,10))
print(math.log10(100))

#返回 x 的反余弦
print(math.acos(0.34))
print(math.atan(0.24))
print(math.sin(2))
print(math.cos(2))
print(math.tan(2))

# 将角度转为弧度
print(math.radians(180.0))
# 将弧度转为角度
print(math.degrees(math.pi))


#随机数

print(random.randint(1,900))
print(random.choice([12,23,34,12,34,23]))
print(random.choice(range(6)))
print(random.choice('abcdefghijklmnopqrstuvwxyz'))
print(random.randrange(100))
print(random.randrange(20,55))
print(random.randrange(1000,9999))#指定递增奇数

print(random.random())#随机产生0到1的随机数
print(int(random.random()*10)) #取整
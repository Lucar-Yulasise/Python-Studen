"""
程序名称：变量和常量 数字类型 类型转换
程序功能：熟悉变量和常量的使用 数字类型的使用
程序作者：杨胜禹
"""
#变量是程序运行时可以发生变化的
age = 22
weight = 20
name = "Mick"
print(type(weight))
print(type(age))
print(type(name))
a = 20
print(a)
print(id(a))
print(id(weight))
a = 23
print(a)
print(id(a))
#删除变量 不能够再继续使用
del a
#print(a)

# 常量是不会变的量
# 定义： 全部大写



# Number 数字类型
# 分类 ： int 整数  float 浮点型 complex
num1 = 100;
print(num1)
num2 = 1.22;
print(num2)

# 用某一个变量给另一个变量赋值
num3 = num1
print(num3)

num4 = num2 =num3 =num1
print(num4)

num7,num8,num9 = 999,78,12;
print(num7,num8,num9)
a = 100
b = 200
tem = 0
tem = b
b = a
a = tem
print(a,b)

#交换数据
n1 = 100
n2 = 200
n1,n2 = n2,n1
print(n1,n2)

f1 = 1.2334
print(f1)
print(type(f1))
f2 = f1
print(f2)
f3 = f4 = f5 = 2.122
print(f3)
f8 = 1.0
f9 = 1.23
print(f8+f9)

# complex 复数
# 定义 complex(y,x) x：代表实数 y:代表虚数
com = complex(12,2)
print(com)

#数字类型转换
# 语法格式： 转换类型（对象）
# int -> float float -> int
#int -> string  str -> float
int1 = 200
print(type(int1))
f01 = float(int1)
print(type(f01))
f02 = 2.9   #数据类型转换，只保留整数部分
int2 = int(f02)
print(int2)
print(type(int2))

srt1 = "1221"
int3 = int(srt1) # 当字符串有不是数字的字符时，转换失败。
print(int3)
#print(int("1+2"))
print(int("+123"))
print(int("-123"))

print(float("2323"))
print(float("22.323"))
#print(float("1.32.3"))
#print(float("1.223advb"))
print(str(12))
print(str(1.32))

# 数学函数
# 1.求绝对值 abs（）
print(abs(-12))
print(abs(-2))
print(abs(3))
# 1. 比较两个数的大小
#    如果前面的数大，返回1，小返回-1，相等返回0

a = 34;
b = 12;
result = (a > b) -(a <b)
print(result)

# 返回指定参数的最大值，最小值max() min()
te1=  [12,23,1,32,3,4]
print(max(te1))
print(min(te1))

# 求幂运算 pow(x,y)
print(pow(2,3))

# 返回浮点数的四舍六入值round() Python3.x 如果距离俩边的整数大小一致，取偶不取奇
# round(x,[n]) x:即将四舍六入的数 n，可选参数，保留几位小数
print(round(23.6))
print(round(12.2))
print(round(2.5))
print(round(1.5))
print(round(1.23743,2))


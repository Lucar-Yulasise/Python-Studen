# 什么是表达式：由变量、常量和运算符组成的式子称为表达式
# 一条语句：见到一个分号代表一条语句的结束，如果一行上面只有一
# 条语句，分号可以省略；如果一行上面有多条语句，每条语句用分号隔开。
# 一行语句：一行上面可以有多条语句，每条语句用分号隔开。
# 建议：一行上面尽量只写一条语句
a = 100
b = 200
print(a)
print(b)

# 运算符

# 1、数学运算符
# 功能：进行数学运算
# +   加号  两个对象相加
# -   减号  两个对象相减
# *   乘号  两个对象相乘
# /   除号  两个对象相除   x / y   返回浮点数
# **  幂运算   x ** y   x的y次幂
# //  整除 地板除    只保留商   python中的整除，如果是负数，向负无穷无限靠近
# %  取余    返回余数
num1 = 5
num2 = 2
print(num1 + num2)  # 7
print(-1 + 3)  # 2
print(4 - 1) # 3
print(4 - 9) # -5
print(1 * 2) # 2
print(-1 * 2)  # -2
print(-1 * (-2)) # 2

print(13 / 4)  # 3.25
print(-13 / (-4))  # 3.25
print(-13 / 4)  # -3.25

print(2 ** 5)

print(13 // 4)  # 3
print(-13 // (-4))  # 3
print(-13 // 4) # -4
# print(7 % 2)

print(13 % 4)  # 1
print(-13 % (-4))  # -1
print(-13 % 4) #  3

# a // b = q  商
# a % b = r    余数
# a = b * q + r
# r = a - b * q
# r = -13 - (4 * -4)

# 2、赋值运算符
# 2.1、基本的赋值运算符    =
# =  将等号右边的内容赋值给左边的变量
# 读： 从右向左读
num3 = 3
num4 = 4 + 5
print(num4)
# 2.2、组合赋值运算符
# +=  -=  *=  /=  //=  %=  **=
# a += b   ====>  a = a + b
# a -= b   ====> a = a - b
# a *= b   ====> a = a * b
# a /= b   ====> a = a / b
# a //= b   ====> a = a // b
# a **= b   ====> a = a ** b
# a %= b   ====> a = a % b
num5 = 1
num5 += 6
print(num5)


# 3、比较运算符   后期用于if判断
# ==  等于 比较两个值是否相等   如果相等返回True，如果不相等返回False
# !=  不等于 比较两个值是否不相等 如果相等返回False，如果不相等返回True
# >   大于   a>b   a大返回True，a小返回False
# <   小于  a<b   a小返回True，a大返回False
# <=   小于等于   a<=b   a小于等于b返回True，否则返回False
# >=   大于等于   a>=b   a大于等于b返回True，否则返回False

a = 20
b = 30
print(a == b)   # F
print(a != b)  # T
print(a > b)  # F
print(a < b)  # T
print(a >= b)  # F
print(a <= b)  # T

# 4、逻辑运算符
# x,y 为可以出现boolean的值的表达式或x，y本身就是boolean值
# and   逻辑与   x and y   当x与y都为True时，整体才为True，
#                 只要有一个为False，整体就是False
# or   逻辑或   x or y   当x与y都为False时，整体才为False，
#                 只要有一个为True，整体就是True
# not   逻辑非   not(x)   将x的值取反

a = 20
b = 30
c = 40
print((a < b) and (a > c))  # F
print((a < b) or (a > c))  # T
print(not (a < b))  # F


# 5、成员运算符
# in  如果在指定范围内能够找到该元素，返回True，否则为False
# not in    如果在指定范围内不能够找到该元素，返回True，否则为False
print("*********************************")
list = [1, 2, 3, 4, 5, 6]  # 列表
print(2 in list)   # T
print(2 not in list)  # F

# 6、身份运算符
# is   判断两个变量是否引用同一个内存地址，如果是，为True，否则为False
# is not   判断两个变量是否引用同一个内存地址，如果不是，为True，否则为False
a = 20
b = a
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

# 7、位运算符：对二进制进行的运算
# &  按位与运算符：参与运算的两个值对应位置都为1时，该位置为1，否则为0
# |  按位或运算符：参与运算的两个值对应位置有一个为1时，该位置为1，否则为0
# ^  按位异或运算符：参与运算的两个值对应位置有且只有一个为1时，该位置为1，否则为0
# ~   按位取反运算符  ~x   -x-1
# <<    左移运算符  x<<y 将x的二进制数向左移动y位
# >>   右移运算符  x>>y 将x的二进制数向右移动y位
a = 10 # 1010
b = 7  # 0111
print(a & b)  #   0010   2
print(a | b)  #  1111   15
print(a ^ b)  #  1101   13
print(~a)   # -11
print(a << 2) # 101000   40
print(a >> 2)  #  0010   2


# 8、运算符的优先级
# 1 + 2 * 3
# (1 > 2) and (3 > 4)

'''
优先级从高相抵排列
()
**
~ + -  正负号
* / // % 
+ -  加法减法
>> <<
&
> < >= <= == !=
is is not
in not in
not or and
'''

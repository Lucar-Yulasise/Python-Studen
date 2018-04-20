# 数据类型转换
# 语法格式： 转换的类型(即将转换的对象)
# int -> float   float -> int  str -> int  str -> float

# 1、int -> float   整型转为浮点型
int1 = 20
print(int1) # 20
print(type(int1)) # int
f1 = float(int1)
print(f1)
print(type(f1))

# 2、float -> int   浮点型转为整型
# 数据类型中。，不存在四舍五入，只保留整数部分
f2 = 2.9
int2 = int(f2)
print(int2)  # 2

# int3 = 1.22
# f3 = float(int3)
# print(f3)

# 3、str -> int   字符串转为整型
print(int("1"))  # 1
#  当字符串含有不是数字的字符时，转换失败
# print(int("1.99"))  # 失败
# print(int("abc"))  # 失败
# print(int("123abc"))  # 失败
# print(int("1+2"))  # 失败

# 当+或-作为符号位时，可以转换成功   +或-代表正负号
print(int("+123"))
print(int("-123"))

# 4、str -> float   字符串转为浮点型
print(float("123"))  # 123.0
print(float("1.234"))  # 1.234
# print(float("1.23.45"))  # 失败
# print(float("1.23abc"))  # 失败


# 5、int -> str  float -> str 整型或浮点型转为字符串
i1 = 1
s1 = str(i1)
print(type(s1))

print(str(1))
print(str(1.22))



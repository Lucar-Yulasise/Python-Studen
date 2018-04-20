# 字符串内嵌函数
# 1、eval(str): 将str当成有效的表达式来计算，将计算的结果返回
print(eval("123"))   # 123
print(eval("+123"))   # 123
print(eval("-123"))   # -123
print(eval("1 + 2"))  # 1 + 2    --> 3
print(eval("12 - 3"))  # 12 - 3   --> 9
# print(eval("abc124"))  # 失败
num = eval("123")
print(type(num))  # int

# 2、len(str)  返回字符串的长度  字符串中字符的个数  必须记住
str1 = "123456789"  # 9
len1 = len(str1)
print(len1)

# 3、字母大小写转换   不影响原始字符串
str2 = "heLLo hi Nihao SawaDiKa"
print(str2)
# lower()  将字符串中的字母全部小写
print(str2.lower())
# upper()  将字符串中的字母全部大写
print(str2.upper())
# swapcase()  将字符串中的大写字母转为小写，小写字母转为大写
print(str2.swapcase())
# capitalize()  字符串中的第一个字母大写，其他小写
print(str2.capitalize())
# title()  将字符串中的每隔单词的首字母大写，其他字母小写
print(str2.title())

# 4、返回一个指定长度的字符串   不影响原始字符串
str3 = "pyc"
# str.center(width [,fillchar]) 返回一个指定长度width的字符串，str这个
# 字符串在中间，其他位置用fillchar补全，默认是空格
print(str3.center(15, "*"))
# str.ljust(width [,fillchar]) 返回一个指定长度width的字符串，str这个
# 字符串在左边，其他位置用fillchar补全，默认是空格
print(str3.ljust(15, "*"))
# str.rjust(width [,fillchar]) 返回一个指定长度width的字符串，str这个
# 字符串在右边，其他位置用fillchar补全，默认是空格
print(str3.rjust(15, "*"))
# str.zfill(width) 返回一个指定长度width的字符串，str这个
# 字符串在右边，其他位置用0补全
print(str3.zfill(15))

# 5、string.count(str [,begin, end]) :返回string里面str出现的次数，
# 如果begin与end有值，查找该范围内的次数
str4 = "good very well good good very"
print(str4.count("good"))
print(str4.count("good", 3, 22))

# 6、检测字符串中有没有另一个字符串
# string.find(str [,begin, end]) 检测string中有没有str，如果存在返回
# 第一次出现的下标，如果begin与end有值，查找该范围
# 当找不到时，返回-1
# 从左向右查找
print(str4.find("very"))
print(str4.find("very", 10, 31))
print(str4.find("qwert"))

# # string.rfind(str [,begin, end]) 检测string中有没有str，如果存在返回
# 第一次出现的下标，如果begin与end有值，查找该范围
# 当找不到时，返回-1
# 从右向左查找
print(str4.rfind("very"))

# string.index(str [,begin, end]) 检测string中有没有str，如果存在返回
# 第一次出现的下标，如果begin与end有值，查找该范围
# 当找不到时，返回Error，程序报错
# 从左向右查找
print(str4.index("very"))
print(str4.index("qwer"))

# string.rindex(str [,begin, end]) 检测string中有没有str，如果存在返回
# 第一次出现的下标，如果begin与end有值，查找该范围
# 当找不到时，返回Error，程序报错
# 从右向左查找
print(str4.rindex("very"))










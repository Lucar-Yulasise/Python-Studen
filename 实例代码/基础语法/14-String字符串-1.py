# 字符串是以 单引号' 或双引号" 引起来的任意文本文字， 比如：'abc' 、"xyz"
# 注：" 或 ' 本身只是一种表示方式，不是字符串的一部分，
# 比如:"abc",只有a、b、c三个字符
# 如果" 或 ' 想要表达的是当前这个字符，那么要用 ' 或 " 引起来
# 字符串是不可变的

# python中没有字符的概念，都是字符串

# 一、创建一个字符串：创建字符串很简单，只需要给一个变量(字符串类型)即可
str1 = '床前明月光'
str2 = "疑是地上霜"
print(str1)
print(str2)
# print("str2")
print(type(str1))  # str
print(type(str2))  # str
str3 = 'A'
print(type(str3))  # str
# 输出一个双引号
str4 = '"'
print(str4)
# 输出一个单引号
str5 = "I'm a girl I'm not a boy"
print(str5)


# 二、字符串的运算
print(1 + 2)  # 加法
# 1、字符串拼接：将两个字符串拼接到一起
str6 = "hello"
str7 = "是你好"
str8 = str6 + str7
str9 = str6 + "  " + str7
print(str8)
print(str9)
# 字符串不能执行减法运算
# print(str6 - str7)

# 2、重复输出字符串  *
print("hellohellohello")
print(str6 * 3)

# 3、通过索引获取字符串中某个字符
# 索引：从0开始
# 索引，下标，index ： 同一个概念  ： 从0开始
# 语法格式： 字符串[索引]
# 可以访问及获取字符串中的一个字符
str10 = "我的愿望是拥有故宫的一块砖"   # 13个字符
print(str10[0])
print(str10[2])
# print(str10[13])  # 索引是不能越界的，越界会报错
# IndexError: string index out of range

# 4、字符串是不可变的
str11 = "hello"
# TypeError: 'str' object does not support item assignment
# str11[0] = "a"
print(str11)  # hello
# str11 = "world"
# print(str11) # world

# 5、截取字符串
str12 = "我的愿望是拥有故宫的一块砖和二环的一套房"
#        0  1 2 3 4 5 6 7 8 9 10111213141516171819
# 语法格式： 字符串[[起始下标]:[结束下标]:[递增基数]]
#
# 从起始下标截取到字符串末尾
str13 = str12[1:]
print(str13)
# 从头开始截取，截取到结束下标之前
str14 = str12[:7]
print(str14)
# 从开始下标截取，截取到结束下标之前
str15 = str12[2:9]
print(str15)
# 截取所有字符
str16 = str12[:]
print(str16)
# 递增基数
str17 = str12[0:9:3]
print(str17)

# 反转字符串
str18 = str12[::-1]
print(str18)

# 6、判断字符串中是否含有某个子字符串
print("北京" in str12)  # F
print("故宫" in str12)  # T
print("北京" not in str12)  # T

# 7、格式化字符串
# %s : 格式化字符串
# %d : 格式化整数
# %f : 格式化浮点数    如果想要设置精度： %.2f  保留两位小数
# 语法格式： 字符串(字符串里面有格式化字符) % (对应的数据)
name = "Lily"
age = 18
weight = 50.2
# 姓名是Lily,年龄是18,体重是50.2kg。
print("姓名是", name, ",年龄是", age, ",体重是", weight, "kg。")
print("姓名是" + name + ",年龄是" + str(age) + ",体重是" + str(weight) + "kg。")

# 当只有一个格式化符号时，可以省略小括号
print("姓名是%s" % name)
# 当有多个格式化符号时，小括号不能省，元素用逗号隔开
print("姓名是%s,年龄是%d,体重是%.2fkg。" % (name, age, weight))

print("%")
print("%%")
f1 = 2.33333333
# 2.33%
print("%.2f" % f1 + "%")
# 当字符串中有格式化字符时，两个%%,输出一个%
print("%.2f%%" % f1)

# 8、转义字符    \(将原本没有实际意义的字符转换为有实际意义的字符，
#                 将原本有实际意义的字符转为没有意义的字符)
#      反斜线本身有实际意义
# \n  --->  换行
print("abc\ndef")
# \'  --->   '
print("abc\'def")
# \"  ---> "
print("abc\"def")
# \\   --->  \
print("abc\\def")
# \r  --->  回车
print("abc\ref")

# \b --> 退格  \t --> 横向制表   \a --> 响铃
# 保留原始字符，不转义
# r  /  R   原始字符串：将所有转义字符直接输出，展示没有意义的普通字符
print("********************************")
print("\\\\\"")   # \\"
print(r"\\\\\"")  # \\\\\"
print(R"\\\\\"")  # \\\\\"

# 正则   文件路径

# 内嵌函数
# 字符串是以 单引号 或者 双引号 引起来的任意文本
# 注： '' 或 “” 本身只是一种表示方式，本身不是字符串的一部分。
str1 = 'abc'
str2 = "abc"
# 如果'' 或 “” 想要表达的是当前这个字符 'a' "adad" 字符串本身不可变
print(str1*12)
print(type(str1))
print(type(str2))

# 字符串运算
print("Hello"+" "+"world") # 字符串拼接
print("Hello\\n"*2) # 重复输出字符串
str3 = "我的愿望是拥有故宫的一块砖"
str4 = "Hello"
print(str3[2]) # 下标不能越界
print(str3[1:])
print(str3[:5])
print(str4[1:2])
print(str3[::-1]) # 反转

# 判断字符串中是否含有某个子字符串
print("北京" in str3);print("北京" not in str3)
print("故宫" in str3);print("故宫" not in str3)

# 格式化字符串
# %s ： 格式化字符串
# %d :   格式化整数
# %f :  格式化浮点数 如何要设置精度： %.2f
name = "Lily"
age = 18
weight = 50.2

#姓名 Lily ， 年龄 18 ，体重 50.2 千克
print("姓名是"+name+"，年龄"+str(age)+"，体重"+str(weight)+"Kg")

print("姓名是%s,年龄是%d，体重是%.2fKg " %(name,age,weight))
f1 = 2.333333333333
print("%.2f"%f1+"%")
# 当字符串中有格式化字符时，两个%%，就输出一个
print("%.2f%%" % f1)

# 转义字符
print("Hell\ne")
print("  Hello\' ")
print(r" Hello \" ")
print("Hello\rworld ")
print("HHebre\tshifwe \t")
var1 = "Hello world"
print("更新字符串",var1[:6]+"Runoob!")
print("\a")

# 保留原始字符
# r /

print(r"guweuv \nhweigwb")

#字符串函数
# Number   数字类型
# 分类：int 整型   float 浮点型  complex 复数  x+yj

# 整型： 数学中的整数  分正负数
# 定义    num1 = 100  读：将100赋值给num1
num1 = 100
print(num1)  # 100

# 用某一个变量给另一个变量赋值
num2 = num1
print(num2)  # 100

# 连续给多个变量赋值
num3 = num4 = num5 = num6 = 400
print(num3)
print(num4)

# 交互式赋值: 注：变量的个数与常量的个数要一致
num7, num8, num9 = 777, 888, 999
print(num7)  # 777
print(num8)  # 888
print(num9)  # 999


a = 100
b = 200
# 交换两个数的值
# 中间变量  c
c = a  # c = 100
a = b  # a = 200
b = c  # b = 100
print(a)
print(b)

e = 666
f = 888
e, f = f, e   # e, f = 888, 666
print(e)
print(f)

print("************窗前明月光******************")
# 浮点型   float
f1 = 1.234
print(f1)
print(type(f1))
f2 = f1  # 1.234
f3 = f4 = f5 = 6.66   # 6.66
f6, f7 = 7.77, 8.88   # 7.77 8.88
f8 = 1.0
f9 = 1.1
print(f8 + f9)  # 2.1
# 2.0999999   在计算机中，浮点数的运算偶尔会有误差

# 复数 complex
# 定义： complex(x, y)  x:代表实数部分   y:代表虚数部分
# 复数后期使用不多，仅作了解
com1 = complex(1, 2)
print(com1)




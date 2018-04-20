# 数学函数

# 1、绝对值   abs()
print(abs(10))
print(abs(-10))

# 2、比较两个数的大小   (数字1 > 数字2) - (数字1 < 数字2)
# 如果前面的数小：返回  -1；
# 如果两个数相等：返回 0；
# 如果前面的数大：返回  1
a = 20
b = 10
# a > b ---> 1
# a < b ---> 0
result = (a > b) - (a < b)
print(result)

# 3、 返回给定参数的最大值或最小值  max()  min()
print(max(1, 2, 3, 4, 5, 6))   # 6
print(min(5, 4, 8, 3, 0))  # 0

# 4、求x的y次幂  pow(x, y)
print(pow(2, 3))

# 5、返回浮点数的四舍六入的值
# round(x, [n])  x: 即将四舍六入的数   n:可选的参数，保留几位小数
# python3.X  如果距离两边的整数大小一致时，取偶不取奇
print(round(2.3))  # 2
print(round(2.6))  # 3
print(round(2.5))  # 2
print(round(1.5))  # 2

print(round(1.4577328, 3))  # 1.458


# math  数学库
# 运算符
# if   字符串


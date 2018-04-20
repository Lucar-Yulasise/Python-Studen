# while
# for 循环
'''
语法格式：
for 变量 in 集合:
    语句
'''
#逻辑：按顺序取'集合'中的每个元素赋值给'变量',再去执行语句。如此
# 往复循环，直到'集合'中的元素取完为止。
i = 0
while i < 5:
    print(i)
    i = i + 1
print("--------------")
for i in range(5):
    print(i)
'''
range([start,] stop [, step])
start: 指定开始的值，这个值包含在取值范围内，如果不写该参数，
默认从0开始
stop:指定结束的值，但这个值不包含在取值范围内
step:指定的递增基数，默认值为1
功能：生成一个数列(数字的集合列表)
'''
a = range(10)  # [0,1,2,3,4,5,6,7,8,9]
print(a)
print(a[0])
print(a[9])


list1 = [100,200,300]
for i in list1:
    print(i)

# 输出5遍hello
for i in range(5):
    print("hello")

# for--else  else:当集合中元素全部遍历结束时执行else下面的语句
'''
语法格式：
for 变量 in 集合:
    语句1
else:
    语句2
'''

for i in range(3):
    print(i)
else:
    print("嗓子痛")


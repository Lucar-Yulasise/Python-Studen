# 语法格式：
#for 变量 in 集合：
#    语句

# for 变量 in 集合：
# else：
#     语句
# 逻辑： 按循序取‘集合’中的每一个元素复制给变量，在去执行语句，循环，直到集合中的元素取完为止
a = range(10)
print(a)

for i in  range(5):
    print(i)


for i in range(3):
    print(i)
else:
    print("嗓子疼")
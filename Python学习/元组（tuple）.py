# 集合类型： list tuple
#tuple 元组
# 本质：是一种有序集合
# 特点，1和list相似 2 元组是不可变的，3 用 （） 创建

# 一，创建元组
# 格式：元祖名 = （元素1，元素2，元素3）

tuple1 = ()
print(tuple1)
print(type(tuple1))
tuple2 = (1,2,3,"1","2","3",None)
print(tuple2)

tuple4 = (1) # 用这种方式创建的数据不是元组类型，而是整数型，这是因为小括号，即可以表示元组，也可以是数学中的小括号，如果将数字括起来，系统会有歧义。
tuple5 = (1,)
print(tuple4)
print(tuple5)
print(type(tuple5))


# 元组中的方法
# 1.获取元组中的元素个数
tuple14 = (1,2,3,4)
print(len(tuple14))
# max in 返回最大值和最小值

# 元组的遍历

for i in tuple14:
    print(i)

num = 0
while num < len(tuple14):
    print(tuple14[num])
    num += 1

# 二维元组
tuple15 = ((1,2,3),(4,5,6),(7,8,9))
print(tuple15[2][0])

# 删除元组
tuple30 = (1,2,3)
del tuple30


# 数据类型转换 list -> tuple tuple >list

list1 = [1,2,3]
tuple31 =tuple(list1)
print(tuple31)
tuple32 = (1,2,3)
list2=list(tuple32)
print(list2)
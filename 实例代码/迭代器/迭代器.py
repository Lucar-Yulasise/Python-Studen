# 迭代器
# Iterable
'''
可迭代对象：可以直接作用于for循环的对象，叫做可迭代对象[Iterable]

可以直接作用于for的对象：
1、基本数据类型：list  tuple dict set string
2、generator生成器：带有yield的生成器函数

判断一个对象是否为可迭代的对象：isinstance(obj, Iterable)
'''
# Iterable  本身属于集合的一种类型
from collections import Iterable

# 判断一个对象是否为可迭代的对象
print(isinstance([], Iterable))  # T
print(isinstance({}, Iterable))  # T
print(isinstance((), Iterable))  # T
print(isinstance("abc", Iterable))  # T
# int不是可迭代的对象
print(isinstance(100, Iterable))  # F
# x for x in range(5)  ---> 是一个列表，产生x的值，x的数量由range决定
# x for x in range(5)  ---> [0,1,2,3,4]
print(isinstance((x for x in range(5)), Iterable))   # T

'''
迭代器：Iterator
迭代器：不仅可以作用于for循环，也可以使用next() 函数不断调用并获取下一个值，
直到取出最后一个。当取出嘴一个元素时，再继续调用next()时，会提出一个
StopIteration错误表示无法继续下一个数据的提取。

可以被next()函数调用并提取元素的对象称为迭代器对象。
判断一个对象是否为迭代器对象：isinstance(obj, Iterator)
'''

print("***********脚麻吗*********")
from  collections import Iterator

print(isinstance([], Iterator))  # F
print(isinstance({}, Iterator))  # F
print(isinstance((), Iterator))  # F
print(isinstance("abc", Iterator))  # F
print(isinstance((x for x in range(5)), Iterator))  # T


# next()
list1 = (x for x in range(5))  # <generator object <genexpr> at 0x0000015EBF809E08>
print(list1)
# for i in l:
#     print(i)
# next(l)  ---> next(obj) ：obj为迭代器对象，返回一个元素
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))
# print(next(list1))   # StopIteration

# 将list、tuple、dict、str转为Iterator对象
a = iter([1, 2, 3])
# for i in a:
#     print(i)
print(next(a))
print(next(a))
print(next(a))
# print(next(a))

print(isinstance(iter([1,2]), Iterator)) # T
print(isinstance(iter({}), Iterator)) # T
print(isinstance(iter(()), Iterator)) # T
print(isinstance(iter("abc"), Iterator)) # T

str1 = iter("abcd")
print(next(str1))  # a

for i in "qwer":
    print(i)

list2 = iter([7,8,9])
for i in list2:
    print(i)
for i in [9,8,7]:
    print(i)


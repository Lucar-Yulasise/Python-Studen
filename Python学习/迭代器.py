# 迭代器
# Iterable
"""
可迭代对象：直接作用于for循环的对象，叫做可迭代对象[Ietable]

可以直接作用于for的对象
1、基本数据类型
2，generator生产
"""
from collections import Iterable

print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance("abc",Iterable))
print(isinstance(100,Iterable))

#x for x in range(5)) ---> 是一个列表，产生x的值，x的数量由range决定
# x for x in range(5)) ———》[0,1,2,3,4]
print(isinstance((x for x in range(5)),Iterable))

"""
迭代器：Iterator
迭代器：不仅可以作用于for循环，也可以使用next()函数，不断调用并获取下一个值，直达取出最后一个值
当取出一个元素时，再继续调用next()时，会提出一个StopIteration错误表示无法继续下一个数据提取。

可以被next()函数调用并提取元素的对象成为迭代器。


"""
print("-----------------------------------------------------------")
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance((),Iterator))
print(isinstance("abc",Iterator))
print(isinstance((x for x in range(5)),Iterator))

list1 = (x for x in range(5))

print(list1)

# for i in list1:
#     print(i)

next(list1) #---> next(obj):obj为可迭代对象
print(next(list1))
print(next(list1))
print(next(list1))
print(next(list1))

print("------------------------------------")
# 将list 、 tuple dict str 转为Iterator对象
a = iter([1,2,3])
# for i in a :
#     print(i)

print(isinstance(iter([1,2]),Iterator))

str1 = iter("abcd")
print(next(str1))

# set 集合
# set： 与dict相比，set是一组存储key的集合，但不存储value
# 本质：一个无序的及不重复的集合

#一 ； 创建
# 创建set需要一个list或tuple或dict作为参数传入

set1 = set([1,2,3,4])
print(set1)
print(type(set1))

# 重复的元素在set中会被自动过滤
set2 = set([1,2,3,4,2,4,5,32,42,3,32,])
print(set2)

set3 = set((1,2,3,4))
print(set3)

set4 = set({"a":2,"b":4})
print(set4)
dic5  ={"a":1,"b":2}
set5 = set(dic5.values())
print(set5)

# set6 = set(100) # 数据类型不匹配
# print(set6)

set7 = set([1,2,3,4])
set7.add("1") # 添加数据： 在set中直接添加一个数据，add在添加元素时，只能添加不可变数据
print(set7)
set7.add(1)
print(set7) # 可以添加重复数据，然而并没有什么卵用
set7.add((1,2))
print(set7)

#set7.add([1,2]) # 只能添加不可变数据，而list是可变的

# 2 update(Iter) 添加数据： 在set中打碎添加集合中数据
# Iter ： list tuple string
set8 = set([1,2,3])
set8.update([1,2,3])
set8.update((1,3,4))
set8.update("PYC")
print(set8)

set9 = set([1,2,3,4])
set9.remove(3)
print(set9)

# 注意： set 是无序的，不支持下标的方式
#print(set9[0])

# 集合的操作
set10 = set([1,2,3,4,5])
set11 = set([4,5,6,7,8])

print(set10 and set11)


# 集合的遍历

for i in set10:
    print(i)


list1  = [1,2,3,4]
print(set(list1))
tuple1 = ((1,2,3,4))
print(set(tuple1))

list11 = [1,2,3,4,34,54,44,3,4,5,44,3,4]
set11 = set(list11)
list12 = list(set11)
print(list12)

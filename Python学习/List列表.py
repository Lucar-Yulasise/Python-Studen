# List 列表
# 为什么要使用列表？

# 集合 ： 存放所有人的年龄
# 列表本质：一个有序的集合
# 数组—列表
# 创建列表
# 语法格式： 列表名 = [元素1,元素2,]
list1 = []
print(list1)
print(type(list1))
list2 = ["helli",232,"nihao",3.12334,None]
print(list2)
print(type(list2))

list4 = [[21,23],["Hello","world"]]
print(list4)
list5 = [1,2,3,4,5,6,7]
print(list5[2])
#print(list5[7]) 下标不能越界
print(list5[-1]) # 当下标为-1时，获取最后的一个元素

list5[2] = 100
print(list5)

# 列表的操作
list6 = [1,2,3]
list7 = [4,5,6,1,2,3]
list8 = list6 + list7
list9 = [0]
print(list9*4)
print(list8)


# 判断某个元素是否在列表中
list10 = [1,2,3,4]
print(4 in list10)
print(100 in list10)

# 列表的截取
# 格式 列表名[[起始参数][结束下标]]
list11 = [0,1,2,3,4,5,6,7,8,9]
print(list11[:6])
print(list11[3:])
print(list11[:])
print(list11[::2])
print(list11[::-1])


# 二维列表
list12 = [[1,2,3],
          [4,5,6],
          [7,8,9],
          [10,11,12]]

print(list12)
print(list12[2][2])
print(list12[3][2])
print(list12[0])

# 列表的操作——增删改查 对原本的列表有影响
# 1 增加元素
arr1 = [1,2,3,4,5]
print(arr1)
arr1.append([6,7,8,9]) # 在列表的末尾添加新的元素
# list.append(obj) obj为即将添加的元素，可以为任意类型
# list.extend(iter) 在列表末尾一次性追加iter里面所有的元素（将iter里面的元素分开添加）
# iter: 数字类型必须时集合类型
# insert 插入数据 在指定的index下标位置新增元素，不会覆盖原来的元素，原数据的下标向后顺移
print(arr1)

arr2 = [1,2,3]
arr2.extend([4,5,6])
print(arr2)
arr3 = [100,200,300,400]
arr3.insert(1,999)
arr3.insert(3,[111,222])
print(arr3)

# 改
arr4 = [1,2,3]
arr4[1]= "200"
print(arr4)

# 删
arr5 = [1,2,3,4,5]
#arr5.pop()# 可以添加下标，默认移除末尾元素,并返回被删除的元素
#arr5.pop(2)
print(arr5.pop(2))
print(arr5)

arr6 = [1,2,3,4,3,2,5,1,2,3]
print(arr6)
arr6.remove(2)
arr6.remove(2)
print(arr6)

arr7 = [1,2,3]
arr7.clear()
print(arr7)

# 查
# list.index(obj) 从列表中找出第一个匹配到下标
# 当找不到元素的时候，会报错
arr8 = [1,2,3,4,5,4,343,324]
print(arr8.index(4))

# 列表中的方法
#  len(list) 返回列表元素长度
#  max(list) 返回列表最大元素
#  min(list) 返回列表最小元素
#  list.count 返回列表元素个数

len(arr8)
max(arr8)
min(arr8)
arr8.count(2)

list3 = [1,2,4,5,6,7,8,9]
list3.reverse()
print(list3)

list4 = [21,324,23,1324,1,4,42,24,5,56]
list4.sort()
list4.reverse()
print(list4)


# 拷贝
# 浅拷贝： 只是表面上多了一个名字，内存地址还是原来的
# 深拷贝： 复制数据，将复制后的数据重新放到一个内存地址

list30 = [1,2,3,4]
list31 = list30
print(list30)
print(list31)
list31[2] = 10000
print(list31)
print(list30)

list40 = [1,2,3,4]
list41 = list40.copy()
list41[1] = 20000000
print(list40)
print(list41)
print(id(list40))
print(id(list41))


# 遍历列表中的元素

listNew = [1,2,3,4,5,6,"3e32"]
i = 0
while  i < len(listNew):
    print(listNew[i])
    i += 1

for i in listNew:
    print(i)
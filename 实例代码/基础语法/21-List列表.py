# int float str complex boolean None
# List  列表
# 为什么要使用列表？
# 计算五个人平均年龄
age1 = 12
age2 = 22
age3 = 33
age4 = 44
age5 = 55
print((age1+age2+age3+age4+age5) / 5)

# 集合：存放所有人的年龄
# List列表本质：一个有序的集合
# 数组-列表

# 一、创建列表
# 语法格式： 列表名 = [元素1, 元素2, 元素3.......,元素n]
# 列表中的元素用逗号隔开
# 1、创建一个空列表
list1 = []
print(list1)
print(type(list1))  # list
# 2、创建一个带有元素列表
list2 = [1, 2, 3, 4]
print(list2)

# 注：列表里面的元素可以是不同类型的数据
list3 = [1, 2, 3.45, "abc", True, None]
print(list3)

list4 = [1, 2, [3, 4, 5], 6]
print(list4)

# 二、列表元素的访问
list5 = [1, 2, 3, 4, 5, 6, 7]
# 1、取值：格式： 列表名[下标]
print(list5[2])
# print(list5[7])  # IndexError: list index out of range  数组取值时，下标不能越界

# 2、取值，从右向左取值
# 当下标为-1时，获取最后一个元素
print(list5[-1])  # 7
# 下标不能越界
# print(list5[-11])  # 错误

# 3、替换元素
# 语法格式： 列表名[下标] = 新值
print(list5)
list5[2] = 100
print(list5)

# 三、列表的操作
# 1、列表组合  +
list6 = [1, 2, 3]
list7 = [4, 5, 6, 1, 2, 3]
list8 = list6 + list7
print(list8)

# 2、列表的重复 *
list9 = [0]
print(list9 * 10)

# 3、判断某一个元素是否在列表中  in  not in
list10 = [1, 2, 3, 4]
print(4 in list10)   # T
print(100 in list10)  # F

# 4、列表的截取
# 格式： 列表名[[起始下标] : [结束下标] : [递增基数]]
# 获取从起始下标开始到结束下标之前的所有元素，默认递增基数为1
list11 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 从头开始截取，截取到数字5
print(list11[:6])
# 从数字3开始截取，截取到末尾
print(list11[3:])
# 截取所有的元素
print(list11[:])
# 隔一取一
print(list11[::2])
# 反转列表
print(list11[::-1])

# 四、二维列表
list12 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print(list12)
print(list12[1])  # [4, 5, 6]
print(list12[2][1])

list13 = list12[2]  # [7, 8, 9]
int1 = list13[1]
print(int1)

# 12
print(list12[3][2])
# [1, 2, 3]
print(list12[0])

# 一维列表   二维列表  三维列表

# 数据进行操作--增删改查
# 五、列表的操作--增删改查   对原本的列表有影响
# 1、增
arr1 = [1, 2, 3, 4, 5]
# append 在列表的末尾添加新的元素
# list.append(obj)  obj为即将添加的元素，obj可以为任意类型
print(arr1)
arr1.append(666)
arr1.append("abc")
arr1.append([100, 200, 300])
print(arr1) #[1, 2, 3, 4, 5, 666, 'abc', [100, 200, 300]]

# extend 在列表末尾添加元素
# list.extend(iter) 在列表末尾一次性追加iter里面所有的元素(将iter里面的元素
# 分开添加)
# iter:数据类型必须是集合类型
arr2 = [1, 2, 3]
arr2.extend([4, 5, 6])
print(arr2)

# insert  插入数据
# list.insert(index, obj)  在指定的index下标位置新增元素，不会覆盖原来的元
# 素，原数据的下标向后顺移
# obj：为任意类型
arr3 = [100, 200, 300, 400]
arr3.insert(1, 999)
arr3.insert(3, [111, 222])
print(arr3)

# arr4 = [1,2,3]
# arr4.insert(1, 999)
# arr4[1]  --> 2
# arr4[1] --> 999
# arr[1+1] --> 2

# 2、改
arr4 = [1, 2, 3]
arr4[1] = 500
print(arr4)

# 3、删
arr5 = [1, 2, 3, 4, 5, 6]
# pop 删除列表中的元素
# pop([index]): 移除指定index位置的元素，如不写index，默认移除最后一个元素。
# 并返回删除的数据
# arr5.pop()
# arr5.pop(2)
print(arr5.pop(2))
print(arr5)

arr6 = [1, 2, 3, 4, 3, 2, 5, 1, 2, 3]
# remove 移除数据
# list.remove(obj)  移除列表中匹配到obj的第一项
print(arr6)
arr6.remove(2)
print(arr6)

arr7 = [1, 2, 3]
# clear()  清除列表中所有的元素：清空列表
print(arr7)
arr7.clear()
print(arr7)


# 4、查
# in    not in
# list.index(obj [, begin, end])  从列表中找出第一个匹配到的下标
# 当找不到元素时，返回一个Error
# 如果给定begin与end：指定范围查找
arr8 = [1, 2, 3, 4, 5, 6, 4, 4, 4, 4]
print(arr8.index(4))
print(arr8.index(4, 5, 7))

# 六、列表的相关方法
# 1、len(list)  返回列表中的元素个数
list3 = [1, 2, 3, 4, 5, 6, 7]
print(len(list3))  # 7
# 2、max(list)  返回列表中的最大的元素
print(max(list3))   # 7
# 3、min(list)  返回列表中的最小的元素
print(min(list3))  # 1
# 4、list.count(obj)  返回obj元素在列表中的出现的次数
list3 = [1, 2, 3, 4, 2, 3, 7, 2, 2]
print(list3.count(2))  # 4

# 5、list.reverse()  将列表中的元素反转
list3.reverse()
print(list3)

# 6、list.sort()  对列表进行排序  默认升序
list4 = [23, 6, 12, 1, 7, 89, 0]
list4.sort()
print(list4)

# 7、拷贝
# 浅拷贝 ： 只是表面上多了一个名字，内存地址还是原来的那个
# 潘颖超   Meakelra
list30 = [1,2,3,4]
list31 = list30
print(list30)
print(list31)
list31[2] = 100000
print(list30)
print(list31)
print(id(list30))
print(id(list31))
print("---------------------------")

# 深拷贝 ； 复制数据，将复制后的数据重新放到一个内存地址中
list40 = [1,2,3,4]
list41 = list40.copy()
print(list40)
print(list41)
print(id(list40))
print(id(list41))
list40[2] = 1000000
print(list40)
print(list41)



# 七、遍历list列表中的元素
listNew = [1,2,3,4,5,6]
# 循环
# while
i = 0
while i < len(listNew):
    print(listNew[i])
    i = i + 1

# for
for i in listNew:
    print(i)


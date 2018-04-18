# 字典 dictionary
# 概述： 使用键—值（key-value）方式存储。
"""
key 的特点：
    1.字典中的key必须是唯一
    2.key必须是不可变数据类型：字符串，元组，Number
    3.list是可变的，不能作为key值使用
字典的本质： 一种无序的集合
"""
# 思考：保存多位学生的姓名，性别，年龄，成绩

# 使用字典：姓名：key 成绩：value

# 创建字典
# 格式： {key1:value1}

student = {"tom":98,"lily":78,"lucy":98,"hmm":45,"lilei":45}
print(student)
dic2 = {}

dic3 = {"a":12}
print(dic3)

dic4 = {"sdfd":9021}
dic5 = {12:12}
print(dic5)
dic6 = {(1,):12}
print(dic6)
#dic7 = {[12]12}# list不可做为key
dic8 = {1:23,1:12}#只保留前面的一个值，不可重复
print(dic8)


# 字典的访问
# 1.获取某个元素的方式1： 字典名[key]
dic9 = {"tom":88,"ll":66,"hmm":77}
print(dic9["ll"])

# 2.获取某个元素的方式2：字典名.get(key),如果当前key值不存在，返回一个空值（None）
print(dic9.get("HE"))
if dic9.get("AA") == None:
    print("当前元素不存在")
else:
    print(dic9.get("AA"))

# 字典的操作
# 1 增 格式 ： 字典名[key] = value
# 2 删   : 将Key值移除，对应的vlue会自动移除
# 3 改   : 直接覆盖

dic10 = {"Tom":98,"Lili":32,"Lucy":66}
dic10["lilei"]=100
print(dic10)
dic10["Lili"]=200
print(dic10)
dic10.pop("Tom")
print(dic10)


# 遍历字典
for key in dic10:
    print(key,dic10[key])

print(dic10.keys()) # 返回一个包含所有key的列表
print(dic10.values())# 返回一个只有value的列表

for key in dic10.keys():
    print(key)

for v in dic10.values():
    print(v)


#print(dic10.items()) # 返回一个包含所有key—value的元组的列表d

for key in dic10.items():
    print(key)

# 元组的获取，可以直接遍历items,分别获取key及value
for key,value in dic10.items():
    print(key,value)

"""
dict 与 list 相比：
dict ： 1、查找及插入速度快，不会随着key及value的增加而变慢
        2、 需要占用的内存大，内存浪费多
list :  1、查找及插入速度会随着key及value的增加而变慢
        2、 需要占用的内存小，内存浪费少
"""
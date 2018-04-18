list1 = [1,2,3,4]
# 枚举遍历：可以将下标及元素同时遍历
for i in enumerate(list1):
    print(i)

for index,data in enumerate(list1):
    print(index,data)

# tuple
tuple1 = (1,2,3,4,5)
for index,data in enumerate(tuple1):
    print(index,data)
# dict
dict1 = {"a":1,"b":12,"c":12}
for index,data in enumerate(dict1):
    print(index,data)

# set
set1 = set([1,2,3,4])
for index,data in enumerate(set1):
    print(index,data)

# 判断数据类型
int1 = 100
print(isinstance(int1,int))
print(isinstance(int1,list))

list12 = [1,[4,5,7],8,"abc"]
for i in list12:
    if isinstance(i,list):
        for j in i:
            print(j)
    else:
        print(i)
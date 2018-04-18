# 二维列表的遍历
# break  continue
# 元组 tuple
# 字典 dict
# 集合 set

list1 =[1,2,3,4]
for i in list1:
    print(i)


print("---------------------------------------------")
list2 = [[1,2,3],[4,5,6],[9,10,11]]
for i in list2:
    for j in i:
        print(j,end="")
    print()

print("---------------------------------------------")
for i in range(len(list2)):
    for j in range(len(list2[i])):
        print(list2[i][j])

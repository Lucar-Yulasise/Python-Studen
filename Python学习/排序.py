list1 = [12,324,1,3,123,1,3,123,1]
for i in range(0 ,len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i] < list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
# break 与 continue 一般只出现在循环语句中
# break
for i in range(10):
    if i == 3:
        break
    print(i)
print("for结束")

for i in range(5):
    for j in  range(10):
        if j == 2:
            break # 结束循环，只能控制离他最近的循环
        print("i = %d ,j=%d"%(i,j))


for i in range(5):
    print(i)
else:
    print("呵呵，心火烧")


print("--------------------------------------------------")
for i in range(10):
    if i == 3:
        continue # 跳出本次循环，不影响下一次循环，只能控制理他最近的循环
    print(i)
else:
    print("HHH")

num = 0
while num <=10 :
    num += 1
    if num == 3:
        break
    print(num)

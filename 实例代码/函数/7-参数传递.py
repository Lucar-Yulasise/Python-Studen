# 值传递 ： 传递的时一个值，传递的是不可变的数据类型；传递的是常量
# str,tuple,number 是不可变的
def fun1(num):
    print(num)
    print('函数内部=', id(num))  #

# fun1(100)
temp = 20
print('函数外部=', id(temp))  # 123
fun1(temp)   # num = temp = 20


# 引用传递:传递的可变数据类型；传递的是变量的内存地址
# list，dict，set是可变的
def fun2(li):
    li[0] = 100
    print(li)

list1 = [1,2,3]
# [1,2,3]
print(list1)
# [100,2,3]
fun2(list1)
# [100,2,3]
print(list1)




# 函数内部变量与函数外部变量
def fun3(num):
    # 函数内部的变量名与函数形参名一致了，在内部使用时，看变量定义的
    # 先后顺序，在变量定义之后使用，则会默认取变量的值；
    # 在变量定义之前使用，则会默认取形参的值
    print('num1==',num)
    num = 200
    print('num2==', num)

tmp = 20
fun3(tmp)
print('num3==', tmp)




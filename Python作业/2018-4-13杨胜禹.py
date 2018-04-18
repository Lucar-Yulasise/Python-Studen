# 1、将一个列表中的某一个元素全部删除
# list1 = [1,1,1,3,4,6,1,4,8,0,34,2,71,2,1,1]
# 将list1中所有的元素1删除
def h1():
    list1 = [1,234,13,14123,1,34,14,5,1,3123,31,1,1,23]
    index1 = 0
    for i in range(0,len(list1)):
        if list1[index1] == 1:
            list1.pop(index1)
        else:
            index1 += 1
    print(list1)

#2、for 计算1-100的和
# 3、输出50以内能被7整除的数
# 4、给定一个字符串，判断该字符串中有多少个a   jhgfdsdtyaaawertyukjbvaa
# 5、给定一个字符串，输出字符串的下标及对应下标位置的字符
def h2():
    num = 1
    for i in range(100):
        num += i
    print("计算的总和为:%d"%num)

def h3():
    for i in range(50):
        if i % 7 == 0:
            print(i)

def h4():
    str1 = "aatdsdsfddsfearardeafsdf"
    for i in range(len(str1)):
        if str1[i] == "a":
            i += 1
    print(i)


def h5():
    str2 = "hello world"
    index1 = 0
    for i in range(len(str2)):
        print(index1,str2[index1])
        index1 += 1



# 6、输出九九乘法
'''
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
'''

def h6():
    for i in range(1,10):
        for j in range(1,i+1):
            print("%d * %d = %s "%(i,j,str(j*i)),end="")
        print()


# 7、
'''
*
**
***
'''
'''
  *
 **
***
'''
def h7():
    for i in range(3):
        for j in range(i+1):
            print("*",end="")
        print()
    print("-------------")


    for i in range(3):
        for j in range(3 - i):
            print(" ",end="")
        for k in range(i+1):
             print("*",end="")
        print()


#8、将一个字符串中的小写字母转为大写，将大写字母转为小写，其他字符不变
# abcED123f  ----> ABCed123F
# 97 -32   +32   for  if
def h8():
    str1 = "HeLLOwsd1232JHJ"
    index1 = 0
    for i in range(len(str1)):
        strType = str1[index1]
        ch = ord(strType)
        if ch < 91:
            s1 = str1[index1].lower()
            print(s1,end="")

        elif ch > 97 :
            s2 = str1[index1].upper()
            print(s2,end="")
        index1 += 1

#9、将字符串abcd变为字符串4567
# asc   -45
# 密码加密
def h9():
    str1 = "abcd"
    index1 = 0
    for i in range(len(str1)):
        ch = ord(str1[i])
        ch -= 45
        print(chr(ch))


#10、随机产生一个长度为6的字符串，字符串中可能包含大写字母，小写字母或数字
# s2AHr6
import random
def h10():
    for i in range(6):
        char1 = [random.randrange(48, 58),random.randrange(65,91),random.randrange(97,123)]
        listS = random.randrange(3)
        print(chr(char1[listS]),end="")




#h1()
#h2()
#h3()
#h4()
#h5()
#h6()
#h7()
#h8()
#h9()
h10()



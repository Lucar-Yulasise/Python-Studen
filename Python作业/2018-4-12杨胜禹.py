
def h1():#  输出 1~ 100 的和
    index = 1
    num = 0
    while index <=100:
        print(index)
        num += index
        index += 1 ;
    print("1+2+3.....+100的结果为 %d"%num)


def h2():#  输出 100 内能被7 整除的数
    index2 = 0
    while index2 <= 100:
        if index2 % 7 == 0:
            print(index2)
        index2 += 1
def h3():#  给定一个字符串，输出字符串的下标，及对应下标的字符
    str = "helloworld"
    i = len(str)
    index2 = 0
    while index2 <  i:
        print(index2,str[index2])
        index2 += 1
def h4():#  打印2000 ~ 2200 所有的闰年
    year = 2000
    while year <= 2200:
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            print(year)
        year += 1
def h5():#  给定一个整数，判断该整数位数
    num1 = int(input("请输入一个整数："))
    x = 0
    while num1:
        num1 = num1 // 10
        x += 1

    print(x)


def h6():# 给定一个字符串，判断该字符串中有多少和 a
    strA = "asdasdsa3reugugguadaguguga"
    strB = len(strA)
    x = 0
    while strB != 0:
        if strA[strB-1] == "a":
            x += 1
        strB -= 1
    print(x)





#h1()
#h2()
#h3()
#h4()
#h5()
#h6()



# 允许函数调用时传入参数顺序与声明时的顺序不一致，但赋值不会错乱
def getNameAndAge(name, age):
    print("%s     %s" % (name, age))

# getNameAndAge("MM", 18)
# getNameAndAge(28, "GG")

# 关键字参数：就是在函数调用时写出形参名称并等号赋值
# 建议：以后尽量在函数调用时使用关键字参数
# 但是用关键字参数时，实参的传入顺序就任意了。
getNameAndAge(name="MM", age=18)
getNameAndAge(age=34, name="QQ")



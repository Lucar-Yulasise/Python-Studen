"""
python 内置读写文件的函数，用法和C是兼容，在磁盘上读写文件的功能是由操作
系统提供的。读取文件的操作就是请求操作系统打开一个文件对象，然后通过操作系统
提供的接口从这个已经打开的文件中提取数据。（读取）,或者把数据写入这个文件中。（写文件）

读文件过程：
1.打开文件
2.读取内容
3.关闭文件

1.打开文件
语句格式：open(path,flag[,encoding][,errors])
path: 文件路径
文件路径：相对路径： 1.py
          绝对路径：C:\\Users\\MickBrujah\\Desktop
flag:文件的打开方式
r : 以只读方式
rb: 以二进制只读方式
r+: 以读写方式
w: 以只写方式
wb: 以二进制只写方式
a:
a+

encoding:文件的编码格式
errors:错误处理
strict:默认方式，如遇到非法字符，抛出异常
"""
# f = open("hello.txt","r")
# f3 = open("file.txt",mode="r",encoding="utf-8")
# f4 = open("file.txt",mode="r",encoding="utf-8",errors="igonre")
#
# """
# 2.读取文件
# """
# # str2 = f3.read()
# # sre  = f.read()
# # str3 = f3.readline()
# # print(str2)
# # print(sre)
# # print(str3)
#
# str6 = f3.readline(2)
# print(str6)
#
# str7 = f3.readline(2)
# print(str7)
#
# str8 = f3.readlines(12)
# print(str8)
#
# f3.seek(3)
# print(f3.read(3))
# """
# 3.写入问价
# """
# f3.close()
#
# try:
#     f2 = open("file.txt","r")
#     print(f2.read())
#
# except FileNotFoundError as e:
#     print("文件没有找到")
# finally:
#     if f2:
#         f2.close()
# 简洁的方式
# with 和try的效果是一样的，当是代码相对简洁一点，而且不必我们自己调用close(),系统会自动执行
with open("file.txt","r+",encoding="utf-8") as f6:
    print(f6.read())
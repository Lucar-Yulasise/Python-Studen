'''
python内置了读写文件的函数，用法和C是兼容的，在磁盘上读写文件的功能是由操作
系统提供的。读写文件的操作就是请求操作系统打开一个文件对象，然后通过值操作系统
提供的接口从这个已经打开的文件中提取数据（读文件）,或者把数据写入到这个文件
中(写文件)。
'''
'''
读文件过程：
1、打开文件
2、读取内容
3、关闭文件
'''
'''
1、打开文件
语法格式：open(path, flag [,encoding][,errors])
path:文件路径
# 文件路径：相对路径  ： 1-读文件.py
            绝对路径  : C:\\Users\\xlg\\Desktop\\文件操作\\1-读文件.py
flag:文件的打开方式
r :以只读的方式打开文件，文件描述符放在文件的开头位置
rb ： 以二进制格式打开文件，文件只读，文件描述符放在文件的开头位置
r+：以读写的方式打开文件，文件描述符放在文件的开头位置
w：以只写的方式打开文件，如果文件存在，那么覆盖该文件，如果文件不存
在，则会创建文件。
wb：以二进制格式打开文件，文件用于写入，如果文件存在，那么覆盖该文件，
如果文件不存在，则会创建文件。
w+：以读写的方式打开文件
a：打开一个文件用于追加写入，如果文件不存在，则会创建文件；如果文件存在，
则会在文件末尾写入内容。
a+：以读写的方式打开文件

encoding：文件的编码格式
errors：错误处理
strict：默认方式，如果遇到非法字符，抛出异常
ignore：忽略非法字符
replace：用?代替非法字符

open：返回值：文件描述符
'''
# 打开普通文件
f1 = open("file.txt", "r", encoding="utf-8")
# 当文件不存在是，抛出异常
# FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# 打开二进制格式的文件:不能设置encoding
f2 = open("file.txt", "rb")
# 打开指定编码格式的文件
f3 = open("file.txt", mode="r", encoding="utf-8")
# 指定错误处理方式
f4 = open("file.txt", mode="r", encoding="utf-8", errors="ignore")
print(f1)
print(f2)
'''
2、读取文件
'''
# read([size])  : 会记录读取的内容，光标向移动
# 1、读取文件中的所有内容
# str1 = f1.read()
# print(str1)
# 2、读取指定的字符个数
# str2 = f1.read(4)
# print(str2)
# str3 = f1.read(4)
# print(str3)

# readline([size])
# 3、读取整行,包括“\n”
# str4 = f1.readline()
# str5 = f1.readline()
# print(str4)
# print(str5)

# 4、读取指定的字符个数
# str6 = f1.readline(2)
# str7 = f1.readline(2)
# print(str6)
# print(str7)

# readlines([size])
# 5、读取所有行，返回一个列表
# str8 = f1.readlines()
# print(str8)

# 6、如果给定的size数字大于0，实际返回的size字符数会比写入的size大，原因
# 需要填充缓冲区
# str9 = f1.readlines(12)
# print(str9)

# 7、修改描述符的位置  seek()
# print(f1.read(3))
# tell()  返回描述符的位置
print(f1.tell())
f1.seek(3)
print(f1.read(3))

'''
3、关闭文件
'''
# 文件使用完毕后bicultural关闭，因为文件会占用操作系统的资源，操作系统在同
# 一时间打开的文件数是有限的。
# 已经关闭的文件不能再继续使用。
# close()
f1.close()


# 一个完整的过程
# 因为文件读取可能会出现异常，但当异常出现时，文件的close的操作是不能再执
# 行的，所以，为了保证无论是否出错，都能正确的关闭文件，使用finally来实现。
'''
try:
    f2 = open("file.txt", "r", encoding="utf-8")
    print(f2.read())
except FileNotFoundError as e:
    print("文件没有找到")
finally:
    if f2:
        f2.close()
'''

# 简洁的方式:
# with和上面的try的效果是一样的，但是代码相对简洁，而且不必我们自己调用
# close(), 系统会自动执行close()
with open("file.txt", "r", encoding="utf-8") as f5:
    print(f5.read())








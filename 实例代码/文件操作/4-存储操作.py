# list  tuple  dict
# 存储：永久性保存对象
# 必须记住
import pickle

'''
有时候，我们需要将某些字符串、列表、字典、元组等数据长久保存，现在，这
个时候，就需要使用永久性存储的模块文件pickle。
pickle模块可以将对象转换为一种可以存储或读取的格式。

pickle:该模块实现了数据的序列化与反序列化，通过pickle的序列化操作，
可以实现将程序中的对象保存到文件信息中，实现永久性存储。
通过pickle的反序列化操作，可以实现将程序中的永久性存储的对象解析出来。
'''
list1 = [1,2,3,4,5,6]
f1 = open("list.data", "wb")
# 将列表信息保存到文件中
# pickle.dump(即将存储的数据对象, 存入的文件)   序列化操作
# 建议：保存对象时，文件的后缀名不要使用电脑系统能够打开的格式
pickle.dump(list1, f1)
f1.close()


# 读取文件
tmp = []
# 打开文件
f2 = open("list.data", "rb")
# pickle.load(读取的文件)  有返回值
tmp = pickle.load(f2)
print(tmp)
f2.close()



# .txt   后缀名  .doc  .docx  .excel   .png
# file.asd


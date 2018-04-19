# list tuple dict
# 存储：永久性保存对象
"""
有时候，我们需要将某些字符串 列表 字典 元组等数据长久的保存下来，现在这个
时候，就需要永久性存储的模块文件
pickle 可以将对象转换为一种可以存储或读取的格式。

pickle ：该模块实现了数据的序列化于反序列化，通过pickle的序列化操作，
可以实现将程序中的对象保存到文件信息中，实现永久性存储
通过pickle的反序列化操作，可以实现将程序中的永久性存储对象解析出来
建议.保存对象时，文件的后缀不要使用电脑系统能够打来的格式
"""

import pickle

list1 = [1,2,3,4,3,2,3,3]
f1 = open("li.data","wb")
# 将列表信息保存到文件中
pickle.dump(list1,f1)
f1.close()

tmp = []
f2 = open("li.data","rb")
tmp = pickle.load(f2)
print(tmp)
f2.close()







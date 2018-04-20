# 数出字符串中出现的单词，及对应单词出现的次数
'''
I have a good friend her name is Li Hua
We are in the same class So it is natural for us
to become partners When we have group work we
will cooperate well One thing that I admire Li Hua
so much is her persistence Sometimes when the task
is too hard to finish and I want to give up but Li
inspires me to hang on and she believes that we will
get over the difficulty Indeed under her leadership
'''
str1 = "I have a good friend her name is Li Hua We are in the same class So it is natural for us to become partners When we have group work we will cooperate well One thing that I admire Li Hua so much is her persistence Sometimes when the task is too hard to finish and I want to give up but Li inspires me to hang on and she believes that we will get over the difficulty Indeed under her leadership"
# 1、字符串切割  split
listStr = str1.split(" ")
# print(listStr)
# 2、创建一个字典，存储单词及单词的次数
dic1 = {}
# 3、遍历单词列表
for i in listStr:
    # dic1[i] = 1
    # 4、通过单词及单词次数设置字典的key及value（方式一）
    # dic1[i] = listStr.count(i)
    # 4、通过判断当前单词是否在字典的key中，
    # 如果不在，设置value为1，如果已经存在，在当前value的基础上加1（方式二）
    # if i in dic1.keys():
    #     dic1[i] += 1
    # else:
    #     dic1[i] = 1
    # 4、获取当前的单词的次数 （方式三）
    countWord = dic1.get(i)
    if countWord == None:
        dic1[i] = 1
    else:
        dic1[i] = dic1[i] + 1
print(dic1)

# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=122&rsv_pq=8142a45f00000158&rsv_t=82306kA0QxvjJUWEmC%2FnCQ6OmG1rHOCML5UCpLG886ZVKxHO1Lkbo39bqVY&rqlang=cn&rsv_enter=1&rsv_sug3=2&rsv_sug1=2&rsv_sug7=100
# {ie:utf-8, f:8}



# 函数   迭代器
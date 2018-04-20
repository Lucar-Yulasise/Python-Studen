# 引入模块
# 格式：import module1[, module2, module3....modulen]

# import:不管用import引入同一个文件多少次，系统默认只会真正引入一次
# import： 防止同一个文件多次引入

# 每次引入一个文件
import math
import random
import pickle
# 一次性引入多个文件
import math, random, pickle

# 使用模块中的内容
print(math.pi)

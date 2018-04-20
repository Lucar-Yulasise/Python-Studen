# 写入文件
# w：重新写入   a：追加内容
# 1、打开文件
f1 = open("a.txt", "a", encoding="utf-8")
# 2、写入内容
# write(str)   将str写入文件，没有返回
# 将信息写入文件
f1.write("123456")
# 3、关闭文件
f1.close()

# 简写
with open("c.txt","w", encoding="utf-8") as f2:
    f2.write("124789kfxfh")






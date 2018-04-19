f1 = open("a.txt","a")
f1.write("adas121")
f1.close()

with open("a.txt","w")as f2:
    f2.write("文件重新写入")


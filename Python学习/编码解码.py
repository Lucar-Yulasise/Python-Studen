# 编码
with open("d.txt","wb") as f1:
    str1 = "北京你好！我有沙尘暴"
    f1.write(str1.encode("GBK"))

with open("d.txt","rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))

    newStr = data.decode("GBK")
    print(newStr)

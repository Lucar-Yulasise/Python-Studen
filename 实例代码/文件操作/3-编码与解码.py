# 编码  encode("编码格式")
with open("d.txt","wb") as f1:
    str1 = "北京你好，我有沙尘暴，hello world"
    f1.write(str1.encode("GBK"))

# 解码  decode("编码格式")
with open("d.txt","rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))  # byte 字节

    newStr =data.decode("GBK")
    print(newStr)
    print(type(newStr))  # str

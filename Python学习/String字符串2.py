# 字符串内建函数
# 1. eval(str) 将str当成有效的表达式来计算，将计算结果返回
print(eval("123"))
print(eval("+123"))
print(eval("-123"))
print(eval("1+2"))
print(eval("12 -3 "))
print("--------------------------------------------------")
# 2 len(str) 返回字符串长度
print(len("Hello"))
print(len("123456789"))
print("--------------------------------------------------")
# 3 字母大小写转换
str2 = "heLLo hi Nihao"
print(str2.lower())
print(str2.upper())
print(str2.swapcase())
print(str2.capitalize())
print(str2.title())
print("--------------------------------------------------")
# 4 字符串长度更改
str3 = "pyc"
print(str3.center(15,"0"))
print(str3.ljust(15,"0"))
print(str3.rjust(15),"*")
print(str3.zfill((15)))
print(str3)
print("--------------------------------------------------")
# 5 、 string.count(str[,being,end]):返回string 里面 str 的 str 的个数
# 如果begin与end有值，查找该范围的次数
str4 = "good very well good good very"
print(str4.count("good"))
print(str4.count("good",3,22))
print("--------------------------------------------------")
# 6 检测字符串中有没有某个值
print(str4.find("very"))#返回匹配第一个符号的字符下标
print(str4.find("very",10,31))
print(str4.find("wdsd"))
print(str4.rfind("very"))
print(str4.index("very"))
#print(str4.index("qwere"))
print(str4.rindex("very"))
print("--------------------------------------------------")
# 7 截掉字符串指定元素
str5 = "        MM is Lily   "
str6 = "********GG is Tom*****"
print(str5.lstrip())
print(str6.lstrip("*"))
print(str6.rstrip("*"))
print(str6.strip("*")) # 有返回值，返回更改后的值
v = str6.count("*")
print(type(v))
print("--------------------------------------------------")
# 8 将字符转为ASCLL 将ASCLL码转为字符
str7 = "A"
str8 = chr(66)
print(str7)
print(ord(str7))
str9 = "我"
print(ord(str9))
print(str8)
print(chr(25105))
print("--------------------------------------------------")
# 9 切割字符串 string.sqlit(str [,num]) 以str切割string这个字符串，返回一个列表型的数据，列表中的元素为切割后的字符
str10 = "MM*GG*TT*HH*QQ"
str10.splitlines()
str11 = "abc\ndef\n123\n789"
str12 = """
dada
dad
daddfds
dasdas
"""
print(str11.splitlines(False))
print(str11.splitlines(True))
print(str12.splitlines())

str13 = "*"
list13 = ["Hello ","good","man"]
print(str13.join(list13))
print("--------------------------------------------------")
# 11 返回字符串中最大的字母或最小的字母
str14 = "dafdgfdsgdsftgujhijokpAolhigfytdsrdtu"
print(max(str14))
print(min(str14))
print("--------------------------------------------------")
# 12 替换字符串
str15 = "nice good well good man nice nice man good nice man"
#print(str15.replace("nice","handsome"))
print(str15.replace("nice","handsome",2))
print(str15)

#
t = str.maketrans("abc","123") # 创建一个映射表，如果里面写两参数，第一参数为字符串，表示即将转换的字符，第二个参数也要为字符串，表示转换的目标字符。两个字符串的字符个数，要一致
t1 = str.maketrans({"a":"1","b":"5"})
print("--------------------------------------------------")
# 如果只有一个参数，参数类型为字典类型，key为即将转换的字符
str16 = "qweawwbuuctttaabbccasdadh"
print(str16.translate(t)) # 根据T给出的映射表，替换string中的字符
print(str16.translate(t1))
print("--------------------------------------------------")
# 13 用于判断的函数
str17  = "23423"
print("sdfdsf".isalpha())#
print("abc123".isalpha())
print("--------------------------------------------------")
print("adc".isupper())
print("ABC".isupper())
print("A123".isupper())
print("abcQWE".isupper())
print("--------------------------------------------------")
print("abc".islower())
print("ABC".islower())
print("abc123".islower())
print("--------------------------------------------------")
print("qer".istitle())
print("AECs".istitle())
print("--------------------------------------------------")
print("123abc".isalnum())
print("123".isalnum())
print("abc".isalnum())
print("abc!@##".isalnum())
print("--------------------------------------------------")
print("abc".isdigit())
print("123".isdigit())
print("--------------------------------------------------")
print("   ".isspace())
print("  abc".isspace())
print("--------------------------------------------------")

str20 ="http://www.baidu.com"
print(str20.startswith("ht"))
print(str20.startswith("http://"))
print(str20.startswith("ttp://"))
print(str20.startswith("ttp://",1,12))

print("--------------------------------------------------")
print(str20.endswith("com"))

# 编码解码
str21 = "pyc是好人"
print(str21)
print(str21.encode("utf-8"))
print(str21.encode("GBK"))

str22 = str21.encode("utf-8")
print(str22.decode("utf-8"))

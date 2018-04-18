str1 = """
I have a good friend her name is Li Hua
We are in the same class So it is natural for us
to become partners When we have group work we
will cooperate well One thing that I admire Li Hua
so much is her persistence Sometimes when the task
is too hard to finish and I want to give up but Li
inspires me to hang on and she believes that we will
get over the difficulty Indeed under her leadership
"""
dic1 = {}
inx = 0
listText = str1.split(" ")
for i in listText:
    dic1[i] = 1
    if i in dic1.keys():
        dic1[i] += 1
    else:
        dic1[i] = 1
print(dic1)

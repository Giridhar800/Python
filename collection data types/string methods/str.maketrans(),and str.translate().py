t1 = str.maketrans("aeiou","!@#$%")
t2 = str.maketrans("!@#$%","aeiou")

str1 = "programming"
print(str1)
str2 = str1.translate(t1)
print(str2)

str3 = str2.translate(t2)
print(str3)

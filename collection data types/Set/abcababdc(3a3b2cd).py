str1 = "abcababdc"
print(str1)
set1 = set(str1)
print(set1) # {'c', 'b', 'd', 'a'}
list1 = list(set1)
print(list1)# ['a', 'c', 'b', 'd']
list1.sort()
str2 = " "
for ch in list1:
    c = str1.count(ch)
    str2 = str2 + str(c) + ch
print(str2)

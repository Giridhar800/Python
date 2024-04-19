list1 = [6,1,5,2,9,8,4,7]
print(list1)


list1.sort()
print(list1)

list1.sort(reverse = True)
print(list1)

list2 = ['a','c','b','A','B','C']
print(list2)

list2.sort()
print(list2)
list2.sort(reverse = True)
print(list2)

list2.sort(key = str.upper)
print(list2)

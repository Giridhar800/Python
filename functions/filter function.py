list1 = ['a','b','c','d','e','f','g','h','i','j']
list2 = list(filter(lambda x:x in "aeiouAEIOU",list1))
print(list2)

list3 = list(range(1,11))
print(list3)
list4 = list(filter(lambda x:x%2 == 0,list3))
print(list4)


# shallow copy

list1 = [10,20,30,40,50]
list2 = list1.copy()
print(list1)
print(id(list1))
print(id(list1[0]))
print(list2)
print(id(list2))
print(id(list2[0]))
l3 = [[10,20],30]
print(l3)
print(l3[0])
print(l3[1])

# Deep copy

list4 = [[10,20],30]
import copy
list5 = copy.deepcopy(list4)
print(list4,list5)
list4.append(40)
print(list4,list5)


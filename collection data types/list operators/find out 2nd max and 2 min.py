n = int(input("enter n value"))

list1 = [int(input("enter value"))for i in range(n)]
print(list1)
list2 = sorted(list1)
print(list2)
c = list2.count(list2[0])
print("2nd minimum is ",list2[c])
c = list2.count(list2[-1])  # c = 2
print("2nd maximum is : ",list2[(len(list1)-1)-c])
                                # ((6-1)-2)=3

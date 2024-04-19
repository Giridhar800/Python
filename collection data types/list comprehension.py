# Without comprehension

n = int(input("enter the value of n"))
list1 = []
for i in range(n):
    values = int(input("enter values "))
    list1.append(values)
print(list1)


# with comprehension

list1 = [int(input("enter any values")) for i in range(n)]
print(list1)

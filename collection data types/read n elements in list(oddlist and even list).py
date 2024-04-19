n = int(input("enter the value of n"))
list1 = []

for i in range(n):
    values = int(input("enter any values"))
    list1.append(values)
print(list1)

even_list = []
odd_list = []

for v in list1:
    if v%2 == 0:
        even_list.append(v)
    else:
        odd_list.append(v)
print(f" even list =>> {even_list}")
print(f" odd list =>> {odd_list}")

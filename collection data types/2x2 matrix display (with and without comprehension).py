# without comprehension

matrix = []
for i in range(2):
    row = []
    for j in range(2):
        values = int(input("enter values"))
        row.append(values)
    matrix.append(row)
print(matrix)


# with comprehension
list1 =[[int(input("enter values")) for j in range(2)]for i in range(2)]
print(list1)

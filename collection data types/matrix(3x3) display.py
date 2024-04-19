matrix = []
for i in range(3):
    row = []
    for j in range(3):
        values = int(input("enter values"))
        row.append(values)
    matrix.append(row)
print(matrix)

for row in matrix:
    for values in row:
        print(values,end=' ' )
    print()

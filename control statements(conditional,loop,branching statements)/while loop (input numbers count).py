num = int(input("enter any number"))
c = 0
while num > 0:
    num = num // 10
    c += 1
print(" count of digits..:",c)

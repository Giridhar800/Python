# find the largest number among the three input numbers

# l =[44,55,53]
# print(max(l))


n1 =float(input("enter no"))
n2 =float(input("enter no"))
n3 =float(input("enter no"))

if (n1>=n2) and (n1>=n3):
    largest = n1
elif (n2>=n1) and (n2>=n3):
    largest = n2
else:
    largest = n3
print("largest number is:",largest)

    

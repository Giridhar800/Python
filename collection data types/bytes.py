str1 = "ABC"
print(str1)
b1 = str1.encode()
print(b1)
btype = type(b1)
print(btype)

list1 = [10,20,30,40,50]
b2 = bytes(list1)
print(b2)
b2type = type(b2)
print(b2type)

b3 = bytes(65)
print(b3)
b3type = type(b3)
print(b3type)

b4 = bytes("ABC",encoding="UTF-8")
print(b4)
b4type = type(b4)
print(b4type)



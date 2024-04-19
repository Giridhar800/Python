str1 = input("enter any string")
str2 = ""
for ch in str1:
    if ch >="a" and ch <= "z":
        str2 = str2+chr(ord(ch)-32)

    elif ch >="A" and ch <="Z":
        str2 = str2+chr(ord(ch)+32)
    else:
        str2 = str2+ch

print(str1)
print(str2)

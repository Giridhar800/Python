str1 = input("enter any string")
str2 = ' '
l = len(str1)
i = 0

while i < l:
    if str1[i] >= 'a' and str1[i] <= 'z':
        str2 = str2 + chr(ord(str1[i])-32)

    elif str1[i] >= 'A' and str1[i] <= 'Z':
        str2 = str2 + chr(ord(str1[i]) + 32)

    else:
        str2 = str2 + str1[i]
    i = i+1
print(str1)
print(str2)

str1 = input("enter any string")
c = 0
for ch in str1:
    if ch in "aeiouAEIOU":
        c = c+1
print("count of vowels is :",c)
    

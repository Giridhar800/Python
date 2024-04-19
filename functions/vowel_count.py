def vowel_count(s):
    c = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            c+=1
    return c

str1 = input("enter string")
k = vowel_count(str1)
print(f"vowel_count is: {k}")

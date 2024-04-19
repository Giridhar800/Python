def patch(s):
    l = 0
    for value in s:
        if value%2 == 0:
            print(value)
            l = l+1
    return l


l1 = list(range(1,11))
print(l1)
c = patch(l1)
print(c)

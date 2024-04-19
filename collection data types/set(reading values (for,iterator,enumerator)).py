set1 = {10,20,30,40,50}
for value in set1:
    print(value)

a = iter(set1) # iterator
v1 = next(a)
v2 = next(a)
print(v1,v2)

e = enumerate(set1)
n1 = next(e)
n2 = next(e)
print(n1,n2)

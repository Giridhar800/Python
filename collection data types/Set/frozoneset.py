set1 = frozenset()
print(set1)
# set1.add(10)  attribute error

set1 = frozenset(range(10,110,10))
print(set1)

set2 = { frozenset({1,2,3,4}),frozenset({5,6,7})}
print(set2)
for i in set2:
    print(i)

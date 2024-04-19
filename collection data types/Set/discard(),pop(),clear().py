set1 = {1,2,3,4,5,6}
# Discard
print(set1)
set1.discard(5)
print(set1)
set1.discard(7)
print(set1)

# pop

set2 = set(range(10,110,10))
print(set2)
v =  set2.pop()
print(v)
print(set2)

# Clear
set2.clear()
print(set2)

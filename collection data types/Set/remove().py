n = int(input("enter n value"))

set1 = set(map(int,input().split()[:n]))
print(set1)
value = int(input("enter remove value"))
if value in set1:
    set1.remove(value)
    print(" value removed...")
else:
    print("value not found")
print(set1)

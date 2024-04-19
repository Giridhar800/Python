list1 = [10,20,30,40,50,60,70,80,90,100]

a = iter(list1) #iterator object

t = type(list1)
t2 = type(a)
print(t,t2)
print(next(a))
print(next(a))
for values in a:
    print(values, end=' ')



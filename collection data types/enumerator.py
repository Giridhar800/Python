list1 = [10,20,30,40,50,60,70,80,90,100]
print(list1)

a = enumerate(list1) #enumerate object

t = type(list1)
t2 = type(a)
print(t,t2,end = '\n')
r = next(a)
r1 = next(a)
r2 = next(a)
r3 = next(a)
print(r)
print(r1)
print(r2)
print(r3)

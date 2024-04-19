import functools
list1 = [10,20,30,40,50]
res1 = functools.reduce(lambda x,y:x+y,list1)
print(res1)

res2 = functools.reduce(lambda x,y: x if x>y else y,list1)
print(res2)

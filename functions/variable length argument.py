def maximum(*n):
    m = 0
    for value in n:
        if value > m:
            m = value
    return m

res1 = maximum()
res2 = maximum(10,20)
res3 = maximum(1,3,5,2,4,8,7,6,10,20,10)
print(res1,res2,res3,sep = "\n")

d1 = {1:10,2:20,3:30,4:40,5:50}
d2 = {6:60,1:99,3:88,8:100}
print(d1,d2,sep='\n')

d1.update(d2)
print(d1)

# reversed()
for i in reversed(d1):
    print(i,d1[i])
    

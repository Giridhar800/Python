a = {10,20,30,40}
b = {50,60,70}
c = {30,40,50}
print(a,b,c,sep = "\n")

# isdisjoint
x = a.isdisjoint(b)
y = a.isdisjoint(c)
print(x,y,sep="\n")

 # sub and super sets

d = {1,2,3}
e = {1,2,3,4,5}
print(d,e,sep="\n")

s1 = e.issubset(d)
s2 = d.issubset(e)
print(s1,s2,sep="\n")
s3 = e.issuperset(d)
print(s3)
